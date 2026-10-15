"""Independent check of every result in lista-lecture-01.tex (graduate, symbolic).

Run: python Listas/lista-lecture-01-check.py
Aborts (AssertionError) on the first mismatch; prints "ALL CHECKS PASSED" otherwise.
Matrix games are solved mechanically (IESDS, every order of weak elimination); closed forms
are checked with sympy; signs, limits and orderings symbolically where possible and
otherwise at many random admissible parameter draws.
"""
import itertools
import random
from fractions import Fraction as Fr
from functools import lru_cache

import sympy as sp

random.seed(20261013)
DRAWS = 1500
ok = lambda e: sp.simplify(e) == 0


def draw(lo, hi):
    return random.uniform(lo, hi)


# ---------------------------------------------------------------- generic machinery
def dominated(diffs, weak):
    """True if the payoff differences (dominator minus candidate) show dominance."""
    if weak:
        return all(d >= 0 for d in diffs) and any(d > 0 for d in diffs)
    return all(d > 0 for d in diffs)


def iesds2(U1, U2, weak=False):
    """Two-player IESDS removing every dominated strategy each round.

    U1, U2: payoff matrices (rows = player 1). Returns (rows, cols, rounds).
    """
    R, C, k = list(range(len(U1))), list(range(len(U1[0]))), 0
    while True:
        dR = [r for r in R if any(dominated([U1[r2][c] - U1[r][c] for c in C], weak)
                                  for r2 in R if r2 != r)]
        dC = [c for c in C if any(dominated([U2[r][c2] - U2[r][c] for r in R], weak)
                                  for c2 in C if c2 != c)]
        if not dR and not dC:
            return R, C, k
        R = [r for r in R if r not in dR]
        C = [c for c in C if c not in dC]
        k += 1


def iesdsn(sets, u, weak=False, order=None):
    """n-player IESDS on finite sets. u(i, profile) -> payoff.

    order=None removes every dominated strategy each round; otherwise order is a
    random.Random used to remove a random nonempty subset each step.
    """
    sets = [list(s) for s in sets]
    n = len(sets)
    while True:
        dom = []
        for i in range(n):
            others = [sets[j] for j in range(n) if j != i]
            for s in sets[i]:
                for s2 in sets[i]:
                    if s2 == s:
                        continue
                    diffs = []
                    for o in itertools.product(*others):
                        p = list(o[:i]) + [s] + list(o[i:])
                        p2 = list(o[:i]) + [s2] + list(o[i:])
                        diffs.append(u(i, tuple(p2)) - u(i, tuple(p)))
                    if dominated(diffs, weak):
                        dom.append((i, s))
                        break
        if not dom:
            return [tuple(s) for s in sets]
        if order is not None:
            dom = order.sample(dom, order.randint(1, len(dom)))
        for i, s in dom:
            sets[i].remove(s)


# ================================================================ BLOCK 1
# ---- Q1 a) n-partner effort/shirk game with synergy theta
def partnership_conditions(n, y, th, c):
    Y = lambda k: y * k + th * k * (k - 1) / 2
    shirk_dom = all(Y(k + 1) / n - c < Y(k) / n for k in range(n))  # vs every k others
    # all-shirk Pareto dominated by some profile: enumerate k effort-takers
    pd = False
    for k in range(1, n + 1):
        eff, shk = Y(k) / n - c, Y(k) / n
        pays = [eff] * k + [shk] * (n - k)
        if all(p >= 0 for p in pays) and any(p > 0 for p in pays):
            pd = True
    return shirk_dom and pd


for _ in range(DRAWS):
    n, y, th = random.randint(2, 7), draw(0.1, 5), draw(0, 3)
    lo, hi = (y + th * (n - 1)) / n, y + th * (n - 1) / 2
    c = draw(0.01, 1.3 * hi + 1)
    if min(abs(c - lo), abs(c - hi)) < 1e-9:
        continue
    assert partnership_conditions(n, y, th, c) == (lo < c < hi)
    assert lo < hi  # the dilemma set is never empty for n >= 2
# distractors differ from the key at some admissible point
n_, y_, th_ = 3, 1.0, 1.0
key1a = ((y_ + th_ * (n_ - 1)) / n_, y_ + th_ * (n_ - 1) / 2)
for d in [(y_ / n_, y_), ((y_ + th_ * (n_ - 1)) / n_, y_ + th_ * (n_ - 1)),
          (y_ / n_, y_ + th_ * (n_ - 1) / 2), ((y_ + th_) / n_, y_ + th_ * n_ / 2)]:
    assert d != key1a, d

