"""Checks the NEW solutions of Listas/pratica-lecture-02-solutions (sol-<slug>.tex), by exercise:
Tadelis 5.5, 5.1, 5.2, 5.3, 5.12, 5.15, 6.1; Gibbons 1.3, 1.5; Munoz-Garcia Ch. 2 Ex. 7; MWG 8.C.1, 8.D.3.
The ten reused solutions (Tadelis 5.6, 5.8, 6.8; Gibbons 1.6, 1.7, 1.12; MWG 8.D.2, 8.D.6; Munoz-Garcia
Ch. 2 Ex. 2, Ch. 3 Ex. 1) are checked by ../lista-reais-lectures-01-05-solutions/check_A2.py.
Exact rational arithmetic (fractions, sympy) and brute force on grids as a second route.

Run: python check_L2.py  -> prints "all L2 checks passed" or fails on the first wrong claim.
"""
import itertools
import random
from fractions import Fraction as F

import numpy as np
import sympy as sp
from scipy.optimize import linprog

random.seed(0)


# ---------------------------------------------------------------- Tadelis 5.5, public good
def u55(contrib, i):
    """Payoff of player i when contrib is a tuple of 0/1; lamp needs >= 2 contributions."""
    lamp = sum(contrib) >= 2
    return 3 * lamp - contrib[i]


profiles = list(itertools.product((0, 1), repeat=3))
ne55 = [p for p in profiles
        if all(u55(p, i) >= u55(p[:i] + (1 - p[i],) + p[i + 1:], i) for i in range(3))]
assert sorted(ne55) == [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0)]
# best-response table by the number k of OTHER contributors
for k, (uc, un, br) in {0: (-1, 0, "N"), 1: (2, 0, "C"), 2: (2, 3, "N")}.items():
    others = tuple([1] * k + [0] * (2 - k))
    assert u55((1,) + others, 0) == uc and u55((0,) + others, 0) == un
    assert ("C" if uc > un else "N") == br
assert u55((1, 1, 1), 0) == 2 and u55((0, 1, 1), 0) == 3        # all-contribute is not NE
assert u55((1, 0, 0), 0) == -1 and u55((0, 0, 0), 0) == 0        # lone contributor is not NE

# ---------------------------------------------------------------- Gibbons 1.3, splitting a dollar
n = 20
grid = [F(i, n) for i in range(n + 1)]


def u13(s1, s2):
    return (s1, s2) if s1 + s2 <= 1 else (F(0), F(0))


ne13 = [(a, b) for a in grid for b in grid
        if u13(a, b)[0] >= max(u13(x, b)[0] for x in grid)
        and u13(a, b)[1] >= max(u13(a, y)[1] for y in grid)]
expected13 = [(a, b) for a in grid for b in grid if a + b == 1] + [(F(1), F(1))]
assert sorted(ne13) == sorted(expected13) and len(ne13) == n + 2
assert u13(F(1), F(1)) == (0, 0) and u13(F(1, 2), F(1, 2)) == (F(1, 2), F(1, 2))

# ---------------------------------------------------------------- Munoz-Garcia Ch. 2 Ex. 7, Cournot duopoly
a, b, c, qi, qj = sp.symbols("a b c q_i q_j", positive=True)
profit = (a - b * (qi + qj)) * qi - c * qi
foc = sp.diff(profit, qi)
assert sp.expand(foc - (a - 2 * b * qi - b * qj - c)) == 0
br = sp.solve(foc, qi)[0]
assert sp.simplify(br - ((a - c) / (2 * b) - qj / 2)) == 0          # the book's BR_i(q_j)
assert sp.diff(profit, qi, 2) == -2 * b                               # concave: FOC is a maximum
qstar = sp.solve(sp.Eq(qi, br.subs(qj, qi)), qi)[0]                   # symmetric crossing
assert sp.simplify(qstar - (a - c) / (3 * b)) == 0                    # the book's answer
sol = sp.solve([sp.Eq(qi, br), sp.Eq(qj, br.subs(qj, qi))], [qi, qj], dict=True)
assert len(sol) == 1 and sp.simplify(sol[0][qi] - qstar) == 0 and sp.simplify(sol[0][qj] - qstar) == 0
Q = 2 * qstar
assert sp.simplify(a - b * Q - (a + 2 * c) / 3) == 0
assert sp.simplify(profit.subs({qi: qstar, qj: qstar}) - (a - c) ** 2 / (9 * b)) == 0
assert sp.simplify(br.subs(qj, (a - c) / b)) == 0                      # BR hits zero at q_j = (a-c)/b
# numerical second route: a = 10, b = 1, c = 2 -> q* = 8/3, on a fine grid of exact rationals
A_, B_, C_ = F(10), F(1), F(2)
gq = [F(i, 60) for i in range(0, 60 * 10 + 1)]


