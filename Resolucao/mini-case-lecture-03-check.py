"""Checks every number in Resolucao/mini-case-lecture-03.tex and mini-case-lecture-03-short.tex.

Lecture 3 mini case "Work or shirk?" (Aula/Lecture03.pdf, PDF pages 77-78 = deck slides 41-42).
Employee (rows) W/S, manager (columns) M/N, payoffs (employee, manager):
(W,M) = (w-g, v-w-h), (W,N) = (w-g, v-w), (S,M) = (0, -h), (S,N) = (w, -w).
p = Pr(S), q = Pr(M). Run: python Resolucao/mini-case-lecture-03-check.py
"""
from fractions import Fraction as F
import sympy as sp

w, g, v, h, p, q, d = sp.symbols("w g v h p q delta", positive=True)
CELLS = [("W", "M"), ("W", "N"), ("S", "M"), ("S", "N")]


def game(w, g, v, h):
    """Payoff table {(employee action, manager action): (u_E, u_M)}."""
    return {("W", "M"): (w - g, v - w - h), ("W", "N"): (w - g, v - w),
            ("S", "M"): (0, -h), ("S", "N"): (w, -w)}


def other(a):
    return {"W": "S", "S": "W", "M": "N", "N": "M"}[a]


def pure_ne(G):
    """Pure Nash equilibria by checking both unilateral deviations in every cell."""
    return [(e, m) for e, m in CELLS
            if G[(e, m)][0] >= G[(other(e), m)][0] and G[(e, m)][1] >= G[(e, other(m))][1]]


def mixed(w, g, v, h):
    """Solve both indifference conditions exactly; return p*, q*, u_E*, u_M*."""
    G = game(w, g, v, h)
    # Employee indifferent between W and S given q -> pins q.
    qs = sp.solve(sp.Eq(q * G["W", "M"][0] + (1 - q) * G["W", "N"][0],
                        q * G["S", "M"][0] + (1 - q) * G["S", "N"][0]), q)
    # Manager indifferent between M and N given p -> pins p.
    ps = sp.solve(sp.Eq((1 - p) * G["W", "M"][1] + p * G["S", "M"][1],
                        (1 - p) * G["W", "N"][1] + p * G["S", "N"][1]), p)
    assert len(qs) == 1 and len(ps) == 1
    ps, qs = sp.nsimplify(ps[0]), sp.nsimplify(qs[0])
    uE = sp.simplify(qs * G["S", "M"][0] + (1 - qs) * G["S", "N"][0])
    uM = sp.simplify((1 - ps) * G["W", "N"][1] + ps * G["S", "N"][1])
    return ps, qs, uE, uM


# ---- (a) best-response cycle, numerically and in general --------------------------------
base_par = dict(w=10, g=2, v=20, h=1)


def sym(par):
    """Map a str-keyed parameter dict to the positive sympy symbols used in .subs()."""
    return {{"w": w, "g": g, "v": v, "h": h}[k]: sp.nsimplify(x) for k, x in par.items()}


base = sym(base_par)
Gb = game(**base_par)
assert pure_ne(Gb) == []
# Deviation gains around the cycle (W,M)->(W,N)->(S,N)->(S,M)->(W,M).
Gs = game(w, g, v, h)
gains = [Gs["W", "N"][1] - Gs["W", "M"][1],   # manager drops monitoring: h
         Gs["S", "N"][0] - Gs["W", "N"][0],   # employee shirks: g
         Gs["S", "M"][1] - Gs["S", "N"][1],   # manager monitors: w - h
         Gs["W", "M"][0] - Gs["S", "M"][0]]   # employee works: w - g
assert [sp.simplify(x) for x in gains] == [h, g, w - h, w - g]
assert [x.subs(base) for x in gains] == [1, 2, 9, 8]
print("(a) pure NE:", pure_ne(Gb), "; deviation gains around the cycle:", [x.subs(base) for x in gains],
      "= [h, g, w-h, w-g] > 0 iff 0<h<w and 0<g<w")

