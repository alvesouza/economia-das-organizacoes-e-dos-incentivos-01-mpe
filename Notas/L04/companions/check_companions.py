"""Check the two Lecture 4 companions against independent Python implementations.

For each page: extract the `// MODEL:BEGIN ... // MODEL:END` block, run it under Node at the
default, low-end and high-end control vectors (plus the presets), and compare every read-out with
Python; sweep each control end to end (others at default) and require the read-outs to change and
stay finite; check the landmarks; syntax-check the page's whole script.
Pattern copied from Aula/aula-01-companions/check_companions.py.

The Rubinstein page is checked against `proposer_share` from
Aula/notes-aulas-01-02/check_part2.py, read out of that file with `ast` so that importing it does
not run that script's own (slow) checks.

Run: python Notas/L04/companions/check_companions.py   (needs `node` on PATH)
Exits non-zero on the first mismatch; prints the three verification vectors per page.
"""
import ast
import json
import math
import re
import subprocess
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def load_function(path, name):
    """Return function `name` defined at top level of `path`, without executing the module."""
    tree = ast.parse(Path(path).read_text(encoding="utf-8"))
    node = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == name)
    ns = {}
    exec(compile(ast.Module([node], []), str(path), "exec"), ns)
    return ns[name]


proposer_share = load_function(ROOT / "Aula/notes-aulas-01-02/check_part2.py", "proposer_share")


def page_script(name):
    html = (HERE / name).read_text(encoding="utf-8")
    return re.search(r"<script>(.*?)</script>", html, re.S).group(1)


