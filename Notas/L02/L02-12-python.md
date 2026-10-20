---
tags: [notes, lecture-02, python, nash-equilibrium, support-enumeration, linear-programming]
date: 2026-10-16
status: estimated
source: "Tadelis (2013) Ch. 4.3, 5, 6 (printed pp. 69–123): every assert below is a number from those pages; Gibbons (1992) §1.2–1.3 (pp. 14–44)"
---

# Lecture 2 · Computation in Python

> Every routine the lecture needs, each with `assert` self-checks against the book's own numbers. Run the blocks in
> order in one session (they share imports); all of them were run together on 2026-10-16 and pass. numpy and scipy
> only (scipy for the linear program in §8).
>
> Prev: [[L02-11-pitfalls]] · Map: [[L02-00-map]] · Formulas: [[L02-10-formulas]]

**Reuse.** Lecture 1's checks (`Listas/lista-lecture-01-check.py`) already contain pure-strategy IESDS (`iesds2`) and
the Cournot best response and IESDS recursion (`BR`, `cournot_iesds`). They are cited rather than imported because that
file runs the whole Lecture 1 list check (sympy, 1500 random draws) on import; the two-line best response is repeated in
§3. Dominance **by a mixed strategy** (§8) is new: `iesds2` compares pure strategies only. The figure script
(`figures/make_figures.py`) and the companion checker (`companions/check_companions.py`) carry their own copies of the
Bertrand, voting and 2×2 routines, so each artefact runs on its own.

---

## 1 · Best responses and pure equilibria in a matrix → [[L02-02-nash-equilibrium]]

```python
import itertools
from fractions import Fraction as Fr
import numpy as np


def best_responses(U1, U2):
    """Pure best-response sets of a bimatrix game.

    U1[r][c], U2[r][c]: payoffs of the row and column player.
    Returns (br1, br2): br1[c] = set of rows that are best replies to column c;
    br2[r] = set of columns that are best replies to row r.
    """
    U1, U2 = np.asarray(U1, float), np.asarray(U2, float)
    br1 = [set(np.flatnonzero(U1[:, c] == U1[:, c].max())) for c in range(U1.shape[1])]
    br2 = [set(np.flatnonzero(U2[r, :] == U2[r, :].max())) for r in range(U2.shape[0])]
    return br1, br2


def pure_nash(U1, U2):
    """Tadelis's underline method (pp. 81-82): cells where both players best-respond."""
    br1, br2 = best_responses(U1, U2)
    return [(r, c) for r in range(len(U1)) for c in range(len(U1[0])) if r in br1[c] and c in br2[r]]


# p. 81: no dominated strategy, unique pure NE (M, C)
U1 = [[7, 4, 1], [2, 5, 2], [8, 3, 0]]
U2 = [[7, 2, 8], [4, 5, 3], [1, 2, 0]]
assert pure_nash(U1, U2) == [(1, 1)]
# p. 72: ties -> BR is a correspondence: BR1(R) = {U, D}, BR1(L) = {M, D}
br1, _ = best_responses([[3, 5, 6], [4, 8, 3], [4, 9, 6]], [[3, 1, 2], [1, 4, 6], [0, 6, 8]])
assert br1[2] == {0, 2} and br1[0] == {1, 2}
# p. 80 (Lecture 1's IESDS game): unique NE (U, L)
assert pure_nash([[4, 5, 6], [2, 8, 3], [3, 9, 2]], [[3, 1, 2], [1, 4, 6], [0, 6, 8]]) == [(0, 0)]
# Battle of the Sexes p. 69: two pure NE; prisoner's dilemma p. 48: (F, F) only
assert pure_nash([[2, 0], [0, 1]], [[1, 0], [0, 2]]) == [(0, 0), (1, 1)]
assert pure_nash([[-2, -5], [-1, -4]], [[-2, -1], [-5, -4]]) == [(1, 1)]
# Stag Hunt p. 84: (S, S) and (H, H); Matching Pennies p. 101: none
assert pure_nash([[5, 0], [3, 3]], [[5, 3], [0, 3]]) == [(0, 0), (1, 1)]
assert pure_nash([[1, -1], [-1, 1]], [[-1, 1], [1, -1]]) == []
```

