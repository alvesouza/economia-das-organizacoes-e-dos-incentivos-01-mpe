"""Checks every number and equilibrium claim in the ten Lecture 5 solutions (items 41-50):
sol-cabral-7-13, sol-tadelis-10-2, sol-munoz-garcia-6-9, sol-tadelis-9-1, sol-tadelis-11-5,
sol-gibbons-2-20, sol-munoz-garcia-6-1, sol-tadelis-10-3, sol-gibbons-2-11, sol-tadelis-10-7.
Exact arithmetic (fractions, sympy); every threshold is tested on both sides.

Run: python check_C_L05.py  -> prints one line per item and "all C L05 checks passed",
or stops with an AssertionError on the first wrong claim.
"""
from fractions import Fraction as F
from itertools import product

import sympy as sp

EPS = F(1, 1000)


def pure_ne(U, rows, cols):
    """Pure Nash equilibria of a bimatrix U[(r, c)] = (u1, u2)."""
    return [(r, c) for r, c in product(rows, cols)
            if U[(r, c)][0] == max(U[(x, c)][0] for x in rows)
            and U[(r, c)][1] == max(U[(r, y)][1] for y in cols)]


def strictly_dominant(U, rows, cols, player):
    """The strictly dominant action of `player` (0 rows, 1 cols), or None."""
    own, other = (rows, cols) if player == 0 else (cols, rows)
    cell = (lambda a, b: (a, b)) if player == 0 else (lambda a, b: (b, a))
    for a in own:
        if all(U[cell(a, b)][player] > U[cell(x, b)][player] for x in own if x != a for b in other):
            return a
    return None


def grim(vc, vd, vstar):
    """Grim-trigger threshold (Tadelis (10.5)): delta >= (v^d - v^c)/(v^d - v*)."""
    return F(vd - vc, vd - vstar)


def grim_ok(vc, vd, vstar, d):
    """Cooperation-phase one-stage deviation test at discount factor d (present values)."""
    return vc / (1 - d) >= vd + d * vstar / (1 - d)


def threshold_tests(vc, vd, vstar, d0):
    """d0 is the exact cutoff: holds at d0 and just above, fails just below, and on a grid."""
    assert grim(vc, vd, vstar) == d0
    assert grim_ok(vc, vd, vstar, d0) and grim_ok(vc, vd, vstar, d0 + EPS)
    assert not grim_ok(vc, vd, vstar, d0 - EPS)
    assert all(grim_ok(vc, vd, vstar, F(k, 1000)) == (F(k, 1000) >= d0) for k in range(1, 1000))


# ============================================================ Cabral 7.13 (finitely repeated PD)
R, C = "TB", "LR"
UC = {("T", "L"): (5, 5), ("T", "R"): (3, 6), ("B", "L"): (6, 3), ("B", "R"): (4, 4)}
assert strictly_dominant(UC, R, C, 0) == "B" and strictly_dominant(UC, R, C, 1) == "R"
assert pure_ne(UC, R, C) == [("B", "R")]
# folded game in any period: stage payoffs + a continuation constant -> same unique NE
for k in (0, 4, F(37, 3)):
    folded = {a: (u[0] + k, u[1] + k) for a, u in UC.items()}
    assert pure_ne(folded, R, C) == [("B", "R")]
# brute force for T = 2: pure strategy = (period-1 action, map from 4 outcomes to an action)
cells = list(product(R, C))
S1 = [(a, dict(zip(cells, m))) for a in R for m in product(R, repeat=4)]
S2 = [(a, dict(zip(cells, m))) for a in C for m in product(C, repeat=4)]


def pay2(s1, s2, d):
    a = (s1[0], s2[0])
    b = (s1[1][a], s2[1][a])
    return tuple(UC[a][i] + d * UC[b][i] for i in range(2)), (a, b)


for d in (F(1, 10), F(1, 2), F(1)):
    ne_paths, spe = set(), []
    for s1, s2 in product(S1, S2):
        v, path = pay2(s1, s2, d)
        if all(pay2(t, s2, d)[0][0] <= v[0] for t in S1) and all(pay2(s1, t, d)[0][1] <= v[1] for t in S2):
            ne_paths.add(path)
            if all(pure_ne(UC, R, C) == [(s1[1][h], s2[1][h])] for h in cells):
                spe.append((s1, s2))
    assert ne_paths == {(("B", "R"), ("B", "R"))}          # every NE path is (B,R) twice
    assert len(spe) == 1 and spe[0][0][0] == "B" and set(spe[0][0][1].values()) == {"B"}
    assert spe[0][1][0] == "R" and set(spe[0][1][1].values()) == {"R"}