def pf(x, y):
    return (A_ - B_ * (x + y)) * x - C_ * x


def best(y):
    return max(gq, key=lambda x: pf(x, y))


assert best(F(8, 3)) == F(8, 3)
assert pf(F(8, 3), F(8, 3)) == F(64, 9) == (A_ - C_) ** 2 / (9 * B_)
assert all(pf(F(8, 3), F(8, 3)) >= pf(x, F(8, 3)) for x in gq)
assert best(F(8)) == 0                                                   # (a - c)/b = 8: firm stays out

# ---------------------------------------------------------------- Tadelis 6.1, Battle of the Sexes
p, q = sp.symbols("p q")                                  # p = Pr(Alex: O), q = Pr(Chris: O)
vA_O, vA_F = 2 * q, 1 - q
vC_O, vC_F = p, 2 * (1 - p)
assert sp.solve(sp.Eq(vA_O, vA_F), q) == [sp.Rational(1, 3)]
assert sp.solve(sp.Eq(vC_O, vC_F), p) == [sp.Rational(2, 3)]
gp = [F(i, 60) for i in range(61)]


def bra(qq):                                              # BR of Alex as a set of p on the grid
    gain = 2 * qq - (1 - qq)
    return {F(1)} if gain > 0 else {F(0)} if gain < 0 else set(gp)


def brc(pp):
    gain = pp - 2 * (1 - pp)
    return {F(1)} if gain > 0 else {F(0)} if gain < 0 else set(gp)


mutual = [(pp, qq) for pp in gp for qq in gp if pp in bra(qq) and qq in brc(pp)]
assert mutual == [(F(0), F(0)), (F(2, 3), F(1, 3)), (F(1), F(1))]
pe, qe = F(2, 3), F(1, 3)
assert 2 * qe == F(2, 3) == pe                            # both players earn 2/3
assert pe * qe + (1 - pe) * (1 - qe) == F(4, 9)           # probability of meeting
assert pe * qe * 2 + (1 - pe) * (1 - qe) * 1 == F(2, 3)    # Alex's expected payoff, directly

# ---------------------------------------------------------------- Tadelis 5.2, weak dominance
ex52 = {("U", "L"): (1, 1), ("U", "R"): (0, 0), ("D", "L"): (0, 0), ("D", "R"): (0, 0)}
R_, C_ = ["U", "D"], ["L", "R"]
ne52 = [(r, cc) for r in R_ for cc in C_
        if all(ex52[r, cc][0] >= ex52[x, cc][0] for x in R_) and all(ex52[r, cc][1] >= ex52[r, y][1] for y in C_)]
assert ne52 == [("U", "L"), ("D", "R")]
assert all(ex52["U", cc][0] >= ex52["D", cc][0] for cc in C_)          # U weakly dominant for 1
assert all(ex52[r, "L"][1] >= ex52[r, "R"][1] for r in R_)             # L weakly dominant for 2
assert any(ex52["U", cc][0] > ex52["D", cc][0] for cc in C_)           # ... and not equivalent to D
assert ex52["D", "R"] == (0, 0) and ex52["U", "R"][0] == 0 and ex52["D", "L"][1] == 0   # D, R are ties, not strict


