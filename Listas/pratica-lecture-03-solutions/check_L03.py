"""Checks every number and equilibrium claim in the five new Lecture 3 solutions:
sol-tadelis-6-5, sol-gibbons-1-14, sol-tadelis-6-3, sol-munoz-garcia-4-4, sol-munoz-garcia-4-9.
(The other 13 items are reused from ../lista-reais-lectures-01-05-solutions/, checked by
check_B_L03.py and others there.) Exact arithmetic (fractions); the only floating-point step
is the linear program that tests strict dominance by a mixed strategy in gibbons-1-14 and
tadelis-6-3, with a 1e-9 tolerance on integer payoffs.

Run: python check_L03.py  -> one line per item and "all L03 checks passed", or an
AssertionError on the first wrong claim.
"""
import random
from fractions import Fraction as F
from itertools import combinations, product

import numpy as np
from scipy.optimize import linprog


# ----------------------------------------------------------------------------- helpers
def pure_ne(A, B):
    """Pure Nash equilibria (row, col) of the bimatrix (A, B)."""
    R, C = len(A), len(A[0])
    return {(r, c) for r in range(R) for c in range(C)
            if A[r][c] == max(A[k][c] for k in range(R))
            and B[r][c] == max(B[r][k] for k in range(C))}


def is_ne(A, B, x, y):
    """Exact test that the mixed profile (x, y) is a Nash equilibrium of (A, B)."""
    R, C = len(A), len(A[0])
    u1 = [sum(A[r][c] * y[c] for c in range(C)) for r in range(R)]
    u2 = [sum(B[r][c] * x[r] for r in range(R)) for c in range(C)]
    return (all(u1[r] == max(u1) for r in range(R) if x[r] > 0)
            and all(u2[c] == max(u2) for c in range(C) if y[c] > 0))


def solve_exact(M, b):
    """Solve M z = b with Fractions by Gauss-Jordan; None if singular."""
    n = len(M)
    a = [[F(v) for v in row] + [F(bi)] for row, bi in zip(M, b)]
    for col in range(n):
        piv = next((r for r in range(col, n) if a[r][col] != 0), None)
        if piv is None:
            return None
        a[col], a[piv] = a[piv], a[col]
        pv = a[col][col]
        a[col] = [v / pv for v in a[col]]
        for r in range(n):
            if r != col and a[r][col] != 0:
                f = a[r][col]
                a[r] = [v - f * w for v, w in zip(a[r], a[col])]
    return [a[r][n] for r in range(n)]


def all_ne(A, B):
    """Every Nash equilibrium of a bimatrix game with isolated equilibria, by support
    enumeration over equal-size supports (exact). Games with a continuum of equilibria are
    not produced by the random draws below with probability that matters; singular systems are
    skipped, and pure equilibria are added separately."""
    R, C = len(A), len(A[0])
    found = [(tuple(F(int(r == i)) for r in range(R)), tuple(F(int(c == j)) for c in range(C)))
             for (i, j) in pure_ne(A, B)]
    for k in range(2, min(R, C) + 1):
        for S1 in combinations(range(R), k):
            for S2 in combinations(range(C), k):
                # y on S2 makes the row player indifferent over S1; x on S1 makes the column
                # player indifferent over S2. Unknowns: k probabilities and the value.
                M = [[A[r][c] for c in S2] + [-1] for r in S1] + [[1] * k + [0]]
                y = solve_exact(M, [0] * k + [1])
                M = [[B[r][c] for r in S1] + [-1] for c in S2] + [[1] * k + [0]]
                x = solve_exact(M, [0] * k + [1])
                if y is None or x is None or min(y[:k]) <= 0 or min(x[:k]) <= 0:
                    continue
                xf = tuple(x[S1.index(r)] if r in S1 else F(0) for r in range(R))
                yf = tuple(y[S2.index(c)] if c in S2 else F(0) for c in range(C))
                if is_ne(A, B, xf, yf):
                    found.append((xf, yf))
    return found


def dominated(U, i, rows):
    """Is row i of the payoff matrix U (restricted to the strategy list `rows`, columns all
    given) strictly dominated by a mixed strategy over `rows`? U is a list of lists."""
    ncol = len(U[0])
    n = len(rows)
    # maximise t s.t. sum_k s_k U[rows[k]][c] - U[i][c] >= t for all c, sum s = 1, s >= 0
    c_obj = [0] * n + [-1]
    A_ub = [[-U[rows[k]][c] for k in range(n)] + [1] for c in range(ncol)]
    b_ub = [-U[i][c] for c in range(ncol)]
    res = linprog(c_obj, A_ub=A_ub, b_ub=b_ub, A_eq=[[1] * n + [0]], b_eq=[1],
                  bounds=[(0, None)] * n + [(None, None)], method="highs")
    return res.status == 0 and -res.fun > 1e-9