# ---- Q1 b) second-price auction with reserve r: truthful weakly dominant, nothing strict
def spa_payoff(i, bids, vals, r):
    hi = max(bids)
    if hi < r:
        return Fr(0)
    winners = [j for j, b in enumerate(bids) if b == hi]
    if i not in winners:
        return Fr(0)
    others = [b for j, b in enumerate(bids) if j != i]
    price = max([r] + others)
    return Fr(vals[i] - price, len(winners))


grid = [Fr(k, 2) for k in range(0, 21)]  # own bids 0, 0.5, ..., 10
opp_grid = grid + [Fr(12)]  # a rival bid above every own bid (bids are unbounded)
r = Fr(2)
for nb in (2, 3):
    vals = [Fr(5), Fr(3), Fr(1)][:nb]  # bidder 0 has v > r; bidder 2 (if any) has v < r
    for i in range(nb):
        opp = [opp_grid] * (nb - 1)
        def pay(b):
            return [spa_payoff(i, tuple(list(o[:i]) + [b] + list(o[i:])), vals, r)
                    for o in itertools.product(*opp)]
        truth = pay(vals[i])
        for b in grid:
            if b == vals[i]:
                continue
            pb = pay(b)
            assert all(t >= q for t, q in zip(truth, pb))  # truthful weakly better
            if vals[i] > r:
                assert any(t > q for t, q in zip(truth, pb))  # ... strictly somewhere
        for b, b2 in itertools.permutations(grid, 2):  # no bid strictly dominated
            assert not all(x > z for x, z in zip(pay(b2), pay(b)))
        if vals[i] > r:  # bids below r: weakly (not strictly) dominated by v_i
            for b in [g for g in grid if g < r]:
                pb = pay(b)
                assert not all(t > q for t, q in zip(truth, pb))

# ---- Q1 c) invariance of a strict DSE in finite games (T)
for _ in range(300):
    m1, m2 = random.randint(2, 4), random.randint(2, 4)
    U1 = [[random.randint(-5, 5) for _ in range(m2)] for _ in range(m1)]
    U2 = [[random.randint(-5, 5) for _ in range(m2)] for _ in range(m1)]
    U1[0] = [max(row[c] for row in U1) + random.randint(1, 3) for c in range(m2)]
    for rr in range(m1):
        U2[rr][0] = max(U2[rr]) + random.randint(1, 3)
    g = min([U1[0][c] - U1[rr][c] for rr in range(1, m1) for c in range(m2)]
            + [U2[rr][0] - U2[rr][c] for rr in range(m1) for c in range(1, m2)])
    eps = g / 2
    P1 = [[v + draw(-0.999, 0.999) * eps for v in row] for row in U1]
    P2 = [[v + draw(-0.999, 0.999) * eps for v in row] for row in U2]
    assert all(P1[0][c] > P1[rr][c] for rr in range(1, m1) for c in range(m2))
    assert all(P2[rr][0] > P2[rr][c] for rr in range(m1) for c in range(1, m2))
# weak dominance is not invariant: U weakly dominates D; perturb u1(D,L) up by eps/2
W1 = [[1, 1], [1, 0]]
assert dominated([W1[0][c] - W1[1][c] for c in range(2)], weak=True)
for eps in [Fr(1, 10), Fr(1, 1000)]:
    W1p = [[1, 1], [1 + eps / 2, 0]]
    assert not dominated([W1p[0][c] - W1p[1][c] for c in range(2)], weak=True)

# ---- Q1 d) n-player Pareto claim (F): 3-player counterexample, true for n = 2
PD = {("M", "M"): (-1, -1), ("M", "F"): (-4, 0), ("F", "M"): (0, -4), ("F", "F"): (-3, -3)}
def u3p(i, p):
    a, b = PD[(p[0], p[1])]
    if i < 2:
        return (a, b)[i]
    return a + b + (1 if p[2] == "X" else 0)