# ---------------------------------------------------------------- generic finite 2-player machinery
def pure_ne_matrix(U1, U2):
    n1, n2 = U1.shape
    return [(r, cc) for r in range(n1) for cc in range(n2)
            if U1[r, cc] == U1[:, cc].max() and U2[r, cc] == U2[r, :].max()]


def iesds_pure(U1, U2):
    """Survivors of iterated elimination of strictly dominated strategies (pure dominators)."""
    R, C = list(range(U1.shape[0])), list(range(U1.shape[1]))
    changed = True
    while changed:
        changed = False
        for r in R[:]:
            if any(all(U1[s, cc] > U1[r, cc] for cc in C) for s in R if s != r):
                R.remove(r)
                changed = True
        for cc in C[:]:
            if any(all(U2[r, s] > U2[r, cc] for r in R) for s in C if s != cc):
                C.remove(cc)
                changed = True
    return R, C


def mixed_dominated(U, i, rows, cols):
    """Is row i strictly dominated by a mixture of the rows in `rows`, against the columns `cols`? (LP)"""
    k = len(rows)
    cost = np.zeros(k + 1)
    cost[-1] = -1
    A = [list(-U[rows, j]) + [1] for j in cols]
    bnd = [-U[i, j] for j in cols]
    r = linprog(cost, A_ub=A, b_ub=bnd, A_eq=[[1] * k + [0]], b_eq=[1],
                bounds=[(0, 1)] * k + [(None, None)])
    return r.status == 0 and -r.fun > 1e-9


def iesds_mixed(U1, U2):
    R, C = list(range(U1.shape[0])), list(range(U1.shape[1]))
    changed = True
    while changed:
        changed = False
        dead = [r for r in R if mixed_dominated(U1, r, R, C)]
        if dead:
            R = [r for r in R if r not in dead]
            changed = True
        dead = [cc for cc in C if mixed_dominated(U2.T, cc, C, R)]
        if dead:
            C = [cc for cc in C if cc not in dead]
            changed = True
    return R, C


def never_br(U, i, rows, cols):
    """Is row i NOT a best reply (among `rows`) to any belief over `cols`?  Feasibility LP."""
    k = len(cols)
    A = [list(U[o, cols] - U[i, cols]) for o in rows if o != i]
    if not A:
        return False
    r = linprog(np.zeros(k), A_ub=A, b_ub=[0] * len(A), A_eq=[[1] * k], b_eq=[1], bounds=[(0, 1)] * k)
    return r.status != 0


def rationalizable(U1, U2):
    R, C = list(range(U1.shape[0])), list(range(U1.shape[1]))
    changed = True
    while changed:
        changed = False
        dead = [r for r in R if never_br(U1, r, R, C)]
        if dead:
            R = [r for r in R if r not in dead]
            changed = True
        dead = [cc for cc in C if never_br(U2.T, cc, C, R)]
        if dead:
            C = [cc for cc in C if cc not in dead]
            changed = True
    return R, C


# ---------------------------------------------------------------- Tadelis 5.1, Proposition 5.1 (random games)
cnt = {"dom": 0, "iesds": 0, "rat": 0}
for _ in range(1200):
    n1, n2 = random.randint(2, 4), random.randint(2, 4)
    U1 = np.array([[random.randint(0, 5) for _ in range(n2)] for _ in range(n1)])
    U2 = np.array([[random.randint(0, 5) for _ in range(n2)] for _ in range(n1)])
    ne = pure_ne_matrix(U1, U2)
    # (1) strict dominant strategy equilibrium
    d1 = [r for r in range(n1) if all(U1[r, cc] > U1[s, cc] for s in range(n1) if s != r for cc in range(n2))]
    d2 = [cc for cc in range(n2) if all(U2[r, cc] > U2[r, s] for s in range(n2) if s != cc for r in range(n1))]
    if d1 and d2:
        cnt["dom"] += 1
        assert ne == [(d1[0], d2[0])]
    # (2) unique survivor of IESDS (pure dominators)
    R, C = iesds_pure(U1, U2)
    if len(R) == 1 and len(C) == 1:
        cnt["iesds"] += 1
        assert ne == [(R[0], C[0])]
    # (3) unique rationalizable profile (beliefs = mixed strategies of the opponent)
    R, C = rationalizable(U1, U2)
    if len(R) == 1 and len(C) == 1:
        cnt["rat"] += 1
        assert ne == [(R[0], C[0])]
