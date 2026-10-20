"""Check the two Lecture 7 companions against independent Python implementations.

For each page: extract the `// MODEL:BEGIN ... // MODEL:END` block, run it under Node at the
default, low-end and high-end control vectors (plus presets), and compare every read-out with a
Python value computed by a different route (numerical integration / brute-force enumeration);
sweep each control end to end and require the read-outs to change and stay finite; syntax-check
the page's whole script. Pattern copied from Aula/aula-01-companions/check_companions.py.

Run: python Notas/L07/companions/check_companions.py   (needs `node` on PATH)
Exits non-zero on the first mismatch.
"""
import json
import math
import re
import subprocess
import tempfile
from pathlib import Path

import numpy as np
from scipy.integrate import quad

HERE = Path(__file__).resolve().parent


def page_script(name):
    html = (HERE / name).read_text(encoding="utf-8")
    return re.search(r"<script>(.*?)</script>", html, re.S).group(1)


def run_node(name, body):
    """Run the page's model block followed by `body` (JS printing JSON); return parsed JSON."""
    model = re.search(r"// MODEL:BEGIN.*?// MODEL:END", page_script(name), re.S).group(0)
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as f:
        f.write(model + "\n" + body)
    out = subprocess.run(["node", f.name], capture_output=True, text=True, check=True).stdout
    return json.loads(out)


def syntax_check(name):
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as f:
        f.write(page_script(name))
    subprocess.run(["node", "--check", f.name], check=True)


def close(a, b, tol=1e-7):
    if a is None or b is None:
        return a is b
    return math.isclose(a, b, rel_tol=tol, abs_tol=tol)


def finite(obj):
    if isinstance(obj, float):
        return math.isfinite(obj)
    if isinstance(obj, dict):
        return all(finite(v) for v in obj.values())
    return True


def sweep(name, defaults, ranges, call="report(V[k])"):
    vecs = {"default": defaults}
    for k, (lo, hi) in ranges.items():
        vecs[f"{k}=lo"] = dict(defaults, **{k: lo})
        vecs[f"{k}=hi"] = dict(defaults, **{k: hi})
    res = run_node(name, f"const V={json.dumps(vecs)};const o={{}};for(const k in V)o[k]={call};"
                         "console.log(JSON.stringify(o));")
    for k, r in res.items():
        assert finite(r), (name, k, r)
    for k in ranges:
        assert res[f"{k}=lo"] != res["default"] or res[f"{k}=hi"] != res["default"], (name, k, "dead control")


# ---------- Companion 1: auction bidding (Tadelis 13.1, Gibbons 3.2.B) ----------
def auction_py(n, th, b):
    """Independent route: FPA bid by numerical argmax of (13.2); SPA payoff and the expected
    payment by integrating over the density (n-1) m^(n-2) of the highest rival value m."""
    dens = lambda m: (n - 1) * m ** (n - 2)

    def fpa_u(x):                                  # rivals bid (n-1)v/n, so rival bid < x iff v < x n/(n-1)
        return min(1.0, x * n / (n - 1)) ** (n - 1) * (th - x)

    def spa_u(x):
        x = min(x, 1.0)
        return quad(lambda m: (th - m) * dens(m), 0, x)[0] if x > 0 else 0.0

    grid = np.linspace(0, 1, 200_001)
    vals = np.minimum(1, grid * n / (n - 1)) ** (n - 1) * (th - grid)
    fb_num = grid[np.argmax(vals)] if th > 0 else 0.0
    fb = (n - 1) * th / n
    assert abs(fb_num - fb) < 2e-5, (n, th, fb_num, fb)
    pwin = th ** (n - 1)
    pay_spa = quad(lambda m: m * dens(m), 0, th)[0] if th > 0 else 0.0   # E[m 1{m<th}]
    assert close(pay_spa, pwin * fb)               # revenue equivalence type by type
    rev_fpa = quad(lambda v: (n - 1) * v / n * n * v ** (n - 1), 0, 1)[0]  # E[max bid]
    rev_spa = quad(lambda v: v * n * (n - 1) * (v ** (n - 2) - v ** (n - 1)), 0, 1)[0]
    assert close(rev_fpa, rev_spa)
    return dict(fpaBid=fb, spaBid=th, shade=th - fb, pwin=pwin, pay=pay_spa,
                surplus=th * pwin - pay_spa, rev=rev_spa, uF=fpa_u(b), uS=spa_u(b),
                lossF=fpa_u(fb) - fpa_u(b), lossS=spa_u(th) - spa_u(b))


