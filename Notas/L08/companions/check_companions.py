"""Check the two Lecture 8 companions against independent Python implementations.

For each page: extract the `// MODEL:BEGIN ... // MODEL:END` block, run it under Node at the
default, all-low and all-high control vectors (plus landmark presets), and compare every read-out
with Python; sweep each control end to end (others at default) and require the read-outs to change
and stay finite; syntax-check the page's whole script. Pattern from Aula/aula-01-companions.

Run:  python Notas/L08/companions/check_companions.py   (needs `node` on PATH). Exits non-zero
on the first mismatch and prints the verification table otherwise.
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
    return re.search(r"<script>(.*?)</script>", (HERE / name).read_text(encoding="utf-8"), re.S).group(1)


def run_node(name, body):
    """Run the page's model block followed by `body` (JS that prints JSON); return parsed JSON."""
    model = re.search(r"// MODEL:BEGIN.*?// MODEL:END", page_script(name), re.S).group(0)
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as f:
        f.write(model + "\n" + body)
    return json.loads(subprocess.run(["node", f.name], capture_output=True, text=True, check=True).stdout)


def syntax_check(name):
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as f:
        f.write(page_script(name))
    subprocess.run(["node", "--check", f.name], check=True)


def close(a, b, tol=1e-9):
    if a is None or b is None:
        return a is None and b is None
    if isinstance(a, bool) or isinstance(b, bool) or isinstance(a, str):
        return a == b
    return math.isclose(float(a), float(b), rel_tol=tol, abs_tol=tol)


def finite(o):
    if isinstance(o, float):
        return math.isfinite(o)
    if isinstance(o, dict):
        return all(finite(v) for v in o.values())
    if isinstance(o, list):
        return all(finite(v) for v in o)
    return True


def eval_vectors(name, vecs, js_fn):
    js = ",".join(f"{json.dumps(k)}:{js_fn}({json.dumps(v)})" for k, v in vecs.items())
    return run_node(name, f"console.log(JSON.stringify({{{js}}}));")


def sweep(name, defaults, ranges, js_fn):
    """Each control at both ends (others at default): finite read-outs, and the control is live."""
    vecs = {"default": defaults}
    for k, (lo, hi) in ranges.items():
        vecs[f"{k}=lo"] = dict(defaults, **{k: lo})
        vecs[f"{k}=hi"] = dict(defaults, **{k: hi})
    res = eval_vectors(name, vecs, js_fn)
    for k, r in res.items():
        assert finite(r), (name, k, r)
    for k in ranges:
        assert res[f"{k}=lo"] != res["default"] or res[f"{k}=hi"] != res["default"], (name, k, "dead control")


# ---------------------------------------------------------------- Spence (M&R pp. 155-156)
def spence_py(tL, tH, p, cL, cH):
    """Independent closed forms: separating IC_L and IC_H, pooled wage, pooling bound, H's gain."""
    d = tH - tL
    wbar = p * tH + (1 - p) * tL
    out = dict(sc=cH < cL, wbar=wbar, epMax=p * d / max(cH, cL), Lloss=wbar - tL,
               sepLo=None, sepHi=None, eStar=None, Hlcs=None, Hgain=None, pStar=None, burned=None, side=None)
    if cH < cL:
        e_star = d / cL                                   # tL = tH - cL e
        out.update(sepLo=e_star, sepHi=d / cH, eStar=e_star, Hlcs=tH - cH * e_star,
                   pStar=1 - cH / cL, burned=p * cH * e_star)
        out["Hgain"] = out["Hlcs"] - wbar
        out["side"] = "at" if abs(p - out["pStar"]) < 1e-9 else ("below" if p < out["pStar"] else "above")
    return out


def check_spence():
    name = "companion-spence-signaling.html"
    D = dict(tL=20, tH=50, p=0.30, cL=20, cH=10)
    ranges = dict(tL=(0, 28), tH=(30, 100), p=(0.01, 0.99), cL=(1, 40), cH=(1, 40))
    vecs = {"default": D,
            "low end": {k: lo for k, (lo, _) in ranges.items()},
            "high end": {k: hi for k, (_, hi) in ranges.items()},
            "landmark p = p*": dict(D, p=0.5),
            "landmark cH = cL": dict(D, cH=20),
            "cH > cL": dict(D, cH=30)}
    js = eval_vectors(name, vecs, "model")
    rows = []
    for k, v in vecs.items():
        py, pg = spence_py(**v), js[k]
        for key, val in py.items():
            assert close(val, pg[key]), (k, key, val, pg[key])
        rows.append((k, v, {x: (round(py[x], 4) if isinstance(py[x], float) else py[x])
                            for x in ("eStar", "sepHi", "wbar", "epMax", "Hgain", "side")}))
    # the book's numbers at the default (M&R pp. 155-156)
    d = js["default"]
    assert (d["sepLo"], d["sepHi"]) == (1.5, 3) and close(d["wbar"], 29) and close(d["Hlcs"], 35)
    assert js["landmark p = p*"]["side"] == "at" and js["landmark cH = cL"]["knife"] is True
    assert js["cH > cL"]["eStar"] is None                                    # no separation
    assert spence_py(20, 50, 0.49, 20, 10)["side"] == "below" and spence_py(20, 50, 0.51, 20, 10)["side"] == "above"
    sweep(name, D, ranges, "model")
    syntax_check(name)
    return rows