assert min(cnt.values()) > 30, cnt
# the proof's lemma: every pure NE is rationalizable
for _ in range(150):
    U1 = np.array([[random.randint(0, 5) for _ in range(3)] for _ in range(3)])
    U2 = np.array([[random.randint(0, 5) for _ in range(3)] for _ in range(3)])
    R, C = rationalizable(U1, U2)
    assert all(r in R and cc in C for r, cc in pure_ne_matrix(U1, U2))

# ---------------------------------------------------------------- Tadelis 5.3, Nash and IESDS
# (a) 2x2, payoffs in {0,1,2,3}: unique pure NE and no ties in the BR comparisons => unique IESDS survivor.
generic_cases = 0
bad_generic = []
bad_ties = 0
for v in itertools.product(range(4), repeat=8):
    U1 = np.array([[v[0], v[1]], [v[2], v[3]]])
    U2 = np.array([[v[4], v[5]], [v[6], v[7]]])
    nogap = (U1[0, 0] != U1[1, 0] and U1[0, 1] != U1[1, 1]
             and U2[0, 0] != U2[0, 1] and U2[1, 0] != U2[1, 1])
    ne = pure_ne_matrix(U1, U2)
    R, C = iesds_pure(U1, U2)
    # always: every pure NE survives (Prop. 1) ...
    assert all(r in R and cc in C for r, cc in ne)
    if nogap:
        generic_cases += 1
        # no ties: #pure NE is 0, 1 or 2; 1 NE => unique survivor; case analysis of the proof
        if len(ne) == 1:
            if (len(R), len(C)) != (1, 1):
                bad_generic.append(v)
        b1 = [int(np.argmax(U1[:, cc])) for cc in range(2)]       # BR of player 1 to each column
        b2 = [int(np.argmax(U2[r, :])) for r in range(2)]
        if b1[0] != b1[1] and b2[0] != b2[1]:                      # case 3 of the proof: BR bijections
            assert len(ne) in (0, 2)
        else:
            assert (len(R), len(C)) == (1, 1)                      # cases 1-2: dominance solvable
    elif len(ne) == 1 and (len(R), len(C)) != (1, 1):
        bad_ties += 1
assert generic_cases > 0 and bad_generic == [] and bad_ties > 0
# the explicit counterexample with ties
U1 = np.array([[1, 1], [1, 0]])
U2 = np.array([[1, 0], [0, 1]])
assert pure_ne_matrix(U1, U2) == [(0, 0)] and iesds_pure(U1, U2) == ([0, 1], [0, 1])
assert iesds_mixed(U1, U2) == ([0, 1], [0, 1])
# (b) 3x3 with a unique pure NE where nothing is strictly dominated (even by mixtures)
M1 = np.array([[2, 0, 0], [0, 2, 0], [0, 0, 2]])
M2 = np.array([[2, 0, 0], [0, 0, 2], [0, 2, 0]])
assert pure_ne_matrix(M1, M2) == [(0, 0)]
assert iesds_pure(M1, M2) == ([0, 1, 2], [0, 1, 2]) and iesds_mixed(M1, M2) == ([0, 1, 2], [0, 1, 2])
brs1 = [int(np.argmax(M1[:, cc])) for cc in range(3)]
brs2 = [int(np.argmax(M2[r, :])) for r in range(3)]
assert sorted(brs1) == [0, 1, 2] and sorted(brs2) == [0, 1, 2]       # every strategy is a strict BR to something
assert [(M1[r, cc], M2[r, cc]) for r in range(3) for cc in range(3)] == [
    (2, 2), (0, 0), (0, 0), (0, 0), (2, 0), (0, 2), (0, 0), (0, 2), (2, 0)]