def check_auction():
    name = "companion-auction-bidding.html"
    D = dict(n=2, th=0.8, b=0.4)
    ranges = dict(n=(2, 10), th=(0, 1), b=(0, 1))
    vecs = {"default": D, "low end": dict(n=2, th=0.0, b=0.0), "high end": dict(n=10, th=1.0, b=1.0),
            "n=5, b=FPA optimum": dict(n=5, th=0.8, b=0.64), "overbid": dict(n=3, th=0.5, b=0.9)}
    js = run_node(name, f"const V={json.dumps(vecs)};const o={{}};for(const k in V)o[k]=report(V[k]);"
                        "console.log(JSON.stringify(o));")
    rows = []
    for k, v in vecs.items():
        py, pg = auction_py(**v), js[k]
        for f in py:
            assert close(py[f], pg[f]), (k, f, py[f], pg[f])
        rows.append((k, v, {f: round(py[f], 4) for f in ("fpaBid", "pwin", "pay", "rev", "uF", "uS")}))
    # landmarks: Gibbons b = v/2 at n = 2; b = theta gives FPA payoff 0 and the SPA optimum
    assert close(js["default"]["fpaBid"], 0.4) and close(js["default"]["rev"], 1 / 3)
    hi = js["high end"]
    assert close(hi["uF"], 0.0) and close(hi["lossS"], 0.0)
    assert js["n=5, b=FPA optimum"]["lossF"] < 1e-12
    assert js["overbid"]["uF"] < 0
    sweep(name, D, ranges)
    syntax_check(name)
    return rows


# ---------- Companion 2: lemons (Tadelis 12.3, Prop. 12.1) ----------
def lemons_py(v1, s, K, d):
    """Independent route: enumerate trade sets {1..k} and offers p = v_k by brute force."""
    v = [v1 + (k - 1) * s for k in range(1, K + 1)]
    feasible = [k for k in range(1, K + 1) if np.mean([x + d for x in v[:k]]) >= v[k - 1] - 1e-9]
    kmax = max(feasible)
    pool = np.mean([x + d for x in v[:kmax]])
    offers = [(sum(x <= p for x in v) / K * (np.mean([x + d for x in v if x <= p]) - p), p) for p in v]
    offers = [o for o in offers if v.index(o[1]) + 1 <= kmax]
    best_u = max(o[0] for o in offers)
    best_p = min(o[1] for o in offers if o[0] > best_u - 1e-12)
    return dict(kmax=kmax, share=kmax / K, pLo=v[kmax - 1], pHi=float(pool), offer=best_p,
                buyerU=float(best_u), gainsEq=d * kmax / K, gainsFull=d, lost=d * (K - kmax) / K,
                dNext=s * kmax / 2 if kmax < K else None, dFull=s * (K - 1) / 2)