S3 = [("M", "F"), ("M", "F"), ("X", "Y")]
assert iesdsn(S3, u3p) == [("F",), ("F",), ("X",)]
sD, sP = ("F", "F", "X"), ("M", "M", "X")
assert all(u3p(i, sP) > u3p(i, sD) for i in range(3)) and sP[2] == sD[2]
for _ in range(500):  # n = 2: any Pareto improvement on a strict DSE moves both players
    U1 = [[random.randint(-4, 4) for _ in range(3)] for _ in range(3)]
    U2 = [[random.randint(-4, 4) for _ in range(3)] for _ in range(3)]
    U1[0] = [max(row[c] for row in U1) + 1 for c in range(3)]
    for rr in range(3):
        U2[rr][0] = max(U2[rr]) + 1
    for a, b in itertools.product(range(3), range(3)):
        better = U1[a][b] >= U1[0][0] and U2[a][b] >= U2[0][0] and \
            (U1[a][b] > U1[0][0] or U2[a][b] > U2[0][0])
        if better:
            assert a != 0 and b != 0

# ---- Q2 partnership with continuous effort
y, c, n, e, ei, k, al = sp.symbols("y c n e e_i k alpha", positive=True)
eD = al * y / c
u_own = al * y * e - c * e**2 / 2  # part of u_i that depends on e_i
assert ok((u_own.subs(e, eD) - u_own) - c / 2 * (e - eD) ** 2)  # dominance identity
# equal shares
eDn = y / (n * c)
uD = y * eDn - c * eDn**2 / 2  # symmetric profile: each partner gets y*e - c e^2/2
assert ok(uD - y**2 * (2 * n - 1) / (2 * n**2 * c))
roots = sp.solve(sp.Eq(y * e - c * e**2 / 2, uD), e)
assert {sp.simplify(r_) for r_ in roots} == {sp.simplify(eDn), sp.simplify((2 * n - 1) * y / (n * c))}
assert ok(sum(roots) / 2 - y / c)  # midpoint = efficient effort
Wstar = n * y**2 / (2 * c)
WD = n * uD
assert ok(WD - y**2 * (2 * n - 1) / (2 * n * c))
assert ok(1 - WD / Wstar - (n - 1) ** 2 / n**2)
assert ok(Wstar / n - uD - y**2 * (n - 1) ** 2 / (2 * n**2 * c))
# second best among balanced sharing rules: W(alpha) = (y^2/c) sum(alpha - alpha^2/2)
for _ in range(DRAWS):
    nn = random.randint(2, 8)
    a_ = [random.random() for _ in range(nn)]
    s_ = sum(a_)
    a_ = [x / s_ for x in a_]
    W_a = sum(x - x**2 / 2 for x in a_)
    assert W_a <= 1 - 1 / (2 * nn) + 1e-12
    assert W_a >= 0.5 - 1e-12  # minimum at a corner alpha = e_1
# signs
for _ in range(DRAWS):
    sub = {y: draw(0.1, 5), c: draw(0.1, 5), n: draw(1.01, 20)}
    assert float(sp.diff(eDn, n).subs(sub)) < 0 and float(sp.diff(eDn, c).subs(sub)) < 0
    assert float(sp.diff(uD, n).subs(sub)) < 0 and float(sp.diff(uD, y).subs(sub)) > 0
    assert float(sp.diff(WD, n).subs(sub)) > 0  # total DSE surplus rises with n
    assert float(sp.diff(WD / n, n).subs(sub)) < 0
    assert float(sp.diff((n - 1) ** 2 / n**2, n).subs(sub)) > 0
assert ok(sp.diff(uD, n) + y**2 * (n - 1) / (n**3 * c))
assert sp.limit((n - 1) ** 2 / n**2, n, sp.oo) == 1

# ================================================================ BLOCK 2
# ---- Q3 a) parametric 3x3: u1(U,C) = x
def game3a(x):
    U1 = [[2, x, 5], [5, 4, 2], [1, 1, 4]]
    U2 = [[3, 2, 0], [3, 4, 2], [4, 5, 6]]
    return U1, U2


xs = [Fr(k, 8) for k in range(-16, 65)] + [Fr(1), Fr(4)]
for x in xs:
    R, C, kk = iesds2(*game3a(x))
    unique = len(R) == 1 and len(C) == 1
    assert unique == (1 < x < 4), x
    if unique:
        assert (R, C, kk) == ([1], [1], 4)  # (M, C) after four rounds
    elif x <= 1:
        assert (R, C, kk) == ([0, 1, 2], [0, 1, 2], 0)
    else:
        assert (R, C) == ([0, 1], [0, 1])

