"""Checks every number and equilibrium claim in the Lecture 4 solutions written by agent B:
sol-gibbons-2-12, sol-tadelis-8-8, sol-tadelis-8-6, sol-tadelis-8-4, sol-tadelis-8-13,
sol-mwg-9-b-5.
Exact arithmetic (fractions, sympy). Backward induction and equilibrium sets are computed,
not typed in.

Run: python check_B_L04.py  -> one line per item and "all B L04 checks passed", or an
AssertionError on the first wrong claim.
"""
import random
from fractions import Fraction as F
from itertools import product

import sympy as sp


def pure_ne(A, B):
    """Pure Nash equilibria (row, col) of the bimatrix (A, B), lists of lists."""
    R, C = len(A), len(A[0])
    return {(r, c) for r in range(R) for c in range(C)
            if A[r][c] == max(A[k][c] for k in range(R))
            and B[r][c] == max(B[r][k] for k in range(C))}


def ne_given_q(A, B, q):
    """Column player has two strategies, plays the first w.p. q: can some mix of the row
    player's best replies make q a best reply?"""
    u1 = [A[r][0] * q + A[r][1] * (1 - q) for r in range(len(A))]
    best = [r for r in range(len(A)) if u1[r] == max(u1)]
    gaps = [B[r][0] - B[r][1] for r in best]
    lo, hi = min(gaps), max(gaps)
    if q == 1:
        return hi >= 0
    if q == 0:
        return lo <= 0
    return lo <= 0 <= hi


# ----------------------------------------------------------------------------- gibbons-2-12
# two-stage Prisoners' Dilemma, Gibbons Fig. 2.3.1 (L = defect, R = cooperate), no discounting
g = {("L", "L"): (1, 1), ("L", "R"): (5, 0), ("R", "L"): (0, 5), ("R", "R"): (4, 4)}
hist = list(product("LR", repeat=2))                       # first-stage outcomes
strats = list(product("LR", repeat=5))                     # (v, w, x, y, z) as in Gibbons p. 93
assert len(hist) == 4 and len(strats) == 32


def total(s1, s2):
    a = (s1[0], s2[0])
    j = hist.index(a)
    b = (s1[1 + j], s2[1 + j])
    return tuple(g[a][i] + g[b][i] for i in range(2))


T = {(i, j): total(s1, s2) for i, s1 in enumerate(strats) for j, s2 in enumerate(strats)}
ne = [(i, j) for i in range(32) for j in range(32)
      if T[(i, j)][0] == max(T[(k, j)][0] for k in range(32))
      and T[(i, j)][1] == max(T[(i, k)][1] for k in range(32))]


def stage_ne(a1, a2):
    return (g[(a1, a2)][0] == max(g[(b, a2)][0] for b in "LR")
            and g[(a1, a2)][1] == max(g[(a1, b)][1] for b in "LR"))


spe = [(i, j) for i, j in ne
       if all(stage_ne(strats[i][1 + h], strats[j][1 + h]) for h in range(4))]
assert len(spe) == 1 and strats[spe[0][0]] == tuple("LLLLL") == strats[spe[0][1]]
assert {T[x] for x in ne} == {(2, 2)}                       # every NE: (L, L) twice
print(f"gibbons-2-12: 32 strategies each, {len(ne)} NE profiles, 1 SPE (L,L,L,L,L) each")
# counts for G(T) with a 2x2 stage game: information sets = (4^T - 1)/3
for TT in [1, 2, 3]:
    assert sum(4 ** (t - 1) for t in range(1, TT + 1)) == (4 ** TT - 1) // 3
assert 2 ** 5 == 32 and 3 ** 10 == 59049                   # 3x3 stage game played twice

