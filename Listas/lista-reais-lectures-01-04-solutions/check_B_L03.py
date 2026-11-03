"""Checks every number and equilibrium claim in items 13-18 (Lecture 3 block):
13 Tadelis 8.8, 14 Munoz-Garcia Ch. 4 Ex. 3, 15 Tadelis 8.10, 16 Tadelis 8.13,
17 Munoz-Garcia Ch. 4 Ex. 12, 18 Gibbons 2.1.

Run: python check_B_L03.py  -> prints "all B L03 checks passed" or fails on the first wrong claim.
"""
from fractions import Fraction as F
from itertools import product

import numpy as np
import sympy as sp


def pure_ne(A, B):
    """Pure Nash equilibria (row, col) of the bimatrix (A, B), given as lists of lists."""
    R, C = len(A), len(A[0])
    return {(r, c) for r in range(R) for c in range(C)
            if A[r][c] == max(A[k][c] for k in range(R))
            and B[r][c] == max(B[r][k] for k in range(C))}


# ---- item 13: Tadelis 8.8, payoffs (NSG, S&P) in $ million, entry cost 2 netted out
out, war, acc = (0, 10), (1 - 2, 1), (4 - 2, 4)
assert acc[1] > war[1]                                  # S&P accommodates after entry
assert acc[0] > out[0]                                  # NSG enters, anticipating accommodation
# normal form: NSG rows {Out, Enter}, S&P columns {War, Accommodate}
A13 = [[out[0], out[0]], [war[0], acc[0]]]
B13 = [[out[1], out[1]], [war[1], acc[1]]]
assert pure_ne(A13, B13) == {(0, 0), (1, 1)}            # (Out, War) and (Enter, Acc)
# robustness: if "each earns 1" were already net of the entry cost, entry still pays
assert 4 > 1 and 4 - 2 > 0 and 1 > 0

# ---- item 14: Munoz-Garcia Ch. 4 Ex. 3, Fig. 4.9 (Confess C, Not confess N)
pay14 = {("C", "C"): (-5, -5), ("C", "N"): (0, -15), ("N", "C"): (-15, 0), ("N", "N"): (-1, -1)}
br2 = {a1: max("CN", key=lambda a2: pay14[(a1, a2)][1]) for a1 in "CN"}
assert br2 == {"C": "C", "N": "C"}
a1_star = max("CN", key=lambda a1: pay14[(a1, br2[a1])][0])
assert a1_star == "C" and pay14[("C", "C")] == (-5, -5)
# normal form of the sequential game: player 2 strategies (reply to C, reply to N)
S2 = list(product("CN", repeat=2))
A14 = [[pay14[(a1, s2[0] if a1 == "C" else s2[1])][0] for s2 in S2] for a1 in "CN"]
B14 = [[pay14[(a1, s2[0] if a1 == "C" else s2[1])][1] for s2 in S2] for a1 in "CN"]
assert {("CN"[r], "".join(S2[c])) for r, c in pure_ne(A14, B14)} == {("C", "CC")}
# simultaneous version (Fig. 1.8): Confess strictly dominant, unique NE (C, C)
A1s = [[-5, 0], [-15, -1]]
assert pure_ne(A1s, [list(x) for x in zip(*A1s)]) == {(0, 0)}

# ---- item 15: Tadelis 8.10, subgame after R: rows C, D; columns A, B
As, Bs = [[8, 0], [6, 2]], [[0, 2], [6, 2]]
assert pure_ne(As, Bs) == set()                         # no pure NE in the subgame
p, q = sp.symbols("p q")                                # p = Pr(C), q = Pr(A)
p_star = sp.solve(sp.Eq(0 * p + 6 * (1 - p), 2 * p + 2 * (1 - p)), p)[0]
q_star = sp.solve(sp.Eq(8 * q, 6 * q + 2 * (1 - q)), q)[0]
assert (p_star, q_star) == (sp.Rational(2, 3), sp.Rational(1, 2))
v1 = 8 * q_star
v2 = 2
assert v1 == 4 and 6 * (1 - p_star) == v2 and v1 > 3   # player 1 takes the risk: 4 > 3
# normal form of the whole game: P1 {SC, SD, RC, RD}, P2 {A, B}
A15 = [[3, 3], [3, 3], [8, 0], [6, 2]]
B15 = [[3, 3], [3, 3], [0, 2], [6, 2]]
assert pure_ne(A15, B15) == {(0, 1), (1, 1)}            # (SC, B), (SD, B)


