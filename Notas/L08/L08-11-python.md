---
tags: [notes, lecture-08, python, pbe, signaling, self-checks]
date: 2026-10-16
status: estimated
source: "Tadelis (2013) Ch. 15–16 (pp. 303–338): every number below is the book's; Gibbons (1992) §4.2.A Fig. 4.2.2 (p. 189) and §4.4 Fig. 4.4.3 (p. 238); Milgrom & Roberts (1992) pp. 155–156"
---

# Lecture 8 · Computation in Python

> Every routine the lecture needs — Bayes' rule at an information set, the Bayesian normal form,
> an exhaustive pure-PBE solver for two-type signaling games, the intuitive-criterion test, the
> Spence intervals, and the limit-pricing bounds — each with `assert` self-checks against the
> books' own numbers. Run the blocks in order (they share names); the last line prints
> `L08 reference implementation: all checks pass.` Python + numpy only.
>
> Prev: [[L08-10-pitfalls]] · Map: [[L08-00-map]] · Formulas: [[L08-09-formulas]]

**Reuse.** Nothing in `Listas/*-check.py` or `Aula/**/check_*.py` covers Bayesian updating or
signaling (those files serve Lectures 1–2), so the routines are new. The companions'
independent checks live in `companions/check_companions.py` (run:
`python Notas/L08/companions/check_companions.py`).

**Two things the code found in the book** (both noted where they occur): the matrix cell
$(DU,BB)$ on p. 322 should read 5.5, not 4.5; the entrant's pooled-entry profit on p. 331 is
$7/36$, not $7/18$. Neither changes a conclusion.

---

## 1 · Bayes' rule at an information set → [[L08-02-beliefs-and-pbe]] §3

Requirement 15.2 as a function. `None` is the off-path case of Requirement 15.3: no type sends the message, so Bayes' rule is silent.

```python
from fractions import Fraction as Fr
from itertools import product


def posterior(prior, send):
    """Bayes' rule at the information set that follows one message.

    prior: {type: Pr(type)}; send: {type: Pr(type sends this message)}.
    Returns {type: posterior} or None when no type sends the message (off the path:
    Requirement 15.3, any belief is allowed).
    """
    den = sum(prior[t] * send[t] for t in prior)
    return None if den == 0 else {t: prior[t] * send[t] / den for t in prior}


p = Fr(1, 3)                                         # any prior works
assert posterior({"C": p, "W": 1 - p}, {"C": 1, "W": 0})["C"] == 1          # EO: entry => competitive
assert posterior({"C": p, "W": 1 - p}, {"C": 0, "W": 0}) is None            # OO: entry is off-path
sC, sW = Fr(1, 2), Fr(1, 4)                                                 # a behavioural mix
assert posterior({"C": p, "W": 1 - p}, {"C": sC, "W": sW})["C"] == p * sC / (p * sC + (1 - p) * sW)
```

---

## 2 · The entry game: Bayesian normal form, BNE, sequential rationality → [[L08-01-subgame-perfection-fails]]

The matrix printed on p. 306, the two pure BNE, and the one-line reason $(OO,F)$ is not a PBE: $A$ beats $F$ at every belief.