---

## 2 · Rationalizability in Cournot and the beauty contest → [[L02-01-best-response-rationalizability]]

```python
def cournot_rationalizable(a=100.0, b=1.0, c=10.0, rounds=40):
    """Interval of quantities surviving k rounds (Sec. 4.3.4): [BR(upper), BR(lower)]."""
    br = lambda q: max(0.0, (a - c - b * q) / (2 * b))
    lo, hi = 0.0, br(0.0)                      # round 1: [0, 45]
    hist = [(lo, hi)]
    for _ in range(rounds - 1):
        lo, hi = br(hi), br(lo)
        hist.append((lo, hi))
    return hist


h = cournot_rationalizable()
assert h[0] == (0.0, 45.0) and h[1] == (22.5, 45.0) and h[2] == (22.5, 33.75)
assert abs(h[-1][0] - 30) < 1e-9 and abs(h[-1][1] - 30) < 1e-9   # converges to 30 (p. 74)


def beauty_never_best(n, top):
    """Is `top` never a best response in the 3/4-beauty contest on {0..top}? (p. 75).

    Checks the binding belief (everyone else plays `top`): `top - 1` wins alone, `top` only ties.
    """
    others = [top] * (n - 1)
    target = lambda x: 0.75 * (sum(others) + x) / n
    return abs(top - 1 - target(top - 1)) < abs(top - target(top - 1))


assert all(beauty_never_best(n, 20) for n in range(2, 50))
avg = lambda n: ((n - 1) * 20 + 19) / n        # footnote 6, p. 75
assert 19.5 <= avg(2) and avg(10**6) < 20 and abs(0.75 * avg(2) - 14.625) < 1e-12
```

---

## 3 · Cournot → [[L02-03-cournot]]

```python
def cournot_br(a, b, ci, qj):
    """Eq. (5.2): BR_i(q_j) = max{0, (a - b q_j - c_i)/(2b)}."""
    return max(0.0, (a - ci - b * qj) / (2 * b))


def cournot_nash(a, b, c1, c2):
    """Unique Cournot-Nash equilibrium of the linear duopoly, corners included."""
    q1, q2 = (a - 2 * c1 + c2) / (3 * b), (a - 2 * c2 + c1) / (3 * b)
    if q1 >= 0 and q2 >= 0:
        return q1, q2
    if q1 < 0:
        q2 = max(0.0, (a - c2) / (2 * b))
        return cournot_br(a, b, c1, q2), q2
    q1 = max(0.0, (a - c1) / (2 * b))
    return q1, cournot_br(a, b, c2, q1)


profit = lambda a, b, ci, qi, qj: (a - b * (qi + qj) - ci) * qi

q1, q2 = cournot_nash(100, 1, 10, 10)
assert (q1, q2) == (30, 30) and 100 - 60 == 40 and profit(100, 1, 10, 30, 30) == 900     # pp. 87, 90
assert cournot_br(100, 1, 10, q2) == q1 and cournot_br(100, 1, 10, q1) == q2            # mutual BR
# monopoly 45 at 55, profit 2025 (p. 89); collusion at 22.5 each is not a best reply (Gibbons p. 17)
assert profit(100, 1, 10, 45, 0) == 2025 and cournot_br(100, 1, 10, 22.5) == 33.75
assert profit(100, 1, 10, 33.75, 22.5) > profit(100, 1, 10, 22.5, 22.5)
# asymmetric costs c1 = 1, c2 = 2: pi_i = b q_i^2; the gap q1 - q2 = (c2 - c1)/b
q1, q2 = cournot_nash(100, 1, 1, 2)
assert abs(q1 - 100 / 3) < 1e-12 and abs(q1 - q2 - 1) < 1e-12
assert abs(profit(100, 1, 1, q1, q2) - q1 ** 2) < 1e-9
# corner: c1 >= (a + c2)/2 -> firm 1 out, firm 2 a monopolist
assert cournot_nash(100, 1, 55, 10) == (0.0, 45.0) and cournot_nash(100, 1, 70, 10) == (0.0, 45.0)
# n firms: q = (a - c)/((n+1) b), price -> c (Tadelis ex. 5.8 / Gibbons 1.4 setting)
n_firm_price = lambda n, a=100, c=10: (a + n * c) / (n + 1)
assert n_firm_price(1) == 55 and n_firm_price(2) == 40 and n_firm_price(10**6) - 10 < 1e-3
```