# ---------------------------------------------------------------- MBA game (Tadelis pp. 319-323)
PROF = {("H", "M"): 10, ("H", "B"): 5, ("L", "M"): 0, ("L", "B"): 3}


def br_interval(a):
    """Beliefs Pr(H) at which job a is a weak best response (employer profits, p. 320)."""
    b = "B" if a == "M" else "M"
    d1, d2 = PROF[("H", a)] - PROF[("H", b)], PROF[("L", a)] - PROF[("L", b)]
    lo, hi = Fr(0), Fr(1)
    if d1 - d2 > 0:
        lo = max(lo, Fr(-d2, d1 - d2))
    elif d1 - d2 < 0:
        hi = min(hi, Fr(-d2, d1 - d2))
    elif d2 < 0:
        return None
    return (lo, hi) if lo <= hi else None


def mba_py(p, cH, cL, wM, wB):
    """Every pure PBE by enumeration, in exact arithmetic, with the intuitive-criterion verdict."""
    p, cH, cL, wM, wB = (Fr(x).limit_denominator(1000) for x in (p, cH, cL, wM, wB))
    u1 = lambda t, m, a: (wM if a == "M" else wB) - ((cH if t == "H" else cL) if m == "D" else 0)
    eqs = []
    for sm, ra in product(["UU", "UD", "DU", "DD"], ["MM", "MB", "BM", "BB"]):
        snd, rsp = {"H": sm[0], "L": sm[1]}, {"U": ra[0], "D": ra[1]}
        bel, ok = {}, True
        for m in "UD":
            iv = br_interval(rsp[m])
            den = p * (snd["H"] == m) + (1 - p) * (snd["L"] == m)
            if den == 0:
                ok, bel[m] = iv is not None, iv
            else:
                mu = p * (snd["H"] == m) / den
                ok, bel[m] = iv is not None and iv[0] <= mu <= iv[1], mu
            if not ok:
                break
        if not ok or not all(u1(t, snd[t], rsp[snd[t]]) >= u1(t, m, rsp[m]) for t in "HL" for m in "UD"):
            continue
        star = {t: u1(t, snd[t], rsp[snd[t]]) for t in "HL"}
        fails = False
        for m in "UD":
            if m in snd.values():
                continue
            keep = [t for t in "HL" if max(u1(t, m, a) for a in "MB") >= star[t]]
            if len(keep) == 1:
                mu = 1 if keep == ["H"] else 0
                br = [a for a in "MB" if br_interval(a)[0] <= mu <= br_interval(a)[1]]
                fails |= min(u1(keep[0], m, a) for a in br) > star[keep[0]]
        eqs.append(dict(sender=sm, receiver=ra, muU=bel["U"], muD=bel["D"],
                        kind="pooling" if sm[0] == sm[1] else "separating", intuitive=not fails))
    return eqs


def same_belief(a, b):
    if isinstance(a, tuple):
        return isinstance(b, list) and close(a[0], b[0]) and close(a[1], b[1])
    return not isinstance(b, list) and close(a, b)


def check_mba():
    name = "companion-mba-game.html"
    D = dict(p=0.25, cH=2, cL=5, wM=10, wB=6)
    ranges = dict(p=(0, 1), cH=(0, 12), cL=(0, 12), wM=(0, 16), wB=(0, 16))
    vecs = {"default": D,
            "low end": {k: lo for k, (lo, _) in ranges.items()},
            "high end": {k: hi for k, (_, hi) in ranges.items()},
            "landmark p = 3/8": dict(D, p=0.375),
            "p = 0.5": dict(D, p=0.5),
            "cL = 3 (L mimics)": dict(D, cL=3)}
    js = eval_vectors(name, vecs, "report")
    rows = []
    for k, v in vecs.items():
        py, pg = mba_py(**v), js[k]["eqs"]
        assert len(py) == len(pg), (k, py, pg)
        for a, b in zip(py, pg):
            for key in ("sender", "receiver", "kind", "intuitive"):
                assert a[key] == b[key], (k, key, a, b)
            assert same_belief(a["muU"], b["muU"]) and same_belief(a["muD"], b["muD"]), (k, a, b)
        assert close(js[k]["threshold"], 0.375)
        rows.append((k, v, [(e["sender"], e["receiver"], "IC ok" if e["intuitive"] else "IC fails") for e in py]))
    # the book's answer at the default (pp. 322-323, 334)
    dflt = {(e["sender"], e["receiver"]): e for e in js["default"]["eqs"]}
    assert set(dflt) == {("DU", "BM"), ("UU", "BB")}
    assert dflt[("UU", "BB")]["muD"] == [0, 0.375] and not dflt[("UU", "BB")]["intuitive"]
    assert dflt[("DU", "BM")]["intuitive"]
    sweep(name, D, ranges, "report")
    syntax_check(name)
    return rows


if __name__ == "__main__":
    for title, rows in [("Spence", check_spence()), ("MBA", check_mba())]:
        print(f"== {title}: Python == page at every vector")
        for k, v, out in rows:
            print(f"  {k:20s} {v}\n  {'':20s} -> {out}")
    print("All companion checks passed.")