# ---- Q3 b) weak elimination: every one-at-a-time order
WB1 = [[1, 1, 0], [1, 2, 2], [0, 2, 1]]
WB2 = [[2, 0, 1], [2, 2, 1], [0, 1, 2]]
assert iesds2(WB1, WB2) == ([0, 1, 2], [0, 1, 2], 0)  # strict IESDS removes nothing


def weak_outcomes(U1, U2):
    res = set()

    @lru_cache(None)
    def go(R, C):
        moves = [("r", r) for r in R if any(dominated([U1[r2][c] - U1[r][c] for c in C], True)
                                            for r2 in R if r2 != r)]
        moves += [("c", c) for c in C if any(dominated([U2[r][c2] - U2[r][c] for r in R], True)
                                             for c2 in C if c2 != c)]
        if not moves:
            res.add((R, C))
            return
        for t, v in moves:
            if t == "r":
                go(tuple(x for x in R if x != v), C)
            else:
                go(R, tuple(x for x in C if x != v))

    go((0, 1, 2), (0, 1, 2))
    return res


outs = weak_outcomes(WB1, WB2)
singles = {(R[0], C[0]) for R, C in outs if len(R) == 1 and len(C) == 1}
assert singles == {(1, 0), (1, 1)}  # (M,L) and (M,C)
assert {WB1[1][0], WB1[1][1]} == {1, 2}  # player 1 gets 1 or 2
assert ((0, 1), (0,)) in outs  # some orders stop at {U,M} x {L}
assert iesds2(WB1, WB2, weak=True)[:2] == ([1], [0, 1])  # all-at-once: {M} x {L,C}
assert all(1 in R for R, C in outs)  # M is never removed

# ---- Q3 c) S_i^infinity can be empty with infinite strategy sets (F); finite: never empty
for s_ in [Fr(0), Fr(1, 2), Fr(99, 100)]:  # S = [0,1), u = s: s dominated by (s+1)/2
    assert (s_ + 1) / 2 > s_ and (s_ + 1) / 2 < 1
for _ in range(300):
    m1, m2 = random.randint(1, 5), random.randint(1, 5)
    U1 = [[random.randint(0, 6) for _ in range(m2)] for _ in range(m1)]
    U2 = [[random.randint(0, 6) for _ in range(m2)] for _ in range(m1)]
    R, C, _ = iesds2(U1, U2)
    assert R and C

# ---- Q3 d) order independence of strict IESDS in finite games (T)
for _ in range(200):
    m1, m2 = random.randint(2, 4), random.randint(2, 4)
    U1 = [[random.randint(0, 4) for _ in range(m2)] for _ in range(m1)]
    U2 = [[random.randint(0, 4) for _ in range(m2)] for _ in range(m1)]
    u = lambda i, p: (U1, U2)[i][p[0]][p[1]]
    base = iesdsn([range(m1), range(m2)], u)
    for _ in range(5):
        assert iesdsn([range(m1), range(m2)], u, order=random.Random(random.random())) == base

# ---- Q4 Cournot by IESDS, asymmetric costs
a, b, c1, c2, q = sp.symbols("a b c_1 c_2 q", positive=True)


def BR(ai, bi, ci, qj):
    return max(Fr(0), (ai - ci - bi * qj) / (2 * bi))


def cournot_iesds(av, bv, cv1, cv2, rounds):
    """Interval recursion S_i^k = [BR_i(U_j^{k-1}), BR_i(L_j^{k-1})], U^0 = infinity."""
    L, U = [Fr(0), Fr(0)], [None, None]
    hist = []
    cs = (cv1, cv2)
    for _ in range(rounds):
        nL = [BR(av, bv, cs[i], U[1 - i]) if U[1 - i] is not None else Fr(0) for i in range(2)]
        nU = [BR(av, bv, cs[i], L[1 - i]) for i in range(2)]
        L, U = nL, nU
        hist.append((tuple(L), tuple(U)))
    return hist


def profit(av, bv, ci, qi, qj):
    return qi * (max(Fr(0), av - bv * (qi + qj)) - ci)


