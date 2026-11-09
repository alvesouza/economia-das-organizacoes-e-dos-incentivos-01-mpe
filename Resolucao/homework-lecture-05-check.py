"""Checks every number in Resolucao/homework-lecture-05.tex and homework-lecture-05-short.tex.

Lecture 5 homework "Tacit collusion in oligopoly" (Aula/Lecture05.pdf, slide 34).
Repeated Cournot duopoly, P = 100 - q1 - q2, C = 10 q; general case P = a - b Q, MC = c.
Run: python Resolucao/homework-lecture-05-check.py
"""
from fractions import Fraction as F
import math
import sympy as sp

a, b, c, n, q, qj, d = sp.symbols("a b c n q q_j delta", positive=True)


def profit(a, b, c, qi, Q):
    """Stage profit of a firm with output qi when industry output is Q."""
    return (a - b * Q - c) * qi


def stage_numbers(a, b, c):
    """Exact (q_N, pi_N, q_C, pi_C, q_D, pi_D) for the duopoly from first principles."""
    a, b, c = F(a), F(b), F(c)
    br = lambda qo: (a - c - b * qo) / (2 * b)            # FOC of (a - b(qi+qo) - c) qi
    qN = (a - c) / (3 * b)                                 # fixed point q = br(q)
    assert br(qN) == qN
    qm = (a - c) / (2 * b)                                 # monopoly output
    qC = qm / 2
    qD = br(qC)
    piN, piC, piD = (profit(a, b, c, x, y) for x, y in [(qN, 2 * qN), (qC, 2 * qC), (qD, qD + qC)])
    return qN, piN, qC, piC, qD, piD


def delta_star(piN, piC, piD):
    """Grim-trigger threshold from piC/(1-d) >= piD + d piN/(1-d)."""
    return (piD - piC) / (piD - piN)


# ---- items 1-2: numbers -------------------------------------------------------------------
qN, piN, qC, piC, qD, piD = stage_numbers(100, 1, 10)
assert (qN, piN, qC, piC, qD, piD) == (30, 900, F(45, 2), F(2025, 2), F(135, 4), F(18225, 16))
assert piC == F(1012.5) and piD == F(1139.0625)
pr = lambda Q: 100 - Q
assert (pr(2 * qN), pr(2 * qC), pr(qD + qC)) == (40, 55, F(175, 4))        # prices 40, 55, 43.75
# Monopoly: max (100 - Q - 10) Q  -> Q = 45, profit 2025, half each = 1012.5
Qm = sp.symbols("Q")
assert sp.solve(sp.diff((100 - Qm - 10) * Qm, Qm), Qm) == [45] and (100 - 45 - 10) * 45 == 2025
# Best-response functions and the three points
assert (100 - 10 - qC) / 2 == qD and (100 - 10 - qN) / 2 == qN
# Cartel is not a stage NE: deviation strictly profitable
assert piD > piC > piN
print("(1) Cournot q =", qN, " pi_N =", piN, " price", pr(2 * qN))
print("    Cartel  Q = 45, q =", float(qC), " pi_C =", float(piC), " price", pr(2 * qC), " (monopoly profit 2025)")
print("(2) Deviation q =", float(qD), " pi_D =", float(piD), " price", float(pr(qD + qC)))

# ---- item 3: threshold, on and off the path ------------------------------------------------
ds = delta_star(piN, piC, piD)
assert ds == F(9, 17) and abs(float(ds) - 0.5294) < 1e-4
assert piD - piC == F(2025, 16) and piD - piN == F(3825, 16)               # 126.5625, 239.0625
assert F(2025, 16) == F(126.5625) and F(3825, 16) == F(239.0625)
# Condition in each form, at delta just below / at / above 9/17
comply = lambda dl: piC                                                    # normalised payoff
deviate = lambda dl: (1 - dl) * piD + dl * piN
assert comply(ds) == deviate(ds)
assert comply(F(1, 2)) < deviate(F(1, 2)) and comply(F(6, 10)) > deviate(F(6, 10))
# Unnormalised form: piC/(1-d) >= piD + d piN/(1-d) <=> same threshold
dd = sp.symbols("dd")
assert sp.solve(sp.Eq(sp.Rational(2025, 2) / (1 - dd), sp.Rational(18225, 16) + dd * 900 / (1 - dd)), dd) == [sp.Rational(9, 17)]
# Off the path: after any deviation the profile prescribes Cournot forever; a one-shot deviation x
# from q = 30 yields (1-d)(100 - x - 30 - 10) x + d 900 <= 900, since x = 30 maximises the stage profit.
xs = sp.symbols("x")
assert sp.solve(sp.diff((100 - xs - 30 - 10) * xs, xs), xs) == [30]
assert all((100 - x - 30 - 10) * x <= 900 for x in range(0, 101))
print("(3) delta* =", ds, "=", round(float(ds), 4), "; pi_D - pi_C =", float(piD - piC), ", pi_D - pi_N =", float(piD - piN))

