"""Checks the Lecture 1 block of the solutions (sol-<slug>.tex), labelled by exercise:
Tadelis 4.5, 4.1, 4.3, 4.6, 4.7; Gibbons 1.2; Munoz-Garcia Ch. 1 Ex. 12, 13; MWG 8.B.4, 8.B.5.

Copied from Listas/lista-reais-lectures-01-04-solutions/check_A1.py, with checks added for the
numbers the deepened solutions introduce and for the four new exercises. IESDS follows the
lecture's definition (Lecture 1, slide 29): each round removes every strategy strictly dominated
by a pure strategy at once.
Run: python check_A1.py  -> prints "all A1 checks passed" or fails on the first wrong claim.
"""
import random
from fractions import Fraction as F
from itertools import product

import numpy as np
import sympy as sp


def dominated(i, si, S, u, strict=True):
    """Return the strategies of player i in S[i] that dominate si given S_{-i} (strictly or weakly)."""
    others = [S[j] for j in range(len(S)) if j != i]
    out = []
    for ti in S[i]:
        if ti == si:
            continue
        diffs = []
        for rest in product(*others):
            p, q = list(rest), list(rest)
            p.insert(i, ti)
            q.insert(i, si)
            diffs.append(u(i, tuple(p)) - u(i, tuple(q)))
        if strict and all(d > 0 for d in diffs):
            out.append(ti)
        if not strict and all(d >= 0 for d in diffs) and any(d > 0 for d in diffs):
            out.append(ti)
    return out


def iesds(S, u):
    """Run IESDS; return (list of per-round removals, surviving sets)."""
    S = [list(s) for s in S]
    rounds = []
    while True:
        rem = [[s for s in S[i] if dominated(i, s, S, u)] for i in range(len(S))]
        if not any(rem):
            return rounds, S
        rounds.append(rem)
        S = [[s for s in S[i] if s not in rem[i]] for i in range(len(S))]


def bimatrix(rows, cols, cells):
    """Two-player game from a dict {(r, c): (u1, u2)}; returns (S, u)."""
    return [rows, cols], (lambda i, p: cells[p][i])


def table(rows, cols, vals):
    return {(r, c): vals[a][b] for a, r in enumerate(rows) for b, c in enumerate(cols)}


def pure_ne(S, u):
    ne = []
    for p in product(*S):
        ok = True
        for i in range(len(S)):
            for t in S[i]:
                q = list(p)
                q[i] = t
                if u(i, tuple(q)) > u(i, p):
                    ok = False
        if ok:
            ne.append(p)
    return ne


def iesds_grid(A, B):
    """IESDS on the bimatrix (A, B) with all strictly dominated rows/columns removed each round;
    returns surviving row and column index arrays."""
    R, C = np.arange(A.shape[0]), np.arange(A.shape[1])
    while True:
        a, b = A[np.ix_(R, C)], B[np.ix_(R, C)]
        dr = np.array([(a > a[r]).all(axis=1).any() for r in range(len(R))])
        dc = np.array([(b[:, c][:, None] < b).all(axis=0).any() for c in range(len(C))])
        if not dr.any() and not dc.any():
            return R, C
        R, C = R[~dr], C[~dc]


# ---- Tadelis 4.5
cells = table("UMD", "LCR", [[(6, 8), (2, 6), (8, 2)], [(8, 2), (4, 4), (9, 5)], [(8, 10), (4, 6), (6, 7)]])
S, u = bimatrix(list("UMD"), list("LCR"), cells)
r, surv = iesds(S, u)
assert r == [[["U"], []], [[], ["C"]]] and surv == [["M", "D"], ["L", "R"]]
assert dominated(0, "U", S, u) == ["M"] and dominated(1, "C", [["M", "D"], list("LCR")], u) == ["R"]
assert dominated(0, "D", surv, u, strict=False) == ["M"]
assert pure_ne(S, u) == [("M", "R"), ("D", "L")]
assert dominated(1, "L", [["M"], ["L", "R"]], u) == ["R"]          # weak route: drop D -> (M, R)

