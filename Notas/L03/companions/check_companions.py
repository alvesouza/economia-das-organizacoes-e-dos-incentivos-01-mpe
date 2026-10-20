"""Check the two Lecture 3 companions against independent Python implementations.

For each page: extract the `// MODEL:BEGIN ... // MODEL:END` block, run it under Node at
the default, low-end and high-end control vectors (plus presets and landmarks), and compare
every read-out with the Python value; sweep each control end to end (others at default) and
require the read-outs to change and stay finite; syntax-check the page's whole script.
Pattern copied from Aula/aula-01-companions/check_companions.py.

Run: python Notas/L03/companions/check_companions.py   (needs `node` on PATH)
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
    model = re.search(r"// MODEL:BEGIN.*?// MODEL:END", page_script(name), re.S).group(0)
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as f:
        f.write(model + "\n" + body)
    return json.loads(subprocess.run(["node", f.name], capture_output=True, text=True, check=True).stdout)


def syntax_check(name):
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as f:
        f.write(page_script(name))
    subprocess.run(["node", "--check", f.name], check=True)


def close(a, b, tol=1e-9):
    return math.isclose(a, b, rel_tol=tol, abs_tol=tol)


def finite(o):
    if isinstance(o, float):
        return math.isfinite(o)
    if isinstance(o, dict):
        return all(finite(v) for v in o.values())
    if isinstance(o, list):
        return all(finite(v) for v in o)
    return True


def sweep(name, defaults, ranges):
    vecs = {"default": defaults}
    for k, (lo, hi) in ranges.items():
        vecs[f"{k}=lo"], vecs[f"{k}=hi"] = dict(defaults, **{k: lo}), dict(defaults, **{k: hi})
    res = run_node(name, f"const V={json.dumps(vecs)};const o={{}};for(const k in V)o[k]=report(V[k]);"
                         "console.log(JSON.stringify(o));")
    for k, r in res.items():
        assert finite(r), (name, k, r)
    for k in ranges:
        assert res[f"{k}=lo"] != res["default"] or res[f"{k}=hi"] != res["default"], (name, k, "dead control")


# ---------- Companion 1: Stackelberg vs Cournot (Tadelis 8.3.2, pp. 160-163) ----------
def br(q, a, b, c):
    return max(0.0, (a - c - b * q) / (2 * b))


def prof(q1, q2, v):
    P = max(0.0, v["a"] - v["b"] * (q1 + q2))
    return dict(q1=q1, q2=q2, P=P, pi1=(P - v["c1"]) * q1, pi2=(P - v["c2"]) * q2)


def cournot_py(v):
    a, b, c1, c2 = v["a"], v["b"], v["c1"], v["c2"]
    q1, q2 = (a - 2 * c1 + c2) / (3 * b), (a - 2 * c2 + c1) / (3 * b)
    if q1 < 0:
        q1, q2 = 0.0, br(0, a, b, c2)
    elif q2 < 0:
        q1, q2 = br(0, a, b, c1), 0.0
    return prof(q1, q2, v)


def stackelberg_py(v, n=200000):
    """Independent path: brute-force the leader's problem on a fine grid, then polish."""
    a, b, c1, c2 = v["a"], v["b"], v["c1"], v["c2"]
    top = max((a - c1) / b, (a - c2) / b, 1.0)
    f = lambda q: prof(q, br(q, a, b, c2), v)["pi1"]
    q = max((top * k / n for k in range(n + 1)), key=f)
    # polish with the closed forms on whichever piece the grid optimum sits
    kink = max(0.0, (a - c2) / b)
    cands = [q, min(max((a - 2 * c1 + c2) / (2 * b), 0), kink), max((a - c1) / (2 * b), kink)]
    q = max(cands, key=f)
    return prof(q, br(q, a, b, c2), v)


