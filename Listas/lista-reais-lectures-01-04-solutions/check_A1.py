"""Checks items 1-6 (Lecture 1 block): Tadelis 4.5, Gibbons 1.2, Tadelis 4.6, Tadelis 4.7,
Munoz-Garcia Ch. 1 Ex. 12, MWG 8.B.5.

Copied from Listas/pratica-lecture-01-solutions/check_A.py (old items 6, 7, 14, 16) and check_B.py
(old items 15, 21), renumbered to this list. IESDS follows the lecture's definition (Lecture 1,
slide 29): each round removes every strategy strictly dominated by a pure strategy at once.
Run: python check_A1.py  -> prints "all A1 checks passed" or fails on the first wrong claim.
"""
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


# ---- item 1: Tadelis 4.5
cells = table("UMD", "LCR", [[(6, 8), (2, 6), (8, 2)], [(8, 2), (4, 4), (9, 5)], [(8, 10), (4, 6), (6, 7)]])
S, u = bimatrix(list("UMD"), list("LCR"), cells)
r, surv = iesds(S, u)
assert r == [[["U"], []], [[], ["C"]]] and surv == [["M", "D"], ["L", "R"]]
assert dominated(0, "U", S, u) == ["M"] and dominated(1, "C", [["M", "D"], list("LCR")], u) == ["R"]
assert dominated(0, "D", surv, u, strict=False) == ["M"]
assert pure_ne(S, u) == [("M", "R"), ("D", "L")]
assert dominated(1, "L", [["M"], ["L", "R"]], u) == ["R"]          # weak route: drop D -> (M, R)

# ---- item 2: Gibbons 1.2
cells = table("TMB", "LCR", [[(2, 0), (1, 1), (4, 2)], [(3, 4), (1, 2), (2, 3)], [(1, 3), (0, 2), (3, 0)]])
S, u = bimatrix(list("TMB"), list("LCR"), cells)
r, surv = iesds(S, u)
assert r == [[["B"], []], [[], ["C"]]] and surv == [["T", "M"], ["L", "R"]]
assert dominated(0, "B", S, u) == ["T"] and dominated(1, "C", S, u) == []
assert dominated(1, "C", [["T", "M"], list("LCR")], u) == ["R"]
assert pure_ne(S, u) == [("T", "R"), ("M", "L")]

# ---- items 3 and 6: the quadratic-payoff lemma u(a) - u(t) = k (t - a)(t + a - 2x)
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


# ---- item 3: Tadelis 4.6 roommates, (10 - t_j) t_i - t_i^2
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

# ---- item 4: Tadelis 4.7 campaigning (row player's win probability; column gets 1 - pi)
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

# ---- item 5: Munoz-Garcia Ch. 1 Ex. 12
cells = table("FCB", "FCB", [[(0, 5), (2, 4), (2, 3)], [(2, 3), (0, 5), (3, 2)], [(5, 0), (2, 4), (2, 3)]])
S, u = bimatrix(list("FCB"), list("FCB"), cells)
assert all(dominated(0, s, S, u) == [] for s in "FCB")
assert dominated(1, "B", S, u) == ["C"] and dominated(1, "F", S, u) == dominated(1, "C", S, u) == []
r, surv = iesds(S, u)
assert r == [[[], ["B"]], [["C"], []]] and surv == [["F", "B"], ["F", "C"]]
assert dominated(0, "F", [list("FCB"), ["F", "C"]], u, strict=False) == ["B"]
assert dominated(0, "F", S, u, strict=False) == ["B"] and dominated(0, "C", S, u) == []

# ---- item 6: MWG 8.B.5 Cournot, m = (a - c)/(2b)
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
# the three-firm Cournot NE (a - c)/(4b) lies inside [0, m] (item 9 with n = 3)
assert sp.simplify((A_ - c_) / (4 * B_) - m / 2) == 0

print("all A1 checks passed")