for _ in range(300):
    av = Fr(random.randint(20, 60))
    bv = Fr(random.randint(1, 5), random.randint(1, 3))
    cv1, cv2 = Fr(random.randint(1, int(av) - 1)), Fr(random.randint(1, int(av) - 1))
    hist = cournot_iesds(av, bv, cv1, cv2, 40)
    m = [(av - cv1) / (2 * bv), (av - cv2) / (2 * bv)]
    assert hist[0] == ((0, 0), (m[0], m[1]))
    for kk in range(1, 40):  # widths halve and swap
        for i in range(2):
            wi = hist[kk][1][i] - hist[kk][0][i]
            wj = hist[kk - 1][1][1 - i] - hist[kk - 1][0][1 - i]
            assert wi <= wj / 2 and wi >= 0
            assert hist[kk][0][i] >= hist[kk - 1][0][i] and hist[kk][1][i] <= hist[kk - 1][1][i]
    if av - 2 * cv1 + cv2 > 0 and av - 2 * cv2 + cv1 > 0:
        qes = [(av - 2 * cv1 + cv2) / (3 * bv), (av - 2 * cv2 + cv1) / (3 * bv)]
        for i in range(2):
            assert hist[-1][0][i] <= qes[i] <= hist[-1][1][i]
            assert abs(float(hist[-1][1][i] - hist[-1][0][i])) < 1e-9
            for kk in range(40):  # never a singleton after finitely many rounds
                assert hist[kk][1][i] > hist[kk][0][i]
                k_ = kk + 1  # exact halving: w_i^k = m_i/2^(k-1) (k odd), m_j/2^(k-1) (k even)
                assert hist[kk][1][i] - hist[kk][0][i] == m[i if k_ % 2 else 1 - i] / 2 ** (k_ - 1)
    else:
        i_out = 0 if av - 2 * cv1 + cv2 <= 0 else 1
        qes = [Fr(0), Fr(0)]
        qes[1 - i_out] = m[1 - i_out]
        for i in range(2):
            assert hist[-1][0][i] <= qes[i] <= hist[-1][1][i]
        if (av - 2 * (cv1, cv2)[i_out] + (cv1, cv2)[1 - i_out]) < 0:
            assert hist[-1][1][i_out] == 0  # out after finitely many rounds
    # strict dominance claims of item a) at sampled points (needs c_i > 0)
    for _ in range(5):
        qj = Fr(random.randint(0, 200), 3)
        qhigh = m[0] + Fr(random.randint(1, 100), 7)
        assert profit(av, bv, cv1, m[0], qj) > profit(av, bv, cv1, qhigh, qj)
# with c_i = 0, q > m is NOT strictly dominated: both earn 0 when q_j >= a/b
av, bv = Fr(10), Fr(1)
assert profit(av, bv, 0, av / 2, av) == profit(av, bv, 0, av, av) == 0
# closed forms
q1 = (a - 2 * c1 + c2) / (3 * b)
q2 = (a - 2 * c2 + c1) / (3 * b)
br1 = lambda x: (a - c1 - b * x) / (2 * b)
br2 = lambda x: (a - c2 - b * x) / (2 * b)
assert ok(br1(q2) - q1) and ok(br2(q1) - q2)
assert ok(br1(br2(q)) - ((a - 2 * c1 + c2) / (4 * b) + q / 4))
Q = q1 + q2
P = a - b * Q
assert ok(P - (a + c1 + c2) / 3) and ok((P - c1) - b * q1)
pi1 = (P - c1) * q1
assert ok(pi1 - (a - 2 * c1 + c2) ** 2 / (9 * b))
for var, sgn in [(a, 1), (c1, -1), (c2, 1), (b, -1)]:
    for _ in range(200):
        cv1_, cv2_ = draw(0.1, 5), draw(0.1, 5)
        sub = {a: draw(max(2 * cv1_ - cv2_, 2 * cv2_ - cv1_, cv1_, cv2_) + 0.1, 20),
               b: draw(0.1, 5), c1: cv1_, c2: cv2_}
        assert sgn * float(sp.diff(q1, var).subs(sub)) > 0
        assert sgn * float(sp.diff(pi1, var).subs(sub)) > 0
        assert float(sp.diff(Q, c1).subs(sub)) < 0 and ok(sp.diff(P, b))
        assert float(sp.diff(P, c1).subs(sub)) > 0 and float(sp.diff(Q, b).subs(sub)) < 0
