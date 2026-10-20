---
tags: [notes, lecture-05, python, repeated-games, verification]
date: 2026-10-16
status: estimated
source: "Tadelis (2013) §10.1–10.3, 10.6, pp. 190–214; Gibbons (1992) §2.3.A–B, pp. 82–102; Cabral (2017) §7.3, pp. 172–173. Code reused from Notas/L05/figures/make_figures.py (pure_ne, coop_rounds)"
---

# Lecture 5 · Computation in Python

> Every routine the lecture needs, each with `assert` checks against the books' own numbers. The
> blocks run top to bottom as one script (numpy and sympy only). **What was reused:** the project has
> dominance and IESDS code in `Listas/lista-lecture-01-check.py` but no Nash-equilibrium finder or
> repeated-game routine, so `pure_ne` and `coop_rounds` are written here and are the same functions
> the figures use (`figures/make_figures.py`).
>
> Map: [[L05-00-map]] · Formulas: [[L05-07-formulas]] · Prev: [[L05-08-pitfalls]]

---

## 1 · Stage games and the unraveling → [[L05-01-finite-repetition-unraveling]]

```python
from fractions import Fraction as Fr
import numpy as np
import sympy as sp

# Tadelis's Prisoner's Dilemma, p. 197: rows M, F (player 1); columns m, f (player 2).
PD = {("M", "m"): (4, 4), ("M", "f"): (-1, 5), ("F", "m"): (5, -1), ("F", "f"): (1, 1)}

def pure_ne(pay, tol=1e-12):
    """Pure Nash equilibria of a bimatrix {(row, col): (u1, u2)}; weak best responses count."""
    rows = sorted({r for r, _ in pay}); cols = sorted({c for _, c in pay})
    return sorted((r, c) for r in rows for c in cols
                  if all(pay[(r, c)][0] >= pay[(r2, c)][0] - tol for r2 in rows)
                  and all(pay[(r, c)][1] >= pay[(r, c2)][1] - tol for c2 in cols))

def fold(pay, cont):
    """Add a continuation payoff cont(cell) = (c1, c2) to every cell: one step of backward induction."""
    return {k: (v[0] + cont(k)[0], v[1] + cont(k)[1]) for k, v in pay.items()}

def unravel(pay, T, delta):
    """Backward induction in G(T, delta) when the stage NE is unique: the NE in every period.
    Returns the list of stage-NE sets, period T first."""
    out, carry = [], (0, 0)
    for t in range(T, 0, -1):
        g = fold(pay, lambda k: carry)            # continuation is the same in every cell
        ne = pure_ne(g)
        assert len(ne) == 1, "Prop. 10.1 needs a unique stage NE"
        out.append(ne)
        u = pay[ne[0]]
        carry = (delta * (u[0] + carry[0]), delta * (u[1] + carry[1]))
    return out

assert pure_ne(PD) == [("F", "f")]
assert all(ne == [("F", "f")] for ne in unravel(PD, 500, 0.97))   # 500 rounds, p. 192
assert pure_ne(fold(PD, lambda k: (1, 1)))[0] == ("F", "f")        # Gibbons Fig. 2.3.2 logic, p. 83
```

## 2 · Two stage equilibria: carrot and stick → [[L05-02-two-stage-carrot-stick]]

```python
G3 = {("M", "m"): (4, 4), ("M", "f"): (-1, 5), ("M", "r"): (0, 0),
      ("F", "m"): (5, -1), ("F", "f"): (1, 1), ("F", "r"): (0, 0),
      ("R", "m"): (0, 0), ("R", "f"): (0, 0), ("R", "r"): (3, 3)}      # Tadelis p. 191
assert pure_ne(G3) == [("F", "f"), ("R", "r")]

def stage1(delta):
    """First stage folded: (R,r) after (M,m), (F,f) otherwise (p. 191)."""
    return fold(G3, lambda k: (3 * delta, 3 * delta) if k == ("M", "m") else (delta, delta))

v_M = lambda d: 4 + 3 * d        # fn. 2, p. 191
v_F = lambda d: 5 + d
assert v_M(0.5) == v_F(0.5) and v_M(0.49) < v_F(0.49)
assert set(pure_ne(stage1(0.5))) == {("M", "m"), ("F", "f"), ("R", "r")}
assert ("M", "m") not in pure_ne(stage1(0.49))

def coop_rounds(d, T, b=5.0, a=4.0, r=3.0, p=1.0):
    """Most rounds of (M,m) in T repetitions: (M,m) x n, then (R,r), deviation -> (F,f).
    Checks every cooperative round (one-stage deviation principle). Same code as the figures."""
    best = 0
    for n in range(T):
        if all(b - a <= sum(d ** (s - t) * ((a if s <= n else r) - p) for s in range(t + 1, T + 1)) + 1e-12
               for t in range(1, n + 1)):
            best = n
    return best

def k_min(d, b=5.0, a=4.0, r=3.0, p=1.0, kmax=200):
    """Shortest reward phase that holds the last cooperative round: closed form of the box in L05-02 §4."""
    for k in range(1, kmax):
        if b - a <= (r - p) * d * (1 - d ** k) / (1 - d) + 1e-12:
            return k
    return None

for d, n in [(0.3, 0), (0.34, 6), (0.4, 8), (0.5, 9), (0.9, 9)]:
    assert coop_rounds(d, 10) == n
    assert n == 0 or n == 10 - k_min(d)                      # only the last round binds
assert k_min(1 / 3 - 1e-9) is None and k_min(0.3334) is not None   # floor delta > 1/3
```

