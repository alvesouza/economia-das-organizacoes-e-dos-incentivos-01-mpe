---
tags: [notes, lecture-04, python, reference-implementation]
date: 2026-10-16
status: estimated
source: "Tadelis (2013) Ch. 9 (pp. 175–189) and Ch. 11 (pp. 220–237); Gibbons (1992) §2.1.D, §2.2 (pp. 68–82); M&R (1992) pp. 140–142; reuses Aula/notes-aulas-01-02/check_part2.py::proposer_share"
---

# Lecture 4 · Computation in Python

> Every routine the unit needs, each followed by `assert` checks against the books' own numbers.
> Python only (numpy). The code blocks run top to bottom as one script; paste them into one file or
> a notebook. **Reuse:** the finite-horizon solver is `proposer_share` from
> `Aula/notes-aulas-01-02/check_part2.py`, loaded with `ast` so that its module-level checks
> (about 10 s, sympy and a Monte Carlo) do not run on import; `Listas/lista-aulas-01-02-check.py`
> has the symbolic twin `finite_share`. The companions' independent check is
> `companions/check_companions.py`.

Map: [[L04-00-map]] · Formulas: [[L04-10-formulas]]

---

## 0 · Setup and the reused solver

```python
import ast
import itertools
import math
from pathlib import Path

import numpy as np

ROOT = Path.cwd()          # run from the repository root
while not (ROOT / "Aula").exists() and ROOT != ROOT.parent:
    ROOT = ROOT.parent


def load_function(path, name):
    """Load top-level function `name` from `path` without executing the rest of the module."""
    tree = ast.parse(Path(path).read_text(encoding="utf-8"))
    node = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == name)
    ns = {}
    exec(compile(ast.Module([node], []), str(path), "exec"), ns)
    return ns[name]


# proposer_share(T, d_first, d_second): share of the round-1 proposer, T rounds, pie 1.
proposer_share = load_function(ROOT / "Aula/notes-aulas-01-02/check_part2.py", "proposer_share")
```

---

## 1 · Multistage games: the Prisoner-Revenge Game → [[L04-02-carrot-and-stick]]

Brute force over every pure strategy profile, using the one-stage deviation principle
([[L04-03-one-stage-deviation]]): a profile is an SPE iff stage 2 is a Nash equilibrium after each of
the four histories **and** no player gains by changing only his stage-1 action.

```python
PD = {("M", "m"): (4, 4), ("M", "f"): (-1, 5), ("F", "m"): (5, -1), ("F", "f"): (1, 1)}   # p. 176
REV = {("L", "l"): (0, 0), ("L", "g"): (-4, -1), ("G", "l"): (-1, -4), ("G", "g"): (-3, -3)}  # p. 177
HIST = list(PD)                                                 # Mm, Mf, Fm, Ff


def stage_nash(game):
    """Pure Nash equilibria of a 2x2 bimatrix given as {(a1, a2): (u1, u2)}."""
    A1 = sorted({a for a, _ in game}); A2 = sorted({b for _, b in game})
    return [(a, b) for a in A1 for b in A2
            if game[(a, b)][0] >= max(game[(x, b)][0] for x in A1)
            and game[(a, b)][1] >= max(game[(a, y)][1] for y in A2)]


def pure_spe_paths(delta):
    """Stage-1 outcomes reachable in some pure SPE, with stage 2 a pure Revenge NE per history."""
    ne2 = stage_nash(REV)
    paths = set()
    for plan in itertools.product(ne2, repeat=4):               # continuation NE for each history
        cont = dict(zip(HIST, plan))
        v = {h: tuple(PD[h][i] + delta * REV[cont[h]][i] for i in (0, 1)) for h in HIST}
        paths.update(stage_nash(v))                              # stage-1 one-stage deviations
    return paths


def two_stage_threshold(gain, carrot, stick):
    """delta* = gain / (carrot - stick); None when the stick is not a punishment."""
    return gain / (carrot - stick) if carrot > stick else None


assert stage_nash(PD) == [("F", "f")]
assert stage_nash(REV) == [("G", "g"), ("L", "l")]
assert 2 ** 5 == 32 and 32 * 32 == 1024                          # strategies, p. 179
assert two_stage_threshold(5 - 4, 0, -3) == 1 / 3                 # (M,m), p. 183
assert two_stage_threshold(1 - (-1), 0, -3) == 2 / 3              # (F,m), p. 184
assert pure_spe_paths(0.2) == {("F", "f")}
assert pure_spe_paths(0.5) == {("M", "m"), ("F", "f")}
assert pure_spe_paths(0.7) == set(HIST)                          # all four once delta >= 2/3
assert ("M", "m") in pure_spe_paths(1 / 3) and ("F", "m") in pure_spe_paths(2 / 3)
# the mixed Revenge equilibrium: q = 1/2 makes L and G indifferent, value -2 (p. 177)
q = 0.5
assert 0 * q - 4 * (1 - q) == -1 * q - 3 * (1 - q) == -2
```