def check_stackelberg():
    name = "companion-stackelberg-vs-cournot.html"
    D = dict(a=100, b=1, c1=10, c2=10)
    ranges = dict(a=(40, 200), b=(0.5, 3), c1=(0, 60), c2=(0, 90))
    vecs = {"default": D,
            "low end": {k: lo for k, (lo, _) in ranges.items()},
            "high end": {k: hi for k, (_, hi) in ranges.items()},
            "landmark c2=40 (S shut-out)": dict(D, c2=40),
            "landmark c2=55 (C shut-out)": dict(D, c2=55),
            "c2=0": dict(D, c2=0), "c1=c2=60, a=40": dict(a=40, b=1, c1=60, c2=60)}
    js = run_node(name, f"const V={json.dumps(vecs)};const o={{}};for(const k in V)o[k]=report(V[k]);"
                        "console.log(JSON.stringify(o));")
    rows = []
    for k, v in vecs.items():
        S, C, pg = stackelberg_py(v), cournot_py(v), js[k]
        for game, py in (("S", S), ("C", C)):
            for f in ("q1", "q2", "P", "pi1", "pi2"):
                assert close(py[f], pg[game][f], 1e-6), (k, game, f, py[f], pg[game][f])
        assert close(S["pi1"] - C["pi1"], pg["fma"], 1e-6) and S["pi1"] - C["pi1"] >= -1e-9, k
        rows.append((k, v, {"S": (round(S["q1"], 3), round(S["q2"], 3), round(S["pi1"], 2), round(S["pi2"], 2)),
                            "C": (round(C["q1"], 3), round(C["q2"], 3), round(C["pi1"], 2), round(C["pi2"], 2)),
                            "fma": round(S["pi1"] - C["pi1"], 2)}))
    d = js["default"]
    assert (d["S"]["q1"], d["S"]["q2"], d["S"]["pi1"], d["S"]["pi2"]) == (45, 22.5, 1012.5, 506.25)   # p. 161
    assert (d["C"]["q1"], d["C"]["pi1"]) == (30, 900) and close(d["ratio"], 9 / 8)
    assert js["landmark c2=40 (S shut-out)"]["S"]["q2"] == 0 and js["default"]["S"]["q2"] > 0
    assert js["landmark c2=55 (C shut-out)"]["C"]["q2"] == 0 and js["landmark c2=40 (S shut-out)"]["C"]["q2"] > 0
    sweep(name, D, ranges)
    syntax_check(name)
    return rows


# ---------- Companion 2: entry deterrence and the bond (Cabral 7.2, pp. 167-171) -------
def entry_py(v):
    """Backward induction written out branch by branch (ties: accommodate, stay out, no bond)."""
    def post(di):
        fight = v["FI"] > di
        e_pay, i_pay = (v["FE"], v["FI"]) if fight else (v["DE"], di)
        enter = e_pay > 0
        return fight, enter, (e_pay, i_pay) if enter else (0, v["M"])
    nb, wb = post(v["DI"]), post(v["DI"] - v["B"])
    buy = wb[2][1] > nb[2][1]
    return dict(nb=nb, wb=wb, buy=buy, value=(wb if buy else nb)[2][1] - nb[2][1], Bstar=v["DI"] - v["FI"])


def check_entry():
    name = "companion-entry-commitment.html"
    D = dict(M=50, DE=10, DI=20, FE=-10, FI=10, B=40)
    ranges = dict(M=(0, 100), DE=(-20, 40), DI=(0, 60), FE=(-40, 20), FI=(-40, 40), B=(0, 80))
    vecs = {"default": D,
            "low end": {k: lo for k, (lo, _) in ranges.items()},
            "high end": {k: hi for k, (_, hi) in ranges.items()},
            "landmark B=B*=10": dict(D, B=10), "B=11": dict(D, B=11),
            "text payoff FI=-10": dict(D, FI=-10),
            "MWG 9.B.1": dict(M=2, DE=2, DI=1, FE=-3, FI=-1, B=0)}
    js = run_node(name, f"const V={json.dumps(vecs)};const o={{}};for(const k in V)o[k]=report(V[k]);"
                        "console.log(JSON.stringify(o));")
    rows = []
    for k, v in vecs.items():
        py, pg = entry_py(v), js[k]
        for br_ in ("nb", "wb"):
            fight, enter, pay = py[br_]
            assert (fight, enter, list(pay)) == (pg[br_]["fight"], pg[br_]["enter"], pg[br_]["pay"]), (k, br_, py[br_], pg[br_])
        assert (py["buy"], py["value"], py["Bstar"]) == (pg["buy"], pg["value"], pg["Bstar"]), (k, py, pg)
        rows.append((k, v, {"no bond": py["nb"][2], "bond": py["wb"][2], "buy": py["buy"], "value": py["value"]}))
    d = js["default"]
    assert d["nb"]["pay"] == [10, 20] and d["wb"]["pay"] == [0, 50] and d["value"] == 30   # pp. 169-170
    assert js["landmark B=B*=10"]["wb"]["tieI"] and not js["landmark B=B*=10"]["buy"] and js["B=11"]["buy"]
    assert js["text payoff FI=-10"]["value"] == 30
    assert js["MWG 9.B.1"]["nb"]["pay"] == [2, 1] and not js["MWG 9.B.1"]["credibleNoBond"]
    sweep(name, D, ranges)
    syntax_check(name)
    return rows


if __name__ == "__main__":
    for title, fn in [("stackelberg-vs-cournot", check_stackelberg), ("entry-commitment", check_entry)]:
        print(f"== {title}")
        for row in fn():
            print("  ", row)
    print("all companion checks pass")