```python
# Tadelis Fig. 15.2 (p. 305): payoffs (entrant, incumbent) after (type, action[, response])
ENTRY = {("C", "O"): (0, 2), ("W", "O"): (0, 2),
         ("C", "E", "F"): (-1, -1), ("C", "E", "A"): (1, 1),
         ("W", "E", "F"): (-2, 0), ("W", "E", "A"): (-1, 1)}


def entry_payoffs(s1, s2, p):
    """Expected payoffs of the Bayesian normal form; s1 = (action of C, action of W), s2 in {F, A}."""
    v = [Fr(0), Fr(0)]
    for t, a, pr in [("C", s1[0], p), ("W", s1[1], 1 - p)]:
        out = ENTRY[(t, a)] if a == "O" else ENTRY[(t, a, s2)]
        v = [v[0] + pr * out[0], v[1] + pr * out[1]]
    return tuple(v)


half = Fr(1, 2)
S1 = [("O", "O"), ("O", "E"), ("E", "O"), ("E", "E")]
# the matrix printed on p. 306 at p = 1/2
assert entry_payoffs(("O", "E"), "F", half) == (-1, 1) and entry_payoffs(("O", "E"), "A", half) == (-half, Fr(3, 2))
assert entry_payoffs(("E", "O"), "F", half) == (-half, half) and entry_payoffs(("E", "O"), "A", half) == (half, Fr(3, 2))
assert entry_payoffs(("E", "E"), "F", half) == (Fr(-3, 2), -half) and entry_payoffs(("E", "E"), "A", half) == (0, 1)


def pure_nash(rows, cols, pay):
    """All pure Nash equilibria of a two-player matrix game given pay(r, c) -> (v1, v2)."""
    return [(r, c) for r in rows for c in cols
            if all(pay(r, c)[0] >= pay(r2, c)[0] for r2 in rows)
            and all(pay(r, c)[1] >= pay(r, c2)[1] for c2 in cols)]


bne = pure_nash(S1, ["F", "A"], lambda r, c: entry_payoffs(r, c, half))
assert sorted(bne) == sorted([(("O", "O"), "F"), (("E", "O"), "A")])        # p. 306
# sequential rationality after entry: A beats F at every belief mu = Pr(C | E)  (p. 310)
assert all(mu * 1 + (1 - mu) * 1 > mu * -1 + (1 - mu) * 0 for mu in [Fr(k, 100) for k in range(101)])
```

---

## 3 · An exhaustive pure-PBE solver for two-type signaling games → [[L08-04-signaling-games]] §3

For every Sender strategy and Receiver strategy: Bayes on used messages, an interval of supporting beliefs on unused ones, then the Sender's incentive constraints. Tested on Gibbons's Fig. 4.2.2, where it must find exactly the two PBE of pp. 188–190.

```python
def br_interval(u2, m, a, acts, t1, t2):
    """Beliefs mu = Pr(t1 | m) in [0, 1] at which action a is a (weak) best response to message m.

    u2(t, m, a) is the receiver's payoff. Each comparison with another action is linear in mu,
    so the set is an interval; returns (lo, hi) or None if empty.
    """
    lo, hi = Fr(0), Fr(1)
    for b in acts:
        if b == a:
            continue
        # mu*d1 + (1-mu)*d2 >= 0, with d = u2(.,m,a) - u2(.,m,b)
        d1 = Fr(u2(t1, m, a) - u2(t1, m, b)); d2 = Fr(u2(t2, m, a) - u2(t2, m, b))
        slope, const = d1 - d2, d2
        if slope == 0:
            if const < 0:
                return None
        elif slope > 0:
            lo = max(lo, -const / slope)
        else:
            hi = min(hi, -const / slope)
    return (lo, hi) if lo <= hi else None


def pure_pbe(types, prior, msgs, acts, u1, u2):
    """Every pure-strategy PBE of a two-type signaling game (Tadelis Def. 15.3; Gibbons p. 188).

    types: (t1, t2); prior: Pr(t1); u1(t, m, a), u2(t, m, a): sender and receiver payoffs.
    Returns a list of (sender {t: m}, receiver {m: a}, beliefs {m: Pr(t1|m) or (lo, hi)}).
    """
    t1, t2 = types
    out = []
    for sm in product(msgs, repeat=2):
        s = dict(zip(types, sm))
        for ra in product(acts, repeat=len(msgs)):
            r = dict(zip(msgs, ra))
            beliefs, ok = {}, True
            for m in msgs:
                post = posterior({t1: prior, t2: 1 - prior}, {t: int(s[t] == m) for t in types})
                iv = br_interval(u2, m, r[m], acts, t1, t2)
                if post is None:                                   # off path: any supporting belief
                    ok = iv is not None
                    beliefs[m] = iv
                else:                                              # on path: Bayes, then optimality
                    mu = post[t1]
                    ok = iv is not None and iv[0] <= mu <= iv[1]
                    beliefs[m] = mu
                if not ok:
                    break
            if ok and all(u1(t, s[t], r[s[t]]) >= max(u1(t, m, r[m]) for m in msgs) for t in types):
                out.append((s, r, beliefs))
    return out


# Gibbons Fig. 4.2.2 (p. 189): (sender, receiver) payoffs; t1, t2 equally likely
G422 = {("t1", "L", "u"): (1, 3), ("t1", "L", "d"): (4, 0), ("t1", "R", "u"): (2, 1), ("t1", "R", "d"): (0, 0),
        ("t2", "L", "u"): (2, 4), ("t2", "L", "d"): (0, 1), ("t2", "R", "u"): (1, 0), ("t2", "R", "d"): (1, 2)}
g = pure_pbe(("t1", "t2"), half, ("L", "R"), ("u", "d"),
             lambda t, m, a: G422[(t, m, a)][0], lambda t, m, a: G422[(t, m, a)][1])
found = {(tuple(s.values()), tuple(r.values())): b for s, r, b in g}
assert set(found) == {(("L", "L"), ("u", "d")), (("R", "L"), ("u", "u"))}       # pp. 188-190
assert found[(("L", "L"), ("u", "d"))]["R"] == (0, Fr(2, 3))                     # q <= 2/3
```

