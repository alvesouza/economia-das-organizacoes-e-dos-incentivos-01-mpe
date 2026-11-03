"""Checks every number and equilibrium claim in items 19-24 (Lecture 4 block):
19 Tadelis 9.1, 20 Gibbons 2.6, 21 Tadelis 9.4, 22 Tadelis 11.2, 23 Tadelis 11.5,
24 Munoz-Garcia Ch. 6 Ex. 8.

Run: python check_B_L04.py  -> prints "all B L04 checks passed" or fails on the first wrong claim.
"""
from fractions import Fraction as F
from itertools import product

import sympy as sp

# ---- item 19: Tadelis 9.1, stage game played twice, v_i = u_i(period 1) + delta u_i(period 2)
R1, C1 = "TMB", "LCR"
U = {("T", "L"): (10, 10), ("T", "C"): (2, 12), ("T", "R"): (0, 13),
     ("M", "L"): (12, 2), ("M", "C"): (5, 5), ("M", "R"): (0, 0),
     ("B", "L"): (13, 0), ("B", "C"): (0, 0), ("B", "R"): (1, 1)}
cells = list(product(R1, C1))
stage_ne = [a for a in cells
            if U[a][0] == max(U[(r, a[1])][0] for r in R1)
            and U[a][1] == max(U[(a[0], c)][1] for c in C1)]
assert stage_ne == [("M", "C"), ("B", "R")]


def gains(a):
    """One-shot deviation gains (player 1, player 2) from period-1 profile a."""
    return (max(U[(r, a[1])][0] for r in R1) - U[a][0],
            max(U[(a[0], c)][1] for c in C1) - U[a][1])


def is_spe(a, cont, d):
    """Pure SPE test: period-1 profile a, continuation map cont: outcome -> stage NE, discount d.
    Period 2 is a stage NE after every history by construction, so only period 1 is checked."""
    v = lambda x, i: U[x][i] + d * U[cont[x]][i]
    return (all(v(a, 0) >= v((r, a[1]), 0) for r in R1)
            and all(v(a, 1) >= v((a[0], c), 1) for c in C1))


spe_count, paths = 0, set()
for a in cells:
    for m in product(stage_ne, repeat=9):
        cont = dict(zip(cells, m))
        if is_spe(a, cont, 1):
            spe_count += 1
            paths.add((a, cont[a]))
supportable = {a for a, _ in paths}
assert supportable == set(cells) - {("M", "R"), ("B", "C")}
assert {g for g in map(gains, [("M", "R"), ("B", "C")])} == {(1, 5), (5, 1)}
assert all(cont == ("M", "C") for a, cont in paths if a not in stage_ne)
assert {cont for a, cont in paths if a in stage_ne} == set(stage_ne)
assert len(paths) == 9                                   # 5 non-NE starts + 2 x 2 NE sequences
print("item 19: number of pure SPE (strategy profiles) at delta = 1:", spe_count)
# smallest delta: max gain / (5 - 1)
dstar = {a: F(max(gains(a)), 4) for a in supportable}
assert dstar == {("T", "L"): F(3, 4), ("T", "C"): F(3, 4), ("T", "R"): F(1, 4),
                 ("M", "L"): F(3, 4), ("B", "L"): F(1, 4), ("M", "C"): 0, ("B", "R"): 0}
best_cont = lambda a: {x: (("M", "C") if x == a else ("B", "R")) for x in cells}
for a, d0 in dstar.items():
    if d0 > 0:
        assert is_spe(a, best_cont(a), d0) and not is_spe(a, best_cont(a), d0 - F(1, 1000))
        # no continuation map does better than the carrot-and-stick map just below d0
        assert not any(is_spe(a, dict(zip(cells, m)), d0 - F(1, 1000))
                       for m in product(stage_ne, repeat=9))