---

## 4 · Bertrand on a cent grid → [[L02-04-bertrand]]

```python
def bertrand_profit(pi, pj, c=10.0, a=100.0):
    """v_i of p. 88 (homogeneous goods, ties split); vectorised in p_i."""
    pi = np.asarray(pi, float)
    full = (a - pi) * (pi - c)
    return np.where(pi < pj - 1e-9, full, np.where(np.abs(pi - pj) <= 1e-9, full / 2, 0.0))


grid = np.round(np.arange(0, 6001) / 100, 2)          # 0.00 .. 60.00 in cents
BR = []
for pj in grid:
    v = bertrand_profit(grid, pj)
    BR.append(set(np.round(grid[np.abs(v - v.max()) <= 1e-9], 2).tolist()))
idx = {p: i for i, p in enumerate(grid.tolist())}
assert BR[idx[57.0]] == {55.0} and BR[idx[30.0]] == {29.99} and BR[idx[10.01]] == {10.01}  # p. 90
assert min(BR[idx[10.0]]) == 10.0 and len(BR[idx[10.0]]) == 5001                           # any p >= 10
NE = sorted((p1, p2) for p1 in grid.tolist() for p2 in BR[idx[p1]] if p1 in BR[idx[p2]])
assert NE == [(10.0, 10.0), (10.01, 10.01)]                                                  # p. 90
# Delta v of p. 89 at p_j = 10.02: 0.0002 with the book's rounding, 0.0001 exactly
dv_book = 55.02 * 10.02 - 0.5 * 10.02 ** 2 - 501.1
dv_exact = 89.99 * 0.01 - 0.5 * 89.98 * 0.02
assert abs(dv_book - 0.0002) < 1e-9 and abs(dv_exact - 0.0001) < 1e-9
# asymmetric, continuous: v1(p1, 2) -> 98 as p1 -> 2 from below, 49 at 2, 0 above (pp. 91-92)
v1 = lambda p1: (100 - p1) * (p1 - 1) if p1 < 2 else (49.0 if p1 == 2 else 0.0)
assert v1(2 - 1e-9) < 98 and 98 - v1(2 - 1e-9) < 1e-6 and v1(2) == 49 and v1(2.5) == 0
# differentiated Bertrand (Gibbons p. 22): p* = (a + c)/(2 - b) solves p = (a + b p + c)/2
a_, b_, c_ = 10.0, 0.5, 2.0
p_star = (a_ + c_) / (2 - b_)
assert abs(p_star - (a_ + b_ * p_star + c_) / 2) < 1e-12
```

---

## 5 · The commons → [[L02-05-commons]]

```python
import math

K = 1.0
k_ne = K / 3                       # k_i = (K - k_j)/2 at both (p. 86)
assert abs(k_ne - (K - k_ne) / 2) < 1e-15
v_sym = lambda k: math.log(k) + math.log(K - 2 * k)
# the symmetric social optimum K/4 (p. 87): grid maximiser of v(k, k)
ks = np.linspace(0.01, 0.49, 48001)
assert abs(ks[np.argmax([v_sym(k) for k in ks])] - 0.25) < 1e-4
gain = v_sym(K / 4) - v_sym(K / 3)
assert abs(gain - math.log(9 / 8)) < 1e-12 and round(gain, 3) == 0.118
# footnote 5 prints 0.051: that is the base-10 value of the same expression
assert round(2 * math.log10(3) - math.log10(2) - math.log10(4), 3) == 0.051
```