# ---- Gibbons 1.2
cells = table("TMB", "LCR", [[(2, 0), (1, 1), (4, 2)], [(3, 4), (1, 2), (2, 3)], [(1, 3), (0, 2), (3, 0)]])
S, u = bimatrix(list("TMB"), list("LCR"), cells)
r, surv = iesds(S, u)
assert r == [[["B"], []], [[], ["C"]]] and surv == [["T", "M"], ["L", "R"]]
assert dominated(0, "B", S, u) == ["T"] and dominated(1, "C", S, u) == []
assert dominated(1, "C", [["T", "M"], list("LCR")], u) == ["R"]
assert pure_ne(S, u) == [("T", "R"), ("M", "L")]

# ---- Tadelis 4.6 and MWG 8.B.5: the quadratic-payoff lemma u(a) - u(t) = k (t - a)(t + a - 2x)
t, s, x, k = sp.symbols("t s x k", real=True)
quad = lambda z: k * z * (2 * x - z)                     # payoff with unconstrained peak at x
assert sp.expand(quad(s) - quad(t) - k * (t - s) * (t + s - 2 * x)) == 0


def rounds(m, K):
    """Intervals S^k = [L_k, U_k], k = 1..K, for best reply max(0, m - q/2) starting from [0, inf)."""
    L, U, out = F(0), m, [(F(0), m)]
    for _ in range(K - 1):
        L, U = max(F(0), m - U / 2), m - L / 2
        out.append((L, U))
    return out


# ---- Tadelis 4.6 roommates, (10 - t_j) t_i - t_i^2
ti, tj = sp.symbols("t_i t_j", real=True)
assert sp.expand((10 - tj) * ti - ti**2 - quad(ti).subs({k: 1, x: (10 - tj) / 2})) == 0
assert sp.solve(sp.diff((10 - tj) * ti - ti**2, ti), ti) == [5 - tj / 2]
r3 = rounds(F(5), 40)
assert r3[:4] == [(0, 5), (F(5, 2), 5), (F(5, 2), F(15, 4)), (F(25, 8), F(15, 4))]
assert r3[4] == (F(25, 8), F(55, 16))                              # [3.125, 3.4375]
u3 = lambda a_, b_: (10 - b_) * a_ - a_ * a_
assert u3(F(10, 3), F(10, 3)) == F(100, 9) and u3(F(5, 2), F(5, 2)) == F(25, 2)
assert sp.solve(sp.diff(2 * ((10 - t) * t - t**2), t), t) == [sp.Rational(5, 2)]  # joint optimum
for kk, (L, U) in enumerate(r3, start=1):
    assert U - L == F(5, 2**(kk - 1))                                      # width halves
    assert (L + U) / 2 - F(10, 3) == F(-1, 2)**(kk - 1) * F(-5, 6)         # midpoint closed form
g = np.arange(0, 61) / 6                                                   # grid route
U3 = np.array([[(10 - y) * z - z * z for y in g] for z in g])
R, C = iesds_grid(U3, U3.T)
assert np.allclose(g[R], [10 / 3]) and np.allclose(g[C], [10 / 3])

# ---- Tadelis 4.7 campaigning (row player's win probability; column gets 1 - pi)
pi = {("P", "P"): F(1, 2), ("P", "B"): 0, ("P", "N"): F(3, 10), ("B", "B"): F(1, 2),
      ("N", "B"): F(6, 10), ("N", "N"): F(1, 2)}
for (a, b), v in list(pi.items()):
    pi[b, a] = 1 - v
cells = {(a, b): (pi[a, b], 1 - pi[a, b]) for a in "PBN" for b in "PBN"}
assert all(cells[a, b] == tuple(reversed(cells[b, a])) for a in "PBN" for b in "PBN")  # symmetric
S, u = bimatrix(list("PBN"), list("PBN"), cells)
assert dominated(0, "P", S, u) == ["B", "N"]
r, surv = iesds(S, u)
assert r == [[["P"], ["P"]], [["B"], ["B"]]] and surv == [["N"], ["N"]]
assert [pi["B", "P"], pi["N", "P"], pi["B", "N"]] == [1, F(7, 10), F(4, 10)]