---

## 2 · Two-stage applications → [[L04-04-two-stage-applications]]

```python
def bank_run_reduced(D, r, R):
    """Date-1 game after substituting date 2's unique NE (R, R); Gibbons Fig. 2.2.1, p. 75."""
    assert D > r > D / 2 and R > D
    return {("w", "w"): (r, r), ("w", "d"): (D, 2 * r - D),
            ("d", "w"): (2 * r - D, D), ("d", "d"): (R, R)}


def tariff_welfare(ti, tj, A=1.0):
    """W_i*(t_i, t_j), Gibbons p. 78, with A = a - c."""
    return (2 * A - ti) ** 2 / 18 + (A + ti) ** 2 / 9 + (A - 2 * tj) ** 2 / 9 + ti * (A - 2 * ti) / 3


def tournament_prize(sigma, gprime_at_opt=1.0):
    """Optimal spread w_H - w_L solving (w_H - w_L) * int f^2 = g'(e*) = 1, normal noise."""
    eps = np.linspace(-12 * sigma, 12 * sigma, 200_001)
    f = np.exp(-eps ** 2 / (2 * sigma ** 2)) / (sigma * math.sqrt(2 * math.pi))
    int_f2 = np.sum(f ** 2) * (eps[1] - eps[0])
    return gprime_at_opt / int_f2, int_f2


assert stage_nash(bank_run_reduced(100, 75, 150)) == [("d", "d"), ("w", "w")]   # run and no run
grid = np.linspace(0, 1, 100_001)
for tj in (0.0, 1 / 3, 0.5):                                     # dominant tariff (a - c)/3
    assert abs(grid[np.argmax(tariff_welfare(grid, tj))] - 1 / 3) < 1e-4
cells = [round(162 * tariff_welfare(a, b)) for a, b in [(0, 0), (1/3, 0), (0, 1/3), (1/3, 1/3)]]
assert cells == [72, 81, 56, 65]                                 # a Prisoners' Dilemma
assert abs((1 + 1/3) / 3 - 4 / 9) < 1e-12 and abs((1 - 2/3) / 3 - 1 / 9) < 1e-12   # h*, e*
prize, int_f2 = tournament_prize(1.0)
assert abs(int_f2 - 1 / (2 * math.sqrt(math.pi))) < 1e-9          # int f^2 = 1/(2 sigma sqrt(pi))
assert abs(prize - 2 * math.sqrt(math.pi)) < 1e-6                 # about 3.545
```

---

## 3 · Alternating offers → [[L04-05-ultimatum-game]], [[L04-06-finite-alternating-offers]], [[L04-07-rubinstein-infinite-horizon]]

```python
def finite_share_closed(T, d):
    """(11.1) and its even-T twin: x_1 = (1 - (-d)^T) / (1 + d)."""
    return (1 - (-d) ** T) / (1 + d)


def rubinstein(d1, d2):
    """Infinite-horizon share of the first proposer; None if delay is free for both."""
    return (1 - d2) / (1 - d1 * d2) if d1 * d2 < 1 else None


def ultimatum_best_offer(grid_step):
    """Proposer's best share on a grid when the responder accepts any positive share (MWG fn. 16)."""
    return 1 - grid_step


assert proposer_share(1, 0.6, 0.6) == 1                          # Prop. 11.2
assert ultimatum_best_offer(0.01) == 0.99                         # one penny to the responder
for d in (0.0, 0.3, 0.6, 0.9, 1.0):
    for T in range(1, 25):
        assert abs(proposer_share(T, d, d) - finite_share_closed(T, d)) < 1e-12
assert np.allclose([proposer_share(T, .6, .6) for T in range(1, 7)],
                   [1, .4, .76, .544, .6736, .59584])
assert proposer_share(2, 0.6, 0.6) == 1 - 0.6                    # two rounds, p. 225
assert proposer_share(39, 1, 1) == 1 and proposer_share(40, 1, 1) == 0   # delta = 1: last word wins
assert abs(rubinstein(.6, .6) - 0.625) < 1e-12                   # (11.4)-(11.5)
assert abs(proposer_share(401, .6, .6) - rubinstein(.6, .6)) < 1e-12   # (11.2)
# Gibbons p. 71: the fixed point of f(s) = 1 - d + d^2 s
d, s = 0.6, 0.0
for _ in range(200):
    s = 1 - d + d * d * s
assert abs(s - 1 / (1 + d)) < 1e-12
# different patience: three rounds and infinite horizon (check_part2.py's numbers)
assert abs(proposer_share(3, .9, .7) - 0.93) < 1e-12
assert abs(rubinstein(.9, .7) - 0.3 / 0.37) < 1e-12
h = 1e-6                                                          # signs of the derivatives
assert rubinstein(.9 + h, .7) > rubinstein(.9, .7) > rubinstein(.9, .7 + h)
# frequent offers: delta_i = exp(-r_i Delta) -> share r2 / (r1 + r2)
r1, r2 = 0.05, 0.10
assert abs(rubinstein(math.exp(-r1 * 1e-6), math.exp(-r2 * 1e-6)) - r2 / (r1 + r2)) < 1e-5
assert rubinstein(1, 1) is None
```

