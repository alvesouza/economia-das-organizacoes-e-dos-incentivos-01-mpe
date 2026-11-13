"""Checks every number and equilibrium claim in the five new Lecture 4 solutions:
sol-gibbons-2-6, sol-munoz-garcia-4-12, sol-tadelis-8-15, sol-tadelis-8-12, sol-tadelis-8-16.
(The other 7 items are reused from ../lista-reais-lectures-01-05-solutions/, checked by
check_B_L04.py and check_D.py there.) Exact arithmetic (sympy, fractions); backward induction
is computed, not typed in.

Run: python check_L04.py  -> one line per item and "all L04 checks passed", or an
AssertionError on the first wrong claim.
"""
from fractions import Fraction as F
from itertools import product

import sympy as sp

# ----------------------------------------------------------------------------- gibbons-2-6
a, c, q1, q2, q3 = sp.symbols("a c q1 q2 q3", positive=True)
P = a - q1 - q2 - q3
# stage 2: followers' Cournot game after q1
sol2 = sp.solve([sp.diff((P - c) * q2, q2), sp.diff((P - c) * q3, q3)], [q2, q3], dict=True)
assert len(sol2) == 1
f2, f3 = sol2[0][q2], sol2[0][q3]
assert sp.simplify(f2 - (a - c - q1) / 3) == 0 and sp.simplify(f3 - f2) == 0
# stage 1: the leader
pi1 = sp.simplify(((P - c) * q1).subs({q2: f2, q3: f3}))
assert sp.simplify(pi1 - (a - c - q1) * q1 / 3) == 0
q1s = sp.solve(sp.diff(pi1, q1), q1)[0]
assert sp.simplify(q1s - (a - c) / 2) == 0
q2s = sp.simplify(f2.subs(q1, q1s))
Ps = sp.simplify(P.subs({q1: q1s, q2: q2s, q3: q2s}))
assert sp.simplify(q2s - (a - c) / 6) == 0 and sp.simplify(Ps - (a + 5 * c) / 6) == 0
prof1 = sp.simplify((Ps - c) * q1s)
prof2 = sp.simplify((Ps - c) * q2s)
assert sp.simplify(prof1 - (a - c) ** 2 / 12) == 0 and sp.simplify(prof2 - (a - c) ** 2 / 36) == 0
cournot = (a - c) ** 2 / 16                       # three-firm Cournot profit
assert sp.simplify(prof1 / cournot - sp.Rational(4, 3)) == 0 and sp.simplify(prof2 / cournot - sp.Rational(4, 9)) == 0
# grid: (a-c)/2 maximises the leader's profit for a = 100, c = 10 (exact fractions)
A_, C_ = 100, 10
grid = [F(i, 4) for i in range(0, 4 * (A_ - C_) + 1)]
best = max(grid, key=lambda x: (A_ - C_ - x) * x / 3)
assert best == F(A_ - C_, 2)
print("gibbons-2-6: q = ((a-c)/2, (a-c)/6, (a-c)/6), P = (a+5c)/6")

# ----------------------------------------------------------------------------- munoz-garcia-4-12
Q1, Q2, Q3 = sp.symbols("Q1 Q2 Q3", real=True)
Pm = 10 - Q1 - Q2 - Q3
mc = 2


def br(profit, var):
    return sp.solve(sp.diff(profit, var), var)[0]