# ---- Munoz-Garcia Ch. 1 Ex. 12
cells = table("FCB", "FCB", [[(0, 5), (2, 4), (2, 3)], [(2, 3), (0, 5), (3, 2)], [(5, 0), (2, 4), (2, 3)]])
S, u = bimatrix(list("FCB"), list("FCB"), cells)
assert all(dominated(0, s, S, u) == [] for s in "FCB")
assert dominated(1, "B", S, u) == ["C"] and dominated(1, "F", S, u) == dominated(1, "C", S, u) == []
r, surv = iesds(S, u)
assert r == [[[], ["B"]], [["C"], []]] and surv == [["F", "B"], ["F", "C"]]
assert dominated(0, "F", [list("FCB"), ["F", "C"]], u, strict=False) == ["B"]
assert dominated(0, "F", S, u, strict=False) == ["B"] and dominated(0, "C", S, u) == []

# ---- MWG 8.B.5 Cournot, m = (a - c)/(2b)
A_, B_, c_, qi, qj = sp.symbols("a b c q_i q_j", positive=True)
m = (A_ - c_) / (2 * B_)
assert sp.expand((A_ - B_ * (qi + qj) - c_) * qi - quad(qi).subs({k: B_, x: m - qj / 2})) == 0
mm = F(1)
r6 = rounds(mm, 60)
assert r6[:4] == [(0, 1), (F(1, 2), 1), (F(1, 2), F(3, 4)), (F(5, 8), F(3, 4))]
assert all(U - L == F(1, 2**(kk - 1)) for kk, (L, U) in enumerate(r6, start=1))
assert abs(float(r6[-1][1]) - 2 / 3) < 1e-12
fp = sp.solve(sp.Eq(qi, m - qi / 2), qi)[0]
assert sp.simplify(fp - (A_ - c_) / (3 * B_)) == 0
# three firms: every q in [0, m] is the best reply to Q = 2(m - q) with both rivals in [0, m]
for q in [F(0), F(1, 4), F(1, 2), F(1)]:
    Q = 2 * (mm - q)
    assert 0 <= Q <= 2 * mm and max(F(0), mm - Q / 2) == q and 0 <= Q / 2 <= mm
gq = np.arange(0, 29) / 2                       # grid route: a - c = 12, b = 1 (m = 6)
surv = list(range(len(gq)))
while True:
    pairs = [gq[j] + gq[l] for j in surv for l in surv]
    pay = np.array([[(12 - (gq[i] + Q)) * gq[i] for Q in pairs] for i in surv])
    dom = [any((pay[r2] > pay[r1]).all() for r2 in range(len(surv))) for r1 in range(len(surv))]
    if not any(dom):
        break
    surv = [s_ for s_, d in zip(surv, dom) if not d]
assert np.allclose(gq[surv], np.arange(0, 13) / 2)      # all of [0, m] = [0, 6] survives
# the three-firm Cournot NE (a - c)/(4b) lies inside [0, m] (Tadelis 5.8 with n = 3)
assert sp.simplify((A_ - c_) / (4 * B_) - m / 2) == 0

# ======================================================================= added for the 01-05 list
random.seed(1)


def br2(S, u, i, other):
    """Best replies of player i (0 or 1) to the opponent's pure strategy `other` in a bimatrix."""
    prof = lambda s: (s, other) if i == 0 else (other, s)
    best = max(u(i, prof(s)) for s in S[i])
    return [s for s in S[i] if u(i, prof(s)) == best]


# ---- Tadelis 4.5: best-response marking
cells = table("UMD", "LCR", [[(6, 8), (2, 6), (8, 2)], [(8, 2), (4, 4), (9, 5)], [(8, 10), (4, 6), (6, 7)]])
S, u = bimatrix(list("UMD"), list("LCR"), cells)
assert [br2(S, u, 0, c) for c in "LCR"] == [["M", "D"], ["M", "D"], ["M"]]
assert [br2(S, u, 1, r) for r in "UMD"] == [["L"], ["R"], ["L"]]
assert dominated(0, "U", S, u) == ["M"] and dominated(0, "D", S, u) == []    # U vs D not ranked