# ----------------------------------------------------------------------------- tadelis-8-8
out, war, acc = (0, 10), (1 - 2, 1), (4 - 2, 4)
assert acc[1] > war[1] and acc[0] > out[0]
A88 = [[out[0], out[0]], [war[0], acc[0]]]                  # rows Out, In; cols W, A
B88 = [[out[1], out[1]], [war[1], acc[1]]]
assert pure_ne(A88, B88) == {(0, 0), (1, 1)}
qs = [F(k, 300) for k in range(301)]                       # q = Pr(W)
assert [q for q in qs if ne_given_q(A88, B88, q)] == [F(0)] + [q for q in qs if q >= F(2, 3)]   # (In, A) and (Out, Pr(W) >= 2/3)
# commitment: a penalty b on accommodating makes war credible iff 4 - b < 1, i.e. b > 3
for b in [F(3), F(301, 100)]:
    assert (4 - b < 1) == (b > 3)
assert 10 - 4 == 6                                          # value of a credible threat to S&P
for cost in [F(399, 100), F(401, 100)]:                     # entry cost that deters on its own
    assert (4 - cost > 0) == (cost < 4)
print("tadelis-8-8: SPE (In, A); NE (Out, Pr(W) >= 2/3); commitment worth up to 6")

# ----------------------------------------------------------------------------- tadelis-8-6
q1, q2 = sp.symbols("q1 q2", nonnegative=True)


def cournot(c1, c2):
    s = sp.solve([sp.diff((100 - q1 - q2 - c1) * q1, q1), sp.diff((100 - q1 - q2 - c2) * q2, q2)],
                 [q1, q2])
    p_ = 100 - s[q1] - s[q2]
    return s[q1], s[q2], (p_ - c1) * s[q1], (p_ - c2) * s[q2]


n1, n2, pn1, pn2 = cournot(10, 10)
i1, i2, pi1, pi2 = cournot(5, 10)
assert (n1, n2, pn1, pn2) == (30, 30, 900, 900)
assert (i1, i2) == (sp.Rational(100, 3), sp.Rational(85, 3))
assert (pi1, pi2) == (sp.Rational(10000, 9), sp.Rational(7225, 9))
Fstar = pi1 - pn1
assert Fstar == sp.Rational(1900, 9)
direct = (sp.Rational(95 - 30, 2)) ** 2 - 900               # firm 2 kept at 30
assert direct == sp.Rational(625, 4) and Fstar - direct == sp.Rational(1975, 36)
# (b) threat profile: firm 2 floods (q2 = 90) after No investment; firm 1 invests.
Fv = sp.Rational(1000, 3)                                   # an F in (F*, 10000/9]
assert Fstar < Fv <= pi1
best_after_N = max((100 - 90 - F(k, 4) - 10) * F(k, 4) for k in range(0, 401))
assert best_after_N == 0                                    # firm 1's best reply to 90 is 0
assert pi1 - Fv >= best_after_N                             # investing is a best reply
assert sp.solve(sp.diff((100 - 0 - q2 - 10) * q2, q2), q2) == [45]   # 90 is not a best reply
# firm 2 on path: best reply to q1 = 100/3 is 85/3
assert sp.solve(sp.diff((100 - i1 - q2 - 10) * q2, q2), q2) == [i2]
# second example, any F > F*: no investment, Cournot (30, 30); firm 2 floods (90) after I
best_after_I = max((100 - 90 - F(k, 4) - 5) * F(k, 4) for k in range(0, 401))
assert best_after_I == F(25, 4) and best_after_I - Fstar < 900
assert sp.solve(sp.diff((100 - 0 - q2 - 10) * q2, q2), q2) != [90]
print("tadelis-8-6: F* = 1900/9; flood threat supports investing for F in (F*, 10000/9]")