def check_lemons():
    name = "companion-lemons.html"
    D = dict(v1=10, s=10, K=3, d=4)
    ranges = dict(v1=(0, 50), s=(1, 30), K=(2, 8), d=(0, 105))
    vecs = {"default": D, "low end": dict(v1=0, s=1, K=2, d=0), "high end": dict(v1=50, s=30, K=8, d=105),
            "full-trade landmark": dict(D, d=10), "just below": dict(D, d=9.5), "K=5, d=10": dict(D, K=5, d=10)}
    js = run_node(name, f"const V={json.dumps(vecs)};const o={{}};for(const k in V)o[k]=report(V[k]);"
                        "console.log(JSON.stringify(o));")
    rows = []
    for k, v in vecs.items():
        py, pg = lemons_py(**v), js[k]
        for f in py:
            assert close(py[f], pg[f]), (k, f, py[f], pg[f])
        rows.append((k, v, {f: py[f] for f in ("kmax", "pLo", "pHi", "offer", "buyerU", "lost")}))
    # Tadelis Prop. 12.1 (p. 260): only L trades, prices [10, 14]; pools worth 14, 19, 24
    d0 = js["default"]
    assert d0["kmax"] == 1 and close(d0["pLo"], 10) and close(d0["pHi"], 14)
    pools = run_node(name, "const p={v1:10,s:10,K:3,d:4};console.log(JSON.stringify([10,20,30].map(x=>poolValue(p,x))));")
    assert pools == [14, 19, 24], pools
    assert js["full-trade landmark"]["kmax"] == 3 and js["just below"]["kmax"] == 2
    # the level v1 never changes the trade set
    lv = run_node(name, "console.log(JSON.stringify([0,25,50].map(v=>report({v1:v,s:10,K:3,d:4}).kmax)));")
    assert lv == [1, 1, 1]
    sweep(name, D, ranges)
    syntax_check(name)
    return rows


DOM_STUB = r"""
const store = {};
function node(id){ return {id, value: '', _t: '', _h: '', kids: [],
  set textContent(v){ this._t = String(v); this.kids = []; if (id) store[id] = this._t; }, get textContent(){ return this._t; },
  set innerHTML(v){ this._h = String(v); if (id) store[id] = this._h; }, get innerHTML(){ return this._h; },
  appendChild(c){ this.kids.push(c); return c; }, setAttribute(k, v){ this[k] = String(v); },
  addEventListener(){} }; }
const nodes = {};
const svgText = [];
globalThis.document = {
  getElementById: id => nodes[id] || (nodes[id] = node(id)),
  createElementNS: () => { const n = node(null); const set = n.setAttribute;
    n.setAttribute = function(k, v){ svgText.push(String(v)); set.call(this, k, v); };
    Object.defineProperty(n, 'textContent', {set(v){ svgText.push(String(v)); }, get(){ return ''; }}); return n; },
  documentElement: {getAttribute: () => null, setAttribute(){}}};
globalThis.matchMedia = () => ({matches: false});
"""


def render_smoke(name, vectors):
    """Run the whole page script against a stub DOM at each vector; no read-out or SVG attribute
    may contain NaN, undefined or Infinity."""
    body = DOM_STUB + page_script(name) + f"""
const out = {{}};
for (const [k, v] of Object.entries({json.dumps(vectors)})) {{ svgText.length = 0; load(v);
  out[k] = Object.values(store).concat(svgText).filter(s => /NaN|undefined|Infinity/.test(s)); }}
console.log(JSON.stringify(out));"""
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as f:
        f.write(body)
    res = json.loads(subprocess.run(["node", f.name], capture_output=True, text=True, check=True).stdout)
    for k, bad in res.items():
        assert not bad, (name, k, bad[:5])


if __name__ == "__main__":
    render_smoke("companion-auction-bidding.html",
                 {"d": dict(n=2, th=0.8, b=0.4), "lo": dict(n=2, th=0, b=0), "hi": dict(n=10, th=1, b=1),
                  "mid": dict(n=7, th=0.33, b=0.95)})
    render_smoke("companion-lemons.html",
                 {"d": dict(v1=10, s=10, K=3, d=4), "lo": dict(v1=0, s=1, K=2, d=0),
                  "hi": dict(v1=50, s=30, K=8, d=105), "mid": dict(v1=3, s=7, K=5, d=10.5)})
    print("render smoke tests pass (no NaN / undefined / Infinity)")
    for title, fn in [("auction-bidding", check_auction), ("lemons", check_lemons)]:
        print(f"== {title}")
        for row in fn():
            print("  ", row)
    print("all L07 companion checks pass")