assert ok(q1.subs(c2, c1) - (a - c1) / (3 * b))
assert ok(q1.subs(c1, (a + c2) / 2)) and ok(q2.subs(c1, (a + c2) / 2) - (a - c2) / (2 * b))
# n >= 3 symmetric firms: every q in [0, m] is the unique best reply to some Q_-i in [0, 2m]
for _ in range(200):
    av, bv, cv = draw(5, 50), draw(0.2, 4), 0.0
    cv = draw(0.1, av - 0.1)
    mm = (av - cv) / (2 * bv)
    qq = draw(0, mm)
    Qm = (av - cv) / bv - 2 * qq
    assert -1e-9 <= Qm <= 2 * mm + 1e-9
    assert abs(max(0, (av - cv - bv * Qm) / (2 * bv)) - qq) < 1e-9

# ================================================================ BLOCK 3
def line_pay(n, w, sa, sb):
    """Customers of the chain at town sa when the rival is at sb (towns 1..n, weights w)."""
    tot = Fr(0)
    for j in range(1, n + 1):
        da, db = abs(j - sa), abs(j - sb)
        if da < db:
            tot += w[j - 1]
        elif da == db:
            tot += Fr(w[j - 1], 2)
    return tot


def line_game(n, w):
    U1 = [[line_pay(n, w, sa, sb) for sb in range(1, n + 1)] for sa in range(1, n + 1)]
    U2 = [[sum(w) - U1[i][j] for j in range(n)] for i in range(n)]
    return U1, U2


def iesds_rounds_detail(U1, U2):
    """Strict IESDS returning the list of removed (rows, cols) per round."""
    R, C, rounds = list(range(len(U1))), list(range(len(U1[0]))), []
    while True:
        dR = [r for r in R if any(all(U1[r2][c] > U1[r][c] for c in C) for r2 in R if r2 != r)]
        dC = [c for c in C if any(all(U2[r][c2] > U2[r][c] for r in R) for c2 in C if c2 != c)]
        if not dR and not dC:
            return R, C, rounds
        rounds.append((dR, dC))
        R = [r for r in R if r not in dR]
        C = [c for c in C if c not in dC]


# ---- Q5 a) ring road: payoffs n/2 everywhere, nothing eliminated, antipodal minimizes distance
for n in range(3, 21):
    ring = lambda i, j: min(abs(i - j), n - abs(i - j))
    for sa in range(n):
        for sb in range(n):
            ua = sum(Fr(1) if ring(t, sa) < ring(t, sb) else Fr(1, 2) if ring(t, sa) == ring(t, sb)
                     else Fr(0) for t in range(n))
            assert ua == Fr(n, 2)
    dist = {(sa, sb): sum(min(ring(t, sa), ring(t, sb)) for t in range(n))
            for sa in range(n) for sb in range(n)}
    best = min(dist.values())
    assert n // 2 in {ring(sa, sb) for (sa, sb), d in dist.items() if d == best}
    assert best == n * n // 8 and dist[(0, 0)] == n * n // 4
    assert dist[(0, 0)] == max(dist.values())