# ---------------------------------------------------------------- Gibbons 1.5, finite Cournot
x = sp.symbols("x")                                        # x = q'/(a-c); units a - c = 1


def pay(qa, qb):
    return qa * (1 - qa - qb)


qm2, qc = sp.Rational(1, 4), sp.Rational(1, 3)
assert pay(qm2, qm2) == sp.Rational(1, 8) and pay(qc, qc) == sp.Rational(1, 9)
assert pay(qm2, qc) == sp.Rational(5, 48) and pay(qc, qm2) == sp.Rational(5, 36)
assert pay(qc, qm2) > pay(qm2, qm2) and pay(qc, qc) > pay(qm2, qc)         # q_c strictly dominant
assert pay(qm2, qm2) > pay(qc, qc)                                           # both better off cooperating
# profit depends on the rival only through its quantity: f(q, y) = q (1 - q - y)
d = sp.symbols("y")
assert sp.solve(sp.Eq(pay(qm2, d), pay(qc, d)), d) == [sp.Rational(5, 12)]  # q_m/2 beats q_c iff y >= 5/12
g = sp.expand(pay(x, d) - pay(qc, d))
assert sp.simplify(g.subs({x: sp.Rational(5, 12), d: sp.Rational(1, 4)})) == 0   # q' = 5/12 ties q_c at y = 1/4
for qp in [F(k, 240) for k in range(1, 240) if F(k, 240) not in (F(1, 4), F(1, 3), F(5, 12))]:
    Qs = [F(1, 4), F(1, 3), qp]
    U = [[a_ * (1 - a_ - b_) for b_ in Qs] for a_ in Qs]
    if qp > F(5, 12):                        # q' strictly dominated by q_c (pure)
        assert all(U[1][j] > U[2][j] for j in range(3))
    else:                                    # q_m/2 strictly dominated by q_c (pure)
        assert all(U[1][j] > U[0][j] for j in range(3))
Qs = [F(1, 4), F(1, 3), F(5, 12)]
U = [[a_ * (1 - a_ - b_) for b_ in Qs] for a_ in Qs]
U_np = np.array([[float(v) for v in row] for row in U])
assert not any(mixed_dominated(U_np, i, [0, 1, 2], [0, 1, 2]) for i in range(3))   # nothing strictly dominated
ne15 = [(i, j) for i in range(3) for j in range(3)
        if U[i][j] >= max(U[k][j] for k in range(3)) and U[j][i] >= max(U[k][i] for k in range(3))]
assert [[int(v * 144) for v in row] for row in U] == [[18, 15, 12], [20, 16, 12], [20, 15, 10]]
assert ne15 == [(0, 2), (1, 1), (2, 0)]                      # (q_c, q_c) plus two weak equilibria (ties)
assert U[0][2] == U[1][2] == F(1, 12) and U[2][0] == U[1][0] == F(5, 36)
assert pay(F(5, 12), F(1, 4)) == F(5, 36) and pay(F(1, 4), F(5, 12)) == F(1, 12)

# ---------------------------------------------------------------- MWG 8.C.1, IESDS vs never-best-response
n_unique = 0
for _ in range(500):
    n1, n2 = random.randint(2, 4), random.randint(2, 4)
    U1 = np.array([[random.randint(0, 6) for _ in range(n2)] for _ in range(n1)])
    U2 = np.array([[random.randint(0, 6) for _ in range(n2)] for _ in range(n1)])
    Rr, Cr = rationalizable(U1, U2)
    Rd, Cd = iesds_mixed(U1, U2)
    assert set(Rr) <= set(Rd) and set(Cr) <= set(Cd) and Rr and Cr          # R^inf inside D^inf, non-empty
    if len(Rd) == 1 and len(Cd) == 1:
        n_unique += 1
        assert (Rr, Cr) == (Rd, Cd)