def iesds(A, B):
    """Survivors (row set, column set) of iterated elimination of strictly dominated strategies,
    dominance by mixed strategies, one simultaneous round at a time."""
    rows, cols = list(range(len(A))), list(range(len(A[0])))
    while True:
        Ar = [[A[r][c] for c in cols] for r in rows]
        Bt = [[B[r][c] for r in rows] for c in cols]
        dr = [rows[i] for i in range(len(rows)) if len(rows) > 1 and dominated(Ar, i, list(range(len(rows))))]
        dc = [cols[j] for j in range(len(cols)) if len(cols) > 1 and dominated(Bt, j, list(range(len(cols))))]
        if not dr and not dc:
            return set(rows), set(cols)
        rows = [r for r in rows if r not in dr]
        cols = [c for c in cols if c not in dc]


def backward_induction(node):
    """Pure backward-induction solutions of a finite perfect-information tree.
    node = ('T', payoffs) or ('D', player, {action: child}). Returns [(payoffs, path)]."""
    if node[0] == 'T':
        return [(node[1], ())]
    _, i, kids = node
    sols = [(v, (a,) + p) for a, ch in kids.items() for v, p in backward_induction(ch)]
    best = max(v[i] for v, _ in sols)
    return [(v, p) for v, p in sols if v[i] == best]


# ----------------------------------------------------------------------------- tadelis-6-5
# rows P (patrol), C (coffee); columns H (hidden), S (prowl)
A65 = [[0, 20], [10, 10]]
B65 = [[0, -10], [0, 10]]
assert pure_ne(A65, B65) == set()
p = F(1, 2)   # robber indifferent: 0 = -10p + 10(1-p)
q = F(1, 2)   # officer indifferent: 20q = 10
assert -10 * p + 10 * (1 - p) == 0 and 20 * q == 10
assert is_ne(A65, B65, (p, 1 - p), (1 - q, q))
ne = all_ne(A65, B65)
assert ne == [((p, 1 - p), (1 - q, q))], ne
u1 = 20 * q * p + 10 * (1 - p)           # officer's equilibrium payoff
assert u1 == 10 and 0 * (1 - q) + (-10 * p + 10 * (1 - p)) * q == 0
# best-response switching points
assert (20 * F(1, 2) == 10) and (-10 * F(1, 2) + 10 * F(1, 2) == 0)
# variant: fine -20 instead of -10 => patrol probability 1/3, officer still gets 10
B65b = [[0, -20], [0, 10]]
assert pure_ne(A65, B65b) == set()
assert -20 * F(1, 3) + 10 * (1 - F(1, 3)) == 0 and all_ne(A65, B65b)[0][0][0] == F(1, 3)
print("tadelis-6-5: no pure NE; mixed NE (1/2,1/2), payoffs (10, 0)")

# ----------------------------------------------------------------------------- gibbons-1-14
# example in the text: row c is dominated by the mix (a + b)/2
Ex = [[3, 0], [0, 3], [1, 1]]
assert not any(Ex[k][0] > Ex[2][0] and Ex[k][1] > Ex[2][1] for k in (0, 1))
assert dominated(Ex, 2, [0, 1, 2]) and all(F(1, 2) * Ex[0][c] + F(1, 2) * Ex[1][c] > Ex[2][c] for c in (0, 1))
rng = random.Random(14)
n_ne = n_mixed = 0
for _ in range(300):
    A = [[rng.randint(0, 9) for _ in range(3)] for _ in range(3)]
    B = [[rng.randint(0, 9) for _ in range(3)] for _ in range(3)]
    surv_r, surv_c = iesds(A, B)
    for x, y in all_ne(A, B):
        n_ne += 1
        n_mixed += sum(v > 0 for v in x) > 1 or sum(v > 0 for v in y) > 1
        assert all(x[r] == 0 or r in surv_r for r in range(3)), (A, B, x)
        assert all(y[c] == 0 or c in surv_c for c in range(3)), (A, B, y)
assert n_ne > 300 and n_mixed > 50
print(f"gibbons-1-14: {n_ne} NE ({n_mixed} with a mixed player) in 300 random games, "
      "every support inside the IESDS survivors")

# ----------------------------------------------------------------------------- tadelis-6-3
# rows U, M, D; columns L, C, R
A63 = [[5, 1, 1], [3, 0, 3], [4, 4, 0]]
B63 = [[1, 4, 0], [2, 0, 5], [3, 4, 3]]
Bt = [[B63[r][c] for r in range(3)] for c in range(3)]      # player 2's payoffs by column strategy
assert not any(all(Bt[k][r] > Bt[0][r] for r in range(3)) for k in (1, 2))   # no pure dominates L
assert not any(all(A63[k][c] > A63[0][c] for c in range(3)) for k in (1, 2))  # none dominates U
assert dominated(Bt, 0, [0, 1, 2])                           # L dominated by a mix (full game)
assert not dominated(A63, 0, [0, 1, 2])                      # U not dominated in the full game
assert [dominated(A63, i, [0, 1, 2]) for i in range(3)] == [False] * 3   # no row dominated in round 1
assert [dominated(Bt, j, [0, 1, 2]) for j in range(3)] == [True, False, False]   # only L