# ---- item 20: Gibbons 2.6
a, c, q1, q2, q3 = sp.symbols("a c q1 q2 q3", positive=True)
foc2 = sp.diff((a - q1 - q2 - q3 - c) * q2, q2)
foc3 = sp.diff((a - q1 - q2 - q3 - c) * q3, q3)
sol = sp.solve([foc2, foc3], [q2, q3])
assert sp.simplify(sol[q2] - (a - c - q1) / 3) == 0 and sp.simplify(sol[q3] - sol[q2]) == 0
pi1 = sp.expand((a - q1 - 2 * (a - c - q1) / 3 - c) * q1)
assert sp.simplify(pi1 - (a - c - q1) * q1 / 3) == 0
q1s = sp.solve(sp.diff(pi1, q1), q1)[0]
assert sp.simplify(q1s - (a - c) / 2) == 0
q2s = sp.simplify(sol[q2].subs(q1, q1s))
assert sp.simplify(q2s - (a - c) / 6) == 0
P = sp.simplify(a - q1s - 2 * q2s)
assert sp.simplify(P - (a + 5 * c) / 6) == 0
assert sp.simplify((P - c) * q1s - (a - c)**2 / 12) == 0
assert sp.simplify((P - c) * q2s - (a - c)**2 / 36) == 0
# vs simultaneous three-firm Cournot: (a - c)/4 each, profit (a - c)^2/16, Q = 3(a - c)/4
assert sp.simplify((a - c)**2 / 12 - (a - c)**2 / 16) == (a - c)**2 / 48     # leader gains
assert sp.Rational(5, 6) > sp.Rational(3, 4) and sp.Rational(1, 36) < sp.Rational(1, 16)
# numeric: a = 13, c = 1; leader on a grid, followers' Cournot reply max(0, (a - c - q1)/3)
best = max((F(k, 20) for k in range(0, 481)), key=lambda x: (12 - x - 2 * max(F(0), (12 - x) / 3)) * x)
assert best == 6 and max(F(0), (12 - best) / 3) == 2

# ---- item 21: Tadelis 9.4
qi, qj, d = sp.symbols("q_i q_j delta", nonnegative=True)
brc = sp.solve(sp.diff((100 - qi - qj) * qi, qi), qi)[0]
assert sp.simplify(brc - (100 - qj) / 2) == 0
qc = sp.solve(sp.Eq(qi, brc.subs(qj, qi)), qi)[0]
assert qc == sp.Rational(100, 3) and qc * (100 - 2 * qc) == sp.Rational(10000, 9)
acc = {("O", "o"): (2500, 2500), ("O", "n"): (-10, 0), ("N", "o"): (0, -10), ("N", "n"): (0, 0)}
acc_ne = [x for x in acc
          if acc[x][0] >= max(acc[(r, x[1])][0] for r in "ON")
          and acc[x][1] >= max(acc[(x[0], s)][1] for s in "on")]
assert sorted(acc_ne) == [("N", "n"), ("O", "o")]
pi_m = 25 * (100 - 50)
pi_d = ((100 - 25) / sp.Integer(2)) * (100 - 25 - (100 - 25) / sp.Integer(2))
assert pi_m == 1250 and pi_d == sp.Rational(5625, 4)    # 1406.25
gain = pi_d - pi_m
assert gain == sp.Rational(625, 4)                      # 156.25
d_star = gain / 2500
assert d_star == sp.Rational(1, 16)
assert pi_m + 1 * 2500 >= pi_d and pi_m + sp.Rational(2, 5) * 2500 >= pi_d
assert pi_m + sp.Rational(2, 5) * 2500 == 2250
# general symmetric q: deviation gain = (9/4)(100/3 - q)^2; sustainable iff gain <= 2500 delta
q = sp.symbols("q", nonnegative=True)
g = ((100 - q) / 2)**2 - q * (100 - 2 * q)
assert sp.expand(g - sp.Rational(9, 4) * (sp.Rational(100, 3) - q)**2) == 0
qmin = sp.Rational(100, 3) * (1 - sp.sqrt(d))
assert sp.simplify(g.subs(q, qmin) - 2500 * d) == 0
assert qmin.subs(d, sp.Rational(1, 16)) == 25 and sp.Rational(2, 5) > sp.Rational(1, 16)
q04 = qmin.subs(d, sp.Rational(1, 25))                   # the variant delta = 0.04
assert q04 == sp.Rational(80, 3) and q04 * (100 - 2 * q04) == sp.Rational(11200, 9)