def run_node(name, vecs):
    """Run the page's model block on every vector in `vecs`; return {key: report(vec)}."""
    model = re.search(r"// MODEL:BEGIN.*?// MODEL:END", page_script(name), re.S).group(0)
    body = (f"const V={json.dumps(vecs)};const o={{}};for(const k in V)o[k]=report(V[k]);"
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
        return a is None and b is None
    if isinstance(a, bool) or isinstance(b, bool):
        return a == b
    return math.isclose(a, b, rel_tol=tol, abs_tol=tol)


def compare(name, py_fn, vecs):
    js = run_node(name, vecs)
    for k, v in vecs.items():
        py = py_fn(v)
        for field, val in py.items():
            assert close(val, js[k][field]), (name, k, field, val, js[k][field])
    return js


def sweep(name, defaults, ranges):
    """Each control at both ends (others default): read-outs finite and not all unchanged."""
    vecs = {"default": defaults}
    for k, (lo, hi) in ranges.items():
        vecs[f"{k}=lo"] = dict(defaults, **{k: lo})
        vecs[f"{k}=hi"] = dict(defaults, **{k: hi})
    res = run_node(name, vecs)
    for k, r in res.items():
        for f, x in r.items():
            assert x is None or not isinstance(x, float) or math.isfinite(x), (name, k, f)
    for k in ranges:
        assert res[f"{k}=lo"] != res["default"] or res[f"{k}=hi"] != res["default"], (name, k, "dead control")


# ---------- Companion 1: Rubinstein bargaining ----------
def rub_py(p):
    """Independent read-outs: shares from check_part2.proposer_share and the closed form."""
    d1, d2 = p["d1"], p["d2"]
    lim = (1 - d2) / (1 - d1 * d2) if 1 - d1 * d2 > 1e-12 else None
    x1 = lim if p["inf"] else proposer_share(p["T"], d1, d2)
    return {"x1": x1, "lim": lim,
            "pay1": None if x1 is None else p["v"] * x1,
            "pay2": None if x1 is None else p["v"] * (1 - x1),
            "gap": None if (p["inf"] or lim is None) else x1 - lim,
            "adv": None if x1 is None else 2 * x1 - 1,
            "last": 0 if p["inf"] else (1 if p["T"] % 2 else 2)}


def check_rubinstein():
    name = "companion-rubinstein-bargaining.html"
    D = dict(d1=0.6, d2=0.6, T=3, inf=False, v=1)
    vecs = {
        "default": D,
        "low end": dict(d1=0.0, d2=0.0, T=1, inf=False, v=1),
        "high end": dict(d1=1.0, d2=1.0, T=40, inf=False, v=100),
        "default, no deadline": dict(D, inf=True),
        "high end, no deadline": dict(d1=1.0, d2=1.0, T=40, inf=True, v=100),
        "preset delta=1, T=39": dict(d1=1, d2=1, T=39, inf=False, v=1),
        "asymmetric .9/.7, T=3": dict(d1=0.9, d2=0.7, T=3, inf=False, v=1),
        "asymmetric .9/.7, inf": dict(d1=0.9, d2=0.7, T=3, inf=True, v=1),
    }
    js = compare(name, rub_py, vecs)
    # book values: Gibbons p. 70 three-period offer 1 - d(1 - d s) with s = 1; Tadelis (11.1), (11.4)-(11.5)
    assert close(js["default"]["x1"], 0.76) and close(js["default"]["lim"], 0.625)
    assert js["low end"]["x1"] == 1                       # ultimatum / delta = 0: proposer takes all
    assert js["high end"]["x1"] == 0                      # delta = 1, T even: last mover (player 2) takes all
    assert js["high end, no deadline"]["x1"] is None      # degenerate case labelled, never NaN
    assert js["preset delta=1, T=39"]["x1"] == 1          # Tadelis fn. 2, p. 227
    assert close(js["asymmetric .9/.7, T=3"]["x1"], 0.93) and close(js["asymmetric .9/.7, inf"]["x1"], 0.3 / 0.37)
    for T in range(1, 41):                                # (11.1) and its even-T twin, delta = 0.6
        assert close(rub_py(dict(D, T=T))["x1"], (1 - (-0.6) ** T) / 1.6)
    sweep(name, D, dict(d1=(0.0, 1.0), d2=(0.0, 1.0), T=(1, 40), v=(1, 100), inf=(False, True)))
    syntax_check(name)
    return [(k, vecs[k], js[k]) for k in ("default", "low end", "high end")]


# ---------- Companion 2: carrot and stick (Prisoner-Revenge) ----------
def cs_py(p):
    """Tadelis pp. 182-184 with R = 4, P = 1, carrot 0 fixed."""
    pun = 0 - p["st"]
    stay1, dev1 = 4.0, p["Tm"] + p["d"] * p["st"]
    stay2, dev2 = p["Sk"], 1 + p["d"] * p["st"]
    okMm, okFm = stay1 >= dev1 - 1e-12, stay2 >= dev2 - 1e-12
    return {"dMm": (p["Tm"] - 4) / pun if pun > 0 else None,
            "dFm": (1 - p["Sk"]) / pun if pun > 0 else None,
            "stay1": stay1, "dev1": dev1, "stay2": stay2, "dev2": dev2,
            "okMm": okMm, "okFm": okFm, "count": 1 + okMm + 2 * okFm}


def check_carrot_stick():
    name = "companion-carrot-and-stick.html"
    D = dict(d=0.5, Tm=5, Sk=-1, st=-3)
    vecs = {
        "default": D,
        "low end": dict(d=0.0, Tm=4.1, Sk=-5, st=-4),
        "high end": dict(d=1.0, Tm=10, Sk=0.9, st=0),
        "delta = 1/3": dict(D, d=1 / 3),
        "delta = 2/3": dict(D, d=2 / 3),
        "delta = 0.33": dict(D, d=0.33),
    }
    js = compare(name, cs_py, vecs)
    assert close(js["default"]["dMm"], 1 / 3) and close(js["default"]["dFm"], 2 / 3)   # pp. 183-184
    assert js["delta = 1/3"]["okMm"] and not js["delta = 0.33"]["okMm"]                  # flips exactly at 1/3
    assert js["delta = 2/3"]["okFm"] and not js["default"]["okFm"]                        # flips exactly at 2/3
    assert js["high end"]["dMm"] is None                                                  # s = 0: no stick
    sweep(name, D, dict(d=(0.0, 1.0), Tm=(4.1, 10), Sk=(-5, 0.9), st=(-4, 0)))
    syntax_check(name)
    return [(k, vecs[k], js[k]) for k in ("default", "low end", "high end")]


if __name__ == "__main__":
    for title, rows in [("Rubinstein bargaining", check_rubinstein()),
                        ("Carrot and stick", check_carrot_stick())]:
        print(f"== {title}: Python == page (node) on every read-out")
        for k, v, r in rows:
            short = {f: (round(x, 4) if isinstance(x, float) else x) for f, x in r.items()}
            print(f"  {k:9s} {v}\n            -> {short}")
    print("all companion checks pass")