---

## 4 · The MBA game: matrix, BNE and PBE → [[L08-05-mba-game]]

The 16-cell Bayesian normal form at $p=1/4$ (p. 322), its two BNE, and the solver's verdict: $(DU,BM)$ with $\mu_U=0,\ \mu_D=1$; $(UU,BB)$ with $\mu_U=1/4$ and $\mu_D\in[0,3/8]$.

```python
# Tadelis Sec. 16.1 (pp. 319-323): wages and study costs, employer profits
def mba(wM=10, wB=6, cH=2, cL=5):
    """Sender/receiver payoffs of the MBA game; returns (u1, u2)."""
    wage, cost = {"M": wM, "B": wB}, {"H": cH, "L": cL}
    prof = {("H", "M"): 10, ("H", "B"): 5, ("L", "M"): 0, ("L", "B"): 3}
    u1 = lambda t, m, a: wage[a] - (cost[t] if m == "D" else 0)
    u2 = lambda t, m, a: prof[(t, a)]
    return u1, u2


u1, u2 = mba()
quarter = Fr(1, 4)
# the 4x4 Bayesian normal form at p = 1/4 (p. 322)
def nf(s1, s2, p=quarter):
    """s1 = (H's message, L's message); s2 = (response to U, response to D)."""
    resp = {"U": s2[0], "D": s2[1]}
    return (p * u1("H", s1[0], resp[s1[0]]) + (1 - p) * u1("L", s1[1], resp[s1[1]]),
            p * u2("H", s1[0], resp[s1[0]]) + (1 - p) * u2("L", s1[1], resp[s1[1]]))


assert nf("UD", "MB") == (Fr(13, 4), Fr(19, 4))                                  # (3.25, 4.75)
ROWS, COLS = ["UU", "UD", "DU", "DD"], ["MM", "MB", "BM", "BB"]
TABLE = {"UU": [(10, 2.5), (10, 2.5), (6, 3.5), (6, 3.5)], "UD": [(6.25, 2.5), (3.25, 4.75), (5.25, 1.25), (2.25, 3.5)],
         "DU": [(9.5, 2.5), (8.5, 1.25), (6.5, 4.75), (5.5, 3.5)], "DD": [(5.75, 2.5), (1.75, 3.5), (5.75, 2.5), (1.75, 3.5)]}
assert all(tuple(map(float, nf(r, c))) == TABLE[r][j] for r in ROWS for j, c in enumerate(COLS))
# (DU, BB): 1/4*4 + 3/4*6 = 5.5; the book prints 4.5 (p. 322), which changes no best response
assert sorted(pure_nash(ROWS, COLS, nf)) == [("DU", "BM"), ("UU", "BB")]

pbe = pure_pbe(("H", "L"), quarter, ("U", "D"), ("M", "B"), u1, u2)
eqs = {(s["H"] + s["L"], r["U"] + r["D"]): b for s, r, b in pbe}
assert set(eqs) == {("DU", "BM"), ("UU", "BB")}
assert eqs[("DU", "BM")] == {"U": 0, "D": 1}                                       # separating, p. 322
assert eqs[("UU", "BB")] == {"U": quarter, "D": (0, Fr(3, 8))}                    # pooling, mu_D <= 3/8
```