# ----------------------------------------------------------------------------- tadelis-8-4
a, cc, Q1, Q2, Q3 = sp.symbols("a c q1 q2 q3", positive=True)
foc2 = sp.diff((a - Q1 - Q2 - Q3 - cc) * Q2, Q2)
foc3 = sp.diff((a - Q1 - Q2 - Q3 - cc) * Q3, Q3)
M = sp.Matrix([[sp.diff(foc2, Q2), sp.diff(foc2, Q3)], [sp.diff(foc3, Q2), sp.diff(foc3, Q3)]])
assert M.det() == 3                                         # FOC system has a unique solution
sol = sp.solve([foc2, foc3], [Q2, Q3])
assert sp.simplify(sol[Q2] - (a - cc - Q1) / 3) == 0 and sp.simplify(sol[Q3] - sol[Q2]) == 0
pi1 = (a - Q1 - 2 * (a - cc - Q1) / 3 - cc) * Q1
q1s = sp.solve(sp.diff(pi1, Q1), Q1)[0]
assert sp.simplify(q1s - (a - cc) / 2) == 0 and sp.diff(pi1, Q1, 2) < 0
assert sp.simplify(sol[Q2].subs(Q1, q1s) - (a - cc) / 6) == 0
# numbers a = 13, c = 1: follower NE unique (best-reply iteration from many starts converges)
av, cv_ = F(13), F(1)
for q1v in [F(0), F(3), F(6), F(11), F(12), F(15)]:
    br = lambda other: max(F(0), (av - cv_ - q1v - other) / 2)
    target = max(F(0), (av - cv_ - q1v) / 3)
    for start in [(F(0), F(0)), (F(20), F(0)), (F(7), F(13))]:
        x2, x3 = start
        for _ in range(60):
            x2, x3 = br(x3), br(x2)
        assert abs(x2 - target) < F(1, 10 ** 6) and abs(x3 - target) < F(1, 10 ** 6)
# (d) NE not SPE: q1 = (a-c)/4 = 3; followers 3 each if q1 = 3, else flood a - c = 12 each
qhat = (av - cv_) / 4
on_path = (av - 3 * qhat - cv_) * qhat
assert on_path == 9
assert max((av - F(k, 4) - 24 - cv_) * F(k, 4) for k in range(0, 61)) <= 0 < on_path
assert max((av - qhat - F(k, 8) - qhat - cv_) * F(k, 8) for k in range(0, 97)) == 9   # follower BR = 3
assert (av - cv_ - 0 - 12) / 2 != 12                        # flooding is not a best reply
print("tadelis-8-4: SPE q1 = (a-c)/2, q2 = q3 = (a-c)/6; flood-threat NE gives Cournot (a-c)/4 each")

# ----------------------------------------------------------------------------- tadelis-8-13
c16, v16, k16 = F(2), F(10), F(1)
prices = [F(i, 4) for i in range(0, 61)]
seller = {pv: (pv if v16 - pv - k16 >= -k16 else c16) for pv in prices}
p_spe = max(prices, key=lambda pv: seller[pv])
assert p_spe == v16 and v16 - p_spe - k16 < 0
assert max(pv for pv in prices if pv < v16) == v16 - F(1, 4)
for ps in [F(5, 2), F(5), F(17, 2)]:
    sell = {pv: (pv if pv <= ps else c16) for pv in prices}
    assert max(sell.values()) == ps == sell[ps] and v16 - ps - k16 > 0 and ps > c16
eps = F(1, 2)
post = {pv: (pv - eps if v16 - pv - k16 >= 0 else c16 - eps) for pv in prices}
p_hat = max(prices, key=lambda pv: post[pv])
assert p_hat == v16 - k16 and post[p_hat] == v16 - k16 - eps > c16
cs, vs, ks, es = sp.symbols("c v k epsilon", positive=True)
assert sp.simplify((vs - ks - es) - cs - ((vs - cs - ks) - es)) == 0
print("tadelis-8-13: SPE p = v, no trade; postcard at v - k is bought, seller nets v - k - eps")