print("Cabral 7.13: unique stage NE (B,R); T=2 brute force (1024 profiles x 3 deltas): 1 SPE, "
      "all NE paths (B,R),(B,R)")

# ============================================================ Tadelis 10.2 (grim trigger)
R, C = "TMB", "LCR"
UT = {("T", "L"): (6, 6), ("T", "C"): (-1, 7), ("T", "R"): (-2, 8),
      ("M", "L"): (7, -1), ("M", "C"): (4, 4), ("M", "R"): (-1, 5),
      ("B", "L"): (8, -2), ("B", "C"): (5, -1), ("B", "R"): (0, 0)}
assert strictly_dominant(UT, R, C, 0) == "B" and strictly_dominant(UT, R, C, 1) == "R"
assert pure_ne(UT, R, C) == [("B", "R")]
assert all(UT[(r, c)] == UT[(c.translate(str.maketrans("LCR", "TMB")),
                                 r.translate(str.maketrans("TMB", "LCR")))][::-1]
           for r, c in product(R, C))                       # symmetric game
# minimax of player 1 = min over columns of the best row = 0 = stage NE payoff
assert min(max(UT[(r, c)][0] for r in R) for c in C) == 0
assert min(UT[("B", c)][0] for c in C) == 0                 # B guarantees >= 0: grim is optimal
dev_M = {r: UT[(r, "C")][0] for r in R}
dev_T = {r: UT[(r, "L")][0] for r in R}
assert max(dev_M, key=dev_M.get) == "B" and dev_M["B"] == 5
assert max(dev_T, key=dev_T.get) == "B" and dev_T["B"] == 8 and dev_T["M"] == 7
threshold_tests(4, 5, 0, F(1, 5))                           # (a) (M,C)
threshold_tests(6, 8, 0, F(1, 4))                           # (b) (T,L)
assert grim(6, 7, 0) == F(1, 7)                             # the wrong "deviate to M" answer
for d in (F(1, 5), F(1, 4), F(9, 10)):                      # punishment phase: deviating loses
    assert all(UT[(r, "R")][0] + d * 0 / (1 - d) <= 0 for r in R)
# window where (M,C) is sustainable but (T,L) is not
assert grim_ok(4, 5, 0, F(22, 100)) and not grim_ok(6, 8, 0, F(22, 100))
print("Tadelis 10.2: stage NE (B,R) (0,0); (a) delta* = 1/5, (b) delta* = 1/4; "
      "grid k/1000 and +-1/1000 around each cutoff pass")