---

## 5 · The intuitive criterion → [[L08-08-intuitive-criterion]]

Tadelis Def. 16.1 for two types. Checked on the MBA game (pooling fails, separating survives), on Gibbons's Fig. 4.2.2 pooling equilibrium, and on Gibbons's Beer–Quiche pooling on Quiche (p. 239).

```python
def intuitive_fails(eq, types, prior, msgs, acts, u1, u2):
    """Tadelis Def. 16.1 for two types: True if some off-path message breaks the PBE `eq`.

    A type is excluded from message m when even the best reply to m (over all beliefs) leaves it
    strictly below its equilibrium payoff. If the remaining types are a nonempty proper subset and
    one of them gains for sure once the receiver believes only they could send m, the PBE fails.
    """
    s, r, _ = eq
    star = {t: u1(t, s[t], r[s[t]]) for t in types}
    t1, t2 = types
    for m in msgs:
        if m in s.values():
            continue
        any_br = [a for a in acts if br_interval(u2, m, a, acts, t1, t2) is not None]
        keep = [t for t in types if max(u1(t, m, a) for a in any_br) >= star[t]]
        if not keep or len(keep) == len(types):
            continue
        mu = Fr(1) if keep == [t1] else Fr(0)                      # belief on the kept type only
        br = [a for a in acts if (iv := br_interval(u2, m, a, acts, t1, t2)) and iv[0] <= mu <= iv[1]]
        if any(min(u1(t, m, a) for a in br) > star[t] for t in keep):
            return True
    return False


by_key = {(s["H"] + s["L"], r["U"] + r["D"]): (s, r, b) for s, r, b in pbe}
assert intuitive_fails(by_key[("UU", "BB")], ("H", "L"), quarter, ("U", "D"), ("M", "B"), u1, u2)       # p. 334
assert not intuitive_fails(by_key[("DU", "BM")], ("H", "L"), quarter, ("U", "D"), ("M", "B"), u1, u2)
# Gibbons Fig. 4.2.2: R is equilibrium-dominated for t2 only (best 1 < 2); believed to be t1,
# the Receiver plays u after R and t1 gets 2 > 1, so the pooling PBE on L fails the criterion
gk = {(tuple(s.values()), tuple(r.values())): (s, r, b) for s, r, b in g}
G1 = lambda t, m, a: G422[(t, m, a)][0]; G2 = lambda t, m, a: G422[(t, m, a)][1]
assert intuitive_fails(gk[(("L", "L"), ("u", "d"))], ("t1", "t2"), half, ("L", "R"), ("u", "d"), G1, G2)

# Beer and Quiche, Gibbons Fig. 4.4.3 (p. 238): wimpy w.p. 0.1; payoffs (Sender, Receiver)
BQ = {("w", "Q", "N"): (3, 0), ("w", "Q", "D"): (1, 1), ("w", "B", "N"): (2, 0), ("w", "B", "D"): (0, 1),
      ("s", "Q", "N"): (2, 0), ("s", "Q", "D"): (0, -1), ("s", "B", "N"): (3, 0), ("s", "B", "D"): (1, -1)}
B1 = lambda t, m, a: BQ[(t, m, a)][0]; B2 = lambda t, m, a: BQ[(t, m, a)][1]
bq = pure_pbe(("w", "s"), Fr(1, 10), ("Q", "B"), ("N", "D"), B1, B2)
bk = {(s["w"] + s["s"], r["Q"] + r["B"]): (s, r, b) for s, r, b in bq}
assert bk[("QQ", "ND")][2]["B"] == (half, 1)                       # pooling on Quiche needs q >= 1/2, p. 238
assert intuitive_fails(bk[("QQ", "ND")], ("w", "s"), Fr(1, 10), ("Q", "B"), ("N", "D"), B1, B2)     # p. 239
# (the full equilibrium set of this game is Tadelis Exercise 16.8, p. 338: left as practice)
```