# ---- item 4: general a, b, c ----------------------------------------------------------------
k = (a - c) ** 2 / b
Q_ = sp.symbols("Q_")
qN_s = sp.solve(sp.Eq(q, (a - c - b * q) / (2 * b)), q)[0]
piN_s = sp.simplify(profit(a, b, c, qN_s, 2 * qN_s))
Qm_s = sp.solve(sp.diff((a - b * Q_ - c) * Q_, Q_), Q_)[0]
qC_s = Qm_s / 2
piC_s = sp.simplify(profit(a, b, c, qC_s, Qm_s))
qD_s = sp.solve(sp.diff(profit(a, b, c, qj, qj + qC_s), qj), qj)[0]
piD_s = sp.simplify(profit(a, b, c, qD_s, qD_s + qC_s))
assert sp.simplify(qN_s - (a - c) / (3 * b)) == 0 and sp.simplify(piN_s - k / 9) == 0
assert sp.simplify(qC_s - (a - c) / (4 * b)) == 0 and sp.simplify(piC_s - k / 8) == 0
assert sp.simplify(qD_s - 3 * (a - c) / (8 * b)) == 0 and sp.simplify(piD_s - 9 * k / 64) == 0
assert sp.simplify(piD_s - piC_s - k / 64) == 0 and sp.simplify(piD_s - piN_s - 17 * k / 576) == 0
ds_s = sp.simplify((piD_s - piC_s) / (piD_s - piN_s))
assert ds_s == sp.Rational(9, 17)
for A, B, C in [(100, 1, 10), (50, 2, 5), (7, F(1, 3), 0), (1000, 10, 999), (13, 5, F(1, 2))]:
    r = stage_numbers(A, B, C)
    assert delta_star(r[1], r[3], r[5]) == F(9, 17), (A, B, C)
    assert (r[1], r[3], r[5]) == tuple(F(x) * F((A - C) ** 2) / F(B) for x in (F(1, 9), F(1, 8), F(9, 64)))
print("(4) pi_N = (a-c)^2/9b, pi_C = (a-c)^2/8b, pi_D = 9(a-c)^2/64b; delta* =", ds_s, "for all a, b, c<a (symbolic + 5 triples)")

# ---- item 5: n firms from first principles ---------------------------------------------------
def n_firm(nn, a=F(100), b=F(1), c=F(10)):
    """Threshold for n symmetric Cournot firms, built from best responses."""
    nn = F(nn)
    # symmetric Nash: q = (a - c - b (n-1) q) / (2b)
    qN = (a - c) / (b * (nn + 1))
    assert qN == (a - c - b * (nn - 1) * qN) / (2 * b)
    qC = (a - c) / (2 * b) / nn
    qD = (a - c - b * (nn - 1) * qC) / (2 * b)
    pN, pC, pD = (profit(a, b, c, x, y) for x, y in [(qN, nn * qN), (qC, nn * qC), (qD, qD + (nn - 1) * qC)])
    return delta_star(pN, pC, pD), (pN, pC, pD)

expected = {2: F(9, 17), 3: F(4, 7), 4: F(25, 41), 5: F(9, 14), 10: F(121, 161)}
table = {}
for nn in range(2, 11):
    ds_n, _ = n_firm(nn)
    assert ds_n == F((nn + 1) ** 2, nn ** 2 + 6 * nn + 1), nn
    assert n_firm(nn, F(7), F(3, 2), F(1))[0] == ds_n                       # parameter-free
    table[nn] = ds_n
for nn, v in expected.items():
    assert table[nn] == v
assert all(table[i] < table[i + 1] for i in range(2, 10))                  # increasing in n
assert all(float(v) < 1 for v in table.values())
# Symbolic in n
nq = (a - c) / (b * (n + 1))
cq = (a - c) / (2 * b * n)
dq = (a - c - b * (n - 1) * cq) / (2 * b)
pN_n, pC_n, pD_n = (sp.simplify(profit(a, b, c, x, y)) for x, y in [(nq, n * nq), (cq, n * cq), (dq, dq + (n - 1) * cq)])
assert sp.simplify(pN_n - k / (n + 1) ** 2) == 0 and sp.simplify(pC_n - k / (4 * n)) == 0
assert sp.simplify(pD_n - k * (n + 1) ** 2 / (16 * n ** 2)) == 0
assert sp.simplify((pD_n - pC_n) / (pD_n - pN_n) - (n + 1) ** 2 / (n ** 2 + 6 * n + 1)) == 0
assert sp.limit((n + 1) ** 2 / (n ** 2 + 6 * n + 1), n, sp.oo) == 1
assert sp.simplify((pD_n - pC_n).subs(n, 2) - k / 64) == 0
print("(5) n-firm threshold (n+1)^2/(n^2+6n+1):", {i: str(v) for i, v in table.items()})
print("    decimals:", {i: round(float(v), 4) for i, v in table.items()})
# delta = exp(-r dt): collusion needs r dt <= ln(17/9)
rdt = math.log(17 / 9)
assert abs(rdt - 0.6360) < 1e-4 and abs(math.exp(-rdt) - 9 / 17) < 1e-12
print("    delta = exp(-r dt): duopoly needs r dt <= ln(17/9) =", round(rdt, 4))
# Numbers quoted in the text
assert piC - piN == F(225, 2) and qD * F(225, 10) == F(60750, 80) == F(759.375)
assert F(1, 2) * piD + F(1, 2) * piN == F(1019.53125) and F(8100) == F(90) ** 2
assert sp.simplify((pD_n - pC_n) - k * (n - 1) ** 2 / (16 * n ** 2)) == 0
assert sp.simplify((pC_n - pN_n) - k * (n - 1) ** 2 / (4 * n * (n + 1) ** 2)) == 0
assert sp.simplify((pD_n - pC_n) / (pC_n - pN_n) - (n + 1) ** 2 / (4 * n)) == 0   # gain / loss
print("    gain/loss = (n+1)^2/(4n); gain = k(n-1)^2/(16n^2); loss = k(n-1)^2/(4n(n+1)^2); text numbers ok")
print("all checks passed")
