---
tags: [notes, lecture-06, repeated-games, collusion, efficiency-wages, python]
date: 2026-10-16
status: estimated
source: "Tadelis (2013) §10.3–10.5, pp. 196–208; Gibbons (1992) §2.3.C–D, pp. 102–111; Cabral (2017) §9.1–9.3, pp. 218–230; Milgrom & Roberts (1992) Ch. 8, pp. 250–263; MWG §12.D, pp. 400–405"
---

# Lecture 6 · Computation in Python

> Every routine the lecture needs, each with `assert` self-checks against the books' own
> numbers. numpy only; the blocks run top to bottom in one session (they share names).
> Prev: [[L06-10-pitfalls]] · Map: [[L06-00-map]] · Formulas: [[L06-09-formulas]]

**Reuse.** The project has no repeated-game code yet (`Listas/*-check.py` and
`Aula/**/check_*.py` cover Lectures 1–2 and the Aula 1–2 notes). The figure script
[`figures/make_figures.py`](figures/make_figures.py) and the companion check
[`companions/check_companions.py`](companions/check_companions.py) re-implement the same
expressions independently on purpose: they are the second path the numbers are verified on.

---

## 1 · The one inequality → [[L06-01-recap-grim-trigger]]

```python
import numpy as np

def discounted(stream, delta):
    """Present value of a finite payoff stream (a long horizon stands in for infinity)."""
    stream = np.asarray(stream, float)
    return float(np.sum(stream * delta ** np.arange(len(stream))))

def grim_cutoff(v_coop, v_dev, v_pun):
    """delta* = (v^d - v^c) / (v^d - v^p): Tadelis (10.5), p. 202.

    v_coop: per-period payoff on the cooperative path; v_dev: best one-period deviation
    payoff; v_pun: per-period payoff in the punishment (stage Nash) forever after.
    Requires v_dev > v_coop > v_pun; returns the smallest delta that deters the deviation.
    """
    assert v_dev > v_coop > v_pun, "not a temptation/punishment configuration"
    return (v_dev - v_coop) / (v_dev - v_pun)

# Tadelis's repeated Prisoner's Dilemma (p. 197): mum 4, fink against mum 5, fink-fink 1.
assert grim_cutoff(4, 5, 1) == 0.25                               # (10.3), p. 200
for d in (0.24, 0.25, 0.26):                                       # one-shot deviation at t = 0
    T = 4000
    conform = discounted([4] * T, d)
    deviate = discounted([5] + [1] * (T - 1), d)
    assert (conform >= deviate - 1e-9) == (d >= 0.25)
```

---

## 2 · Tadelis's tacit collusion, with the corrected firm-2 numbers → [[L06-02-cournot-collusion]]

```python
A, C = 100.0, 10.0                    # p = 100 - q, c_i(q_i) = 10 q_i  (p. 201)

def profit(qi, qj, a=A, c=C):
    return (a - qi - qj - c) * qi

def br(qj, a=A, c=C):
    return (a - c - qj) / 2           # (10.4), p. 202

assert profit(30, 30) == 900 and profit(22.5, 22.5) == 1012.5                  # p. 201
assert profit(22, 23) == 990 and profit(23, 22) == 1035                        # p. 201
assert br(23) == 33.5 and br(22) == 34                                          # p. 202
assert profit(33.5, 23) == 1122.25                                              # firm 1, p. 202
assert profit(34, 22) == 1156          # firm 2 deviates against q1 = 22; the book prints 1122
assert (100 - 23 - 34) * 34 - 10 * 34 == 1122   # ...which is what using q_j = 23 gives
d1 = grim_cutoff(990, 1122.25, 900)
d2 = grim_cutoff(1035, 1156, 900)
assert round(d1, 3) == 0.595                     # p. 202, unchanged
assert abs(d2 - 121 / 256) < 1e-12               # 0.473, not the printed 0.392
assert round(grim_cutoff(1035, 1122, 900), 3) == 0.392
assert d1 > d2                                   # the book's conclusion survives the fix
assert A - 45 == 55                              # collusive price is 55 (p. 203 prints 45)
```

---

## 3 · The symmetric $n$-firm Cournot cartel → [[L06-02-cournot-collusion]]

