"""Check the three Aula 1 companions against independent Python implementations.

For each page: extract the `// MODEL:BEGIN ... // MODEL:END` block, run it under Node at
the default, low-end, high-end and preset control vectors, and compare every read-out with
the Python value; sweep each control end to end (others at default) and require the read-outs
to change and stay finite; syntax-check the page's whole script.

Run from this directory: python check_companions.py   (needs `node` on PATH)
Exits non-zero on the first mismatch.
"""
import json
import math
import re
import subprocess
import sys
import tempfile
from itertools import permutations
from pathlib import Path

import model_two_systems as m2

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
    return math.isclose(a, b, rel_tol=tol, abs_tol=tol)


def finite(obj):
    if isinstance(obj, float):
        return math.isfinite(obj)
    if isinstance(obj, dict):
        return all(finite(v) for v in obj.values())
    if isinstance(obj, list):
        return all(finite(v) for v in obj)
    return True


def sweep(name, defaults, ranges, js_call):
    """Each control at both ends (others default): read-outs finite and different from default."""
    vecs = {"default": defaults}
    for k, (lo, hi) in ranges.items():
        vecs[f"{k}=lo"] = dict(defaults, **{k: lo})
        vecs[f"{k}=hi"] = dict(defaults, **{k: hi})
    res = run_node(name, f"const V={json.dumps(vecs)};const o={{}};for(const k in V)o[k]={js_call};"
                         "console.log(JSON.stringify(o));")
    for k, r in res.items():
        assert finite(r), (name, k, r)
    for k in ranges:
        assert res[f"{k}=lo"] != res["default"] or res[f"{k}=hi"] != res["default"], (name, k, "dead control")
    return res


# ---------- Companion 1: two coherent systems ----------
def check_two_systems():
    name = "two_systems.html"
    D = dict(m2.DEFAULTS)
    ranges = dict(A=(5, 60), Q=(20, 400), h=(0.2, 3), Sf=(0.5, 20), dc=(0, 2))
    vecs = {
        "default": D,
        "low end": {k: lo for k, (lo, _) in ranges.items()},
        "high end": {k: hi for k, (_, hi) in ranges.items()},
        "preset A=30": dict(D, A=30),
        "preset dc=0.85": dict(D, dc=0.85),
    }
    js = run_node(name, f"const V={json.dumps(vecs)};const o={{}};for(const k in V)o[k]=report(V[k]);"
                        "console.log(JSON.stringify(o));")
    rows = []
    for k, v in vecs.items():
        py, pg = m2.report(**v), js[k]
        for key, idx in [("F", 0), ("T", 1)]:
            for j, field in enumerate(["n", "b", "profit"]):
                assert close(py[key][j], pg[key][field]), (k, key, field, py[key][j], pg[key][field])
        assert close(py["nhat"], pg["nhat"]) and py["F_coh"] == pg["Fcoh"] and py["T_coh"] == pg["Tcoh"], k
        assert close(py.get("valley"), pg["valley"], 1e-6), (k, py.get("valley"), pg["valley"])
        rows.append((k, v, round(py["F"][2], 2), round(py["T"][2], 2), round(py["nhat"], 2),
                     None if py.get("valley") is None else round(py["valley"], 2), py["F_coh"], py["T_coh"]))
    sweep(name, D, ranges, "report(V[k])")
    # landmark: the n = 1 corner is reachable (specialized corner at defaults; flexible corner at A=5)
    assert m2.report(**D)["F"][3] and m2.report(**dict(D, A=5))["T"][3]
    # at each coherent point, neither manager gains from a small move (it is a local max)
    for v in vecs.values():
        r = m2.report(**v)
        for key, S, dc, coh in [("F", m2.S_S, 0, r["F_coh"]), ("T", v["Sf"], v["dc"], r["T_coh"])]:
            if not coh:
                continue
            n, b, pi, _ = r[key]
            f = lambda n_, b_: m2.M * v["Q"] + v["A"] * math.log(n_) - S * v["Q"] / b_ - v["h"] * n_ * b_ / 2 - dc * v["Q"]
            for dn, db in [(1.01, 1), (0.99, 1), (1, 1.01), (1, 0.99)]:
                if n * dn >= 1:
                    assert f(n * dn, b * db) <= pi + 1e-9, (key, v)
    syntax_check(name)
    return rows


# ---------- Companion 2: the valley ----------
def cube_py(p):
    pay = {}
    for J in (0, 1):
        for T in (0, 1):
            for S in (0, 1):
                pay[f"{J}{T}{S}"] = (10 + p["vJ"] * J + p["vT"] * T + p["vS"] * S + p["iJT"] * J * T
                                     + p["iJS"] * J * S + p["iTS"] * T * S + p["iJTS"] * J * T * S)
    worsts = []
    for order in permutations(range(3)):
        v, seq = [0, 0, 0], []
        for i in order:
            v[i] = 1
            seq.append(pay["".join(map(str, v))])
        worsts.append(min(seq))
    first = [pay["100"], pay["010"], pay["001"]]
    last = [pay["011"], pay["101"], pay["110"]]
    # supermodularity on the lattice {0,1}^3, by the definition (join + meet >= sum)
    keys = list(pay)
    sm = all(pay["".join(max(a, b) for a, b in zip(x, y))] + pay["".join(min(a, b) for a, b in zip(x, y))]
             >= pay[x] + pay[y] for x in keys for y in keys)
    return dict(pay=pay, bestWorst=max(worsts), gain=pay["111"] - pay["000"],
                bestFirst=max(first) - pay["000"], fordLocal=all(x < pay["000"] for x in first),
                fullLocal=all(x < pay["111"] for x in last), supermodular=sm)


