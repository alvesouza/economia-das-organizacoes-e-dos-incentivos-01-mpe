"""Check the two Lecture 6 companions against independent Python implementations.

For each page: extract the `// MODEL:BEGIN ... // MODEL:END` block, run it under Node at the
default, low-end and high-end control vectors (plus presets), compare every read-out with the
Python value, sweep each control end to end (others at default) and require the read-outs to
change and stay finite, check that the landmarks are hit exactly, and syntax-check the whole
page script. Pattern copied from Aula/aula-01-companions/check_companions.py.

Run: python Notas/L06/companions/check_companions.py   (needs `node` on PATH)
Exits non-zero on the first mismatch.
"""
import json
import math
import re
import subprocess
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent


def page_script(name):
    html = (HERE / name).read_text(encoding="utf-8")
    return re.search(r"<script>(.*?)</script>", html, re.S).group(1)


def run_node(name, body):
    """Run the page's model block followed by `body` (JS that prints JSON); return parsed JSON."""
    model = re.search(r"// MODEL:BEGIN.*?// MODEL:END", page_script(name), re.S).group(0)
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as f:
        f.write(model + "\n" + body)
    out = subprocess.run(["node", f.name], capture_output=True, text=True, check=True).stdout
    return json.loads(out)


def syntax_check(name):
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as f:
        f.write(page_script(name))
    subprocess.run(["node", "--check", f.name], check=True)


def close(a, b, tol=1e-9):
    if a is None or b is None:
        return a is b
    if isinstance(a, bool) or isinstance(b, bool):
        return a == b
    return math.isclose(a, b, rel_tol=tol, abs_tol=tol)


def finite(obj):
    if isinstance(obj, float):
        return math.isfinite(obj)
    if isinstance(obj, dict):
        return all(finite(v) for v in obj.values())
    return True


def run_vectors(name, vecs):
    return run_node(name, f"const V={json.dumps(vecs)};const o={{}};for(const k in V)o[k]=report(V[k]);"
                          "console.log(JSON.stringify(o));")


def sweep(name, defaults, ranges):
    """Each control at both ends (others default): read-outs finite and different from default."""
    vecs = {"default": defaults}
    for k, (lo, hi) in ranges.items():
        vecs[f"{k}=lo"] = dict(defaults, **{k: lo})
        vecs[f"{k}=hi"] = dict(defaults, **{k: hi})
    res = run_vectors(name, vecs)
    for k, r in res.items():
        assert finite(r), (name, k, r)
    for k in ranges:
        assert res[f"{k}=lo"] != res["default"] or res[f"{k}=hi"] != res["default"], (name, k, "dead control")


# ---------- Companion 1: collusion threshold (Tadelis 10.4, Gibbons 2.3.C, Cabral 9.1) ----------
def collusion_py(s):
    """Independent path: profits by direct optimization on a fine grid, cutoff by (10.5)."""
    A, n, d = s["a"] - s["c"], s["n"], s["d"]
    piM = A * A / 4
    share = piM / n
    if s["mode"] == "cournot":
        others = (n - 1) * A / (2 * n)
        q = [i * A / 200000 for i in range(200001)]
        dev = max((A - others - x) * x for x in q)          # best response by brute force
        qN = A / (n + 1)
        pun = (A - n * qN) * qN
        dstar = (dev - share) / (dev - pun)
        # most collusive sustainable symmetric output: smallest grid q in [A/2n, qN] that satisfies it
        grid = [A / (2 * n) + i * (qN - A / (2 * n)) / 200000 for i in range(200001)]
        qs = next(x for x in grid
                  if (A - n * x) * x >= (1 - d) * ((A - (n - 1) * x) / 2) ** 2 + d * pun - 1e-9)
        psus = s["a"] - n * qs
        r = dict(share=share, dev=dev, pun=pun, dstar=dstar, qsus=qs, psus=psus, pisus=(psus - s["c"]) * qs)
    else:
        dev, pun = piM, 0.0
        dstar = (dev - share) / (dev - pun)
        ok = d >= dstar - 1e-12
        r = dict(share=share, dev=dev, pun=pun, dstar=dstar, psus=(s["a"] + s["c"]) / 2 if ok else s["c"],
                 pisus=share if ok else 0.0)
    r["sustainable"] = d >= r["dstar"] - 1e-12
    r["gap"] = share - ((1 - d) * dev + d * pun)
    return r