```python
def cournot_cartel(a, c, n):
    """Per-firm profits: collusive share pi_m/n, best deviation pi_d, Cournot pi_N.

    Linear demand P = a - Q, constant marginal cost c < a, n identical firms.
    """
    s = a - c
    pi_share = s ** 2 / (4 * n)
    q_dev = s * (n + 1) / (4 * n)                  # best response to (n-1) * s/(2n)
    pi_dev = q_dev ** 2
    pi_N = s ** 2 / (n + 1) ** 2
    return pi_share, pi_dev, pi_N

def cournot_threshold(n):
    """Closed form of grim_cutoff for the n-firm cartel: (n+1)^2 / (n^2 + 6n + 1)."""
    return (n + 1) ** 2 / (n ** 2 + 6 * n + 1)

def best_sustainable_q(a, c, n, delta):
    """Lowest symmetric per-firm output that grim trigger (Nash reversion) sustains.

    Condition: (a - nq - c) q >= (1 - delta) pi_d(q) + delta pi_N, pi_d(q) = (a - c - (n-1) q)^2 / 4.
    The condition is a concave quadratic in q that vanishes at the Cournot output, so the
    other root is (product of roots) / q_N. Returns max(q_m / n, that root).
    """
    s = a - c
    c2 = -n - (1 - delta) * (n - 1) ** 2 / 4
    c0 = -(1 - delta) * s ** 2 / 4 - delta * s ** 2 / (n + 1) ** 2
    qN = s / (n + 1)
    return max(s / (2 * n), (c0 / c2) / qN)

# Gibbons p. 103: n = 2 gives delta >= 9/17.
sh, dv, nash = cournot_cartel(1, 0, 2)
assert (sh, dv, nash) == (1 / 8, 9 / 64, 1 / 9)
assert abs(grim_cutoff(sh, dv, nash) - 9 / 17) < 1e-12
for n in range(2, 30):
    assert abs(grim_cutoff(*cournot_cartel(100, 10, n)) - cournot_threshold(n)) < 1e-12
# Gibbons p. 104: q* = (9 - 5 delta) / (3 (9 - delta)) (a - c) for delta < 9/17.
for d in np.linspace(0, 9 / 17, 50):
    assert abs(best_sustainable_q(1, 0, 2, d) - (9 - 5 * d) / (3 * (9 - d))) < 1e-12
assert best_sustainable_q(1, 0, 2, 0.0) == 1 / 3 and best_sustainable_q(1, 0, 2, 0.6) == 0.25
# brute force: q* is the smallest q on a fine grid that satisfies the condition (n = 4)
a, c, n, d = 100, 10, 4, 0.4
q = np.linspace(90 / 8, 90 / 5, 200001)
ok = (a - n * q - c) * q >= (1 - d) * (a - c - (n - 1) * q) ** 2 / 4 + d * (90 / 5) ** 2 - 1e-9
assert abs(q[ok].min() - best_sustainable_q(a, c, n, d)) < 1e-3
# Tadelis's numbers at Gibbons's delta = 1/2: q* = 22.94 per firm, price 54.12
assert round(best_sustainable_q(100, 10, 2, 0.5), 2) == 22.94
```

---

## 4 · Bertrand, the number of firms, and Cabral's discount factor → [[L06-03-bertrand-market-structure]]

```python
def bertrand_threshold(n):
    """Nash reversion sustains any p in (c, p_m] iff delta >= 1 - 1/n (MWG Prop. 12.D.1 for n = 2)."""
    return 1 - 1 / n

def cabral_delta(r, f=1, h=0.0, g=0.0):
    """Cabral (9.5), p. 220: delta = (1 + g)(1 - h) / (1 + r/f)."""
    return (1 + g) * (1 - h) / (1 + r / f)

assert bertrand_threshold(2) == 0.5                                 # Cabral (9.4), p. 219
# collusion holds iff share/(1 - delta) >= whole monopoly profit
for n in (2, 3, 10):
    for d in (bertrand_threshold(n) - 1e-6, bertrand_threshold(n) + 1e-6):
        assert ((1 / n) / (1 - d) >= 1) == (d >= bertrand_threshold(n))
# Cabral p. 221: 10% a year, monthly prices -> "dozens" of firms can collude
d = cabral_delta(0.10, f=12)
assert round(d, 4) == 0.9917 and int(np.floor(1 / (1 - d) + 1e-9)) == 121
assert cabral_delta(0.10, f=1) < cabral_delta(0.10, f=12)          # delta rises with f
assert cabral_delta(0.10, 12, h=0.05) < d < cabral_delta(0.10, 12, g=0.02)
# Cabral p. 229: two identical markets -> the same threshold, 1/2
d = 0.5
assert np.isclose(2 * 0.5 / (1 - d), 2 * 1.0)
```

---

## 5 · Abreu's carrot and stick → [[L06-04-punishments-price-wars]]

```python
def two_phase_band(delta):
    """Punishment outputs x/(a - c) that satisfy Gibbons (2.3.3) and (2.3.4) (pp. 105-106).

    (2.3.3): delta (1/8 - pi(x)) >= 9/64 - 1/8      (collusive phase)
    (2.3.4): delta (1/8 - pi(x)) >= pi_dp(x) - pi(x) (punishment phase)
    with pi(x) = (1 - 2x) x and pi_dp(x) = (1 - x)^2 / 4. Grid search on [0, 1/2].
    """
    x = np.linspace(0, 0.5, 500001)
    pix = (1 - 2 * x) * x
    ok = (delta * (1 / 8 - pix) >= 1 / 64 - 1e-12) & \
         (delta * (1 / 8 - pix) >= (1 - x) ** 2 / 4 - pix - 1e-12)
    return x[ok].min(), x[ok].max()

lo, hi = two_phase_band(0.5)
assert abs(lo - 3 / 8) < 1e-5 and abs(hi - 1 / 2) < 1e-5            # Gibbons p. 106
assert 0.5 < 9 / 17          # the carrot and stick reaches the monopoly outcome grim trigger cannot
```

