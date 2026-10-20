---
tags: [notes, lecture-07, python, reference-implementation]
date: 2026-10-16
status: estimated
source: "Every routine of notes L07-01 to L07-09, with assert self-checks against Tadelis (2013) Ch. 12–13, Gibbons (1992) Ch. 3, M&R (1992) pp. 151–153, Cabral (2017) pp. 174–176 and MWG p. 442. Reuses by citation Listas/lista-lecture-01-check.py::spa_payoff."
---

# Lecture 7 · Computation in Python

> Every routine the lecture needs, each followed by the asserts that must pass. Python, numpy, scipy
> (quadrature only). The blocks run **in order as one script**; together they are the source of every
> number quoted in the notes that is not printed in a book.
>
> Prev: [[L07-11-pitfalls]] · Map: [[L07-00-map]] · Formulas: [[L07-10-formulas]]

**Reuse.** Lecture 1 already checks weak dominance in the second-price auction, with a reserve price and
ties, on a grid of bids (`Listas/lista-lecture-01-check.py::spa_payoff`, list Q1 b). That script runs all
its checks on import, so it is cited rather than imported; §7 below only adds the three-case proof of
Prop. 13.1 against a continuum of rival bids. The two companions have their own independent check,
`companions/check_companions.py` (Node runs each page's model; Python recomputes it by another route).

**Run.** Copy the blocks into one file, or run `python Notas/L07/figures/make_figures.py` and
`python Notas/L07/companions/check_companions.py` for the figure and page checks.

---

## 1 · Harsanyi normal form, pure equilibria, posteriors

→ [[L07-01-bayesian-games-harsanyi]]: the entry game's matrix at $p=2/3$ and its three equilibria; the 1/6–1/3 prior.

```python
import itertools
from fractions import Fraction as Fr

import numpy as np


def harsanyi_normal_form(types1, types2, prior, acts1, acts2, u1, u2):
    """Expected-payoff matrices of a two-player static Bayesian game (Tadelis Sec. 12.1, p. 244).

    types1, types2: lists of types; prior[(t1, t2)]: common prior (dict, sums to 1);
    acts1, acts2: action lists; u1(a1, a2, t1, t2), u2(...): type-dependent payoffs.
    Returns (S1, S2, U1, U2): pure strategies (tuples, one action per type, in type order)
    and the ex-ante expected payoff matrices, rows = S1, columns = S2.
    """
    S1 = list(itertools.product(acts1, repeat=len(types1)))
    S2 = list(itertools.product(acts2, repeat=len(types2)))
    U1 = [[sum(prior[(t1, t2)] * u1(s1[i], s2[j], t1, t2)
               for i, t1 in enumerate(types1) for j, t2 in enumerate(types2)) for s2 in S2] for s1 in S1]
    U2 = [[sum(prior[(t1, t2)] * u2(s1[i], s2[j], t1, t2)
               for i, t1 in enumerate(types1) for j, t2 in enumerate(types2)) for s2 in S2] for s1 in S1]
    return S1, S2, U1, U2


def pure_nash(U1, U2):
    """All pure Nash equilibria (row, col) of a bimatrix game: mutual best responses."""
    R, Cn = len(U1), len(U1[0])
    return [(r, c) for r in range(R) for c in range(Cn)
            if U1[r][c] == max(U1[k][c] for k in range(R)) and U2[r][c] == max(U2[r][k] for k in range(Cn))]


def posterior(prior, own_index, own_type):
    """phi_i(t_-i | t_i) by Bayes' rule (Tadelis Def. 12.2, eq. 12.1). prior[(t1, t2)]."""
    tot = sum(p for t, p in prior.items() if t[own_index] == own_type)
    return {t[1 - own_index]: p / tot for t, p in prior.items() if t[own_index] == own_type}


# --- Entry game, Figs. 12.1-12.2 (pp. 243-245): player 2 rational (prob p) or crazy -------------
p = Fr(2, 3)
pay = {("O", "A"): (0, 2), ("O", "F"): (0, 2), ("E", "A"): (1, 1), ("E", "F"): (-1, -1)}
crazy = {("E", "F"): (-1, 2)}                       # the crazy type enjoys fighting


def entry(a1, a2, t1, t2, who):
    table = crazy if t2 == "c" and (a1, a2) in crazy else pay
    return table[(a1, a2)][who]


S1, S2, U1, U2 = harsanyi_normal_form(["one"], ["r", "c"], {("one", "r"): p, ("one", "c"): 1 - p},
                                      ["O", "E"], ["A", "F"],
                                      lambda a, b, s, t: entry(a, b, s, t, 0), lambda a, b, s, t: entry(a, b, s, t, 1))
assert U1[1] == [1, Fr(1, 3), Fr(-1, 3), -1] and U2[1] == [1, Fr(4, 3), Fr(-1, 3), 0]   # matrix, p. 244
eq = {("".join(S1[r]), "".join(S2[c])) for r, c in pure_nash(U1, U2)}
assert eq == {("O", "FA"), ("O", "FF"), ("E", "AF")}                                    # p. 245

# --- Posterior example, Sec. 12.1.2 (pp. 248-249) -------------------------------------------------
joint = {("a", "c"): Fr(1, 6), ("a", "d"): Fr(1, 3), ("b", "c"): Fr(1, 3), ("b", "d"): Fr(1, 6)}
assert posterior(joint, 0, "a") == {"c": Fr(1, 3), "d": Fr(2, 3)}
assert posterior(joint, 0, "b") == {"c": Fr(2, 3), "d": Fr(1, 3)}
```

## 2 · Chicken with incomplete information

→ [[L07-02-bayesian-nash-equilibrium]]: the full 4×4 matrix at $R=8$, $H=16$, $L=0$, the unique BNE $(DC,dc)$, and the flip to $(CD,cd)$ when $L$ and $H$ swap.

```python
# --- Chicken with incomplete information, Sec. 12.2.1 (pp. 252-255): R=8, H=16, L=0 ---------------
R, K = 8, {"L": 0, "H": 16}


def chicken(i):
    def u(a1, a2, t1, t2):
        mine, theirs, k = (a1, a2.upper(), K[t1]) if i == 0 else (a2.upper(), a1, K[t2])
        if mine == "C":
            return 0
        return R if theirs == "C" else Fr(R, 2) - k
    return u


prior4 = {(s, t): Fr(1, 4) for s in "LH" for t in "LH"}
S1, S2, U1, U2 = harsanyi_normal_form(["L", "H"], ["L", "H"], prior4, ["C", "D"], ["c", "d"], chicken(0), chicken(1))
row = {"".join(s): i for i, s in enumerate(S1)}
col = {"".join(s): j for j, s in enumerate(S2)}
assert (U1[row["CD"]][col["dd"]], U2[row["CD"]][col["dd"]]) == (Fr(R, 4) - 8, Fr(3 * R, 4) - 4)  # R/4-H/2, 3R/4-L/4-H/4
assert [(U1[row["DC"]][c], U2[row["DC"]][c]) for c in range(4)] == [(4, 0), (3, -1), (3, 3), (2, 2)]
assert [(U1[row["CD"]][c], U2[row["CD"]][c]) for c in range(4)] == [(4, 0), (-1, -1), (-1, 3), (-6, 2)]
assert [("".join(S1[r]), "".join(S2[c])) for r, c in pure_nash(U1, U2)] == [("DC", "dc")]  # unique BNE, p. 254
K = {"L": 16, "H": 0}                                  # the reversed story (p. 255)
S1, S2, U1, U2 = harsanyi_normal_form(["L", "H"], ["L", "H"], prior4, ["C", "D"], ["c", "d"], chicken(0), chicken(1))
assert [("".join(S1[r]), "".join(S2[c])) for r, c in pure_nash(U1, U2)] == [("CD", "cd")]
```

## 3 · Cournot with a privately known cost

→ [[L07-03-cournot-private-costs]]: closed forms checked against the three FOCs and against best-response iteration; the profit comparison.

```python
# --- Cournot with a privately known cost, Gibbons Sec. 3.1.A (pp. 144-146) ------------------------
def cournot_bne(a, c, cH, cL, theta):
    """BNE of P = a - Q; firm 1 cost c; firm 2 cost cH (prob theta) or cL. Returns (q1, q2H, q2L)."""
    q2H = (a - 2 * cH + c) / 3 + (1 - theta) * (cH - cL) / 6
    q2L = (a - 2 * cL + c) / 3 - theta * (cH - cL) / 6
    q1 = (a - 2 * c + theta * cH + (1 - theta) * cL) / 3
    return q1, q2H, q2L


a, c, cH, cL, th = 10.0, 2.0, 3.0, 1.0, 0.5           # illustrative: Gibbons uses letters only
q1, q2H, q2L = cournot_bne(a, c, cH, cL, th)
assert abs(q2H - (a - q1 - cH) / 2) < 1e-12 and abs(q2L - (a - q1 - cL) / 2) < 1e-12        # firm 2's FOCs
assert abs(q1 - (a - c - (th * q2H + (1 - th) * q2L)) / 2) < 1e-12                           # firm 1's FOC
x = np.zeros(3)                                       # same point by best-response iteration (a contraction)
for _ in range(200):
    x = np.array([(a - c - (th * x[1] + (1 - th) * x[2])) / 2, (a - x[0] - cH) / 2, (a - x[0] - cL) / 2])
assert np.allclose(x, [q1, q2H, q2L])
assert q2H > (a - 2 * cH + c) / 3 and q2L < (a - 2 * cL + c) / 3          # Gibbons p. 146
assert abs(q1 - (th * (a - 2 * c + cH) / 3 + (1 - th) * (a - 2 * c + cL) / 3)) < 1e-12      # the "misleading" average
# profits: with linear demand each margin equals the quantity, so profit = quantity^2
pi1_bne, pi1_ci = q1 ** 2, th * ((a - 2 * c + cH) / 3) ** 2 + (1 - th) * ((a - 2 * c + cL) / 3) ** 2
assert abs(pi1_bne - 64 / 9) < 1e-12 and abs(pi1_ci - 65 / 9) < 1e-12           # firm 1 loses from not knowing
assert q2H ** 2 > ((a - 2 * cH + c) / 3) ** 2 and q2L ** 2 < ((a - 2 * cL + c) / 3) ** 2
```

## 4 · Thresholds, purification, the jury

→ [[L07-04-threshold-strategies-purification]] and [[L07-09-common-values-curses]] §1: $c^{1/3}$ by fixed-point iteration, Gibbons's limit $2/3$, the pivotal posterior $=q$, and the reply to $CC$.

```python
# --- Study groups, Sec. 12.2.2 (pp. 255-258); MWG Example 8.E.2 (p. 256) --------------------------
def study_group_br(t_other, c):
    """Best-response threshold (12.5): sqrt(c / t_other) if t_other >= c, else 1."""
    return (c / t_other) ** 0.5 if t_other >= c else 1.0


for cc in (0.05, 1 / 8, 0.5, 0.9):
    t = 1.0
    for _ in range(2000):                             # iterate the symmetric map t -> BR(t)
        t = 0.5 * t + 0.5 * study_group_br(t, cc)     # damped: the plain map oscillates
    assert abs(t - cc ** (1 / 3)) < 1e-9 and cc < cc ** 0.5 < cc ** (1 / 3) < 1

# --- Purification of the Battle of the Sexes, Gibbons Sec. 3.2.A (pp. 152-154) -------------------
def bos_purified(x):
    """Probability Chris plays Opera (= Pat plays Fight) in the threshold BNE: 1 - (-3 + sqrt(9+4x))/(2x)."""
    return 1 - (-3 + (9 + 4 * x) ** 0.5) / (2 * x)


for xx in (1.0, 0.1, 1e-4):
    cstar = (-3 + (9 + 4 * xx) ** 0.5) / 2            # c = p solves p^2 + 3p - x = 0 (from 3.2.1-3.2.2)
    assert abs(cstar ** 2 + 3 * cstar - xx) < 1e-12 and abs(xx / cstar - 3 - cstar) < 1e-9   # (3.2.1)
assert abs(bos_purified(1e-6) - 2 / 3) < 1e-6

# --- Jury voting, Sec. 12.4 (pp. 261-264): the pivotal posterior equals the prior -----------------
for q, pp in [(0.6, 0.7), (0.55, 0.9), (0.8, 0.85)]:
    post_I = q * (1 - pp) / (q * (1 - pp) + (1 - q) * pp)
    assert (post_I < 0.5) == (pp > q)                   # alone, an innocence signal acquits iff p > q
    piv = q * (1 - pp) * pp / (q * (1 - pp) * pp + (1 - q) * pp * (1 - pp))
    assert abs(piv - q) < 1e-12                         # Pr{G | own theta_I, other theta_G} = q
# Best reply of a theta_I juror to a partner who always convicts (CC): he is always pivotal,
# so he conditions on his own signal only and acquits iff p > q (see L07-09 Sec. 1.3).
def theta_I_reply_to_CC(q, pp):
    return "A" if q * (1 - pp) / (q * (1 - pp) + (1 - q) * pp) < 0.5 else "C"


assert theta_I_reply_to_CC(0.6, 0.7) == "A" and theta_I_reply_to_CC(0.7, 0.6) == "C"
```

## 5 · Adverse selection

→ [[L07-05-adverse-selection-lemons]] §2–6, §8: Prop. 12.1, M&R's breakdown condition, Cabral's $-2.55$, MWG Example 13.B.1.

```python
# --- Adverse selection, Tadelis Sec. 12.3 (pp. 258-261), Prop. 12.1 -------------------------------
def lemons_trade(seller_vals, premium, probs=None):
    """Largest set of lowest qualities that can trade in a BNE, and the price interval supporting it.
    seller_vals sorted ascending; buyer value = seller value + premium; quality k sells iff p >= v_k.
    Returns (k_max, (p_lo, p_hi)) with k_max >= 1 counting the qualities that trade."""
    v = np.asarray(seller_vals, float)
    w = np.full(len(v), 1 / len(v)) if probs is None else np.asarray(probs, float)
    kmax = max(k for k in range(1, len(v) + 1) if np.average(v[:k] + premium, weights=w[:k]) >= v[k - 1] - 1e-12)
    return kmax, (v[kmax - 1], np.average(v[:kmax] + premium, weights=w[:kmax]))


k, band = lemons_trade([10, 20, 30], 4)
assert k == 1 and np.allclose(band, (10, 14))                       # only L trades, p* in [10, 14]
assert lemons_trade([10, 20, 30], 10)[0] == 3 and lemons_trade([10, 20, 30], 9.5)[0] == 2

# --- M&R's insurance market (pp. 151-152), eqs. (5.1)-(5.2): x ~ U[0, xbar] -----------------------
def mr_market_exists(xbar, v, c):
    """True iff some marginal buyer x has P_b(x) = x + v >= P_s(x) = (x + xbar)(1 + c)/2 (c < 1)."""
    xs = np.linspace(0, xbar, 10001)
    return bool(np.any(xs + v >= (xs + xbar) * (1 + c) / 2 - 1e-12))


for xbar, v, c in [(100, 5, 0.1), (100, 15, 0.1), (100, 8, 0.1)]:
    assert mr_market_exists(xbar, v, c) == (c * xbar <= v)          # breakdown iff c*xbar > v
# c*xbar > v > c*xbar/2: mandatory coverage would add value, the private market cannot exist
assert not mr_market_exists(100, 8, 0.1) and 8 > 0.1 * 100 / 2

# --- Cabral Sec. 7.4 (pp. 174-176): 10% high risk; values 20 / 3, costs 30 / 1 ($000) -------------
def insurer_payoff(price, risk=((0.1, 20, 30), (0.9, 3, 1))):
    """Expected profit when each patient type buys iff its value >= price."""
    return sum(pr * (price - cost) for pr, val, cost in risk if val >= price)


assert abs(insurer_payoff(4.5) - (-2.55)) < 1e-12 and insurer_payoff(30) == 0     # Cabral rounds to -2.5
assert abs(0.1 * 20 + 0.9 * 3 - 4.7) < 1e-12 and abs(0.1 * 30 + 0.9 * 1 - 3.9) < 1e-12

# --- MWG Example 13.B.1 (p. 442): theta ~ U[0,2], r(theta) = alpha theta --------------------------
def mwg_wages(alpha, grid=np.linspace(0, 2, 200001)):
    """Competitive wages w = E[theta | alpha theta <= w] = min(w / (2 alpha), 1) (13.B.6)."""
    return grid[np.abs(np.minimum(grid / (2 * alpha), 1.0) - grid) < 1e-9]


assert list(mwg_wages(0.75)) == [0.0]                                  # alpha > 1/2: complete unravelling
assert 1.0 in mwg_wages(0.4)                                            # alpha < 1/2: everyone hired at w = 1
```

## 6 · The double auction

→ [[L07-05-adverse-selection-lemons]] §7: the linear BNE, trade iff $v_b\ge v_s+\tfrac14$, gains $9/64$ vs $1/6$ vs $1/8$, and a numerical check of the buyer's best reply (3.2.5).

```python
# --- Double auction, Gibbons Sec. 3.2.C (pp. 158-163) ---------------------------------------------
def linear_double_auction(vb, vs):
    """Linear BNE (3.2.7)-(3.2.8): p_b = 2/3 v_b + 1/12, p_s = 2/3 v_s + 1/4; trade iff p_b >= p_s."""
    pb, ps = 2 / 3 * vb + 1 / 12, 2 / 3 * vs + 1 / 4
    return pb >= ps, (pb + ps) / 2


rng = np.random.default_rng(3)
vb, vs = rng.random(400_000), rng.random(400_000)
trade, price = linear_double_auction(vb, vs)
assert np.array_equal(trade, vb >= vs + 0.25 - 1e-12)                  # trade iff v_b >= v_s + 1/4
assert abs(((vb - vs) * trade).mean() - 9 / 64) < 2e-3                  # expected gains 9/64
assert abs(((vb - vs) * (vb >= vs)).mean() - 1 / 6) < 2e-3              # efficient benchmark 1/6
one_price = lambda x: x * (1 - x) / 2                                   # gains of the one-price BNE at x
assert abs(((vb - vs) * ((vs <= 0.5) & (vb >= 0.5))).mean() - one_price(0.5)) < 2e-3 and one_price(0.5) < 9 / 64
# best-reply check of (3.2.5): buyer facing p_s = a_s + c_s v_s, here a_s = 1/4, c_s = 2/3
b_grid = np.linspace(0.25, 0.95, 70001)
for vbb in (0.4, 0.7, 1.0):
    obj = (vbb - 0.5 * (b_grid + (0.25 + b_grid) / 2)) * (b_grid - 0.25) / (2 / 3)
    assert abs(b_grid[np.argmax(obj)] - (2 / 3 * vbb + 1 / 3 * 0.25)) < 1e-4
```

## 7 · Second-price and first-price bidding

→ [[L07-06-second-price-english]], [[L07-07-first-price-dutch]]: the three cases of Prop. 13.1; (13.7) for any $F$ reproducing (13.8); numerical best replies.

```python
# --- Second-price auction, Tadelis Prop. 13.1 (pp. 273-274) ---------------------------------------
# Lecture 1 already checks weak dominance with a reserve price and ties on a grid of bids:
# Listas/lista-lecture-01-check.py::spa_payoff (Q1 b). Here: the three cases of the proof.
def spa_payoff(bid, theta, m):
    """Payoff against the highest rival bid m (ties: neither wins, footnote 2 p. 272)."""
    return np.where(bid > m, theta - m, 0.0)


m = np.linspace(0, 1, 100001)
theta = 0.6
for bid in (0.0, 0.3, 0.45, 0.75, 0.9, 1.0):
    gap = spa_payoff(theta, theta, m) - spa_payoff(bid, theta, m)
    assert gap.min() >= 0 and gap.max() > 0          # never worse, sometimes strictly better

# --- First-price auction, Tadelis (13.7)-(13.8) (pp. 278-279); Gibbons p. 156 ---------------------
def fpa_bid(theta, n, F=None, lo=0.0):
    """Symmetric BNE bid (13.7): theta - int_lo^theta F(x)^(n-1) dx / F(theta)^(n-1). Uniform [0,1] if F is None."""
    if F is None:
        return (n - 1) * theta / n                     # (13.8)
    xs = np.linspace(lo, theta, 20001)
    return theta - np.trapezoid(F(xs) ** (n - 1), xs) / F(theta) ** (n - 1)


def fpa_best_reply(theta, n, rival_bid=lambda v, n: (n - 1) * v / n):
    """Numerical best reply to n-1 rivals using rival_bid(v, n), values uniform on [0,1]."""
    b = np.linspace(0, theta, 40001)
    slope = rival_bid(1.0, n)                          # linear rival strategy: Pr(rival bid < b) = b / slope
    U = np.minimum(1, b / slope) ** (n - 1) * (theta - b)
    return b[np.argmax(U)]


for n in (2, 3, 5, 10):
    for th in (0.2, 0.55, 0.9):
        assert abs(fpa_best_reply(th, n) - fpa_bid(th, n)) < 5e-5
        assert abs(fpa_bid(th, n, F=lambda x: x) - fpa_bid(th, n)) < 1e-8      # (13.7) reproduces (13.8)
assert fpa_bid(0.5, 2) == 0.25                                                  # Gibbons: b(v) = v/2
```

## 8 · Revenue equivalence

→ [[L07-08-revenue-equivalence]]: (13.9)–(13.10) by quadrature, type-by-type payments, Monte Carlo, and the variance comparison.

```python
# --- Revenue equivalence, Tadelis Sec. 13.1.4 (pp. 279-282) ---------------------------------------
from scipy.integrate import quad


def revenue_closed(n):
    return (n - 1) / (n + 1)


def revenue_fpa(n):
    """E[highest bid]: density of the max of n bids uniform on [0,(n-1)/n], eq. (13.9)."""
    top = (n - 1) / n
    return quad(lambda x: x * n * (n / (n - 1)) ** n * x ** (n - 1), 0, top)[0]


def revenue_spa(n):
    """E[second-highest value]: density from (13.10), n(n-1)(x^(n-2) - x^(n-1))."""
    return quad(lambda x: x * n * (n - 1) * (x ** (n - 2) - x ** (n - 1)), 0, 1)[0]


for n in range(2, 11):
    assert abs(revenue_fpa(n) - revenue_closed(n)) < 1e-10 and abs(revenue_spa(n) - revenue_closed(n)) < 1e-10
# type by type: expected payment of value theta is theta^(n-1) (n-1) theta / n in both formats
for n in (2, 4):
    for th in (0.3, 0.8):
        pay_spa = quad(lambda x: x * (n - 1) * x ** (n - 2), 0, th)[0]          # E[max rival value; it < theta]
        assert abs(pay_spa - th ** (n - 1) * fpa_bid(th, n)) < 1e-12
rng = np.random.default_rng(1)
v = np.sort(rng.random((300_000, 4)), axis=1)
assert abs((3 / 4 * v[:, -1]).mean() - 0.6) < 3e-3 and abs(v[:, -2].mean() - 0.6) < 3e-3   # n = 4: 3/5
# same mean, different risk (n = 2): Var(max/2) = 1/72, Var(min) = 1/18
var_fpa = quad(lambda x: (x / 2) ** 2 * 2 * x, 0, 1)[0] - (1 / 3) ** 2
var_spa = quad(lambda x: x ** 2 * 2 * (1 - x), 0, 1)[0] - (1 / 3) ** 2
assert abs(var_fpa - 1 / 72) < 1e-12 and abs(var_spa - 1 / 18) < 1e-12
```

## 9 · Common values: the oil field

→ [[L07-09-common-values-curses]] §2: $E[v\mid L]=15$, $E[v\mid H]=25$, and the $-1.25$ of bidding 15.

```python
# --- Common values: the oil field, Tadelis Sec. 13.2 (pp. 283-284) --------------------------------
states = {(10, "L", "L"): Fr(1, 4), (20, "L", "H"): Fr(1, 4), (20, "H", "L"): Fr(1, 4), (30, "H", "H"): Fr(1, 4)}


def cond_value(sig):
    num = sum(v * pr for (v, s1, s2), pr in states.items() if s1 == sig)
    return num / sum(pr for (v, s1, s2), pr in states.items() if s1 == sig)


assert cond_value("L") == 15 and cond_value("H") == 25                 # E[v | L] = 15, E[v | H] = 25
# player 1 with L bids 15 while player 2 bids E[v | own signal]: tie (coin flip) only when both are L
bid2 = {"L": 15, "H": 25}
ev = sum(pr * (Fr(1, 2) * (v - 15) if bid2[s2] == 15 else 0)
         for (v, s1, s2), pr in states.items() if s1 == "L") / Fr(1, 2)
assert ev == Fr(-5, 4)                                                  # -1.25: the winner's curse
```

---

## Links

- Map: [[L07-00-map]] · formulas: [[L07-10-formulas]] · pitfalls: [[L07-11-pitfalls]].
- Figures: `figures/make_figures.py` (seven figures, each with its own asserts).
- Companion checks: `companions/check_companions.py`.