# ---- (b) mixed NE, general and base ---------------------------------------------------------
P, Q, UE, UM = mixed(w, g, v, h)
assert sp.simplify(P - h / w) == 0 and sp.simplify(Q - g / w) == 0
assert sp.simplify(UE - (w - g)) == 0
assert sp.simplify(UM - (v - w - h * v / w)) == 0
assert sp.simplify(UM - ((1 - h / w) * (v - w) - h)) == 0      # the (1-p*)(v-w) - h form
# Expected-payoff lines in the base case.
uEW, uES = Gb["W", "M"][0], q * 0 + (1 - q) * 10
uMM = sp.expand((1 - p) * Gb["W", "M"][1] + p * Gb["S", "M"][1])
uMN = sp.expand((1 - p) * Gb["W", "N"][1] + p * Gb["S", "N"][1])
assert uEW == 8 and sp.expand(uES) == 10 - 10 * q
assert uMM == 9 - 10 * p and uMN == 10 - 20 * p
pb, qb, uEb, uMb = (x.subs(base) for x in (P, Q, UE, UM))
assert (pb, qb, uEb, uMb) == (F(1, 10), F(1, 5), 8, 8)
outcome = {(e, m): (pb if e == "S" else 1 - pb) * (qb if m == "M" else 1 - qb) for e, m in CELLS}
assert outcome == {("W", "M"): F(9, 50), ("W", "N"): F(18, 25), ("S", "M"): F(1, 50), ("S", "N"): F(2, 25)}
assert sum(outcome.values()) == 1
# Check the mixed payoffs against the full expected-payoff formula u_i(sigma).
assert sum(outcome[c] * Gb[c][0] for c in CELLS) == 8 and sum(outcome[c] * Gb[c][1] for c in CELLS) == 8
print("(b) u_E(W,q)=8, u_E(S,q)=10-10q; u_M(M,p)=9-10p, u_M(N,p)=10-20p")
print("    p* = Pr(S) =", pb, " q* = Pr(M) =", qb, " u_E* =", uEb, " u_M* =", uMb)
print("    outcome distribution:", {k: str(x) for k, x in outcome.items()})

# ---- (c) h = 1/2, (d) w = 20 ---------------------------------------------------------------
res = {}
for name, par in [("base", base_par), ("(c) h=1/2", dict(base_par, h=F(1, 2))), ("(d) w=20", dict(base_par, w=20))]:
    assert pure_ne(game(**par)) == []
    res[name] = tuple(x.subs(sym(par)) for x in (P, Q, UE, UM))
    print(f"{name:10s} p* = {res[name][0]}, q* = {res[name][1]}, u_E* = {res[name][2]}, u_M* = {res[name][3]}")
assert res["(c) h=1/2"] == (F(1, 20), F(1, 5), 8, 9)
assert res["(d) w=20"] == (F(1, 20), F(1, 10), 18, -1)