---

## 4 · Legislative bargaining → [[L04-08-legislative-bargaining]]

```python
def closed_rule_k(N, d):
    """(11.8): proposer's share under the closed rule."""
    return 1 - d * (N - 1) / (2 * N)


def open_guaranteed(d):
    """(11.9)."""
    return 1 / (1 + 2 * d)


def open_risky(d):
    """Solve (11.10)-(11.12) as a linear system in (v_k, v_0, k); compare with (11.13)."""
    M = np.array([[1, -d / 2, -0.5],     # v_k - (d/2) v_0 - k/2 = 0
                  [-d / 2, 1, 0],        # v_0 - (d/2) v_k = 0
                  [d, 0, 1]])            # k + d v_k = 1
    v_k, v_0, k = np.linalg.solve(M, [0, 0, 1])
    return v_k, k


assert abs(closed_rule_k(3, 0.9) - 0.7) < 1e-12 and abs(closed_rule_k(5, 0.9) - 0.64) < 1e-12
N, d = 3, 0.9                                                     # v = 1/N solves (11.6)-(11.7)
v = 1 / N
k = 1 - (N - 1) / 2 * d * v
assert abs(v - (k / N + (N - 1) / (2 * N) * d * v)) < 1e-12
for d in np.linspace(0.01, 0.99, 99):
    v_k, k = open_risky(d)
    assert abs(v_k - 2 / (4 + 2 * d - d * d)) < 1e-12 and abs(k - (4 - d * d) / (4 + 2 * d - d * d)) < 1e-12
    assert closed_rule_k(3, d) > max(open_guaranteed(d), v_k)    # footnotes 7-8
lo, hi = 0.0, 1.0                                                 # where risky overtakes guaranteed
for _ in range(60):
    mid = (lo + hi) / 2
    lo, hi = (mid, hi) if open_risky(mid)[0] < open_guaranteed(mid) else (lo, mid)
assert abs(lo - (math.sqrt(3) - 1)) < 1e-12
```

---

## 5 · Bargaining over a sale → [[L04-09-bargaining-private-information]]

```python
def ic_price_bounds(pS0=0.8, pB3=0.8):
    """M&R pp. 141-142: price p (seller 0, buyer 3) needed for truthful reports."""
    seller_min = (pB3 * 2 - (1 - pB3) * 1) / pB3            # (1-pB3)*1 + pB3*p >= pB3*2
    buyer_max = 3 - ((pS0 * (3 - 1)) - (1 - pS0) * (3 - 2)) / pS0   # (1-pS0)(1) + pS0(3-p) >= pS0*2
    return seller_min, buyer_max


lo_p, hi_p = ic_price_bounds()
assert abs(lo_p - 1.75) < 1e-12 and abs(hi_p - 1.25) < 1e-12 and lo_p > hi_p   # no price works
assert abs(0.2 * 0.2 - 0.04) < 1e-15                              # no-trade efficient 4% of the time
print("Lecture 4 reference implementation: all checks pass")
```

---

## Links

- Figures use the same expressions: `figures/make_figures.py` (run
  `python Notas/L04/figures/make_figures.py`).
- Companion checks: `python Notas/L04/companions/check_companions.py` (node required).
- Earlier code: `Aula/notes-aulas-01-02/check_part2.py`, `Listas/lista-aulas-01-02-check.py`.
