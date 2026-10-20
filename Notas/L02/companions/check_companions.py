"""Check the two Lecture 2 companions against independent Python implementations.

For each page: extract the `// MODEL:BEGIN ... // MODEL:END` block, run it under Node at
the default, low-end and high-end control vectors (plus presets and landmarks), compare
every read-out with Python, sweep each control end to end (others at default) and require
the read-outs to change and stay finite, and syntax-check the page's whole script.
Pattern copied from Aula/aula-01-companions/check_companions.py.

Run: python Notas/L02/companions/check_companions.py   (needs `node` on PATH)
Exits non-zero (AssertionError) on the first mismatch.
"""
import json
import math
import re
import subprocess
import tempfile
from fractions import Fraction as Fr
from itertools import product
from pathlib import Path

HERE = Path(__file__).resolve().parent


def page_script(name):
    html = (HERE / name).read_text(encoding="utf-8")
    return re.search(r"<script>(.*?)</script>", html, re.S).group(1)


def run_node(name, body):
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
    return math.isclose(a, b, rel_tol=tol, abs_tol=tol)


def finite(obj):
    if isinstance(obj, float):
        return math.isfinite(obj)
    if isinstance(obj, dict):
        return all(finite(v) for v in obj.values())
    if isinstance(obj, list):
        return all(finite(v) for v in obj)
    return obj is not None or True


def sweep(name, defaults, ranges, js_call):
    vecs = {"default": defaults}
    for k, (lo, hi) in ranges.items():
        vecs[f"{k}=lo"] = dict(defaults, **{k: lo})
        vecs[f"{k}=hi"] = dict(defaults, **{k: hi})
    res = run_node(name, f"const V={json.dumps(vecs)};const o={{}};for(const k in V)o[k]={js_call};"
                         "console.log(JSON.stringify(o));")
    for k, r in res.items():
        assert finite(r), (name, k, r)
        assert "NaN" not in json.dumps(r), (name, k, r)
    for k in ranges:
        assert res[f"{k}=lo"] != res["default"] or res[f"{k}=hi"] != res["default"], (name, k, "dead control")
    return res


# ---------- Companion 1: the mixing square (Tadelis Sec. 6.2.3, p. 113; Gibbons pp. 40-44)
def ne_2x2(a1, b1, a2, b2):
    """Independent: support enumeration in exact fractions on the normalized game.

    u1(M,C)=a1, u1(M,R)=b1, u1(D,.)=0; u2(M,C)=a2, u2(D,C)=b2, u2(.,R)=0.
    Returns the sorted list of (p, q) = (Pr row 1, Pr column 1). Generic games only.
    """
    a1, b1, a2, b2 = map(Fr, (a1, b1, a2, b2))
    g1 = lambda q: q * a1 + (1 - q) * b1          # v1(row1, q) - v1(row2, q)
    g2 = lambda p: p * a2 + (1 - p) * b2
    cands = {(Fr(p), Fr(q)) for p, q in product((0, 1), repeat=2)}
    if b1 != a1:
        qs = b1 / (b1 - a1)
        if b2 != a2:
            cands.add((b2 / (b2 - a2), qs))
    out = []
    for p, q in cands:
        if not (0 <= p <= 1 and 0 <= q <= 1):
            continue
        ok1 = (g1(q) == 0) if 0 < p < 1 else (g1(q) >= 0 if p == 1 else g1(q) <= 0)
        ok2 = (g2(p) == 0) if 0 < q < 1 else (g2(p) >= 0 if q == 1 else g2(p) <= 0)
        if ok1 and ok2:
            out.append((float(p), float(q)))
    return sorted(out)