---

## 6 · Spence with linear costs, and the hybrid equilibria → [[L08-06-spence-job-market]]

M&R's numbers: separating $[1.5,3]$, pooled wage 29, pooling up to 0.45, H nets 35, $p^*=0.5$; Gibbons (4.2.8)–(4.2.10) for the hybrid at $e_h=1$.

```python
def spence(tH, tL, p, cH, cL):
    """Two-type Spence model, unproductive education, cost c_t * e (M&R pp. 155-156).

    Returns the separating interval for e_H (L's education is 0), the pooled wage, the largest
    pooling education sustained by the belief 'any other e means L', H's least-cost-separating
    payoff, and the prior above which H prefers a world without signaling.
    """
    assert tH > tL and 0 < p < 1 and cH < cL, "single crossing needs c_H < c_L"
    lo, hi = (tH - tL) / cL, (tH - tL) / cH          # IC_L: tL >= tH - cL e ; IC_H: tH - cH e >= tL
    wbar = p * tH + (1 - p) * tL
    return dict(sep=(lo, hi), wbar=wbar, ep_max=(wbar - tL) / cL,
                H_lcs=tH - cH * lo, p_star=1 - cH / cL)


mr = spence(50, 20, 0.30, 10, 20)
assert mr["sep"] == (1.5, 3.0)                 # M&R: "E_H a little bit more than 1.5"; E_H = 2 works
assert abs(mr["wbar"] - 29) < 1e-12            # (.3 x 50) + (.7 x 20) = 29
assert abs(mr["ep_max"] - 0.45) < 1e-12 and mr["H_lcs"] == 35 and mr["p_star"] == 0.5
assert 50 - 20 * 2 == 10 < 20 and 50 - 10 * 2 == 30 > 20      # M&R's E_H = 2 check, p. 156


def hybrid(tH, tL, p, cH, cL, eh):
    """Gibbons (4.2.8)-(4.2.10): L mixes between 0 and eh; returns (wage, belief r, L's prob pi)."""
    wh = tL + cL * eh                           # L indifferent: tL - 0 = wh - cL eh   (4.2.9)
    r = (wh - tL) / (tH - tL)                   # wh = r tH + (1 - r) tL               (4.2.10)
    pi = p * (1 - r) / (r * (1 - p))            # invert r = p / (p + (1 - p) pi)      (4.2.8)
    return wh, r, pi


wh, r, pi = hybrid(50, 20, 0.30, 10, 20, 1.0)
assert (wh, round(r, 4), round(pi, 4)) == (40, 0.6667, 0.2143)
assert hybrid(50, 20, 0.30, 10, 20, 1.5)[2] == 0                   # eh -> least-cost: pure separation
assert abs(hybrid(50, 20, 0.30, 10, 20, 0.45)[2] - 1) < 1e-12        # eh -> pooling bound: L always pools
```

---

## 7 · Limit pricing: monopoly, Cournot, separating and pooling bounds → [[L08-07-limit-pricing]]

Every number of §16.2: Steps 1–2 as linear systems, the separating interval $[2.62,3.32]$, the Bayesian Cournot quantities $(19/12, 13/12, 5/6)$, the pooling interval $[1.493,1.917]$, and the intuitive-criterion inequality (16.3).