assert n_unique > 30, n_unique

# ---------------------------------------------------------------- MWG 8.D.3, first-price auction
def ua(v, bid, other):
    return F(v - bid) if bid > other else (F(v - bid, 2) if bid == other else F(0))


def auction_ne(v1, v2, top):
    bids = range(top + 1)
    return [(b1, b2) for b1 in bids for b2 in bids
            if ua(v1, b1, b2) >= max(ua(v1, x_, b2) for x_ in bids)
            and ua(v2, b2, b1) >= max(ua(v2, x_, b1) for x_ in bids)]


def predicted(v1, v2):
    out = {(b, b) for b in range(max(max(v1, v2) - 2, 0), min(v1, v2) + 1)}
    out |= {(b1, b1 - 1) for b1 in range(max(v2, 1), v1)}           # player 1 wins at b1 = b2 + 1
    out |= {(b2 - 1, b2) for b2 in range(max(v1, 1), v2)}           # player 2 wins at b2 = b1 + 1
    return sorted(out)


for v1 in range(1, 11):
    for v2 in range(1, 11):
        top = max(v1, v2) + 4                  # bids above the valuations are never part of a NE
        ne = auction_ne(v1, v2, top)
        assert ne == predicted(v1, v2), (v1, v2, ne)
        assert len(ne) >= 2                    # never unique
        dd = abs(v1 - v2)
        assert len(ne) == (2 if v1 == v2 == 1 else 3 if dd <= 2 else dd)   # counting rule of the solution
        assert all(max(pair) <= max(v1, v2) for pair in ne)
assert auction_ne(5, 5, 9) == [(3, 3), (4, 4), (5, 5)]
assert auction_ne(7, 5, 11) == [(5, 4), (5, 5), (6, 5)]
assert auction_ne(8, 5, 12) == [(5, 4), (6, 5), (7, 6)]
# (a) no strictly dominated strategy: against a bid above every bid in play, all bids lose and earn 0
for v in range(1, 9):
    top = v + 4
    U = np.array([[float(ua(v, bb, o)) for o in range(top + 2)] for bb in range(top + 1)])   # rival may bid top+1
    assert all(U[bb, top + 1] == 0 for bb in range(top + 1))
    assert not any(mixed_dominated(U, bb, list(range(top + 1)), list(range(top + 2))) for bb in range(top + 1))
# (b) weakly dominated: every bid >= v (v >= 1); bid 0 as well when v >= 2; the undominated bids are 1..v-1
for v in range(1, 9):
    top = v + 4
    cols = range(top + 1)

    def weakly_dominated(bb):
        return any(all(ua(v, s, o) >= ua(v, bb, o) for o in cols) and any(ua(v, s, o) > ua(v, bb, o) for o in cols)
                   for s in range(top + 1) if s != bb)

    undominated = [bb for bb in range(top + 1) if not weakly_dominated(bb)]
    assert undominated == (list(range(1, v)) if v >= 2 else [0]), (v, undominated)
    assert all(weakly_dominated(bb) for bb in range(v, top + 1))
    assert weakly_dominated(v) and all(ua(v, v - 1, o) >= ua(v, v, o) for o in cols)   # v-1 weakly beats v

# ---------------------------------------------------------------- Tadelis 5.12, asymmetric Bertrand on a cent grid
N = 10001                                            # prices 0.00 ... 100.00 in cents (prices >= 100 sell nothing)
cents = np.arange(N, dtype=np.int64)


def prof(cost_cents, own, other):
    """2 * profit in units of 1e-4 dollars (the tie payoff is halved, hence the factor 2)."""
    margin = own - cost_cents
    qty = np.maximum(10000 - own, 0)
    return np.where(own < other, 2 * margin * qty, np.where(own == other, margin * qty, 0))