---

## 6 · Hotelling voting → [[L02-06-hotelling-voting]]

```python
PLAT = range(-50, 51)


def vote_payoff(ai, aj):
    """1 win, 1/2 tie, 0 lose; equidistant citizens abstain (Tadelis fn. 9, p. 94)."""
    if ai == aj:
        return 0.5
    mine = sum(abs(x - ai) < abs(x - aj) for x in PLAT)
    theirs = sum(abs(x - aj) < abs(x - ai) for x in PLAT)
    return 1.0 if mine > theirs else 0.5 if mine == theirs else 0.0


assert sum(abs(x + 15) < abs(x - 22) for x in PLAT) == 54          # Fig. 5.4: citizens -50..3
PAY = {(i, j): vote_payoff(i, j) for i in PLAT for j in PLAT}
BRv = {j: [i for i in PLAT if PAY[i, j] == max(PAY[k, j] for k in PLAT)] for j in PLAT}
assert BRv[22] == list(range(-21, 22)) and BRv[-15] == list(range(-14, 15))
assert BRv[0] == BRv[1] == BRv[-1] == [0]                            # footnote 10
assert [(i, j) for j in PLAT for i in BRv[j] if j in BRv[i]] == [(0, 0)]
```

---

## 7 · Mixed equilibria: indifference and support enumeration → [[L02-07-mixed-strategies]]