def check_collusion():
    name = "companion-collusion-threshold.html"
    D = dict(mode="cournot", n=2, d=0.5, a=100, c=10)
    vecs = {
        "default": D,
        "low end": dict(mode="cournot", n=2, d=0.0, a=60, c=0),
        "high end": dict(mode="cournot", n=12, d=0.999, a=200, c=50),
        "bertrand default": dict(D, mode="bertrand"),
        "bertrand n=12, d=0.9": dict(D, mode="bertrand", n=12, d=0.9),
        "cournot n=4, d=0.4": dict(D, n=4, d=0.4),
    }
    js = run_vectors(name, vecs)
    rows = []
    for k, v in vecs.items():
        py, pg = collusion_py(v), js[k]
        for f in ["share", "dev", "pun", "dstar", "psus", "pisus", "gap", "sustainable"]:
            assert close(py[f], pg[f], 1e-6), (k, f, py[f], pg[f])
        if v["mode"] == "cournot":
            assert close(py["qsus"], pg["qsus"], 1e-4), (k, py["qsus"], pg["qsus"])
        rows.append((k, round(pg["dstar"], 4), round(pg["share"], 2), round(pg["dev"], 2), round(pg["pun"], 2),
                     round(pg["psus"], 2), pg["sustainable"]))
    # book landmarks
    assert close(js["default"]["dstar"], 9 / 17) and close(js["bertrand default"]["dstar"], 0.5)
    assert abs(js["default"]["qsus"] - 22.94) < 0.005 and abs(js["default"]["psus"] - 54.12) < 0.005
    assert close(js["default"]["share"], 1012.5) and close(js["default"]["pun"], 900)
    # snap-to-threshold lands exactly and flips the verdict
    at = run_node(name, "const out=[];for(const m of ['cournot','bertrand'])for(const n of [2,3,7,12]){"
                        "const ds=dstarOf(m,n);const s={mode:m,n:n,a:100,c:10};"
                        "out.push([report({...s,d:ds}).sustainable, report({...s,d:ds-1e-6}).sustainable,"
                        "Math.abs(report({...s,d:ds}).gap)]);}console.log(JSON.stringify(out));")
    assert all(a and not b and g < 1e-6 for a, b, g in at), at
    sweep(name, D, dict(n=(2, 12), d=(0, 0.999), a=(60, 200), c=(0, 50)))
    sweep(name, dict(D, mode="bertrand"), dict(n=(2, 12), d=(0, 0.999), a=(60, 200), c=(0, 50)))
    syntax_check(name)
    return rows


# ---------- Companion 2: efficiency wage (Gibbons 2.3.D, M&R pp. 251-252) ----------
def wage_py(s):
    """Independent path: w* as the root of V_e(w) = V_s(w) by bisection (Gibbons pp. 109-110)."""
    d, p, e, w0, y = s["d"], s["p"], s["e"], s["w0"], s["y"]
    Ve = lambda w: (w - e) / (1 - d)
    Vs = lambda w: ((1 - d) * w + d * (1 - p) * w0) / ((1 - d * p) * (1 - d))
    lo, hi = w0, w0 + e + 1e6
    for _ in range(200):
        mid = (lo + hi) / 2
        if Ve(mid) >= Vs(mid):
            hi = mid
        else:
            lo = mid
    w = hi
    S = y - e - w0
    if e == 0:
        dmin = 0.0 if S >= 0 else None
    else:
        dmin = e / (e + (1 - p) * S) if S > 0 else None
    return dict(wstar=w, premium=w - w0 - e, N=d / (1 - d), firm=y - w, firmPays=y - w >= -1e-9, dmin=dmin,
                efficient=S > 0, shirkWorse=w0 > p * y, avgValue=w - e)


def check_wage():
    name = "companion-efficiency-wage.html"
    D = dict(d=0.5, p=0.95, e=1, w0=39, y=41)
    vecs = {
        "default": D,
        "low end": dict(d=0.01, p=0.0, e=0.0, w0=0.0, y=0.0),
        "high end": dict(d=0.99, p=0.99, e=10, w0=80, y=120),
        "M&R N=2": dict(D, d=2 / 3),
        "perfect monitoring": dict(D, p=0.0),
    }
    js = run_vectors(name, vecs)
    rows = []
    for k, v in vecs.items():
        py, pg = wage_py(v), js[k]
        for f in ["wstar", "premium", "N", "firm", "firmPays", "dmin", "efficient", "shirkWorse", "avgValue"]:
            assert close(py[f], pg[f], 1e-7), (k, f, py[f], pg[f])
        rows.append((k, round(pg["wstar"], 3), round(pg["premium"], 3), pg["firmPays"],
                     None if pg["dmin"] is None else round(pg["dmin"], 4)))
    # M&R landmarks: USD 60,000 at N = 1, 50,000 at N = 2 (p. 252)
    assert close(js["default"]["wstar"], 60) and close(js["M&R N=2"]["wstar"], 50)
    # Gibbons's assumptions hold at the default
    assert js["default"]["efficient"] and js["default"]["shirkWorse"]
    # landmark: at delta = delta_min the firm is exactly indifferent and the verdict flips there
    flip = run_node(name, "const s={p:0.95,e:1,w0:39,y:41,d:0.5};const dm=report(s).dmin;"
                          "console.log(JSON.stringify([dm,report({...s,d:dm}).firm,report({...s,d:dm}).firmPays,"
                          "report({...s,d:dm-1e-6}).firmPays]));")
    assert close(flip[0], 1 / 1.05) and abs(flip[1]) < 1e-9 and flip[2] and not flip[3], flip
    # the two value lines cross exactly at w*
    cross = run_node(name, "const s={d:0.5,p:0.95,e:1,w0:39,y:41};const w=report(s).wstar;"
                           "console.log(JSON.stringify([effortAvg(w,s),shirkAvg(w,s)]));")
    assert close(cross[0], cross[1]), cross
    sweep(name, D, dict(d=(0.01, 0.99), p=(0.0, 0.99), e=(0.0, 10), w0=(0.0, 80), y=(0.0, 120)))
    syntax_check(name)
    return rows


if __name__ == "__main__":
    for title, fn in [("collusion-threshold", check_collusion), ("efficiency-wage", check_wage)]:
        print(f"== {title}")
        for row in fn():
            print("  ", row)
    print("all companion checks pass")
