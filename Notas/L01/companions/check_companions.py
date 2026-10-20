"""Check the two Lecture 1 companions against independent Python implementations.

For each page: extract the `// MODEL:BEGIN ... // MODEL:END` block, run it under Node at the
default, low-end, high-end and landmark control vectors, and compare every read-out with the
Python value; sweep each control end to end (others at default) and require the read-outs to
change and stay finite; confirm the landmarks sit on the slider grids; syntax-check the page's
whole script. Pattern copied from Aula/aula-01-companions/check_companions.py.

The Python side reuses Listas/lista-lecture-01-check.py (cournot_iesds, partnership_conditions),
loading only its function definitions so its own randomized checks do not run.

Run: python Notas/L01/companions/check_companions.py   (needs `node` on PATH)
Exits non-zero on the first mismatch; prints the three verification vectors per page.
"""
import ast
import itertools
import json
import math
import pathlib
import random
import re
import subprocess
import tempfile
from fractions import Fraction as Fr
from functools import lru_cache

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def lista_functions():
    """Function definitions of Listas/lista-lecture-01-check.py, without running its checks."""
    path = ROOT / "Listas" / "lista-lecture-01-check.py"
    tree = ast.parse(path.read_text(encoding="utf-8"))
    defs = [n for n in tree.body if isinstance(n, ast.FunctionDef)]
    ns = {"Fr": Fr, "itertools": itertools, "lru_cache": lru_cache, "random": random}
    exec(compile(ast.Module(body=defs, type_ignores=[]), str(path), "exec"), ns)
    return ns


LISTA = lista_functions()


def page_script(name):
    html = (HERE / name).read_text(encoding="utf-8")
    return re.search(r"<script>(.*?)</script>", html, re.S).group(1)


def run_node(name, vecs, expr):
    """Run the page's model block on each vector; `expr` is JS evaluated with `p` bound."""
    model = re.search(r"// MODEL:BEGIN.*?// MODEL:END", page_script(name), re.S).group(0)
    body = (f"const V={json.dumps(vecs)};const o={{}};for(const k in V){{const p=V[k];o[k]={expr};}}"
            "console.log(JSON.stringify(o));")
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
    return True


def sweep(name, defaults, ranges, expr):
    """Each control at both ends (others at default): read-outs finite and different from default."""
    vecs = {"default": defaults}
    for k, (lo, hi) in ranges.items():
        vecs[f"{k}=lo"] = dict(defaults, **{k: lo})
        vecs[f"{k}=hi"] = dict(defaults, **{k: hi})
    res = run_node(name, vecs, expr)
    for k, r in res.items():
        assert finite(r), (name, k, r)
        assert "NaN" not in json.dumps(r), (name, k)
    for k in ranges:
        assert res[f"{k}=lo"] != res["default"] or res[f"{k}=hi"] != res["default"], (name, k, "dead control")


# ---------------------------------------------------------------- partnership
def partnership_py(p):
    """Slide 4 partnership with n partners: gain y/n - c, all-E y - c, dilemma y/n < c < y."""
    y, c, n = p["y"], p["c"], p["n"]
    gain = y / n - c
    dom = "E" if gain > 1e-9 else ("S" if gain < -1e-9 else "none")
    dilemma = dom == "S" and y - c > 1e-9
    uE = [y * (k + 1) / n - c for k in range(n)]
    uS = [y * k / n for k in range(n)]
    return dict(gain=gain, dom=dom, allE=y - c, dilemma=dilemma, lo=y / n, hi=y,
                waste=(y - c) if dilemma else 0, uE=uE, uS=uS)


def check_partnership():
    name = "companion-partnership-dominance.html"
    D = dict(y=6, c=4, n=2)
    ranges = dict(y=(0.6, 12), c=(0, 15), n=(2, 6))
    vecs = {"default": D, "low end": dict(y=0.6, c=0, n=2), "high end": dict(y=12, c=15, n=6),
            "landmark c=y/n": dict(y=6, c=3, n=2), "landmark c=y": dict(y=6, c=6, n=2),
            "n=3 dilemma": dict(y=6, c=2.5, n=3)}
    js = run_node(name, vecs, "report(p)")
    rows = []
    for k, v in vecs.items():
        py, pg = partnership_py(v), js[k]
        for f in ["gain", "allE", "lo", "hi", "waste"]:
            assert close(py[f], pg[f]), (k, f, py[f], pg[f])
        assert py["dom"] == pg["dom"] and py["dilemma"] == pg["dilemma"], (k, py, pg)
        assert all(close(a, b) for a, b in zip(py["uE"] + py["uS"], pg["uE"] + pg["uS"])), k
        # independent cross-check: the lista's n-partner dilemma condition with no synergy
        if abs(v["c"] - v["y"] / v["n"]) > 1e-9 and abs(v["c"] - v["y"]) > 1e-9:
            assert LISTA["partnership_conditions"](v["n"], v["y"], 0, v["c"]) == pg["dilemma"], k
        rows.append((k, v, f"gain={py['gain']:.2f}", py["dom"], f"dilemma={py['dilemma']}",
                     f"page gain={pg['gain']:.2f}", pg["dom"], f"page dilemma={pg['dilemma']}"))
    # the default is the slides' PD plus 4: (E,E)=2, (E,S)=-1, (S,E)=3, (S,S)=0
    d = js["default"]
    assert [d["uE"][1], d["uE"][0], d["uS"][1], d["uS"][0]] == [2, -1, 3, 0]
    # landmarks: c = y/n and c = y on the c grid (step 0.01) for every y on its grid (step 0.6) and n
    for j in range(1, 21):
        y = round(0.6 * j, 10)
        for n in range(2, 7):
            assert abs(round(y / n * 100) - y / n * 100) < 1e-6, (y, n)
        assert abs(round(y * 100) - y * 100) < 1e-6
    sweep(name, D, ranges, "report(p)")
    syntax_check(name)
    return rows