```python
def mixed_2x2(U1, U2):
    """Totally mixed NE of a 2x2 game from the two indifference conditions (Prop. 6.1).

    Returns (p, q) = (Pr row 1, Pr column 1) as Fractions, or None if not in (0,1)^2.
    """
    (a, b), (c, d) = [[Fr(x) for x in r] for r in U1]
    (e, f), (g, h) = [[Fr(x) for x in r] for r in U2]
    # player 1 indifferent: q a + (1-q) b = q c + (1-q) d
    den1, den2 = (a - c) - (b - d), (e - f) - (g - h)
    if den1 == 0 or den2 == 0:
        return None
    q = (d - b) / den1
    p = (h - g) / den2                    # player 2 indifferent: p e + (1-p) g = p f + (1-p) h
    return (p, q) if 0 < p < 1 and 0 < q < 1 else None


assert mixed_2x2([[1, -1], [-1, 1]], [[-1, 1], [1, -1]]) == (Fr(1, 2), Fr(1, 2))     # p. 111
assert mixed_2x2([[0, 3], [4, 0]], [[0, 5], [4, 3]]) == (Fr(1, 6), Fr(3, 7))         # p. 113
assert mixed_2x2([[2, 0], [0, 1]], [[1, 0], [0, 2]]) == (Fr(2, 3), Fr(1, 3))         # BoS
assert mixed_2x2([[5, 0], [3, 3]], [[5, 3], [0, 3]]) == (Fr(3, 5), Fr(3, 5))         # Stag Hunt


def support_enumeration(U1, U2):
    """All NE of a nondegenerate bimatrix game (MWG Prop. 8.D.1): equal payoffs on the
    support, no better payoff off it. Exact arithmetic; returns list of (sigma1, sigma2)."""
    U1 = [[Fr(x) for x in r] for r in U1]
    U2 = [[Fr(x) for x in r] for r in U2]
    m, n = len(U1), len(U1[0])
    out = []

    def solve(A, rhs):
        """Square system by Gaussian elimination over Fractions; None if singular."""
        A = [row[:] + [v] for row, v in zip(A, rhs)]
        k = len(A)
        for col in range(k):
            piv = next((r for r in range(col, k) if A[r][col] != 0), None)
            if piv is None:
                return None
            A[col], A[piv] = A[piv], A[col]
            A[col] = [x / A[col][col] for x in A[col]]
            for r in range(k):
                if r != col and A[r][col] != 0:
                    A[r] = [x - A[r][col] * y for x, y in zip(A[r], A[col])]
        return [A[i][-1] for i in range(k)]

    for k in range(1, min(m, n) + 1):
        for S1 in itertools.combinations(range(m), k):
            for S2 in itertools.combinations(range(n), k):
                # sigma2 on S2 makes player 1 indifferent over S1 (unknowns: probs + value)
                A = [[U1[r][c] for c in S2] + [Fr(-1)] for r in S1] + [[Fr(1)] * k + [Fr(0)]]
                x2 = solve(A, [Fr(0)] * k + [Fr(1)])
                A = [[U2[r][c] for r in S1] + [Fr(-1)] for c in S2] + [[Fr(1)] * k + [Fr(0)]]
                x1 = solve(A, [Fr(0)] * k + [Fr(1)])
                if x1 is None or x2 is None or min(x1[:-1]) < 0 or min(x2[:-1]) < 0:
                    continue
                s1 = [Fr(0)] * m
                s2 = [Fr(0)] * n
                for i, r in enumerate(S1):
                    s1[r] = x1[i]
                for i, c in enumerate(S2):
                    s2[c] = x2[i]
                v1 = [sum(U1[r][c] * s2[c] for c in range(n)) for r in range(m)]
                v2 = [sum(U2[r][c] * s1[r] for r in range(m)) for c in range(n)]
                if max(v1) == x2[-1] and max(v2) == x1[-1]:        # nothing off-support does better
                    out.append((tuple(s1), tuple(s2)))
    return out


RPS1 = [[0, -1, 1], [1, 0, -1], [-1, 1, 0]]
RPS2 = [[-x for x in r] for r in RPS1]
third = (Fr(1, 3),) * 3
assert support_enumeration(RPS1, RPS2) == [(third, third)]                          # pp. 111-113
# p. 81: (M, C) is the unique PURE NE, but the game has five NE in all (four mixed)
eq81 = support_enumeration(U1, U2)
s16 = (Fr(1, 6), Fr(5, 6), Fr(0))
assert len(eq81) == 5 and ((0, 1, 0), (0, 1, 0)) in eq81 and (s16, s16) in eq81
# a degenerate game (1 for both at (first, first), else 0): two pure NE and no mixed one,
# the exception to "two pure => a third, mixed" (pitfalls item 17; the companion's exact solver agrees)
weak = support_enumeration([[1, 0], [0, 0]], [[1, 0], [0, 0]])
assert set(weak) == {((1, 0), (1, 0)), ((0, 1), (0, 1))}
eq = support_enumeration([[0, 3], [4, 0]], [[0, 5], [4, 3]])
assert len(eq) == 3 and ((Fr(1, 6), Fr(5, 6)), (Fr(3, 7), Fr(4, 7))) in eq           # p. 113
# RPS payoffs against (1/2, 1/2, 0): R -1/2, P 1/2, S 0 (p. 106)
s2 = [Fr(1, 2), Fr(1, 2), Fr(0)]
assert [sum(RPS1[r][c] * s2[c] for c in range(3)) for r in range(3)] == [Fr(-1, 2), Fr(1, 2), 0]
# all-pay auction against U[0,1] (p. 107): every bid in [0,1] earns 0
assert all(abs((1 - s) * (-s) + s * (1 - s)) < 1e-15 for s in np.linspace(0, 1, 101))
```

---

## 8 · Dominance by a mixed strategy (linear program) → [[L02-08-iesds-rationalizability-revisited]]