# ============================================================ Munoz-Garcia Ch. 6 Ex. 9
R, C = "UD", "LR"
UM = {("U", "L"): (9, 9), ("U", "R"): (1, 10), ("D", "L"): (10, 1), ("D", "R"): (7, 7)}
assert strictly_dominant(UM, R, C, 0) == "D" and strictly_dominant(UM, R, C, 1) == "R"
assert pure_ne(UM, R, C) == [("D", "R")]
# mixed minimax: q = Pr(L); u1(U,q) = 1 + 8q, u1(D,q) = 7 + 3q; min over q of the max = 7 at q=0
q = sp.symbols("q")
u1U, u1D = 9 * q + 1 * (1 - q), 10 * q + 7 * (1 - q)
assert sp.expand(u1U - (1 + 8 * q)) == 0 and sp.expand(u1D - (7 + 3 * q)) == 0
grid = [F(k, 1000) for k in range(1001)]
assert min(max(1 + 8 * x, 7 + 3 * x) for x in grid) == 7
assert all(7 + 3 * x > 1 + 8 * x for x in grid)            # D strictly better for every q
# the book's u2(L;p) = 9p + 1(1-p) is 1 + 8p, not 7 + 3p (a slip; 7 + 3p is u2(R;p))
p = sp.symbols("p")
assert sp.expand(9 * p + (1 - p) - (1 + 8 * p)) == 0 and sp.expand(10 * p + 7 * (1 - p) - (7 + 3 * p)) == 0
# feasible set: convex hull of the four payoff vectors is the triangle (1,10), (10,1), (9,9)
hull = sp.convex_hull(*[sp.Point(*u) for u in UM.values()])
assert set(hull.vertices) == {sp.Point(1, 10), sp.Point(10, 1), sp.Point(9, 9)}
assert F(3, 7) * 9 + F(2, 7) * 1 + F(2, 7) * 10 == 7       # (7,7) = 3/7 (9,9) + 2/7 (1,10) + 2/7 (10,1)
assert hull.encloses_point(sp.Point(7, 7))                  # strictly inside
# FIR corners: edges (1,10)-(9,9) and (10,1)-(9,9) cut v1 = 7 and v2 = 7 at 37/4
e1 = sp.Line(sp.Point(1, 10), sp.Point(9, 9)).intersection(sp.Line(sp.Point(7, 0), sp.Point(7, 1)))[0]
e2 = sp.Line(sp.Point(10, 1), sp.Point(9, 9)).intersection(sp.Line(sp.Point(0, 7), sp.Point(1, 7)))[0]
assert e1 == sp.Point(7, sp.Rational(37, 4)) and e2 == sp.Point(sp.Rational(37, 4), 7)
fir = sp.Polygon(sp.Point(7, 7), e2, sp.Point(9, 9), e1)
assert fir.area == sp.Rational(9, 2)                         # area of the FIR quadrilateral
# (d) grim trigger supporting (U,L): 9/(1-d) >= 10 + 7d/(1-d) <=> d >= 1/3, both players
threshold_tests(9, 10, 7, F(1, 3))
dl = sp.symbols("delta", positive=True)
assert sp.solve(sp.Eq(9 / (1 - dl), 10 + 7 * dl / (1 - dl)), dl) == [sp.Rational(1, 3)]
# necessity for ANY Nash equilibrium: D guarantees >= 7 each period, so a deviator gets >= 10 + 7d/(1-d)
assert min(UM[("D", c)][0] for c in C) == 7 and min(UM[(r, "R")][1] for r in R) == 7
print("Munoz-Garcia 6.9: stage NE (D,R) (7,7) = minimax; hull = triangle (1,10),(10,1),(9,9); "
      "FIR corners (7,7),(37/4,7),(9,9),(7,37/4); delta* = 1/3 (book: 1/3)")

# ============================================================ Tadelis 9.1 (played twice)
R1, C1 = "TMB", "LCR"
U = {("T", "L"): (10, 10), ("T", "C"): (2, 12), ("T", "R"): (0, 13),
     ("M", "L"): (12, 2), ("M", "C"): (5, 5), ("M", "R"): (0, 0),
     ("B", "L"): (13, 0), ("B", "C"): (0, 0), ("B", "R"): (1, 1)}
cells = list(product(R1, C1))
stage_ne = pure_ne(U, R1, C1)
assert stage_ne == [("M", "C"), ("B", "R")]


def gains(a):
    """One-shot deviation gains (player 1, player 2) from period-1 profile a."""
    return (max(U[(r, a[1])][0] for r in R1) - U[a][0],
            max(U[(a[0], c)][1] for c in C1) - U[a][1])