## 3 · Discounting and average payoffs → [[L05-03-discounting-histories-strategies]]

```python
def pv(stream, delta):
    """Definition 10.2 truncated to the given stream."""
    return sum(delta ** t * v for t, v in enumerate(stream))

def average(stream, delta):
    """Definition 10.3: (1 - delta) x PV."""
    return (1 - delta) * pv(stream, delta)

def s_finite(v, delta, T):
    """(10.1)-(10.2): v + delta v + ... + delta^(T-1) v = (v - delta^T v)/(1 - delta)."""
    return (v - delta ** T * v) / (1 - delta)

assert abs(s_finite(4, 0.9, 30) - pv([4] * 30, 0.9)) < 1e-12
assert abs(s_finite(4, 0.9, 10_000) - 40) < 1e-9 and abs(average([4] * 10_000, 0.9) - 4) < 1e-9
assert abs(0.97 ** 100 - 0.0475) < 1e-4 and abs(0.97 ** 500 - 2.4315e-7) < 1e-10   # p. 194
assert 4 ** 3 == 64                                   # information sets at stage 4, fn. 5, p. 195
```

## 4 · Grim trigger → [[L05-04-grim-trigger-spe]]

```python
def grim_threshold(T, R, P):
    """(10.3)/(10.5) in PD labels: delta* = (T - R)/(T - P), exact if given ints/Fractions."""
    return Fr(T - R, T - P) if all(isinstance(x, int) for x in (T, R, P)) else (T - R) / (T - P)

def on_path_check(T, R, P, delta, horizon=4000):
    """One-stage deviation on the cooperative path, computed from explicit streams."""
    follow = pv([R] * horizon, delta)
    deviate = pv([T] + [P] * (horizon - 1), delta)
    return follow >= deviate - 1e-9

def off_path_check(P, S, delta, horizon=4000):
    """In the punishment state: F against f (P forever) vs M today (S) then P forever."""
    return pv([P] * horizon, delta) >= pv([S] + [P] * (horizon - 1), delta)

assert grim_threshold(5, 4, 1) == Fr(1, 4)                       # Tadelis p. 200; Gibbons p. 92
assert grim_threshold(6, 5, 4) == Fr(1, 2)                       # Cabral p. 173
assert on_path_check(5, 4, 1, 0.25) and not on_path_check(5, 4, 1, 0.24)
assert all(off_path_check(1, -1, d) for d in (0.01, 0.5, 0.99))  # punishment credible for every delta
# the table in L05-04 §4.2
for d, (vc, vd) in {0.2: (5.0, 5.25), 0.25: (16 / 3, 16 / 3), 0.5: (8.0, 6.0)}.items():
    assert abs(4 / (1 - d) - vc) < 1e-12 and abs(5 + d / (1 - d) - vd) < 1e-12
# the deviation stream converges to 1 - 3 delta/(1 - delta)  (figure L05-deviation-stream)
assert abs(pv([1] + [-3] * 4000, 0.5) - (1 - 3 * 0.5 / 0.5)) < 1e-9
```

## 5 · The general threshold and its comparative statics → [[L05-05-critical-discount-factor]]

