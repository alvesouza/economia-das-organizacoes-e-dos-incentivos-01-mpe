"""Check the two Lecture 5 companions against independent Python implementations.

Pattern copied from Aula/aula-01-companions/check_companions.py: extract each page's
`// MODEL:BEGIN ... // MODEL:END` block, run it under Node at the default, low-end,
high-end and preset control vectors, compare every read-out with Python, sweep each
control end to end (others at default) and require the read-outs to change and stay
finite, and syntax-check the page's whole script.

Run:  python Notas/L05/companions/check_companions.py   (needs `node` on PATH)
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
    if a is None or b is None or isinstance(a, bool) or isinstance(b, bool):
        return a == b
    return math.isclose(a, b, rel_tol=tol, abs_tol=tol)


def finite(obj):
    if isinstance(obj, float):
        return math.isfinite(obj)
    if isinstance(obj, dict):
        return all(finite(v) for v in obj.values())
    if isinstance(obj, list):
        return all(finite(v) for v in obj)
    return True


def compare(name, vecs, py_fn, fields):
    js = run_node(name, f"const V={json.dumps(vecs)};const o={{}};for(const k in V)o[k]=report(V[k]);"
                        "console.log(JSON.stringify(o));")
    for k, v in vecs.items():
        py, pg = py_fn(v), js[k]
        for f in fields:
            if isinstance(py[f], list):
                assert len(py[f]) == len(pg[f]) and all(close(a, b) for a, b in zip(py[f], pg[f])), (name, k, f)
            else:
                assert close(py[f], pg[f]), (name, k, f, py[f], pg[f])
        assert finite(pg), (name, k, pg)
    return js


def sweep(name, defaults, ranges):
    vecs = {"default": defaults}
    for k, (lo, hi) in ranges.items():
        vecs[f"{k}=lo"] = dict(defaults, **{k: lo})
        vecs[f"{k}=hi"] = dict(defaults, **{k: hi})
    res = run_node(name, f"const V={json.dumps(vecs)};const o={{}};for(const k in V)o[k]=report(V[k]);"
                         "console.log(JSON.stringify(o));")
    for k, r in res.items():
        assert finite(r), (name, k, r)
    for k in ranges:
        assert res[f"{k}=lo"] != res["default"] or res[f"{k}=hi"] != res["default"], (name, k, "dead control")


# ---------- Companion 1: grim trigger (Tadelis (10.3) p. 200; Thm 10.1 pp. 209-214) ----------
def grim_py(s):
    T, R, P, S, d = s["T"], s["R"], s["P"], s["S"], s["d"]
    out = dict(valid=T > R > P > S, gain=T - R, loss=R - P, pvCoop=R / (1 - d), pvDev=T + d * P / (1 - d),
               avgCoop=R, avgDev=(1 - d) * T + d * P, alt1=(T + d * S) / (1 + d), alt2=(S + d * T) / (1 + d))
    if not out["valid"]:
        out.update(dstar=None, sustained=None, dAltBad=None, altOk=None)
        return out
    out["dstar"] = (T - R) / (T - P)                      # (10.5) with v^d=T, v^c=R, v^*=P
    out["sustained"] = d >= out["dstar"] - 1e-12
    out["dAltBad"] = (P - S) / (T - P)
    # alternating path, p. 213-214: bad period (S+dT)/(1+d) >= P; good period vs (1-d)R + dP
    out["altOk"] = out["alt2"] >= P - 1e-12 and out["alt1"] >= (1 - d) * R + d * P - 1e-12
    # cross-check the PV form against the average form (the two must agree)
    assert out["sustained"] == (out["pvCoop"] >= out["pvDev"] - 1e-9)
    return out


def check_grim():
    name = "companion-grim-trigger.html"
    D = dict(T=5, R=4, P=1, S=-1, d=0.5)
    ranges = dict(T=(4, 10), R=(2, 8), P=(-1, 4), S=(-4, 2), d=(0, 0.99))
    vecs = {
        "default": D,
        "low end": dict(T=4, R=2, P=-1, S=-4, d=0.0),
        "high end": dict(T=10, R=8, P=4, S=2, d=0.99),
        "Gibbons p. 90": dict(T=5, R=4, P=1, S=0, d=0.5),
        "landmark d=d*": dict(D, d=0.25),
        "below d*": dict(D, d=0.24),
        "invalid order": dict(D, R=6),
    }
    fields = ["valid", "gain", "loss", "pvCoop", "pvDev", "avgDev", "alt1", "alt2", "dstar", "sustained",
              "dAltBad", "altOk"]
    js = compare(name, vecs, grim_py, fields)
    # book numbers: delta* = 1/4 (p. 200, Gibbons p. 92); alternating path needs delta >= 1/2 (p. 214)
    assert grim_py(D)["dstar"] == 0.25 and grim_py(D)["dAltBad"] == 0.5
    assert grim_py(dict(D, d=0.25))["sustained"] and not grim_py(dict(D, d=0.24))["sustained"]
    assert grim_py(dict(D, d=0.5))["altOk"] and not grim_py(dict(D, d=0.49))["altOk"]
    assert abs(grim_py(dict(D, d=0.9))["alt1"] - 2.158) < 5e-4 and abs(grim_py(dict(D, d=0.9))["alt2"] - 1.842) < 5e-4
    sweep(name, D, ranges)
    syntax_check(name)
    rows = []
    for k in ("default", "low end", "high end"):
        py, pg = grim_py(vecs[k]), js[k]
        rows.append((k, vecs[k], "py", round(py["dstar"], 4), round(py["pvCoop"], 3), round(py["pvDev"], 3),
                     py["sustained"], "page", round(pg["dstar"], 4), round(pg["pvCoop"], 3),
                     round(pg["pvDev"], 3), pg["sustained"]))
    return rows


# ---------- Companion 2: finite carrot and stick (Tadelis p. 191) ----------
def finite_py(s, a=4.0):
    d, T, b, r, p = s["d"], s["T"], s["b"], s["r"], s["p"]

    def path(n):                                           # stage payoffs along the proposed path
        return [a if t <= n else r for t in range(1, T + 1)]

    def loss(t, n):                                        # PV at t of (follow - deviate) from t+1 on
        u = path(n)
        return sum(d ** (s_ - t) * (u[s_ - 1] - p) for s_ in range(t + 1, T + 1))

    feasible = [n for n in range(T) if all(b - a <= loss(t, n) + 1e-12 for t in range(1, n + 1))]
    n = max(feasible)
    carrot = r > p
    u = path(n)
    return dict(n=n, k=T - n, gain=b - a, carrot=carrot,
                d1=(b - a) / (r - p) if carrot else None,
                dInf=(b - a) / (b - a + r - p) if carrot else None,
                slack=loss(n, n) - (b - a) if n > 0 else None,
                losses=[loss(t, n) for t in range(1, n + 1)],
                pv=sum(d ** (t - 1) * u[t - 1] for t in range(1, T + 1)),
                pvr=sum(d ** (t - 1) * r for t in range(1, T + 1)))


def check_finite():
    name = "companion-finite-carrot-stick.html"
    D = dict(d=0.5, T=2, b=5, r=3, p=1)
    ranges = dict(d=(0, 0.99), T=(2, 20), b=(4.25, 8), r=(0.5, 4), p=(0.1, 3))
    vecs = {
        "default": D,
        "low end": dict(d=0.0, T=2, b=4.25, r=0.5, p=0.1),
        "high end": dict(d=0.99, T=20, b=8, r=4, p=3),
        "preset T=10 d=0.4": dict(d=0.4, T=10, b=5, r=3, p=1),
        "below 1/2": dict(D, d=0.49),
        "no carrot": dict(D, r=1.0, p=1.0),
    }
    fields = ["n", "k", "gain", "carrot", "d1", "dInf", "slack", "losses", "pv", "pvr"]
    js = compare(name, vecs, finite_py, fields)
    # book: two-stage game, (M,m) in stage 1 iff delta >= 1/2 (fn. 2, p. 191)
    assert finite_py(D)["n"] == 1 and finite_py(dict(D, d=0.49))["n"] == 0
    assert finite_py(D)["d1"] == 0.5 and abs(finite_py(D)["dInf"] - 1 / 3) < 1e-12
    # independent closed form for the last cooperative round with k reward rounds
    s = vecs["preset T=10 d=0.4"]
    k = finite_py(s)["k"]
    assert k == 2 and 2 * 0.4 * (1 - 0.4 ** k) / 0.6 >= 1 > 2 * 0.4 * (1 - 0.4) / 0.6
    assert finite_py(vecs["no carrot"])["n"] == 0
    sweep(name, D, dict(d=(0, 0.99), T=(2, 20), b=(4.25, 8), r=(0.5, 4), p=(0.1, 3)))
    syntax_check(name)
    rows = []
    for k_ in ("default", "low end", "high end"):
        py, pg = finite_py(vecs[k_]), js[k_]
        rows.append((k_, vecs[k_], "py", py["n"], py["d1"] and round(py["d1"], 4), round(py["pv"], 3),
                     "page", pg["n"], pg["d1"] and round(pg["d1"], 4), round(pg["pv"], 3)))
    return rows


if __name__ == "__main__":
    for title, fn in [("grim-trigger", check_grim), ("finite-carrot-stick", check_finite)]:
        print(f"== {title}")
        for row in fn():
            print("  ", row)
    print("all companion checks pass")