# ---- Gibbons 1.2: best-response marking, round-1 table
cells = table("TMB", "LCR", [[(2, 0), (1, 1), (4, 2)], [(3, 4), (1, 2), (2, 3)], [(1, 3), (0, 2), (3, 0)]])
S, u = bimatrix(list("TMB"), list("LCR"), cells)
assert [br2(S, u, 0, c) for c in "LCR"] == [["M"], ["T", "M"], ["T"]]
assert [br2(S, u, 1, r) for r in "TMB"] == [["R"], ["L"], ["L"]]
assert all(dominated(1, s, S, u) == [] for s in "LCR") and dominated(0, "M", S, u) == []

# ---- Munoz-Garcia Ch. 1 Ex. 12: marking and the unique pure NE
cells = table("FCB", "FCB", [[(0, 5), (2, 4), (2, 3)], [(2, 3), (0, 5), (3, 2)], [(5, 0), (2, 4), (2, 3)]])
S, u = bimatrix(list("FCB"), list("FCB"), cells)
assert [br2(S, u, 0, c) for c in "FCB"] == [["B"], ["F", "B"], ["C"]]
assert [br2(S, u, 1, r) for r in "FCB"] == [["F"], ["C"], ["C"]]
assert pure_ne(S, u) == [("B", "C")]

# ---- Tadelis 4.7: unique pure NE
pi = {("P", "P"): F(1, 2), ("P", "B"): 0, ("P", "N"): F(3, 10), ("B", "B"): F(1, 2),
      ("N", "B"): F(6, 10), ("N", "N"): F(1, 2)}
for (a, b), v in list(pi.items()):
    pi[b, a] = 1 - v
S, u = bimatrix(list("PBN"), list("PBN"), {(a, b): (pi[a, b], 1 - pi[a, b]) for a in "PBN" for b in "PBN"})
assert pure_ne(S, u) == [("N", "N")]
assert [br2(S, u, 0, c) for c in "PBN"] == [["B"], ["N"], ["N"]]

# ---- MWG 8.B.5: round 5 of the duopoly recursion
assert r6[4] == (F(5, 8), F(11, 16))

# ---- Munoz-Garcia Ch. 1 Ex. 13 (rows U, M, D; columns L, R)
cells = table("UMD", "LR", [[(-10, 10), (0, 12)], [(-12, 0), (2, 2)], [(-9, 0), (1, 0)]])
S, u = bimatrix(list("UMD"), list("LR"), cells)
assert dominated(0, "U", S, u) == ["D"] and dominated(0, "M", S, u) == dominated(0, "D", S, u) == []
assert dominated(1, "L", S, u) == [] and dominated(1, "L", S, u, strict=False) == ["R"]
assert [br2(S, u, 0, c) for c in "LR"] == [["D"], ["M"]]          # no strictly dominant row
r, surv = iesds(S, u)
assert r == [[["U"], []]] and surv == [["M", "D"], ["L", "R"]]
assert pure_ne(S, u) == [("M", "R"), ("D", "L")]


# ---- Tadelis 4.1 and MWG 8.B.4: random finite games
def rand_game(n_pl, sizes, lo=-2, hi=2):
    S = [list(range(m)) for m in sizes]
    pay = {p: tuple(random.randint(lo, hi) for _ in range(n_pl)) for p in product(*S)}
    return S, pay


def is_dominant(i, si, S, u, strict):
    """si strictly (or weakly: >= everywhere, > somewhere) dominates every other strategy of i."""
    return all(si in dominated(i, s, S, u, strict=strict) for s in S[i] if s != si)


strict_eq_games = 0
for trial in range(3000):
    n_pl = random.choice([2, 3])
    sizes = [random.randint(2, 4) for _ in range(n_pl)]
    S, pay = rand_game(n_pl, sizes)
    if trial % 2:                                   # plant a strictly dominant strategy 0
        for p in pay:
            pay[p] = tuple(pay[p][i] + (20 if p[i] == 0 else 0) for i in range(n_pl))
    u = lambda i, p, pay=pay: pay[p][i]
    sd = [[s for s in S[i] if is_dominant(i, s, S, u, True)] for i in range(n_pl)]
    assert all(len(x) <= 1 for x in sd)            # at most one strictly dominant strategy
    if all(sd):
        strict_eq_games += 1
        sD = tuple(x[0] for x in sd)
        for p in product(*S):                      # no other profile of (weakly) dominant strategies
            if p != sD:
                assert not all(is_dominant(i, p[i], S, u, False) for i in range(n_pl))
        assert iesds(S, u)[1] == [[s] for s in sD]