```python
T_, R_, P_, S_, d_ = sp.symbols("T R P S delta", real=True)
vd, vc, vs = sp.symbols("v_d v_c v_star", positive=True)
# (10.5): solve v_c/(1-d) >= v_d + d v*/(1-d) for the boundary delta
boundary = sp.solve(sp.Eq(vc / (1 - d_), vd + d_ * vs / (1 - d_)), d_)[0]
assert sp.simplify(boundary - (vd - vc) / (vd - vs)) == 0

ds = (T_ - R_) / (T_ - P_)
signs = {x: sp.simplify(sp.diff(ds, x)) for x in (T_, R_, P_, S_)}
assert sp.simplify(signs[T_] - (R_ - P_) / (T_ - P_) ** 2) == 0     # > 0 when R > P
assert sp.simplify(signs[R_] + 1 / (T_ - P_)) == 0                  # < 0
assert sp.simplify(signs[P_] - (T_ - R_) / (T_ - P_) ** 2) == 0     # > 0 when T > R
assert signs[S_] == 0                                               # the sucker payoff is irrelevant

def threshold_many(players):
    """Gibbons App. 2.3.B: delta >= max_i (d_i - x_i)/(d_i - e_i), each < 1 when d_i >= x_i > e_i."""
    vals = [(d - x) / (d - e) for d, x, e in players]
    assert all(v < 1 for v in vals)
    return max(vals)

assert threshold_many([(5, 4, 1), (6, 5, 4)]) == 0.5
g, l = 5 - 4, 4 - 1
assert abs(1 / (1 + l / g) - 0.25) < 1e-12        # r <= l/g = 3 is the interest-rate reading
```

## 6 · The folk theorem → [[L05-06-folk-theorem]]

```python
def alternating(T, R, P, S, delta):
    """(F,m),(M,f),... : averages (T + dS)/(1+d), (S + dT)/(1+d) and the three checks (pp. 212-214)."""
    v1, v2 = (T + delta * S) / (1 + delta), (S + delta * T) / (1 + delta)
    good = v1 >= (1 - delta) * R + delta * P - 1e-12      # deviate to M in one's good period
    bad = v2 >= P - 1e-12                                 # deviate to F in one's bad period
    return v1, v2, good and bad

v1, v2, ok = alternating(5, 4, 1, -1, 0.9)
assert ok and abs(v1 - 2.158) < 5e-4 and abs(v2 - 1.842) < 5e-4           # Remark, p. 214
assert alternating(5, 4, 1, -1, 0.5)[2] and not alternating(5, 4, 1, -1, 0.49)[2]
assert all(alternating(5, 4, 1, -1, d)[0] >= (1 - d) * 4 + d for d in np.linspace(0.01, 0.99, 99))
assert abs(alternating(5, 4, 1, -1, 1 - 1e-9)[0] - 2) < 1e-8               # -> (2, 2)
# series check of the closed form
assert abs(average([5, -1] * 3000, 0.9) - (5 - 0.9) / 1.9) < 1e-9

# Remark's adjustments: book = Delta * d^(t-1)/(1+d); a one-off change = (1-d) * d^(t-1) * Delta
book = lambda D, t, d=0.9: D * d ** (t - 1) / (1 + d)
assert [round(book(4, 26), 3), round(book(2, 26), 3), round(book(1, 36), 3), round(book(5, 36), 3)] == \
       [0.151, 0.076, 0.013, 0.066]
every_second = lambda D, t, d=0.9: (1 - d) * D * sum(d ** (t - 1 + 2 * j) for j in range(5000))
assert abs(book(4, 26) - every_second(4, 26)) < 1e-12
assert round((1 - 0.9) * 0.9 ** 25 * 4, 3) == 0.029

def in_hull(pt, V):
    """Point in the convex hull of a convex polygon V listed counter-clockwise (cross products)."""
    return all((b[0] - a[0]) * (pt[1] - a[1]) - (b[1] - a[1]) * (pt[0] - a[0]) >= -1e-12
               for a, b in zip(V, V[1:] + V[:1]))

HULL = [(1, 1), (5, -1), (4, 4), (-1, 5)]            # counter-clockwise, Figure 10.4
assert in_hull((2, 2), HULL) and in_hull((4.4, 2), HULL) and not in_hull((4.5, 4.5), HULL)
assert np.allclose(0.6 * np.array([4, 4]) + 0.4 * np.array([5, -1]), [4.4, 2])   # Def. 10.6
assert abs(5 - (1 + 1) / 5 - 4.6) < 1e-12              # IR corner (1, 4.6)
print("L05 python checks pass")
```

## 7 · The companions' own check

`companions/check_companions.py` runs each page's model under Node at the default, low-end,
high-end and preset vectors, compares every read-out with an independent Python implementation,
sweeps every control, and syntax-checks the page. Run: `python Notas/L05/companions/check_companions.py`.

---

## Links

- Figures script (same `pure_ne`, `coop_rounds`): `figures/make_figures.py`.
- Notes served: [[L05-01-finite-repetition-unraveling]] · [[L05-02-two-stage-carrot-stick]] · [[L05-03-discounting-histories-strategies]] · [[L05-04-grim-trigger-spe]] · [[L05-05-critical-discount-factor]] · [[L05-06-folk-theorem]].
- Earlier-lecture code: `Listas/lista-lecture-01-check.py` (dominance, IESDS).