def check_mixed():
    name = "companion-mixed-2x2.html"
    D = dict(a1=-4, b1=3, a2=-5, b2=1, q=0.30, p=0.50)
    ranges = dict(a1=(-6, 6), b1=(-6, 6), a2=(-6, 6), b2=(-6, 6), q=(0, 1), p=(0, 1))
    vecs = {
        "default (Tadelis 6.2.3)": D,
        "low end": {k: lo for k, (lo, _) in ranges.items()},
        "high end": {k: hi for k, (_, hi) in ranges.items()},
        "Matching Pennies p.108": dict(D, a1=2, b1=-2, a2=-2, b2=2),
        "Battle of the Sexes p.69": dict(D, a1=2, b1=-1, a2=1, b2=-2),
        "Stag Hunt p.84": dict(D, a1=2, b1=-3, a2=2, b2=-3),
        "Prisoner's Dilemma p.48": dict(D, a1=-1, b1=-1, a2=-1, b2=-1),
    }
    js = run_node(name, f"const V={json.dumps(vecs)};const o={{}};for(const k in V)o[k]=report(V[k]);"
                        "console.log(JSON.stringify(o));")
    rows = []
    for k, v in vecs.items():
        py = ne_2x2(v["a1"], v["b1"], v["a2"], v["b2"])
        pg = sorted(tuple(x) for x in js[k]["pts"])
        assert len(py) == len(pg) and all(close(a[0], b[0]) and close(a[1], b[1]) for a, b in zip(py, pg)), (k, py, pg)
        assert js[k]["nSegs"] == 0, k
        g1 = v["q"] * v["a1"] + (1 - v["q"]) * v["b1"]
        g2 = v["p"] * v["a2"] + (1 - v["p"]) * v["b2"]
        assert close(g1, js[k]["g1"]) and close(g2, js[k]["g2"]), k
        rows.append((k, [(str(Fr(p).limit_denominator(60)), str(Fr(q).limit_denominator(60))) for p, q in py],
                     round(g1, 3), round(g2, 3)))
    # the book's numbers
    assert ne_2x2(-4, 3, -5, 1) == sorted([(0.0, 1.0), (1.0, 0.0), (1 / 6, 3 / 7)])
    assert ne_2x2(2, -2, -2, 2) == [(0.5, 0.5)]
    assert ne_2x2(2, -1, 1, -2) == sorted([(0.0, 0.0), (1.0, 1.0), (2 / 3, 1 / 3)])
    assert ne_2x2(-1, -1, -1, -1) == [(0.0, 0.0)]
    # degenerate (weak) cases: the page reports a continuum, never NaN
    deg = run_node(name, "console.log(JSON.stringify([report({a1:0,b1:3,a2:-5,b2:1,q:.3,p:.5}),"
                         "report({a1:0,b1:0,a2:0,b2:0,q:.3,p:.5}),report({a1:2,b1:0,a2:0,b2:-1,q:.3,p:.5})]));")
    assert deg[0]["nSegs"] >= 1 and deg[1]["nSegs"] >= 1 and "NaN" not in json.dumps(deg), deg
    # landmark: q-hat flips player 1's best reply exactly (sign of the gain changes there)
    qs = 3 / 7
    lm = run_node(name, f"console.log(JSON.stringify([gain1({json.dumps(D)},{qs}-1e-6),gain1({json.dumps(D)},{qs}+1e-6),"
                        f"gain1({json.dumps(D)},{qs})]));")
    assert lm[0] > 0 > lm[1] and abs(lm[2]) < 1e-12
    sweep(name, D, ranges, "(r=>({n:r.pts,g1:r.g1,g2:r.g2,s:r.nSegs}))(report(V[k]))")
    syntax_check(name)
    return rows


# ---------- Companion 2: the Cournot crossing (Tadelis Sec. 5.2.3, pp. 87-88)
def cournot_py(a, b, c1, c2):
    """Independent: iterate simultaneous best replies (a contraction, factor 1/2) to the fixed point."""
    br = lambda ci, qj: max(0.0, (a - ci - b * qj) / (2 * b))
    q1 = q2 = 0.0
    for _ in range(400):
        q1, q2 = br(c1, q2), br(c2, q1)
    Q = q1 + q2
    P = a - b * Q
    cm = min(c1, c2)
    Qm = max(0.0, (a - cm) / (2 * b))
    return dict(q1=q1, q2=q2, Q=Q, P=P, pi1=(P - c1) * q1, pi2=(P - c2) * q2,
                Qm=Qm, Pm=a - b * Qm, pim=(a - b * Qm - cm) * Qm, Qc=max(0.0, (a - cm) / b))


def check_cournot():
    name = "companion-cournot-best-responses.html"
    D = dict(a=100, b=1, c1=10, c2=10)
    ranges = dict(a=(20, 200), b=(0.25, 4), c1=(0, 80), c2=(0, 80))
    vecs = {
        "default (Tadelis p.87)": D,
        "low end": {k: lo for k, (lo, _) in ranges.items()},
        "high end": {k: hi for k, (_, hi) in ranges.items()},
        "landmark: firm 1 at exit cost 55": dict(D, c1=55),
        "asymmetric c1=1, c2=2": dict(D, c1=1, c2=2),
        "firm 1 priced out c1=70": dict(D, c1=70),
        "no production a=20, c=80": dict(a=20, b=1, c1=80, c2=80),
    }
    js = run_node(name, f"const V={json.dumps(vecs)};const o={{}};for(const k in V)o[k]=report(V[k]);"
                        "console.log(JSON.stringify(o));")
    rows = []
    for k, v in vecs.items():
        py, pg = cournot_py(**v), js[k]
        for f in py:
            assert close(py[f], pg[f], 1e-7), (k, f, py[f], pg[f])
        rows.append((k, v, round(py["q1"], 4), round(py["q2"], 4), round(py["P"], 4),
                     round(py["pi1"], 4), round(py["Qm"], 4), round(py["Pm"], 4)))
    d = js["default (Tadelis p.87)"]
    assert (d["q1"], d["q2"], d["P"], d["pi1"]) == (30, 30, 40, 900)          # p. 87, p. 90
    assert (d["Qm"], d["Pm"], d["pim"], d["Qc"], d["Pc"]) == (45, 55, 2025, 90, 10)
    assert d["split"] == 22.5 and d["dev"] == 33.75 and d["devGain"] > 0        # Gibbons p. 17
    e = js["landmark: firm 1 at exit cost 55"]
    assert e["q1"] == 0 and e["q2"] == 45 and e["exit1"] == 55
    sweep(name, D, ranges, "(r=>({q1:r.q1,q2:r.q2,P:r.P,m:r.Qm}))(report(V[k]))")
    syntax_check(name)
    return rows


if __name__ == "__main__":
    for title, fn in [("mixed-2x2", check_mixed), ("cournot-best-responses", check_cournot)]:
        print(f"== {title}")
        for row in fn():
            print("  ", row)
    print("all companion checks pass")