def ne_q_15(qv):
    """Is there a P1 mix that, with P2's Pr(A) = qv, forms a Nash equilibrium? Returns the
    attainable range of P2's payoff gap u2(A) - u2(B) over P1's best-reply mixes, if feasible."""
    u1 = [3, 3, 8 * qv, 2 + 4 * qv]
    best = [i for i in range(4) if u1[i] == max(u1)]
    gaps = [B15[i][0] - B15[i][1] for i in best]        # SC, SD: 0; RC: -2; RD: +4
    lo, hi = min(gaps), max(gaps)                        # mixes attain every gap in [lo, hi]
    if 0 < qv < 1:
        return lo <= 0 <= hi
    return hi >= 0 if qv == 1 else lo <= 0


crit = [F(0), F(1, 4), F(3, 8), F(1, 2), F(1)]
grid = sorted(set(crit + [F(k, 240) for k in range(241)]))
ok = [qv for qv in grid if ne_q_15(qv)]
assert all(qv <= F(1, 4) for qv in ok if qv != F(1, 2))
assert F(1, 2) in ok and F(1, 4) in ok and F(0) in ok
assert not any(F(1, 4) < qv < 1 and qv != F(1, 2) for qv in ok) and F(1) not in ok
# at q = 1/2 the P1 mix must make P2 indifferent: -2 w_RC + 4 w_RD = 0, w_RC + w_RD = 1
w = sp.solve([-2 * sp.Symbol("a") + 4 * sp.Symbol("b"), sp.Symbol("a") + sp.Symbol("b") - 1])
assert w == {sp.Symbol("a"): sp.Rational(2, 3), sp.Symbol("b"): sp.Rational(1, 3)}

# ---- item 16: Tadelis 8.13, numbers c = 2, v = 10, k = 1 (v > c + k), prices on a 0.25 grid
c16, v16, k16 = F(2), F(10), F(1)
prices = [F(i, 4) for i in range(0, 61)]                 # 0 .. 15


def accept(pv):
    """Sequentially rational reply; accept at indifference (p = v), as the SPE requires."""
    return (v16 - pv - k16) >= -k16


seller = {pv: (pv if accept(pv) else c16) for pv in prices}
p_spe = max(prices, key=lambda pv: seller[pv])
assert p_spe == v16 and seller[p_spe] == v16
assert v16 - p_spe - k16 < 0                             # buyer stays home: payoffs (0, c)
# if the buyer rejected at p = v, the seller's best offer would be the largest grid price below v:
# on a continuum no best offer exists, so "reject at v" is not part of any SPE
assert max(pv for pv in prices if pv < v16) == v16 - F(1, 4)
# Pareto improvement: trade at p in (c, v - k)
for pv in [F(5, 2), F(5), F(17, 2)]:
    assert c16 < pv < v16 - k16 and v16 - pv - k16 > 0 and pv > c16
# Nash equilibrium with threshold p*: buyer commutes, accepts iff p <= p*; seller offers p*
for ps in [F(5, 2), F(5), F(17, 2)]:
    sell = {pv: (pv if pv <= ps else c16) for pv in prices}
    assert max(sell.values()) == ps == sell[ps]           # seller's best offer is p*
    assert v16 - ps - k16 > 0                            # commuting beats staying home (0)
# postcard: seller commits to p_hat; buyer commutes iff v - p_hat - k >= 0
eps = F(1, 2)
assert eps < v16 - c16 - k16
post = {pv: (pv - eps if v16 - pv - k16 >= 0 else c16 - eps) for pv in prices}
p_hat = max(prices, key=lambda pv: post[pv])
assert p_hat == v16 - k16 and post[p_hat] == v16 - k16 - eps > c16   # 8.5 > 2: send it
cs, vs, ks, es = sp.symbols("c v k epsilon", positive=True)
assert sp.simplify((vs - ks - es) - cs - ((vs - cs - ks) - es)) == 0  # gain = (v-c-k) - eps