---

## 6 · Reputation: trust game, M&R's multiplier, the guarantor → [[L06-05-reputation-trust]], [[L06-06-institutions-reputation]]

```python
def trust_threshold(V, G):
    """Honour trust iff V/(1 - delta) >= V + G, i.e. delta >= G / (V + G)."""
    return G / (V + G)

def mr_multiplier(r, t=1):
    """M&R footnote 11, p. 263: N = 1/[(1 + r)^t - 1] + 1 = 1/(1 - delta), delta = (1 + r)^-t."""
    return 1 / ((1 + r) ** t - 1) + 1

assert trust_threshold(1, 1) == 0.5            # Tadelis Fig. 10.1 payoffs: delta >= 1/2, p. 205
r = 0.05
assert np.isclose(mr_multiplier(r), 1 / (1 - 1 / (1 + r)))
# M&R's honour condition N V >= V + G is the same inequality as delta >= G/(V + G)
for V, G, d in [(1, 1, 0.49), (1, 1, 0.51), (3, 1, 0.24), (3, 1, 0.26)]:
    assert (V / (1 - d) >= V + G) == (d >= trust_threshold(V, G))
# Law merchant (Tadelis p. 207): fee 0.1 forever vs keeping the bond 2 once
assert grim_cutoff(0.1, 2.0, 0.0) == 0.95
```

---

## 7 · Efficiency wages → [[L06-07-efficiency-wages]]

```python
def w_star(w0, e, p, delta):
    """Gibbons (2.3.5), p. 110: lowest wage at which effort beats shirking.

    w0: self-employment wage; e: disutility of effort; p: probability that output is high
    when the worker shirks (so 1 - p is the detection probability); delta in (0, 1).
    """
    return w0 + e + (1 - delta) * e / (delta * (1 - p))

def worker_values(w, w0, e, p, delta):
    """Present values of effort and of shirking at wage w (Gibbons pp. 109-110)."""
    Ve = (w - e) / (1 - delta)
    Vs = ((1 - delta) * w + delta * (1 - p) * w0) / ((1 - delta * p) * (1 - delta))
    return Ve, Vs

def firm_delta_min(y, w0, e, p):
    """Smallest delta with y >= w*: (2.3.5) and (2.3.7) together (Gibbons p. 110)."""
    surplus = y - e - w0
    return e / (e + (1 - p) * surplus) if surplus > 0 else None

def mr_efficiency_wage(w_bar, g, P, N):
    """M&R p. 252: smallest wage deterring cheating, w_bar + g / (N P)."""
    return w_bar + g / (N * P)

# the two values coincide exactly at w*
for args in [(39, 1, 0.95, 0.5), (10, 2, 0.3, 0.8), (0, 5, 0.0, 0.2)]:
    w = w_star(*args)
    Ve, Vs = worker_values(w, *args)
    assert np.isclose(Ve, Vs)
    assert worker_values(w + 0.01, *args)[0] > worker_values(w + 0.01, *args)[1]
# p = 0 reproduces (2.3.6), p. 110: w* = w0 + (1 + (1 - delta)/delta) e
assert np.isclose(w_star(10, 2, 0.0, 0.5), 10 + (1 + 1) * 2)     # w0 + (1 + (1-d)/d) e
# M&R p. 251: rent 10, detection .05, gain 1 ($000): expected loss .5 < 1 -> cheat at N = 1
assert 0.05 * (50 - 40) * 1 < 1
assert mr_efficiency_wage(40, 1, 0.05, 1) == 60 and mr_efficiency_wage(40, 1, 0.05, 2) == 50
# mapping: g = e, P = 1 - p, N = delta / (1 - delta), w_bar = w0 + e
for d in (0.5, 2 / 3, 0.9):
    assert np.isclose(w_star(39, 1, 0.95, d), mr_efficiency_wage(40, 1, 0.05, d / (1 - d)))
# the firm's side at the companion default y = 41
dmin = firm_delta_min(41, 39, 1, 0.95)
assert np.isclose(dmin, 1 / 1.05) and np.isclose(w_star(39, 1, 0.95, dmin), 41)
```

---

## 8 · Run it

Copy the blocks into one file or a notebook cell in order; every `assert` passes. The
figures (`python Notas/L06/figures/make_figures.py`) and the companion check
(`python Notas/L06/companions/check_companions.py`) are independent re-implementations of
§2–§7.

## Links

- Map [[L06-00-map]] · formulas [[L06-09-formulas]] · pitfalls [[L06-10-pitfalls]].
- The repeated-game basics these routines build on: [[../L05/L05-00-map|Lecture 5]].
- Rules: [[../../rules/game-theory|rules/game-theory]] (item 4: patience and observable
  deviations), [[../../rules/06_racionalidade_limitada_contratos|rules/06]].