# ---- (e) comparative statics and the firm's payoff ------------------------------------------
assert [sp.diff(P, x) for x in (w, g, v, h)] == [-h / w**2, 0, 0, 1 / w]
assert [sp.diff(Q, x) for x in (w, g, v, h)] == [-g / w**2, 1 / w, 0, 0]
pi = v - w - h * v / w
assert sp.simplify(sp.diff(pi, h) + v / w) == 0
assert sp.simplify(sp.diff(pi, w) - (-1 + h * v / w**2)) == 0
assert sp.simplify(sp.diff(pi, v) - (1 - h / w)) == 0
assert sp.diff(pi, h).subs(base) == -2 and sp.diff(pi, w).subs(base) == F(-4, 5)
assert sp.diff(pi, v).subs(base) == F(9, 10)
wstar = sp.solve(sp.Eq(sp.diff(pi, w), 0), w)
assert wstar == [sp.sqrt(h * v)]
assert sp.simplify(sp.diff(pi, w, 2) + 2 * h * v / w**3) == 0          # < 0: a maximum
ws = sp.sqrt(20)
assert ws == 2 * sp.sqrt(5) and abs(float(ws) - 4.4721) < 1e-4
assert ws > 2 and ws > 1                                               # g < w*, h < w*: still no pure NE
assert sp.simplify(pi.subs(w, sp.sqrt(h * v)) - (v - 2 * sp.sqrt(h * v))) == 0
pis = pi.subs({v: 20, h: 1, w: ws})
assert sp.simplify(pis - (20 - 4 * sp.sqrt(5))) == 0 and abs(float(pis) - 11.056) < 1e-3
assert abs(float(ws - 2) - 2.472) < 1e-3                               # employee payoff w* - g
assert sp.simplify(P.subs({h: 1, w: ws}) - 1 / ws) == 0 and abs(float(1 / ws) - 0.2236) < 1e-4
assert abs(float(2 / ws) - 0.4472) < 1e-4                              # q* at w*
print("(e) p* = h/w, q* = g/w, u_E* = w-g, pi(w,h) = v - w - hv/w")
print("    dpi/dh = -v/w =", sp.diff(pi, h).subs(base), "; dpi/dw = -1 + hv/w^2 =", sp.diff(pi, w).subs(base))
print(f"    argmax_w pi = sqrt(hv) = sqrt(20) = {float(ws):.4f}; pi there = 20 - 4 sqrt(5) = {float(pis):.4f};"
      f" u_E there = {float(ws - 2):.4f}; p* = {float(1 / ws):.4f}, q* = {float(2 / ws):.4f}")

# Imperfect detection delta in (0,1]: a monitored shirker is caught with probability delta.
Gd = {("W", "M"): (w - g, v - w - h), ("W", "N"): (w - g, v - w),
      ("S", "M"): ((1 - d) * w, -h - (1 - d) * w), ("S", "N"): (w, -w)}
qd = sp.solve(sp.Eq(w - g, q * Gd["S", "M"][0] + (1 - q) * w), q)[0]
pdl = sp.solve(sp.Eq((1 - p) * Gd["W", "M"][1] + p * Gd["S", "M"][1], (1 - p) * (v - w) + p * (-w)), p)[0]
assert sp.simplify(qd - g / (d * w)) == 0 and sp.simplify(pdl - h / (d * w)) == 0
pid = sp.simplify((1 - pdl) * (v - w) + pdl * (-w))
assert sp.simplify(pid - (v - w - h * v / (d * w))) == 0
assert sp.simplify(pid.subs(d, 1) - pi) == 0
print("    detection delta: p* = h/(delta w), q* = g/(delta w), pi = v - w - hv/(delta w)")

# Comparison of the two levers from the base case.
assert res["(c) h=1/2"][3] - res["base"][3] == 1 and res["(d) w=20"][3] - res["base"][3] == -9

# ---- commitment variant (Lecture 3: first mover, credibility) ------------------------------
# Manager commits to a monitoring probability q before the employee chooses; the employee observes q.
# Employee works iff w - g >= (1 - q) w, i.e. q >= g/w (ties broken toward W).
qc = g / w
assert sp.simplify((w - g) - (1 - qc) * w) == 0
pic = v - w - qc * h
assert sp.simplify(pic - (v - w - h * g / w)) == 0
assert pic.subs(base) == F(49, 5)                                      # 9.8
assert sp.simplify(pic - pi - h * (v - g) / w) == 0                   # gain over Nash = h(v-g)/w
assert (pic - pi).subs(base) == F(9, 5)                                # 1.8
assert (v - w - h).subs(base) == 9 and (-w).subs(base) == -10          # commit q=1: 9; q=0: employee shirks, -10
# Ex post, once the employee works, monitoring costs h and catches no one: N beats M (time inconsistency).
assert (Gs["W", "N"][1] - Gs["W", "M"][1]) == h
print(f"(e) commitment: q = g/w = {qc.subs(base)}, p = 0, pi = v - w - hg/w = {pic.subs(base)}"
      f" (= {float(pic.subs(base))}) > {res['base'][3]}; gain h(v-g)/w = {(pic - pi).subs(base)}")