# ---- item 17: Munoz-Garcia Ch. 4 Ex. 12, p = 10 - Q, MC = 2
q1, q2, q3 = sp.symbols("q1 q2 q3", nonnegative=True)
r2 = sp.solve(sp.diff((8 - q1 - q2) * q2, q2), q2)[0]
assert sp.simplify(r2 - (4 - q1 / 2)) == 0
q1a = sp.solve(sp.diff((8 - q1 - r2) * q1, q1), q1)[0]
q2a = r2.subs(q1, q1a)
assert (q1a, q2a, 10 - q1a - q2a) == (4, 2, 4)
assert ((10 - 6 - 2) * 4, (10 - 6 - 2) * 2) == (8, 4)
r3 = sp.solve(sp.diff((8 - q1 - q2 - q3) * q3, q3), q3)[0]
assert sp.simplify(r3 - (4 - (q1 + q2) / 2)) == 0
r2b = sp.solve(sp.diff((8 - q1 - q2 - r3) * q2, q2), q2)[0]
assert sp.simplify(r2b - (4 - q1 / 2)) == 0             # same rule as in (a)
r3b = sp.simplify(r3.subs(q2, r2b))
assert sp.simplify(r3b - (2 - q1 / 4)) == 0
q1b = sp.solve(sp.diff((8 - q1 - r2b - r3b) * q1, q1), q1)[0]
q2b, q3b = r2b.subs(q1, q1b), r3b.subs(q1, q1b)
assert (q1b, q2b, q3b) == (4, 2, 1)
pb = 10 - (q1b + q2b + q3b)
assert pb == 3 and ((pb - 2) * q1b, (pb - 2) * q2b, (pb - 2) * q3b) == (4, 2, 1)
assert sp.diff((8 - q1 - r2b - r3b) * q1, q1, 2) < 0     # leader's problem concave
# numeric route: leader on a 0.01 grid, followers best-reply max(0, (8 - output before them)/2)
g = np.round(np.arange(0, 8.0001, 0.01), 2)


def br(rest):
    return max(0.0, (8 - rest) / 2)


best1 = max(g, key=lambda x: (8 - x - br(x)) * x)
assert abs(best1 - 4) < 1e-9 and abs(br(4.0) - 2) < 1e-9
best1b = max(g, key=lambda x: (8 - x - br(x) - br(x + br(x))) * x)
assert abs(best1b - 4) < 1e-9 and abs(br(4.0 + br(4.0)) - 1) < 1e-9
# firm 2 in (b), on a grid against firm 3's rule, given q1 = 4
best2b = max(g, key=lambda y: (8 - 4 - y - br(4 + y)) * y)
assert abs(best2b - 2) < 1e-9

# ---- item 18: Gibbons 2.1, Rotten Kid
# (i) general: c*(Y) solves V'(Y - c) = k U'(c); implicit derivative V''/(V'' + k U'') in (0, 1)
Vpp, Upp, kk = sp.symbols("Vpp Upp k", negative=False)
dcdY = (-Vpp) / ((-Vpp) + kk * (-Upp))                   # with V'' = -Vpp < 0, U'' = -Upp < 0
for vals in [(1, 1, 1), (2, 0.5, 3), (0.1, 5, 0.2)]:
    d = float(dcdY.subs({Vpp: vals[0], Upp: vals[1], kk: vals[2]}))
    assert 0 < d < 1
# (ii) worked example: U(x) = V(x) = -exp(-x), k = 2, I_C = 4A - A^2 (A_C = 2), I_P = 10A - A^2 (A_P = 5)
kv = 2.0
IC = lambda A: 4 * A - A**2
IP = lambda A: 10 * A - A**2
U = lambda x: -np.exp(-x)
Bs_ = np.linspace(-40, 40, 160001)                       # bequest grid, step 0.0005


def bequest(ic, ip):
    """Parent's best bequest on the grid, given the two incomes."""
    return Bs_[np.argmax(U(ip - Bs_) + kv * U(ic + Bs_))]


As_ = np.round(np.arange(0, 6.0001, 0.05), 2)
child = [U(IC(a) + bequest(IC(a), IP(a))) for a in As_]
A_kid = As_[int(np.argmax(child))]
assert abs(A_kid - 3.5) < 1e-9                           # = argmax of I_C + I_P = 14A - 2A^2
assert abs(As_[np.argmax(IC(As_) + IP(As_))] - 3.5) < 1e-9 and abs(As_[np.argmax(IC(As_))] - 2) < 1e-9
# closed form for CARA: c* = (Y + ln k)/2, strictly increasing in Y
Y = IC(3.5) + IP(3.5)
assert abs((IC(3.5) + bequest(IC(3.5), IP(3.5))) - (Y + np.log(kv)) / 2) < 1e-3

print("all B L03 checks passed")