# (a) two firms
b2 = br((Pm.subs(Q3, 0) - mc) * Q2, Q2)
assert sp.simplify(b2 - (4 - Q1 / 2)) == 0
lead = (Pm.subs({Q3: 0, Q2: b2}) - mc) * Q1
qa1 = br(lead, Q1)
qa2 = b2.subs(Q1, qa1)
pa = Pm.subs({Q3: 0, Q1: qa1, Q2: qa2})
assert (qa1, qa2, pa) == (4, 2, 4)
assert ((pa - mc) * qa1, (pa - mc) * qa2) == (8, 4)
# (b) three firms, firm 3 last
b3 = br((Pm - mc) * Q3, Q3)
assert sp.simplify(b3 - (4 - (Q1 + Q2) / 2)) == 0
p2 = (Pm.subs(Q3, b3) - mc) * Q2
assert sp.simplify(p2 - (4 - Q1 / 2 - Q2 / 2) * Q2) == 0
b2c = br(p2, Q2)
assert sp.simplify(b2c - (4 - Q1 / 2)) == 0
b3c = sp.simplify(b3.subs(Q2, b2c))
assert sp.simplify(b3c - (2 - Q1 / 4)) == 0
margin1 = sp.simplify(Pm.subs({Q2: b2c, Q3: b3c}) - mc)
assert sp.simplify(margin1 - (2 - Q1 / 4)) == 0
qb1 = br(margin1 * Q1, Q1)
qb2, qb3 = b2c.subs(Q1, qb1), b3c.subs(Q1, qb1)
pb = Pm.subs({Q1: qb1, Q2: qb2, Q3: qb3})
assert (qb1, qb2, qb3, pb) == (4, 2, 1, 3)
assert ((pb - mc) * qb1, (pb - mc) * qb2, (pb - mc) * qb3) == (4, 2, 1)
# the entrant halves the earlier movers' margins, so their maximisers are unchanged
assert sp.simplify((Pm.subs({Q3: b3}) - mc).subs(Q2, Q2) - (Pm.subs({Q3: 0}) - mc) / 2) == 0
# no unilateral gain along the reply functions (integer grid), three firms
rep3 = lambda x1, x2: F(8 - x1 - x2, 2)
rep2 = lambda x1: 4 - F(x1, 2)
prof = lambda i, x: (10 - sum(x) - 2) * x[i]
x_star = (F(4), F(2), F(1))
assert all(prof(0, (F(d, 4), rep2(F(d, 4)), rep3(F(d, 4), rep2(F(d, 4))))) <= prof(0, x_star) for d in range(0, 4 * 8 + 1))
assert all(prof(1, (F(4), F(d, 4), rep3(F(4), F(d, 4)))) <= prof(1, x_star) for d in range(0, 4 * 8 + 1))
assert all(prof(2, (F(4), F(2), F(d, 4))) <= prof(2, x_star) for d in range(0, 4 * 8 + 1))
print("munoz-garcia-4-12: (a) q = (4, 2), p = 4; (b) q = (4, 2, 1), p = 3")

# ----------------------------------------------------------------------------- tadelis-8-15, 8-16
K = sp.symbols("K", positive=True)
x1, x2, x3 = sp.symbols("x1 x2 x3", positive=True)
beta = sp.Rational(1, 2)
# (a) naive plan
v = sp.log(x1) + beta * sp.log(x2) + beta * sp.log(x3)
s = sp.solve([sp.diff(v.subs(x1, K - x2 - x3), x2), sp.diff(v.subs(x1, K - x2 - x3), x3)], [x2, x3], dict=True)[0]
n2, n3 = s[x2], s[x3]
n1 = sp.simplify(K - n2 - n3)
assert (sp.simplify(n1 - K / 2), sp.simplify(n2 - K / 4), sp.simplify(n3 - K / 4)) == (0, 0, 0)
# (b) period-2 self with K2 = K - n1
K2 = sp.symbols("K2", positive=True)
v2 = sp.log(x2) + beta * sp.log(K2 - x2)
r2 = sp.solve(sp.diff(v2, x2), x2)[0]
assert sp.simplify(r2 - sp.Rational(2, 3) * K2) == 0
assert sp.simplify(r2.subs(K2, K - n1) - K / 3) == 0 and sp.simplify((K - n1 - r2.subs(K2, K - n1)) - K / 6) == 0
# exponential benchmark: K/3 each
ve = sp.log(x1) + sp.log(x2) + sp.log(x3)
se = sp.solve([sp.diff(ve.subs(x1, K - x2 - x3), x2), sp.diff(ve.subs(x1, K - x2 - x3), x3)], [x2, x3], dict=True)[0]
assert sp.simplify(se[x2] - K / 3) == 0 and sp.simplify(se[x3] - K / 3) == 0
# grid search at K = 90 for the naive plan and self-2's plan
import math
Kn = 90.0
bx = max((i / 10 for i in range(1, 899)),
         key=lambda t: math.log(t) + 0.5 * math.log((Kn - t) / 2) + 0.5 * math.log((Kn - t) / 2))
assert abs(bx - 45) < 0.11                                                   # x1 = K/2
b2g = max((i / 10 for i in range(1, 449)), key=lambda t: math.log(t) + 0.5 * math.log(45 - t))
assert abs(b2g - 30) < 0.11                                                  # x2 = K/3 = 30
print("tadelis-8-15: naive plan (K/2, K/4, K/4); self-2 plan (K/3, K/6)")