def check_valley():
    name = "valley.html"
    D = dict(vJ=-4, vT=-2, vS=-1, iJT=4, iJS=5, iTS=2, iJTS=2)
    ranges = dict(vJ=(-8, 4), vT=(-8, 4), vS=(-8, 4), iJT=(-4, 8), iJS=(-4, 8), iTS=(-4, 8), iJTS=(-6, 6))
    vecs = {
        "default": D,
        "low end": {k: lo for k, (lo, _) in ranges.items()},
        "high end": {k: hi for k, (_, hi) in ranges.items()},
        "preset additive": dict(D, iJT=0, iJS=0, iTS=0, iJTS=0),
        "preset no losses": dict(D, vJ=0, vT=0, vS=0),
    }
    js = run_node(name, f"const V={json.dumps(vecs)};const o={{}};for(const k in V){{const r=report(V[k]);"
                        "o[k]={pay:r.pay,bestWorst:r.best.worst,gain:r.gain,bestFirst:r.bestFirst,fordLocal:r.fordLocal,"
                        "fullLocal:r.fullLocal,supermodular:r.fails.length===0};}console.log(JSON.stringify(o));")
    rows = []
    for k, v in vecs.items():
        py = cube_py(v)
        assert py == js[k], (k, py, js[k])
        rows.append((k, py["pay"]["111"], py["gain"], py["bestWorst"], py["bestFirst"], py["supermodular"]))
    # the video's cube is the default
    assert [cube_py(D)["pay"][x] for x in ["000", "100", "010", "001", "110", "101", "011", "111"]] == [10, 6, 8, 9, 8, 10, 9, 16]
    assert cube_py(D)["bestWorst"] == 9 and cube_py(dict(D, vJ=0, vT=0, vS=0))["bestWorst"] >= 10
    sweep(name, D, ranges, "(r=>({pay:r.pay,w:r.best.worst,f:r.fails}))(report(V[k]))")
    syntax_check(name)
    return rows


# ---------- Companion 3: the multiplier ----------
def multi_py(p):
    d = p["c"] ** 2 - p["b"] ** 2
    if d <= 0:
        return None
    x = (p["c"] * p["t"] + p["b"] * p["s"]) / d
    y = (p["c"] * p["s"] + p["b"] * p["t"]) / d
    # FOCs hold
    assert abs(p["t"] + p["b"] * y - p["c"] * x) < 1e-9 and abs(p["s"] + p["b"] * x - p["c"] * y) < 1e-9
    return dict(x=x, y=y, dxdt=p["c"] / d, dydt=p["b"] / d, mult=1 / (1 - (p["b"] / p["c"]) ** 2))


def check_multiplier():
    name = "multiplier.html"
    D = dict(t=1, s=1, b=1, c=2)
    ranges = dict(t=(0, 4), s=(0, 4), b=(-1.9, 1.9), c=(1, 4))
    vecs = {
        "default": D,
        "low end": dict(t=0, s=0, b=-1.9, c=4),
        "high end": dict(t=4, s=4, b=1.9, c=4),
        "preset b=0": dict(D, b=0),
        "preset b=-1": dict(D, b=-1),
        "degenerate": dict(D, b=1.5, c=1.0),
    }
    js = run_node(name, f"const V={json.dumps(vecs)};const o={{}};for(const k in V){{const s=solve(V[k]);"
                        "o[k]=s.ok?{x:s.x,y:s.y,dxdt:s.dxdt,dydt:s.dydt,mult:s.mult,rounds:staircase(V[k],s).rounds}:null;}"
                        "console.log(JSON.stringify(o));")
    rows = []
    for k, v in vecs.items():
        py, pg = multi_py(v), js[k]
        if py is None:
            assert pg is None, k
            rows.append((k, v, "no maximum"))
            continue
        for f in ["x", "y", "dxdt", "dydt", "mult"]:
            assert close(py[f], pg[f]), (k, f, py[f], pg[f])
        rows.append((k, v, round(py["x"], 3), round(py["y"], 3), round(py["mult"], 3), round(py["dydt"], 3), pg["rounds"]))
    assert close(multi_py(D)["mult"], 4 / 3) and multi_py(dict(D, b=0))["mult"] == 1.0
    # the default staircase starts at (0.5, 0.5) and converges to (1, 1)
    assert close(multi_py(D)["x"], 1) and close(multi_py(D)["y"], 1)
    sweep(name, D, dict(t=(0, 4), s=(0, 4), b=(-1.9, 1.9), c=(2, 4)),
          "(s=>s.ok?{x:s.x,y:s.y,m:s.mult}:'none')(solve(V[k]))")
    syntax_check(name)
    return rows


if __name__ == "__main__":
    for title, fn in [("two_systems", check_two_systems), ("valley", check_valley), ("multiplier", check_multiplier)]:
        print(f"== {title}")
        for row in fn():
            print("  ", row)
    print("all companion checks pass")
    sys.exit(0)