assert strict_eq_games >= 1500


def dominated_set(T, u):
    """All (i, s) with s in T[i] strictly dominated in T by a pure strategy in T[i]."""
    return [(i, s) for i in range(len(T)) for s in T[i] if dominated(i, s, T, u)]


for trial in range(2000):
    n_pl = random.choice([2, 3])
    S, pay = rand_game(n_pl, [random.randint(2, 4) for _ in range(n_pl)], -1, 2)
    u = lambda i, p, pay=pay: pay[p][i]
    target = iesds(S, u)[1]
    for _ in range(20):                             # random deletion orders
        T = [list(s) for s in S]
        while True:
            D = dominated_set(T, u)
            if not D:
                break
            pick = random.sample(D, random.randint(1, len(D)))
            T = [[s for s in T[i] if (i, s) not in pick] for i in range(n_pl)]
        assert T == target and all(T)

# weak dominance: the order matters (rows T, M, B; columns L, R)
cells = table("TMB", "LR", [[(1, 1), (0, 0)], [(1, 1), (2, 1)], [(0, 0), (2, 1)]])
S, u = bimatrix(list("TMB"), list("LR"), cells)
assert dominated(0, "T", S, u, strict=False) == ["M"] and dominated(0, "B", S, u, strict=False) == ["M"]
assert iesds(S, u)[0] == []                                          # nothing strictly dominated
assert dominated(1, "L", [["M", "B"], ["L", "R"]], u, strict=False) == ["R"]   # route 1: drop T, then L
assert dominated(1, "R", [["T", "M"], ["L", "R"]], u, strict=False) == ["L"]   # route 2: drop B, then R
assert {cells["M", "R"], cells["B", "R"]} == {(2, 1)} and {cells["T", "L"], cells["M", "L"]} == {(1, 1)}

# one player, S = [0, 1], u(s) = s for s < 1, u(1) = 0 (on exact rationals)
uc = lambda s: s if s < 1 else F(0)
for s in [F(i, 50) for i in range(50)]:
    assert uc((1 + s) / 2) > uc(s)                  # every s < 1 is dominated
assert uc(F(1, 2)) > uc(F(1))                       # and so is s = 1: maximal deletion leaves nothing
assert uc(F(0)) == uc(F(1)) == 0                    # after deleting (0, 1), {0, 1} is a tie

# ---- Tadelis 4.3: discrete first-price auction, values 3 and 5, bids 0, 1, 2
val = (3, 5)


def auction(b):
    b1, b2 = b
    if b1 > b2:
        return (val[0] - b1, 0)
    if b2 > b1:
        return (0, val[1] - b2)
    return (F(val[0] - b1, 2), F(val[1] - b2, 2))


cells = {(b1, b2): auction((b1, b2)) for b1 in range(3) for b2 in range(3)}
assert [cells[b1, b2] for b1 in range(3) for b2 in range(3)] == [
    (F(3, 2), F(5, 2)), (0, 4), (0, 3), (2, 0), (1, 2), (0, 3), (1, 0), (1, 0), (F(1, 2), F(3, 2))]
S, u = bimatrix([0, 1, 2], [0, 1, 2], cells)
assert all(dominated(0, s, S, u) == [] for s in range(3))
assert dominated(0, 0, S, u, strict=False) == [1]
assert dominated(1, 0, S, u) == [2] and dominated(1, 1, S, u) == dominated(1, 2, S, u) == []
r, surv = iesds(S, u)
assert r == [[[], [0]], [[0], []], [[], [1]], [[1], []]] and surv == [[2], [2]]
assert pure_ne(S, u) == [(2, 2)] and cells[2, 2] == (F(1, 2), F(3, 2))
mix = [F(3, 4) * cells[1, c][0] + F(1, 4) * cells[2, c][0] for c in range(3)]
assert mix == [F(7, 4), 1, F(1, 8)] and all(m > cells[0, c][0] for c, m in enumerate(mix))

print("all A1 checks passed")