```python
from scipy.optimize import linprog


def dominated_by_mix(U, s, others):
    """Is pure row `s` strictly dominated by a mix over `others` (Def. 6.7)?

    U[r][c]: the player's payoff, own strategies as rows. Maximise eps subject to
    sum_r x_r U[r][c] >= U[s][c] + eps for every column c, x in the simplex.
    Returns (eps, x); dominated iff eps > 0.
    """
    U = np.asarray(U, float)
    k, n = len(others), U.shape[1]
    c = np.zeros(k + 1)
    c[-1] = -1.0                                      # maximise eps
    A_ub = np.hstack([-U[others].T, np.ones((n, 1))])
    b_ub = -U[s]
    A_eq = np.hstack([np.ones((1, k)), np.zeros((1, 1))])
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=[1.0],
                  bounds=[(0, 1)] * k + [(None, None)], method="highs")
    return res.x[-1], res.x[:-1]


# Tadelis p. 115: player 2's L is dominated by a C/R mix; (0, 1/2, 1/2) gives 2, 2.5, 3.5
V2 = np.array([[1, 4, 0], [2, 0, 5], [3, 4, 3]], float).T           # player 2's payoffs, own strategies as rows
eps, x = dominated_by_mix(V2, 0, [1, 2])
assert eps > 0 and np.allclose(0.5 * V2[1] + 0.5 * V2[2], [2, 2.5, 3.5])
# no pure strategy dominates L (pure IESDS does nothing)
assert not any(all(V2[j] > V2[0]) for j in (1, 2))
# p. 116: after L is gone, U is dominated by (0, 1/2, 1/2) over M, D: 2 and 1.5 against 1 and 1
V1 = np.array([[1, 1], [0, 3], [4, 0]], float)                      # player 1, columns C, R
eps, _ = dominated_by_mix(V1, 0, [1, 2])
assert eps > 0 and np.allclose(0.5 * V1[1] + 0.5 * V1[2], [2, 1.5])
# ...but not before L is removed (against L, U's 5 beats the mix's 3.5)
V1full = np.array([[5, 1, 1], [3, 0, 3], [4, 4, 0]], float)
assert dominated_by_mix(V1full, 0, [1, 2])[0] <= 1e-9
# Gibbons p. 32: B = (1, 1) dominated by T/2 + M/2; B = (2, 2) is not dominated
assert dominated_by_mix([[3, 0], [0, 3], [1, 1]], 2, [0, 1])[0] > 0
assert dominated_by_mix([[3, 0], [0, 3], [2, 2]], 2, [0, 1])[0] <= 1e-9
```

---

## 9 · Equilibria as fixed points of $BR$ → [[L02-09-existence]]

```python
def br1(q):  # Tadelis (6.3), p. 119: p as a set, the 6.2.3 game
    return {1.0} if q < 3 / 7 else ({0.0} if q > 3 / 7 else "all")


def br2(p):  # (6.4)
    return {1.0} if p < 1 / 6 else ({0.0} if p > 1 / 6 else "all")


def is_fixed(q, p):
    b1, b2 = br1(q), br2(p)
    return (b1 == "all" or p in b1) and (b2 == "all" or q in b2)


pts = [(q, p) for q in np.linspace(0, 1, 701) for p in np.linspace(0, 1, 601) if is_fixed(q, p)]
assert sorted(pts) == [(0.0, 1.0), (1.0, 0.0)]         # the grid misses 3/7 and 1/6 ...
assert is_fixed(3 / 7, 1 / 6)                           # ... the mixed fixed point is exact
assert br1(0.8) == {0.0} and br2(0.5) == {0.0}          # (q1, p1) -> (0, 0), Fig. 6.6
print("Lecture 2 python note: all checks pass")
```

The last block also shows why the companion and these checks solve for equilibria **exactly** rather than on a grid:
the mixed fixed point $(\tfrac37,\tfrac16)$ is not on any decimal grid, and a grid search silently loses it.

---

## Links

- Figures: `figures/make_figures.py` (run: `python Notas/L02/figures/make_figures.py`).
- Companion checks: `companions/check_companions.py` (run: `python Notas/L02/companions/check_companions.py`).
- Lecture 1 code: `Listas/lista-lecture-01-check.py`.
