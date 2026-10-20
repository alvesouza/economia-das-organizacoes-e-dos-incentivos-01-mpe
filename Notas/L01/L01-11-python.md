---
tags: [notes, lecture-01, python, iesds, dominance, cournot]
date: 2026-10-16
status: taught
source: "Listas/lista-lecture-01-check.py (iesds2, iesds_rounds_detail, cournot_iesds, line_game, spa_payoff, weak_outcomes, partnership_conditions: reused, not rewritten); Tadelis (2013) pp. 48, 52, 60, 64-68; Gibbons pp. 5-7; MWG p. 238; M&R Table 5.1 p. 138"
---

# Lecture 1 · Computation in Python

> Every routine the lecture needs, each followed by `assert` checks against the slides' and the
> books' own numbers. Python only, numpy optional. The blocks run top to bottom from the
> repository root as one script (the unit's check does exactly that).
>
> Prev: [[L01-10-pitfalls]] · Map: [[L01-00-map]] · Formulas: [[L01-09-formulas]]

**Reuse.** `Listas/lista-lecture-01-check.py` already implements and tests IESDS, the Cournot
interval recursion, the location game and the second-price payoff. Importing it would run its
1,500-draw sympy checks, so §0 loads **only its function definitions**. New code here covers
what that file does not have: single-step dominance tests, Pareto sets, and the walking distance.
`Notas/L01/figures/make_figures.py` and `companions/check_companions.py` use the same loader.

---

## 0 · Load the existing routines

```python
import ast, itertools, pathlib, random
from fractions import Fraction as Fr
from functools import lru_cache

def lista_functions(path="Listas/lista-lecture-01-check.py"):
    """Execute only the `def` statements of the lista check script; return them as a dict."""
    tree = ast.parse(pathlib.Path(path).read_text(encoding="utf-8"))
    defs = [n for n in tree.body if isinstance(n, ast.FunctionDef)]
    ns = {"Fr": Fr, "itertools": itertools, "lru_cache": lru_cache, "random": random}
    exec(compile(ast.Module(body=defs, type_ignores=[]), path, "exec"), ns)
    return ns

L = lista_functions()
iesds2, rounds_detail = L["iesds2"], L["iesds_rounds_detail"]
assert {"iesds2", "cournot_iesds", "line_game", "spa_payoff", "weak_outcomes"} <= set(L)
```

## 1 · Games as payoff matrices → [[L01-01-games-normal-form]]

Two-player finite games are pairs of matrices `U1[r][c]`, `U2[r][c]` (rows = player 1).

```python
PD_1 = [[-2, -5], [-1, -4]]          # rows/cols (M, F), Tadelis p. 48
PD_2 = [[-2, -1], [-5, -4]]
GRADE_1 = [[0, 3], [-1, 1]]          # rows/cols (alpha, beta), slide 12
GRADE_2 = [[0, -1], [3, 1]]
M41_1 = [[4, 5, 6], [2, 8, 3], [3, 9, 2]]   # matrix (4.1), Tadelis p. 64 = slide 27
M41_2 = [[3, 1, 2], [1, 4, 6], [0, 6, 8]]

def partnership(y, c):
    """2x2 partnership of slide 4, rows/cols (E, S): half of output minus own effort cost."""
    U1 = [[y - c, y / 2 - c], [y / 2, 0]]
    return U1, [list(r) for r in zip(*U1)]       # symmetric game: U2 = U1 transposed

# Tadelis's quadratic-cost Cournot (p. 49): competitive benchmark and the deviation to 24
v = lambda qi, qj: (100 - qi - qj) * qi - qi**2 if qi + qj < 100 else -qi**2
assert v(25, 25) == 625 and v(24, 25) == 648
```

## 2 · Dominance, dominant-strategy equilibrium, Pareto → [[L01-04-dominance]], [[L01-05-pareto-social-dilemmas]]

```python
def payoff_rows(U1, U2, player):
    """Player's own payoffs as rows indexed by his strategies (columns = opponent strategies)."""
    return U1 if player == 0 else [list(r) for r in zip(*U2)]

def dominates(a, b, weak=False):
    """Does payoff row a dominate payoff row b (strictly, or weakly with one strict)?"""
    d = [x - y for x, y in zip(a, b)]
    return all(t >= 0 for t in d) and any(t > 0 for t in d) if weak else all(t > 0 for t in d)

def dominated(U1, U2, player, weak=False):
    """Strategies of `player` dominated by some other pure strategy: {s: [dominators]}."""
    P = payoff_rows(U1, U2, player)
    out = {s: [t for t in range(len(P)) if t != s and dominates(P[t], P[s], weak)] for s in range(len(P))}
    return {s: d for s, d in out.items() if d}

def dominant(U1, U2, player, weak=False):
    """The (strictly or weakly) dominant strategy of `player`, or None."""
    P = payoff_rows(U1, U2, player)
    for s in range(len(P)):
        if all(dominates(P[s], P[t], weak) for t in range(len(P)) if t != s):
            return s
    return None

def dse(U1, U2, weak=False):
    """Dominant-strategy equilibrium (row, col) or None (Tadelis Def. 4.3)."""
    s1, s2 = dominant(U1, U2, 0, weak), dominant(U1, U2, 1, weak)
    return None if s1 is None or s2 is None else (s1, s2)

def pareto_optimal(U1, U2):
    """Profiles not Pareto dominated by any other (Tadelis Def. 3.5, p. 57)."""
    cells = {(r, c): (U1[r][c], U2[r][c]) for r in range(len(U1)) for c in range(len(U1[0]))}
    return {s for s, u in cells.items() if not any(dominates(w, u, weak=True) for t, w in cells.items() if t != s)}

assert dse(PD_1, PD_2) == (1, 1)                                   # (F, F), slide 24
assert pareto_optimal(PD_1, PD_2) == {(0, 0), (0, 1), (1, 0)}      # all but (F, F), p. 57
assert dse(GRADE_1, GRADE_2) == (0, 0) and (1, 1) in pareto_optimal(GRADE_1, GRADE_2)
# Example 3 (slide 27): no dominant strategy; only C is dominated (by R)
assert dse(M41_1, M41_2) is None and dominated(M41_1, M41_2, 0) == {}
assert dominated(M41_1, M41_2, 1) == {1: [2]}
assert pareto_optimal(M41_1, M41_2) == {(2, 1), (2, 2)}            # (D, C) and (D, R)
# Advertising game (Tadelis p. 60): L dominated by M, nothing else
AD_1 = [[6, 2, 0], [8, 4, 1], [4, 3, 2]]
AD_2 = [list(r) for r in zip(*AD_1)]
assert dominated(AD_1, AD_2, 0) == {0: [1]}
# Never best, yet not dominated by a pure strategy (note 04, section 7.1)
assert dominated([[3, 0], [1, 1], [0, 3]], [[0, 0]] * 3, 0) == {}
# Weak dominance: unique weakly dominant strategy under the slides' definition (note 04, section 7)
assert dominant([[1, 1], [1, 0]], [[0, 0], [0, 0]], 0, weak=True) == 0
assert dominant([[1, 1], [1, 1]], [[0, 0], [0, 0]], 0, weak=True) is None   # identical rows: neither
```

## 3 · IESDS → [[L01-06-iesds]]

```python
# Matrix (4.1): C, then M and D, then R (Tadelis pp. 64-65)
R, C, rounds = rounds_detail(M41_1, M41_2)
assert (R, C) == ([0], [0]) and rounds == [([], [1]), ([1, 2], []), ([], [2])]
# Prop. 4.2: a strict DSE is the unique survivor, after one round
assert rounds_detail(PD_1, PD_2)[:2] == ([1], [1]) and len(rounds_detail(PD_1, PD_2)[2]) == 1
# Gibbons Figure 1.1.1 (pp. 5-7): (Up, Middle)
G1 = [[1, 1, 0], [0, 0, 2]]; G2 = [[0, 2, 1], [3, 1, 0]]
assert iesds2(G1, G2)[:2] == ([0], [1])
# No bite: Battle of the Sexes (Tadelis p. 54) and Gibbons Figure 1.1.4 (p. 7)
assert iesds2([[2, 0], [0, 1]], [[1, 0], [0, 2]])[:2] == ([0, 1], [0, 1])
F114_1 = [[0, 4, 5], [4, 0, 5], [3, 3, 6]]; F114_2 = [[4, 0, 3], [0, 4, 3], [5, 5, 6]]
assert iesds2(F114_1, F114_2)[:2] == ([0, 1, 2], [0, 1, 2])
# Weak elimination depends on the order: MWG Figure 8.B.3 (p. 238)
W1 = [[5, 4], [6, 3], [6, 4]]; W2 = [[1, 0], [0, 1], [4, 4]]
def weak_orders(U1, U2, R=None, C=None):
    """End states of every one-at-a-time order of weak elimination (the lista's
    weak_outcomes is hard-wired to 3x3, so this generalizes it to any size)."""
    R = tuple(range(len(U1))) if R is None else R
    C = tuple(range(len(U1[0]))) if C is None else C
    moves = [("r", r) for r in R if any(dominates([U1[t][c] for c in C], [U1[r][c] for c in C], True) for t in R if t != r)]
    moves += [("c", c) for c in C if any(dominates([U2[r][t] for r in R], [U2[r][c] for r in R], True) for t in C if t != c)]
    if not moves:
        return {(R, C)}
    return set().union(*(weak_orders(U1, U2, tuple(x for x in R if x != v), C) if k == "r"
                         else weak_orders(U1, U2, R, tuple(x for x in C if x != v)) for k, v in moves))
assert weak_orders(W1, W2) == {((2,), (1,)), ((2,), (0,)), ((2,), (0, 1))}   # (D, R), (D, L), or D x {L, R}
assert iesds2(W1, W2)[:2] == ([0, 1, 2], [0, 1])                   # strict IESDS removes nothing
```

## 4 · Partnership and changing the game → [[L01-05-pareto-social-dilemmas]]

```python
def partnership_verdict(y, c, n):
    """Dominance and dilemma verdict for n partners: gain from effort y/n - c, all-E vs all-S y - c."""
    g = y / n - c
    dom = "E" if g > 0 else ("S" if g < 0 else "none")
    return dom, (dom == "S" and y - c > 0)          # (dominant strategy, social dilemma?)

assert partnership_verdict(6, 4, 2) == ("S", True)          # default: the dilemma
assert partnership_verdict(6, 2, 2) == ("E", False)
assert partnership_verdict(6, 7, 2) == ("S", False)         # shirking dominant AND efficient
assert partnership_verdict(6, 3, 2) == ("none", False)      # c = y/n: no dominance at all
# y = 6, c = 4, n = 2 is Tadelis's PD plus 4 on every payoff
U1, U2 = partnership(6, 4)
assert [[x - 4 for x in row] for row in U1] == PD_1      # rows (E, S) <-> (M, F)
# reuse: the lista's n-partner condition with no synergy (theta = 0) is exactly y/n < c < y
assert L["partnership_conditions"](2, 6, 0, 4) and not L["partnership_conditions"](2, 6, 0, 7)

# Mafia-modified PD (Tadelis pp. 62-63): M strictly dominant iff z > 1
def mafia(z):
    return [[-2, -5], [-1 - z, -4 - z]], [[-2, -1 - z], [-5, -4 - z]]
assert dse(*mafia(1.01)) == (0, 0) and dse(*mafia(0.99)) == (1, 1) and dse(*mafia(1)) is None
# M&R grabbing (Table 5.1, p. 138), A as rows (Grab, Don't)
GR_A = [[-1, 3], [-2, 2]]; GR_B = [[-1, -2], [3, 2]]
assert dse(GR_A, GR_B) == (0, 0) and (1, 1) in pareto_optimal(GR_A, GR_B)
```

The partnership's rows are $(E,S)$ and the PD's $(M,F)$: effort plays the role of mum
(cooperate), shirking the role of fink (defect).

## 5 · Cournot by IESDS → [[L01-07-cournot-iesds]]

```python
cournot_iesds = L["cournot_iesds"]      # [(lows, highs) per round], exact Fractions

hist = cournot_iesds(Fr(100), Fr(1), Fr(10), Fr(10), 12)
assert [(h[0][0], h[1][0]) for h in hist[:4]] == [(0, 45), (Fr(45, 2), 45), (Fr(45, 2), Fr(135, 4)), (Fr(225, 8), Fr(135, 4))]
assert all(h[1][0] - h[0][0] == Fr(45, 2 ** k) for k, h in enumerate(hist))      # width 45 / 2^(k-1)
assert hist[-1][0][0] < 30 < hist[-1][1][0]                                       # never a point in finite rounds

def cournot_eq(a, b, c1, c2):
    """Interior Cournot point q_i = (a - 2c_i + c_j) / (3b), price and profits."""
    q1, q2 = (a - 2 * c1 + c2) / (3 * b), (a - 2 * c2 + c1) / (3 * b)
    p = a - b * (q1 + q2)
    return q1, q2, p, (p - c1) * q1, (p - c2) * q2

assert cournot_eq(100, 1, 10, 10) == (30, 30, 40, 900, 900)                      # Tadelis p. 67
profit = lambda q, qj: (90 - q - qj) * q
assert profit(20, 20) == 1000 and profit(22.5, 22.5) == 1012.5                   # p. 68; joint optimum
# round-1 dominance identity v(45,q2) - v(q1,q2) = (q1-45)(q1-45+q2), on a grid
assert all(profit(45, q2) - profit(q1, q2) == (q1 - 45) * (q1 - 45 + q2) for q1 in range(0, 120) for q2 in range(0, 60))
# exit: c1 >= (a + c2)/2 drives firm 1 to zero
h = cournot_iesds(Fr(100), Fr(1), Fr(60), Fr(10), 40)
assert h[-1][1][0] == 0 and h[-1][0][1] == h[-1][1][1] == 45                    # firm 2 at monopoly (100-10)/2
```

## 6 · Second-price auction: weak, not strict → [[L01-04-dominance]] §6

```python
spa = L["spa_payoff"]                    # spa(i, bids, values, reserve), exact Fractions
vals, grid = [Fr(5), Fr(3)], [Fr(k, 2) for k in range(0, 21)]
def pay(b):                              # bidder 0's payoffs against every rival bid on the grid
    return [spa(0, (b, m), vals, Fr(0)) for m in grid + [Fr(12)]]
truth = pay(vals[0])
for b in grid:
    if b != vals[0]:
        assert dominates(truth, pay(b), weak=True)        # truthful weakly dominates b ...
        assert not dominates(truth, pay(b))               # ... but never strictly
```

## 7 · The pharmacy avenue → [[L01-08-spatial-competition]]

```python
U_A, U_B = L["line_game"](7, [1] * 7)
uA = lambda a, b: Fr(a + b - 1, 2) if a < b else Fr(7, 2) if a == b else 7 - Fr(a + b - 1, 2)
assert all(U_A[a - 1][b - 1] == uA(a, b) for a in range(1, 8) for b in range(1, 8))
assert all(U_A[1][b] > U_A[0][b] for b in range(7))                 # (b) block 1 < block 2
assert dominant(U_A, U_B, 0) is None                                 # (b) no dominant block
R, C, rounds = rounds_detail(U_A, U_B)
assert R == C == [3] and [r[0] for r in rounds] == [[0, 6], [1, 5], [2, 4]]   # (c) (4, 4) in 3 rounds
D = lambda x, y: sum(min(abs(j - x), abs(j - y)) for j in range(1, 8))
best = min(D(x, y) for x in range(1, 8) for y in range(1, 8))
assert D(4, 4) == 12 and best == 6                                   # (d) IESDS doubles the walking
assert {(x, y) for x in range(1, 8) for y in range(x, 8) if D(x, y) == 6} == {(2, 5), (2, 6), (3, 6)}
print("L01 python note: all checks pass")
```

---

## Links

- The routines' source and their randomized tests: `Listas/lista-lecture-01-check.py` (run it with `python Listas/lista-lecture-01-check.py`; needs sympy).
- Figures built from the same functions: `Notas/L01/figures/make_figures.py`. Companion checks: `Notas/L01/companions/check_companions.py`.
- Rules pack: [[../../rules/game-theory|rules/game-theory]] rule 12 (computational solution, verified by checking deviations); [[../../rules/lang-python|rules/lang-python]].