# ---- item 22: Tadelis 11.2, numbers v_L = 4, v_H = 10, c_L = 1, c_H = 3 (v_H - c_H > v_L - c_L)
vL, vH, cL, cH = F(4), F(10), F(1), F(3)
assert vH > vL > 0 and cH > cL > 0 and vH - cH > vL - cL
step = F(1, 4)


def offers(v):
    return [k * step for k in range(int(v / step) + 1)]  # player 2's share y in [0, v]


# SPE: player 2 accepts every y >= 0 (accepting y = 0 is the only sequentially rational tie rule
# that leaves player 1 a best offer); player 1 offers y = 0
spe2 = {lvl: -cst for lvl, cst in (("L", cL), ("H", cH))}
assert max(spe2, key=spe2.get) == "L"                   # player 2 invests low
assert (vL, -cL) == (4, -1)
# Pareto improvement through H with transfer y in (c_H - c_L, v_H - v_L) = (2, 6)
for y in [F(5, 2), F(4), F(11, 2)]:
    assert vH - y > vL and y - cH > -cL
# Nash equilibrium: after H, 2 accepts iff y >= y*; 1 offers y*; after L, 1 offers 0, 2 accepts all
for ys in [F(5, 2), F(4), F(11, 2)]:
    p1H = {y: (vH - y if y >= ys else 0) for y in offers(vH)}
    assert max(p1H.values()) == vH - ys == p1H[ys]       # player 1's best offer after H is y*
    assert ys - cH > 0 - cL                              # player 2 prefers H to L
    assert vH - ys > vL                                  # player 1 better off than in the SPE

# ---- item 23: Tadelis 11.5, three periods, player i discounts with delta_i
d1, d2 = sp.symbols("delta_1 delta_2", positive=True)
x3 = 1                                                  # period 3: player 1 takes everything
x2 = d1 * x3                                            # period 2: P1 indifferent, d1 x = d1^2 x3
x1 = 1 - d2 * (1 - x2)                                  # period 1: P2 gets d2 (1 - x2)
assert sp.expand(x1 - (1 - d2 + d1 * d2)) == 0
dd = sp.symbols("delta", positive=True)
x1eq = x1.subs({d1: dd, d2: dd})
assert sp.expand(x1eq - (1 - dd + dd**2)) == 0
assert sp.expand(2 * x1eq - 1 - ((1 - dd)**2 + dd**2)) == 0   # x1 - (1 - x1) > 0
# equal patience: edge (1-d)^2 + d^2 is minimal (1/2) at d = 1/2; v1 -> 1 as d -> 0 and d -> 1
edge = (1 - dd)**2 + dd**2
assert sp.solve(sp.diff(edge, dd), dd) == [sp.Rational(1, 2)] and edge.subs(dd, sp.Rational(1, 2)) == sp.Rational(1, 2)
assert x1eq.subs(dd, sp.Rational(1, 2)) == sp.Rational(3, 4)
assert sp.limit(x1eq, dd, 0) == 1 and sp.limit(x1eq, dd, 1) == 1
assert sp.diff(x1, d1) == d2 and sp.simplify(sp.diff(x1, d2) + (1 - d1)) == 0
# player 2 ahead iff d2 (1 - d1) > 1/2
for a_, b_ in [(F(1, 5), F(9, 10)), (F(1, 10), F(3, 5)), (F(1, 2), F(9, 10)), (F(9, 10), F(7, 10))]:
    s1 = 1 - b_ * (1 - a_)
    assert (1 - s1 > s1) == (b_ * (1 - a_) > F(1, 2))