# ---------------------------------------------------------------- Cournot IESDS
def cournot_py(p):
    """Interval after k rounds (lista's exact recursion), Cournot point, price, profits."""
    a, b, c1, c2, k = (Fr(str(p[x])) for x in ("a", "b", "c1", "c2", "k"))
    k = int(k)
    if k == 0:
        lo, hi = [0.0, 0.0], [None, None]
    else:
        h = LISTA["cournot_iesds"](a, b, c1, c2, k)[-1]
        lo, hi = [float(x) for x in h[0]], [float(x) for x in h[1]]
    m = [max(0.0, float((a - c1) / (2 * b))), max(0.0, float((a - c2) / (2 * b)))]
    r1, r2 = float((a - 2 * c1 + c2) / (3 * b)), float((a - 2 * c2 + c1) / (3 * b))
    q = [0.0, m[1]] if r1 <= 0 else ([m[0], 0.0] if r2 <= 0 else [r1, r2])
    price = max(0.0, float(a) - float(b) * (q[0] + q[1]))
    prof = [(price - float(c1)) * q[0], (price - float(c2)) * q[1]]
    return dict(L=lo, U=hi, q=q, price=price, profit=prof, m=m)


def check_cournot():
    name = "companion-cournot-iesds.html"
    D = dict(a=100, b=1, c1=10, c2=10, k=3)
    ranges = dict(a=(20, 200), b=(0.5, 5), c1=(0, 60), c2=(0, 60), k=(0, 12))
    vecs = {"default": D, "low end": dict(a=20, b=0.5, c1=0, c2=0, k=0),
            "high end": dict(a=200, b=5, c1=60, c2=60, k=12),
            "exit landmark": dict(a=100, b=1, c1=55, c2=10, k=12),
            "past exit": dict(a=100, b=1, c1=60, c2=10, k=12),
            "costs above a": dict(a=20, b=1, c1=30, c2=60, k=5)}
    expr = "(r=>({L:r.L,U:r.U,q:r.q,price:r.price,profit:r.profit,m:r.m}))(report(p))"
    js = run_node(name, vecs, expr)       # JSON turns Infinity into null
    rows = []
    for k, v in vecs.items():
        py, pg = cournot_py(v), js[k]
        for f in ["L", "U", "q", "profit", "m"]:
            assert all(close(a, b, 1e-9) for a, b in zip(py[f], pg[f])), (k, f, py[f], pg[f])
        assert close(py["price"], pg["price"]), (k, py["price"], pg["price"])
        rows.append((k, v, f"S1={py['L'][0]:.4g}..{py['U'][0] if py['U'][0] is None else round(py['U'][0], 4)}",
                     f"q*=({py['q'][0]:.4g}, {py['q'][1]:.4g})", f"p*={py['price']:.4g}",
                     f"page S1={pg['L'][0]:.4g}..{pg['U'][0] if pg['U'][0] is None else round(pg['U'][0], 4)}",
                     f"page q*=({pg['q'][0]:.4g}, {pg['q'][1]:.4g})"))
    # Tadelis pp. 66-68: rounds 1-3 and the limit
    t = run_node(name, {"r": D}, "report(p).hist.slice(0,3).map(h=>[h.L[0],h.U[0]])")["r"]
    assert t == [[0, 45], [22.5, 45], [22.5, 33.75]], t
    d = cournot_py(D)
    assert d["q"] == [30, 30] and d["price"] == 40 and d["profit"] == [900, 900]
    # exit landmark (a + c2)/2 on the 0.5 grid whenever a and c2 are integers
    assert all(((a + c2) / 2 * 2) % 1 == 0 for a in range(20, 201) for c2 in range(0, 61))
    ex = cournot_py(vecs["exit landmark"])
    assert ex["q"] == [0.0, 45.0] and 0 < ex["U"][0] < 0.05      # at the landmark: 0 only in the limit
    assert cournot_py(vecs["past exit"])["U"][0] == 0                # past it: out in finitely many rounds
    sweep(name, D, ranges, "(r=>({L:r.L,U:r.U,q:r.q,price:r.price}))(report(p))")
    syntax_check(name)
    return rows


if __name__ == "__main__":
    for title, fn in [("partnership-dominance", check_partnership), ("cournot-iesds", check_cournot)]:
        print(f"== {title}")
        for row in fn():
            print("  ", row)
    print("all companion checks pass")