# ---- Q5 b) capital town with 1 + 2h households: survivor (n+1)/2 - h
for n in range(3, 24, 2):
    for h in range(0, (n - 1) // 2 + 1):
        w = [1 + 2 * h] + [1] * (n - 1)
        R, C, _ = iesds2(*line_game(n, w))
        assert R == C == [(n + 1) // 2 - h - 1], (n, h, R)
# distractors differ for h >= 1
for n, h in [(9, 1), (11, 2)]:
    key = (n + 1) // 2 - h
    assert key not in {(n + 1) // 2 - 2 * h, (n + 1) // 2, 1} or h == 0

# ---- Q5 c) median strictly dominant only for n = 3 (F for odd n >= 5)
for n in range(3, 22, 2):
    U1, _ = line_game(n, [1] * n)
    med = (n + 1) // 2 - 1
    strict_dom = all(all(U1[med][cc] > U1[r][cc] for cc in range(n)) for r in range(n) if r != med)
    assert strict_dom == (n == 3)
    if n >= 5:
        brs = [r for r in range(n) if U1[r][0] == max(U1[x][0] for x in range(n))]
        assert brs == [1]  # best reply to a rival at town 1 is town 2

# ---- Q5 d) zoning by halves (n even): n/2 strictly dominant for A, n/2+1 for B (T)
for n in range(4, 31, 2):
    W, E = range(1, n // 2 + 1), range(n // 2 + 1, n + 1)
    for sa in W:
        if sa != n // 2:
            assert all(line_pay(n, [1] * n, n // 2, sb) > line_pay(n, [1] * n, sa, sb) for sb in E)
    for sb in E:
        if sb != n // 2 + 1:
            assert all(line_pay(n, [1] * n, n // 2 + 1, sa) > line_pay(n, [1] * n, sb, sa)
                       for sa in W)

# ---- Q6 uniform line, general n
for n in range(2, 41):
    U1, U2 = line_game(n, [1] * n)
    for sa in range(1, n + 1):
        for sb in range(1, n + 1):
            f = Fr(sa + sb - 1, 2) if sa < sb else Fr(n, 2) if sa == sb else n - Fr(sa + sb - 1, 2)
            assert U1[sa - 1][sb - 1] == f
            assert U1[sa - 1][sb - 1] + U1[sb - 1][sa - 1] == n  # constant sum
    R, C, rounds = iesds_rounds_detail(U1, U2)
    if n == 2:
        assert R == C == [0, 1] and not rounds
        continue
    for kk, (dR, dC) in enumerate(rounds, start=1):  # round k removes towns k and n+1-k
        assert dR == dC == [kk - 1, n - kk]
    if n % 2:
        assert R == C == [(n - 1) // 2] and len(rounds) == (n - 1) // 2
    else:
        assert R == C == [n // 2 - 1, n // 2] and len(rounds) == n // 2 - 1
    # welfare: total travel distance
    dist = lambda x, y_: sum(min(abs(j - x), abs(j - y_)) for j in range(1, n + 1))
    dmin = min(dist(x, y_) for x in range(1, n + 1) for y_ in range(1, n + 1))
    assert dmin == n * n // 8
    if n % 2:
        des = dist((n + 1) // 2, (n + 1) // 2)
        assert des == (n * n - 1) // 4 and Fr(des, dmin) == 2
    else:
        vals = {dist(x + 1, y_ + 1) for x in R for y_ in C}
        assert vals == {n * n // 4, n * (n - 2) // 4}
        if n % 4 == 0:
            assert Fr(n * n // 4, dmin) == 2
        else:
            assert Fr(n * n // 4, dmin) == Fr(2 * n * n, n * n - 4) > 2
            assert Fr(n * (n - 2) // 4, dmin) == Fr(2 * n, n + 2)
assert Fr(36 // 4, 36 // 8) == Fr(9, 4)  # n = 6 counterexample (Q5 d draft / Q6 d)

# ---- Q6 c) continuum [0,1]
def ucont(a_, b_):
    if a_ < b_:
        return (a_ + b_) / 2
    if a_ == b_:
        return Fr(1, 2)
    return 1 - (a_ + b_) / 2


rng = random.Random(7)
for _ in range(4000):
    ap = Fr(rng.randint(1, 999), 1000)
    bb = Fr(rng.randint(0, 1000), 1000)
    if ap <= Fr(2, 3):  # 0 strictly dominated by any a' in (0, 2/3]
        assert ucont(ap, bb) > ucont(Fr(0), bb)
    else:  # a' > 2/3 fails against b just below a'
        bw = ap - Fr(1, 10**6)
        assert ucont(ap, bw) <= ucont(Fr(0), bw)
    # interior a is never strictly dominated: explicit witness against every a'
    a_ = Fr(rng.randint(1, 999), 1000)
    a2 = Fr(rng.randint(1, 999), 1000)
    if a2 == a_:
        continue
    if a_ <= Fr(1, 2):
        bw = a_ / 2 if a2 > a_ else (a_ + a2) / 2
    else:
        bw = (1 + a_) / 2 if a2 < a_ else (a_ + a2) / 2
    assert 0 < bw < 1
    assert ucont(a2, bw) <= ucont(a_, bw)
x = sp.symbols("x")
dcl = sp.integrate(sp.Abs(x - sp.Rational(1, 2)), (x, 0, 1))
dopt = 2 * sp.integrate(sp.Abs(x - sp.Rational(1, 4)), (x, 0, sp.Rational(1, 2)))
assert dcl == sp.Rational(1, 4) and dopt == sp.Rational(1, 8)
# per-household averages: (n^2-1)/(4n) and floor(n^2/8)/n, ratio to the stretch length -> 1/4, 1/8
nn = sp.symbols("n", positive=True)
assert sp.limit((nn**2 - 1) / (4 * nn) / (nn - 1), nn, sp.oo) == sp.Rational(1, 4)
assert sp.limit((nn**2 / 8) / nn / (nn - 1), nn, sp.oo) == sp.Rational(1, 8)

print("ALL CHECKS PASSED")