assert 1 - (1 - F(9, 10) * (1 - F(1, 5))) == F(18, 25)   # 0.72 for (0.2, 0.9)
assert 1 - F(7, 10) * (1 - F(9, 10)) == F(93, 100)       # notes' example (0.9, 0.7): 0.93
# numeric backward induction on a grid of offers (step 1/1000), ties accepted
for a_, b_ in [(F(9, 10), F(7, 10)), (F(1, 5), F(9, 10)), (F(3, 5), F(3, 5))]:
    grid_ = [F(k, 1000) for k in range(1001)]
    w1, w2 = a_**2 * 1, F(0)                            # values from period 3
    s2 = min(x for x in grid_ if a_ * x >= w1)           # P2 offers P1 the least he accepts
    w1, w2 = a_ * s2, b_ * (1 - s2)
    s1 = max(x for x in grid_ if 1 - x >= w2)            # P1 keeps the most P2 accepts
    assert s1 == 1 - b_ * (1 - a_)

# ---- item 24: Munoz-Garcia Ch. 6 Ex. 8, stationary SPE, proposers cycle 1 -> 2 -> 3 -> 1
dl = sp.symbols("delta", positive=True)
V = {(i, j): sp.Symbol(f"V_{i}{j}") for i in range(3) for j in range(3)}  # i's value when j proposes
nxt = lambda j: (j + 1) % 3
eqs = []
for j in range(3):
    for i in range(3):
        if i != j:
            eqs.append(sp.Eq(V[(i, j)], dl * V[(i, nxt(j))]))   # responder gets his continuation
    eqs.append(sp.Eq(V[(j, j)], 1 - sum(V[(i, j)] for i in range(3) if i != j)))
solv = sp.solve(eqs, list(V.values()), dict=True)
assert len(solv) == 1
sv = solv[0]
den = 1 + dl + dl**2
for j in range(3):
    assert sp.simplify(sv[V[(j, j)]] - 1 / den) == 0
    assert sp.simplify(sv[V[(nxt(j), j)]] - dl / den) == 0
    assert sp.simplify(sv[V[(nxt(nxt(j)), j)]] - dl**2 / den) == 0
    # proposer prefers immediate agreement: 1/den > delta * V_j(j+1) = delta^3/den
    assert sp.simplify(sv[V[(j, j)]] - dl * sv[V[(j, nxt(j))]] - (1 - dl**3) / den) == 0
# numbers at delta = 0.8 and limits
x = [sv[V[(i, 0)]].subs(dl, sp.Rational(4, 5)) for i in range(3)]
assert x == [sp.Rational(25, 61), sp.Rational(20, 61), sp.Rational(16, 61)]
assert [sp.limit(sv[V[(i, 0)]], dl, 1) for i in range(3)] == [sp.Rational(1, 3)] * 3
# one-shot deviations from the stationary profile at delta = 4/5 on a grid of proposals
dv = F(4, 5)
a0 = 1 / (1 + dv + dv**2)
share = {0: a0, 1: dv * a0, 2: dv**2 * a0}             # proposer, next proposer, the one after
best = F(-1)
for k1 in range(0, 201):
    for k2 in range(0, 201 - k1):
        y1, y2 = F(k1, 200), F(k2, 200)                  # offers to next proposer and the one after
        ok = y1 >= dv * share[0] and y2 >= dv * share[1]  # both accept iff >= continuation
        own = 1 - y1 - y2 if ok else dv * (dv**2 * a0)   # rejection: proposer becomes "the one after"
        best = max(best, own)
assert a0 - F(1, 100) < best <= a0                      # no grid proposal beats the stationary one
assert a0 == F(25, 61)
# "everyone always rejects" under simultaneous votes: given the other responder rejects, a
# responder's vote does not change the outcome, so rejecting is a best reply (payoff 0 = 0)
passed = lambda vote_i, vote_other: vote_i and vote_other  # unanimity
assert all(passed(v_i, False) is False for v_i in (True, False))

print("all B L04 checks passed")