```python
import numpy as np

# Tadelis Sec. 16.2 (pp. 323-332): P = 5 - Q, c2 = 2, entry cost 1/2, c1 in {1 (L), 2 (H)}
mono = lambda c: ((5 - c) / 2, ((5 - c) / 2) ** 2)                # Step 1: q and profit
assert mono(1) == (2, 4) and mono(2) == (1.5, 2.25)
# Step 2 (complete information Cournot), solved as a linear system of the two FOCs
def cournot(c1, c2=2):
    q = np.linalg.solve([[2, 1], [1, 2]], [5 - c1, 5 - c2])
    price = 5 - q.sum()
    return q, (price - c1) * q[0], (price - c2) * q[1] - 0.5
qH, v1H, v2H = cournot(2); qL, v1L, v2L = cournot(1)
assert np.allclose(qH, [1, 1]) and abs(v1H - 1) < 1e-12 and abs(v2H - 0.5) < 1e-12
assert np.allclose(qL, [5 / 3, 2 / 3]) and abs(v1L - 25 / 9) < 1e-12 and abs(v2L + 1 / 18) < 1e-12

# best deviation payoffs when any deviation triggers entry with q2 = 1
dev_H = 2.25 + 1.0          # monopoly now, Cournot reply (2 - q) q at q = 1 next period
dev_L = 4.0 + 2.25          # monopoly now, reply (3 - q) q at q = 1.5 next period
# separating: H must not mimic, L must not deviate (pp. 328-329)
sep_lo = (3 + 5 ** 0.5) / 2                                 # (3 - q) q + 2.25 <= 3.25
sep_hi = 2 + 1.75 ** 0.5                                    # (4 - q) q + 4 >= 6.25
assert abs((3 - sep_lo) * sep_lo + 2.25 - dev_H) < 1e-12 and abs((4 - sep_hi) * sep_hi + 4 - dev_L) < 1e-12
assert (round(sep_lo, 2), round(sep_hi, 2)) == (2.62, 3.32)
assert (5 - 2 - 2) * 2 + 2.25 == 4.25 > 3.25                # q1L = 2 fails: H mimics (p. 328)

# pooling: Bayesian Cournot after entry with belief 1/2 (pp. 330-331)
A = np.array([[2, 0, 1], [0, 2, 1], [0.5, 0.5, 2]])          # FOCs in (qL, qH, q2)
qL2, qH2, q2 = np.linalg.solve(A, [4, 3, 3])
assert np.allclose([qL2, qH2, q2], [19 / 12, 13 / 12, 5 / 6])
v2_pool = q2 * (3 - q2 - (qL2 + qH2) / 2) - 0.5
assert abs(v2_pool - 7 / 36) < 1e-12                       # > 0: entry. The book prints 7/18 (p. 331)
roots = lambda b, c: sorted(np.roots([1, -b, c]).real)     # q^2 - b q + c = 0
pH = roots(3, 3.25 - qH2 ** 2); pL = roots(4, 6.25 - qL2 ** 2)
assert np.allclose(pH, [13 / 12, 23 / 12]) and np.allclose(pL, [1.4931, 2.5069], atol=1e-4)
pool = (max(pH[0], pL[0]), min(pH[1], pL[1]))
assert (round(pool[0], 3), round(pool[1], 3)) == (1.493, 1.917)          # p. 332
# intuitive criterion at q = 3 (p. 334): H loses for sure, L gains if believed
assert (5 - 3 - 2) * 3 + 2.25 < 3.25 and (5 - 3 - 1) * 3 + 4 == 7 > 4 + qL2 ** 2
```

---

## 8 · Sequential equilibrium: trembles pin the belief → [[L08-03-sequential-equilibrium]]

Fig. 15.4: whatever the tremble, Bayes gives $\mu_2(x_1)=1/2$, so $R$ (which needs $\mu>2/3$) is never sequentially rational.

```python
# Tadelis Fig. 15.4 (p. 312): consistency pins mu2(x1) = 1/2 for every tremble
for eps in [Fr(1, 10), Fr(1, 1000), Fr(1, 10 ** 6)]:
    post = posterior({"x1": half, "x2": half}, {"x1": eps, "x2": eps})    # 1 cannot condition on Nature
    assert post["x1"] == half
mu = half
assert 3 * mu < 2                                  # R pays 3 mu, L pays 2: R is not sequentially rational
assert all(3 * m > 2 for m in [Fr(7, 10), Fr(9, 10)])   # the PBE (U, R) needs mu2(x1) > 2/3
print("L08 reference implementation: all checks pass.")
```

---

## Links

- Figures: `figures/make_figures.py` (run `python Notas/L08/figures/make_figures.py`), whose
  asserts re-check the plotted numbers.
- Companions and their checks: [[L08-00-map]] §Interactive companions.
- Rules: [[../../rules/game-theory|rules/game-theory]] item 12 ("verify by checking no player has a
  profitable deviation" — which is what `pure_pbe` does exhaustively).