br1, br2 = [], []
for pj in range(N):
    pr = prof(100, cents, pj)
    br1.append(set(np.flatnonzero(pr == pr.max()).tolist()))
    pr = prof(200, cents, pj)
    br2.append(set(np.flatnonzero(pr == pr.max()).tolist()))
ne512 = [(p1, p2) for p2 in range(N) for p1 in br1[p2] if p2 in br2[p1]]
assert sorted(ne512) == [(k, k + 1) for k in range(101, 201)]     # p2 = p1 + 0.01, p1 = 1.01 ... 2.00
assert len(ne512) == 100 and (199, 200) in ne512 and (200, 201) in ne512
assert (100, 101) not in ne512 and (201, 202) not in ne512
assert prof(100, np.array([199]), 200)[0] == 2 * 99 * 9801 and prof(100, np.array([200]), 200)[0] == 100 * 9800
assert prof(100, np.array([200]), 201)[0] == 2 * 100 * 9800 and prof(200, np.array([201]), 200)[0] == 0
# case split of the proof: at p1 = p2 = p >= 2 undercutting by one cent beats half the market
for pp in range(200, 10000):
    m, dd = pp - 100, 10000 - pp
    assert 2 * (m - 1) * (dd + 1) > m * dd, pp
assert sorted(br1[102]) == [101] and sorted(br1[101]) == [101] and sorted(br1[5200]) == [5050]   # BR_1 cases

# ---------------------------------------------------------------- Tadelis 5.15, Hotelling with a continuum of voters
def shares(x1, x2, cdf):
    """Vote share of candidate 1 when platforms are x1, x2 (indifferent voters split evenly)."""
    if x1 == x2:
        return F(1, 2)
    lo, hi = (x1, x2) if x1 < x2 else (x2, x1)
    low_share = cdf((lo + hi) / 2)
    return low_share if x1 < x2 else 1 - low_share


def win(sh):
    return F(1) if sh > F(1, 2) else F(1, 2) if sh == F(1, 2) else F(0)


def hotelling(points, cdf):
    u = lambda x_i, x_j: win(shares(x_i, x_j, cdf))
    ne = [(x1, x2) for x1 in points for x2 in points
          if u(x1, x2) >= max(u(z, x2) for z in points) and u(x2, x1) >= max(u(z, x1) for z in points)]
    return ne, u


pts = [F(i, 10) for i in range(-10, 11)]                    # uniform on [-1, 1]
ne_u, u_u = hotelling(pts, lambda t: (t + 1) / 2)
assert ne_u == [(F(0), F(0))]
for aj in pts:                                              # best-response correspondence (part a)
    best_i = [z for z in pts if u_u(z, aj) == max(u_u(w_, aj) for w_ in pts)]
    if aj > 0:
        assert best_i == [z for z in pts if -aj < z < aj]
    elif aj < 0:
        assert best_i == [z for z in pts if aj < z < -aj]
    else:
        assert best_i == [F(0)]
assert u_u(F(3, 10), F(3, 10)) == F(1, 2) and u_u(F(-3, 10), F(3, 10)) == F(1, 2)    # ties at +-a_j
assert u_u(F(4, 10), F(3, 10)) == 0 and u_u(F(2, 10), F(3, 10)) == 1


def cdf_gen(t):                                             # continuous, strictly increasing on [0,1], median 1/2
    return 2 * t * t if t <= F(1, 2) else 1 - 2 * (1 - t) ** 2


assert cdf_gen(F(1, 2)) == F(1, 2) and cdf_gen(F(0)) == 0 and cdf_gen(F(1)) == 1
pts2 = [F(i, 20) for i in range(21)]
ne_g, _ = hotelling(pts2, cdf_gen)
assert ne_g == [(F(1, 2), F(1, 2))]                          # both choose the median voter

print("all L2 checks passed")