# 8-16: commitment value
Bv, cc = sp.symbols("B c", positive=True)
v_commit = lambda B: sp.log(B / 2) + beta * sp.log(B / 4) + beta * sp.log(B / 4)
assert sp.simplify(sp.expand_log(v_commit(Bv) - sp.log(Bv ** 2 / 8), force=True)) == 0
# sophisticated plan: self 1 substitutes self 2's reply
vs = sp.log(x1) + beta * sp.log(sp.Rational(2, 3) * (K - x1)) + beta * sp.log(sp.Rational(1, 3) * (K - x1))
xs1 = sp.solve(sp.diff(vs, x1), x1)[0]
assert sp.simplify(xs1 - K / 2) == 0
plan_spe = (K / 2, K / 3, K / 6)
v_spe = lambda Kv: sum(w * sp.log(p.subs(K, Kv)) for w, p in zip((1, beta, beta), plan_spe))
assert abs(float(v_spe(1)) - math.log(1 / (6 * math.sqrt(2)))) < 1e-12        # ln(K^2 / (6 sqrt 2)) at K = 1
# fee: v_commit(K - c) = v_spe(K), K = 90, solved exactly
Kv = 90
fee = sp.solve(sp.Eq(sp.log((Kv - cc) ** 2 / 8), sp.log(sp.Integer(Kv) ** 2 / (6 * sp.sqrt(2)))), cc)
fee = [f for f in fee if 0 < f < Kv]
assert len(fee) == 1
cstar = float(fee[0])
assert abs(cstar - Kv * (1 - (8 / 9) ** 0.25)) < 1e-9 and abs(cstar - 2.6115) < 5e-4
# below c* committing beats the SPE plan, above it does not
for ctest in (cstar - 0.01, cstar + 0.01):
    gain = math.log((Kv - ctest) ** 2 / 8) - math.log(Kv ** 2 / (6 * math.sqrt(2)))
    assert (gain > 0) == (ctest < cstar)
# the book's printed plan (2K/3, 2K/9, K/9) would overstate the fee near 7.6
v_printed = math.log(2 * Kv / 3) + 0.5 * math.log(2 * Kv / 9) + 0.5 * math.log(Kv / 9)
cprinted = Kv - math.sqrt(8 * math.exp(v_printed))
assert 7.5 < cprinted < 7.7 and cprinted > cstar
print(f"tadelis-8-16: commit plan (K/2,K/4,K/4); SPE plan (K/2,K/3,K/6); c* = {cstar:.4f} at K = 90")

# ----------------------------------------------------------------------------- tadelis-8-12
v1f = lambda y: 10 - abs(y - 1)
v2f = lambda y: 10 - abs(y - 3)
SQ = F(4)


def final(x, A):
    return x if x in A else SQ


def is_ne(x, A, X):
    y = final(x, A)
    # player 2 best-replies at the proposal made (flipping his choice at x must not help)
    alt = SQ if x in A else x
    if v2f(y) < v2f(alt):
        return False
    return all(v1f(final(z, A)) <= v1f(y) for z in X)


def is_spe(x, A, X):
    ok2 = all((z in A) if v2f(z) > v2f(SQ) else ((z not in A) if v2f(z) < v2f(SQ) else True) for z in X)
    return ok2 and is_ne(x, A, X)


X = [F(i, 2) for i in range(0, 11)]
outcomes, spe_out = set(), set()
for mask in range(1 << len(X)):
    A = {X[i] for i in range(len(X)) if mask >> i & 1}
    for x in X:
        if is_ne(x, A, X):
            outcomes.add(final(x, A))
            if is_spe(x, A, X):
                spe_out.add(final(x, A))
# NE outcomes are exactly the grid policies of [2, 4]; none outside
assert outcomes == {F(k, 2) for k in range(4, 9)}, outcomes
# on the 1/2 grid the SPE outcome is 2 (tie at 2 accepted) or 2.5 (tie rejected); only 2 survives refinement
assert spe_out == {F(2), F(5, 2)}, spe_out
# player 2 accepts exactly when |x-3| <= 1 (grid)
assert [x for x in X if v2f(x) >= v2f(SQ)] == [x for x in X if 2 <= x <= 4]
# examples in the text
assert is_ne(F(3), {F(3)}, X) and not is_spe(F(3), {F(3)}, X)
assert is_ne(F(0), set(), X) and not is_spe(F(0), set(), X) and final(F(0), set()) == 4
assert (v1f(2), v2f(2)) == (9, 9) and (v1f(3), v2f(3)) == (8, 10) and (v1f(4), v2f(4)) == (7, 9)
# refine the grid: with the tie accepted the best proposal is 2; rejected, it is 2 + h
for k in range(1, 7):
    h = F(1, 2 ** k)
    Xh = [h * i for i in range(int(5 / h) + 1)]
    acc = lambda x, tie: v2f(x) > v2f(SQ) or (v2f(x) == v2f(SQ) and tie)
    for tie, expect in ((True, F(2)), (False, F(2) + h)):
        best = max(Xh, key=lambda x: (v1f(x) if acc(x, tie) else v1f(SQ), -x))
        assert best == expect, (h, tie, best)
print("tadelis-8-12: SPE outcome x = 2 (payoffs 9, 9); NE outcomes = [2, 4]")

print("all L04 checks passed")