def beats_L(a):
    mix = lambda r: a * B63[r][1] + (1 - a) * B63[r][2]
    return all(mix(r) > B63[r][0] for r in range(3))


def beats_U(b):
    mix = lambda c: b * A63[1][c] + (1 - b) * A63[2][c]
    return all(mix(c) > A63[0][c] for c in (1, 2))


grid = [F(i, 400) for i in range(401)]
assert [a for a in grid if beats_L(a)] == [a for a in grid if F(1, 4) < a < F(3, 5)]
assert [b for b in grid if beats_U(b)] == [b for b in grid if F(1, 3) < b < F(3, 4)]
assert beats_L(F(1, 2)) and beats_L(F(1, 3)) and beats_U(F(1, 2)) and beats_U(F(2, 5))
assert not beats_L(F(1, 4)) and not beats_L(F(3, 5)) and not beats_U(F(1, 3)) and not beats_U(F(3, 4))
# after removing L, U is dominated by a mix of M and D
A63r = [[A63[r][c] for c in (1, 2)] for r in range(3)]
assert dominated(A63r, 0, [0, 1, 2])
print("tadelis-6-3: L dominated for a in (1/4,3/5); U dominated for b in (1/3,3/4)")

# ----------------------------------------------------------------------------- munoz-garcia-4-4
# wife (player 0) moves first: F or O; husband (player 1) replies. Payoffs (wife, husband).
bos = {("F", "F"): (1, 3), ("F", "O"): (0, 0), ("O", "F"): (0, 0), ("O", "O"): (3, 1)}
tree = ('D', 0, {w: ('D', 1, {h: ('T', bos[(w, h)]) for h in "FO"}) for w in "FO"})
sol = backward_induction(tree)
assert sol == [((3, 1), ("O", "O"))], sol
# normal form: husband strategy = (reply after F, reply after O)
HS = [("F", "F"), ("F", "O"), ("O", "F"), ("O", "O")]
Aw = [[bos[(w, hs[0 if w == "F" else 1])][0] for hs in HS] for w in "FO"]
Bh = [[bos[(w, hs[0 if w == "F" else 1])][1] for hs in HS] for w in "FO"]
assert Aw == [[1, 1, 0, 0], [0, 3, 0, 3]] and Bh == [[3, 3, 0, 0], [0, 1, 0, 1]]
ne_pure = {("FO"[r], "".join(HS[c])) for r, c in pure_ne(Aw, Bh)}
assert ne_pure == {("F", "FF"), ("O", "FO"), ("O", "OO")}, ne_pure
# only (O, FO) is subgame perfect: the husband's reply must be optimal at both nodes
spe = {(w, "".join(hs)) for w in "FO" for hs in HS
       if all(bos[(wf, hs[0 if wf == "F" else 1])][1] == max(bos[(wf, h)][1] for h in "FO") for wf in "FO")
       and bos[(w, hs[0 if w == "F" else 1])][0] == max(bos[(wf, hs[0 if wf == "F" else 1])][0] for wf in "FO")}
assert spe == {("O", "FO")}, spe
# simultaneous version: two pure NE (F,F) and (O,O) and a mixed one
As = [[bos[(w, h)][0] for h in "FO"] for w in "FO"]
Bs = [[bos[(w, h)][1] for h in "FO"] for w in "FO"]
assert pure_ne(As, Bs) == {(0, 0), (1, 1)} and len(all_ne(As, Bs)) == 3
print("munoz-garcia-4-4: SPE (O, FO); pure NE (F,FF), (O,FO), (O,OO)")

# ----------------------------------------------------------------------------- munoz-garcia-4-9
def centipede(T):
    """T-stage centipede: odd stages depositor 0 (stop pays (2k,2k-2) at t=2k-1), even stages
    depositor 1 (stop pays (2k-1,2k+1) at t=2k); continuing after the last stage pays (T,T) for T even."""
    def stop(t):
        k = (t + 1) // 2
        return (2 * k, 2 * k - 2) if t % 2 else (2 * k - 1, 2 * k + 1)

    def node(t):
        if t > T:
            return ('T', (T, T))
        return ('D', 0 if t % 2 else 1, {"S": ('T', stop(t)), "C": node(t + 1)})
    return node(1), stop


tree100, stop100 = centipede(100)
assert [stop100(t) for t in (1, 2, 3, 98, 99, 100)] == [(2, 0), (1, 3), (4, 2), (97, 99), (100, 98), (99, 101)]
for T in list(range(2, 21, 2)) + [100]:
    tree, stop = centipede(T)
    sol = backward_induction(tree)
    assert sol == [((2, 0), ("S",))], (T, sol)
    # every mover stops at every node and stopping beats continuing by exactly one dollar
    def walk(node, t):
        if node[0] == 'T':
            return
        _, i, kids = node
        cont = backward_induction(kids["C"])[0][0][i]
        assert stop(t)[i] - cont == 1, (T, t)
        walk(kids["C"], t + 1)
    walk(tree, 1)
print("munoz-garcia-4-9: SPE = Stop at every stage; outcome (2,0); margin 1 everywhere")

print("all L03 checks passed")