# ----------------------------------------------------------------------------- mwg-9-b-5
def seq_spne(phi1, phi2, m1, m2):
    """All pure SPNE of the sequential game: P1 picks a in range(m1); P2 observes it.
    Returns list of (a, s2) with s2 a tuple of replies."""
    out = []
    for s2 in product(range(m2), repeat=m1):
        if not all(phi2[a][s2[a]] == max(phi2[a]) for a in range(m1)):
            continue                                        # NE in every P2 subgame
        for a in range(m1):
            if phi1[a][s2[a]] == max(phi1[b][s2[b]] for b in range(m1)):
                out.append((a, s2))
    return out


def seq_ne(phi1, phi2, m1, m2):
    out = []
    for s2 in product(range(m2), repeat=m1):
        for a in range(m1):
            if (phi1[a][s2[a]] == max(phi1[b][s2[b]] for b in range(m1))
                    and phi2[a][s2[a]] == max(phi2[a])):
                out.append((a, s2))
    return out


rng = random.Random(95)
checked_c = checked_d = 0
for _ in range(3000):
    m1, m2 = rng.randint(2, 3), rng.randint(2, 3)
    phi1 = [[rng.randint(0, 4) for _ in range(m2)] for _ in range(m1)]
    phi2 = [[rng.randint(0, 4) for _ in range(m2)] for _ in range(m1)]
    sp_ = seq_spne(phi1, phi2, m1, m2)
    assert len(sp_) >= 1
    cells = [(a, b) for a in range(m1) for b in range(m2)]
    ties1 = any(phi1[x[0]][x[1]] == phi1[y[0]][y[1]] for x in cells for y in cells if x != y)
    ties2 = any(phi2[x[0]][x[1]] == phi2[y[0]][y[1]] for x in cells for y in cells if x != y)
    if len(sp_) > 1:
        assert ties1 or ties2                               # (c)
        checked_c += 1
    if not ties2:                                           # (d)
        sim = pure_ne(phi1, phi2)
        for (a, b) in sim:
            for (a1, s2) in sp_:
                assert phi1[a1][s2[a1]] >= phi1[a][b]
        checked_d += 1
assert checked_c > 0 and checked_d > 0
# (b) counts: P2 has m2^m1 strategies
assert len(list(product(range(3), repeat=2))) == 3 ** 2
# (d) a NE of the sequential game below the simultaneous NE payoff: rows O, F; cols O, F
p1 = [[2, 0], [0, 1]]
p2 = [[1, 0], [-1, 2]]                                      # P2 never indifferent
assert pure_ne(p1, p2) == {(0, 0), (1, 1)}
assert {(a, s) for a, s in seq_spne(p1, p2, 2, 2)} == {(0, (0, 1))}
assert (1, (1, 1)) in seq_ne(p1, p2, 2, 2) and p1[1][1] == 1 < 2
# (e1) MWG manual's example: P2 indifferent; SPNE (U, (L, L)) gives P1 0 < 1 = payoff of NE (U, R)
e1 = ([[0, 1], [0, 1]], [[1, 1], [0, 0]])
assert (0, 1) in pure_ne(*e1) and e1[0][0][1] == 1
assert (0, (0, 0)) in seq_spne(*e1, 2, 2) and e1[0][0][0] == 0
# (e2) matching pennies: mixed NE gives P1 1/2; every SPNE gives 0
e2 = ([[1, 0], [0, 1]], [[0, 1], [1, 0]])
assert pure_ne(*e2) == set()
assert sorted(seq_spne(*e2, 2, 2)) == [(0, (1, 0)), (1, (1, 0))]
assert all(e2[0][a][s[a]] == 0 for a, s in seq_spne(*e2, 2, 2))
assert sum(F(1, 4) * e2[0][r][c] for r in range(2) for c in range(2)) == F(1, 2)
print(f"mwg-9-b-5: (c) on {checked_c} random games with multiple SPNE, (d) on {checked_d} games; "
      "examples (d), (e1), (e2) confirmed")

print("all B L04 checks passed")