def is_spe(a, cont, d):
    """Pure SPE test: period-1 profile a, continuation map cont: outcome -> stage NE.
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
assert {a for a, _ in paths} == set(cells) - {("M", "R"), ("B", "C")}
assert gains(("M", "R")) == (1, 5) and gains(("B", "C")) == (5, 1)
assert len(paths) == 9 and spe_count == 992
dstar = {a: F(max(gains(a)), 4) for a, _ in paths}
assert dstar == {("T", "L"): F(3, 4), ("T", "C"): F(3, 4), ("T", "R"): F(1, 4),
                 ("M", "L"): F(3, 4), ("B", "L"): F(1, 4), ("M", "C"): 0, ("B", "R"): 0}
best_cont = lambda a: {x: (("M", "C") if x == a else ("B", "R")) for x in cells}
for a, d0 in dstar.items():
    if d0 > 0:
        assert is_spe(a, best_cont(a), d0) and is_spe(a, best_cont(a), d0 + EPS)
        assert not any(is_spe(a, dict(zip(cells, m)), d0 - EPS) for m in product(stage_ne, repeat=9))
        assert all(is_spe(a, best_cont(a), F(k, 1000)) == (F(k, 1000) >= d0) for k in range(1, 1001))
# (T,L) worked numbers at delta = 1: path 15, best deviation 14 for each player
assert U[("T", "L")][0] + U[("M", "C")][0] == 15 and U[("B", "L")][0] + U[("B", "R")][0] == 14
print(f"Tadelis 9.1: stage NE (M,C),(B,R); {spe_count} pure SPE at delta=1 on 9 paths; "
      "delta* = 3/4 (TL, TC, ML), 1/4 (TR, BL); grid and +-1/1000 pass")

# ============================================================ Tadelis 11.5 (asymmetric patience)
d1, d2 = sp.symbols("delta_1 delta_2", positive=True)
x3 = 1
x2 = d1 * x3
x1 = 1 - d2 * (1 - x2)
assert sp.expand(x1 - (1 - d2 + d1 * d2)) == 0
dd = sp.symbols("delta", positive=True)
x1eq = x1.subs({d1: dd, d2: dd})
assert sp.expand(2 * x1eq - 1 - ((1 - dd)**2 + dd**2)) == 0
edge = (1 - dd)**2 + dd**2
assert sp.solve(sp.diff(edge, dd), dd) == [sp.Rational(1, 2)] and edge.subs(dd, sp.Rational(1, 2)) == sp.Rational(1, 2)
assert sp.limit(x1eq, dd, 0) == 1 and sp.limit(x1eq, dd, 1) == 1
assert sp.diff(x1, d1) == d2 and sp.simplify(sp.diff(x1, d2) + (1 - d1)) == 0
assert sp.expand(x1 - d1**2 - (1 - d1) * (1 + d1 - d2)) == 0   # P1 prefers agreement to delay
# player 2 ahead iff d2 (1 - d1) > 1/2; boundary at d2 = 9/10 is d1 = 1 - 1/(2 d2) = 4/9
b_ = F(9, 10)
cut = 1 - 1 / (2 * b_)
assert cut == F(4, 9)
for a_ in (cut - EPS, cut, cut + EPS):
    v2 = b_ * (1 - a_)
    assert (v2 > F(1, 2)) == (a_ < cut)
assert F(9, 10) * (1 - F(1, 5)) == F(18, 25)
assert 1 - F(7, 10) * (1 - F(9, 10)) == F(93, 100)
# player 2 can never be ahead with d2 <= 1/2
assert all(F(j, 100) * (1 - F(i, 100)) <= F(1, 2) for j in range(1, 51) for i in range(1, 100))
# numeric backward induction on a grid of offers, ties accepted
for a_, b2 in [(F(9, 10), F(7, 10)), (F(1, 5), F(9, 10)), (F(3, 5), F(3, 5))]:
    g = [F(k, 1000) for k in range(1001)]
    s2 = min(x for x in g if a_ * x >= a_**2)
    s1 = max(x for x in g if 1 - x >= b2 * (1 - s2))
    assert s1 == 1 - b2 * (1 - a_)
    # proposer prefers the cheapest acceptable offer to a rejected one
    assert s1 >= a_ * s2 and b2 * (1 - s2) >= b2**2 * 0
print("Tadelis 11.5: v1 = 1 - d2(1 - d1), v2 = d2(1 - d1); equal delta edge (1-d)^2 + d^2 >= 1/2; "
      "P2 ahead iff d2(1-d1) > 1/2 (boundary 4/9 at d2 = 9/10 checked +-1/1000)")

# ============================================================ Gibbons 2.20 (Rubinstein SPE)
dl = sp.symbols("delta", positive=True)
ss = 1 / (1 + dl)
assert sp.simplify(1 - ss - dl * ss) == 0          # 1 - s* = delta s*
assert sp.simplify(1 - dl * ss - ss) == 0          # 1 - delta s* = s*
assert sp.solve(sp.Eq(sp.Symbol("s"), 1 - dl * (1 - dl * sp.Symbol("s"))), sp.Symbol("s")) == [ss]
for d in (F(1, 2), F(3, 4), F(9, 10), F(99, 100)):
    s = 1 / (1 + d)
    p2_acc = lambda x: 1 - x >= d * s               # P2 accepts (x, 1-x) iff 1 - x >= delta s*
    p1_acc = lambda x: x >= d * s                   # P1 accepts (x, 1-x) iff x >= delta s*
    assert p2_acc(s) and not p2_acc(s + EPS) and p2_acc(s - EPS)
    assert p1_acc(1 - s) and not p1_acc(1 - s - EPS)
    # P1 one-stage deviation in its offer: accepted -> x; rejected -> P2 offers 1 - s*, P1 accepts
    p1 = lambda x: x if p2_acc(x) else d * (1 - s)
    offers = sorted(set([F(k, 1000) for k in range(1001)] + [s, s - EPS, s + EPS]))
    assert max(offers, key=p1) == s and p1(s) == s and p1(s + EPS) == d * d * s < s
    # P2 one-stage deviation in its offer (P2's share y): accepted iff 1 - y >= delta s*
    p2 = lambda y: y if p1_acc(1 - y) else d * (1 - s)
    assert max(offers, key=p2) == s and p2(s + EPS) == d * d * s < s
    # responder rules equal "accept iff offer >= value of rejecting" (continuation delta s*)
    for x in offers:
        assert p2_acc(x) == (1 - x >= d * s) and p1_acc(x) == (x >= d * s)
    # NE: best agreement date for P2 against P1's strategy: odd t gives d^(t-1)(1 - s*),
    # even t gives at most d^(t-1) s*; the max d s* = 1 - s* is reached at t = 1 (and t = 2)
    vals = [d**(t - 1) * ((1 - s) if t % 2 else s) for t in range(1, 60)]
    assert max(vals) == 1 - s == vals[0] == vals[1] == d * s
    # and for P1 against P2's strategy: odd t at most d^(t-1) s*, even t gives d^(t-1)(1 - s*)
    vals1 = [d**(t - 1) * (s if t % 2 else (1 - s)) for t in range(1, 60)]
    assert max(vals1) == s == vals1[0] and vals1[1] == d * d * s
print("Gibbons 2.20: s* = 1/(1+delta), 1 - s* = delta s*; one-stage deviations by proposers and "
      "responders unprofitable for delta in {1/2, 3/4, 9/10, 99/100}; cutoffs +-1/1000 pass")

# ============================================================ Munoz-Garcia Ch. 6 Ex. 1 (k-period punishment)
R, C = ("C", "NC"), ("C", "NC")
UP = {("C", "C"): (2, 2), ("C", "NC"): (6, 0), ("NC", "C"): (0, 6), ("NC", "NC"): (3, 3)}
assert pure_ne(UP, R, C) == [("C", "C")] and strictly_dominant(UP, R, C, 0) == "C"
dl = sp.symbols("delta", positive=True)


def kpun_gap(k, d):
    """Cooperate minus deviate (present values) with a k-period reversion to (C,C):
    sum_{t=0}^{k} 3 d^t - (6 + sum_{t=1}^{k} 2 d^t) = sum_{j=1}^{k} d^j - 3."""
    return sum(3 * d**t for t in range(k + 1)) - (6 + sum(2 * d**t for t in range(1, k + 1)))


for k in (1, 2, 3, 4, 10):
    assert sp.expand(kpun_gap(k, dl) - (sum(dl**j for j in range(1, k + 1)) - 3)) == 0
# (a) k = 1: delta >= 3 impossible; (b) k = 2: delta^2 + delta - 3 >= 0, root (-1 + sqrt 13)/2 > 1
assert all(kpun_gap(1, F(j, 1000)) < 0 and kpun_gap(2, F(j, 1000)) < 0 for j in range(1, 1000))
assert sp.solve(dl**2 + dl - 3, dl) == [-sp.Rational(1, 2) + sp.sqrt(13) / 2]
assert (-sp.Rational(1, 2) + sp.sqrt(13) / 2) > 1
assert all(kpun_gap(3, F(j, 1000)) < 0 for j in range(1, 1000))   # k = 3: root exactly 1
# (c) k = 10: unique root in (0,1) of sum_{j=1}^{10} delta^j = 3
roots10 = [r for r in sp.Poly(sum(dl**j for j in range(1, 11)) - 3, dl).nroots(n=30)
           if r.is_real and 0 < r < 1]
assert len(roots10) == 1
d10 = roots10[0]
assert abs(d10 - sp.Float("0.762700984479401")) < 1e-12
lo, hi = F(762700, 10**6), F(762701, 10**6)
assert kpun_gap(10, lo) < 0 < kpun_gap(10, hi)                 # bracket of width 1e-6
assert kpun_gap(10, F(76, 100)) < 0 and kpun_gap(10, F(77, 100)) > 0   # book's "0.76" fails
assert abs(float(sum(F(76, 100)**j for j in range(1, 11))) - 2.963) < 1e-3   # the sum at 0.76
assert all((kpun_gap(10, F(j, 1000)) >= 0) == (F(j, 1000) >= F(763, 1000)) for j in range(1, 1000))
# grim (k -> infinity): delta/(1-delta) >= 3 <=> delta >= 3/4; thresholds fall with k
thr = {}
for k in (4, 5, 6, 8, 10, 20):
    r = [x for x in sp.Poly(sum(dl**j for j in range(1, k + 1)) - 3, dl).nroots() if x.is_real and 0 < x < 1]
    thr[k] = r[0]
assert all(thr[a] > thr[b] for a, b in [(4, 5), (5, 6), (6, 8), (8, 10), (10, 20)]) and thr[20] > 0.75
threshold_tests(3, 6, 2, F(3, 4))
print("Munoz-Garcia 6.1: k=1 and k=2 never work (k=3 needs delta=1); k=10: delta >= "
      f"{float(d10):.6f} (book: 0.76, which fails); grim: 3/4; k=4: {float(thr[4]):.4f}")

# ============================================================ Tadelis 10.3 (length-T punishment)
R, C = "MF", "mf"
UN = {("M", "m"): (4, 4), ("M", "f"): (-1, 5), ("F", "m"): (5, -1), ("F", "f"): (1, 1)}
assert pure_ne(UN, R, C) == [("F", "f")]


def tpun_gap(T, d):
    """Cooperate minus deviate with a length-T reversion to (F,f): 3 sum_{j=1}^T d^j - 1."""
    return sum(4 * d**t for t in range(T + 1)) - (5 + sum(1 * d**t for t in range(1, T + 1)))


for T in (1, 2, 5):
    assert sp.expand(tpun_gap(T, dl) - (3 * sum(dl**j for j in range(1, T + 1)) - 1)) == 0
# (a) T = 1: delta >= 1/3
assert tpun_gap(1, F(1, 3)) == 0 and tpun_gap(1, F(1, 3) + EPS) > 0 > tpun_gap(1, F(1, 3) - EPS)
# (b) T = 2: the book's cubic, present values over (1 - delta): 3 d^3 - 4 d + 1 = 0
cub = sp.cancel((4 / (1 - dl) - (5 + dl * (1 - dl**2) / (1 - dl) + 4 * dl**3 / (1 - dl))) * (1 - dl))
assert sp.expand(cub + (3 * dl**3 - 4 * dl + 1)) == 0
assert sp.expand((dl - 1) * (3 * dl**2 + 3 * dl - 1) - (3 * dl**3 - 4 * dl + 1)) == 0
d2s = (-3 + sp.sqrt(21)) / 6
assert sp.simplify(3 * d2s**2 + 3 * d2s - 1) == 0 and abs(float(d2s) - 0.2637626158) < 1e-9
assert sp.simplify(tpun_gap(2, d2s)) == 0
lo, hi = F(263762, 10**6), F(263763, 10**6)
assert tpun_gap(2, lo) < 0 < tpun_gap(2, hi)
assert all((tpun_gap(2, F(j, 1000)) >= 0) == (F(j, 1000) >= F(264, 1000)) for j in range(1, 1000))
# (c) ordering: delta_1 = 1/3 > delta_2 > grim 1/4
assert F(1, 3) > d2s > sp.Rational(1, 4) and grim(4, 5, 1) == F(1, 4)
# punishment phase: deviating from (F,f) loses today, future unchanged or longer punishment
assert UN[("M", "f")][0] < UN[("F", "f")][0]
print(f"Tadelis 10.3: delta_1 = 1/3; delta_2 = (sqrt(21) - 3)/6 = {float(d2s):.6f}; grim 1/4")

# ============================================================ Gibbons 2.11 (two stages, no discounting)
R, C = "TMB", "LCR"
UG = {("T", "L"): (3, 1), ("T", "C"): (0, 0), ("T", "R"): (5, 0),
      ("M", "L"): (2, 1), ("M", "C"): (1, 2), ("M", "R"): (3, 1),
      ("B", "L"): (1, 2), ("B", "C"): (0, 1), ("B", "R"): (4, 4)}
ne = pure_ne(UG, R, C)
assert ne == [("T", "L"), ("M", "C")]
assert max(R, key=lambda r: UG[(r, "R")][0]) == "T"            # BR1(R) = T (5 > 4), not B
cells = list(product(R, C))


def spe2(a, cont, d):
    """Pure SPE test for period-1 profile a and continuation map cont (pure stage NE)."""
    v = lambda x, i: UG[x][i] + d * UG[cont[x]][i]
    return (all(v(a, 0) >= v((r, a[1]), 0) for r in R) and all(v(a, 1) >= v((a[0], c), 1) for c in C))


good = [m for m in product(ne, repeat=9) if spe2(("B", "R"), dict(zip(cells, m)), 1)]
assert good and all(dict(zip(cells, m))[("B", "R")] == ("T", "L") for m in good)
assert all(dict(zip(cells, m))[("T", "R")] == ("M", "C") for m in good)   # P1's deviation punished
print(f"Gibbons 2.11: stage NE (T,L),(M,C); (B,R) first is a pure SPE: {len(good)} of 512 maps work, "
      "all with (T,L) after (B,R) and (M,C) after (T,R)")
std = {x: (("T", "L") if x == ("B", "R") else ("M", "C")) for x in cells}
assert spe2(("B", "R"), std, 1)
assert UG[("B", "R")][0] + UG[("T", "L")][0] == 7 and UG[("T", "R")][0] + UG[("M", "C")][0] == 6
assert all(spe2(("B", "R"), std, F(k, 1000)) == (F(k, 1000) >= F(1, 2)) for k in range(1, 1001))
# Munoz-Garcia's mixed punishment: after deleting B and R, MSNE p = q = 1/2, payoffs (3/2, 1)
assert all(F(2, 3) * UG[("T", c)][0] + F(1, 3) * UG[("M", c)][0] > UG[("B", c)][0] for c in C)
assert all(F(1, 2) * UG[(r, "L")][1] + F(1, 2) * UG[(r, "C")][1] > UG[(r, "R")][1] for r in "TM")
mix1 = F(1, 2) * (F(1, 2) * 3 + F(1, 2) * 0) + F(1, 2) * (F(1, 2) * 2 + F(1, 2) * 1)
mix2 = F(1, 2) * (F(1, 2) * 1 + F(1, 2) * 0) + F(1, 2) * (F(1, 2) * 1 + F(1, 2) * 2)
assert (mix1, mix2) == (F(3, 2), F(1))
assert 4 + 3 > 5 + mix1                                             # their profile also works

# ============================================================ Tadelis 10.7 (Diluted Happiness)
v, c, p, d, x = sp.symbols("v c p delta x", positive=True)
assert sp.diff(p - c * x, x) == -c and sp.diff(-c * x, x) == -c   # x = 0 strictly dominant
# (c) customer: (v - p)/(1 - delta) >= 0; bartender: (p - c)/(1 - delta) >= p  <=>  p >= c/delta
bart = sp.simplify((p - c) / (1 - d) - p)
assert sp.simplify(bart * (1 - d) - (d * p - c)) == 0
for vv, cc in ((F(3), F(1)), (F(10), F(9))):
    for dd_ in (F(1, 2), F(9, 10), cc / vv, cc / vv + EPS):
        lo_p, hi_p = cc / dd_, vv
        ok = lambda pp: (pp - cc) / (1 - dd_) >= pp and (vv - pp) / (1 - dd_) >= 0
        if lo_p <= hi_p:
            assert ok(lo_p) and ok(hi_p) and not ok(lo_p - EPS) and not ok(hi_p + EPS)
        else:
            assert not any(ok(lo_p - k * EPS) for k in range(0, 50))
    # (d) the range is non-empty iff delta >= c/v
    for k in range(1, 1000):
        dd_ = F(k, 1000)
        assert (cc / dd_ <= vv) == (dd_ >= cc / vv)
    # partial dilution x in (0,1) is a worse deviation than x = 0: p - c x < p
    assert all(F(5) - cc * F(j, 10) < F(5) for j in range(1, 11))
assert (F(1) / F(1, 2), F(3)) == (2, 3)                      # c=1, v=3, delta=1/2: p in [2, 3]
print("Tadelis 10.7: stage NE x = 0, no purchase (p > 0); SPE price range c/delta <= p <= v; "
      "non-empty iff delta >= c/v (checked at c/v and +-1/1000)")

print("all C L05 checks passed")