# ---- critique: dismissal destroys a future rent R >= 0 on top of the wage ------------------
R = sp.symbols("R", nonnegative=True)
qR = sp.solve(sp.Eq(w - g, q * (-R) + (1 - q) * w), q)[0]
assert sp.simplify(qR - g / (w + R)) == 0                              # less monitoring needed; p* = h/w unchanged
print("    dismissal rent R: q* = g/(w+R); p* = h/w unchanged")
# ---- extra identities quoted in the text ----------------------------------------------------
# Payoff differences behind each indifference condition.
uMM_g = (1 - p) * Gs["W", "M"][1] + p * Gs["S", "M"][1]
uMN_g = (1 - p) * Gs["W", "N"][1] + p * Gs["S", "N"][1]
assert sp.simplify(uMM_g - ((1 - p) * (v - w) - h)) == 0 and sp.simplify(uMN_g - ((v - w) - p * v)) == 0
assert sp.simplify(uMM_g - uMN_g - (p * w - h)) == 0                  # monitoring: saves w with prob p, costs h
uES_g = q * Gs["S", "M"][0] + (1 - q) * Gs["S", "N"][0]
assert sp.simplify(uES_g - (w - g) - (g - q * w)) == 0                # shirking: saves g, loses w with prob q
assert sp.simplify(UM - (v - w - P * v)) == 0                          # pi = v - w - p* v
# Expected-payoff lines for (c) and (d).
for par, lines in [(dict(base_par, h=F(1, 2)), (8, 10 - 10 * q, F(19, 2) - 10 * p, 10 - 20 * p)),
                   (dict(base_par, w=20), (18, 20 - 20 * q, -1, -20 * p))]:
    sb = sym(par)
    got = (sp.expand((w - g).subs(sb)), sp.expand(uES_g.subs(sb)), sp.expand(uMM_g.subs(sb)), sp.expand(uMN_g.subs(sb)))
    assert got == tuple(sp.nsimplify(x) for x in lines), got
# Base-case matrix for (d): W row (18,-1),(18,0); S row (0,-1),(20,-20).
assert game(20, 2, 20, 1) == {("W", "M"): (18, -1), ("W", "N"): (18, 0), ("S", "M"): (0, -1), ("S", "N"): (20, -20)}
# Commitment combined with cheaper monitoring (h = 1/2): 10 - (1/2)(1/5) = 9.9.
assert pic.subs(sym(dict(base_par, h=F(1, 2)))) == F(99, 10)
# Not committing to any q < g/w: the employee shirks and the firm gets q(-h) + (1-q)(-w) < 0.
assert all(qq * (-1) + (1 - qq) * (-10) < 0 for qq in (F(0), F(1, 10), F(19, 100)))
# Participation threshold: the in-model optimal wage leaves the employee sqrt(hv) - g.
assert sp.simplify((ws - 2) - (2 * sp.sqrt(5) - 2)) == 0
# (c): at the old p = 0.1 the manager now strictly prefers M (8.5 > 8); p* v falls 2 -> 1 in (c) and (d).
sc = sym(dict(base_par, h=F(1, 2)))
assert uMM_g.subs(sc).subs(p, F(1, 10)) == F(17, 2) and uMN_g.subs(sc).subs(p, F(1, 10)) == 8
assert (P * v).subs(base) == 2 and (P * v).subs(sc) == 1 and (P * v).subs(sym(dict(base_par, w=20))) == 1
# Raising w to 20: sure transfer 10, shirking loss saved 1 -> net -9.
assert (res["(d) w=20"][3] - res["base"][3]) == -(20 - 10) + (2 - 1)
# False positives: a monitored worker is wrongly flagged w.p. phi -> q* = g/((1-phi) w) > g/w.
phi = sp.symbols("phi", positive=True)
qfp = sp.solve(sp.Eq(w - g - q * phi * w, (1 - q) * w), q)[0]
assert sp.simplify(qfp - g / ((1 - phi) * w)) == 0
print("    identities: u_M(M,p)-u_M(N,p) = pw - h; u_E(S,q)-u_E(W,q) = g - qw; pi = v - w - p* v;"
      " commitment with h=1/2: pi =", pic.subs(sym(dict(base_par, h=F(1, 2)))))
print("all checks passed")
