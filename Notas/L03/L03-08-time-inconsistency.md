---
tags: [notes, lecture-03, time-inconsistency, hyperbolic-discounting, multiple-selves, commitment]
date: 2026-10-16
status: estimated
source: "Tadelis (2013) §8.3.4 (pp. 166–169): eqs. (8.3)–(8.9), the sophisticated three-period example with beta = 1/2, delta = 1"
---

# 8.3.4 · Time-inconsistent preferences: a game against your future self

> **Claim.** With exponential discounting, a plan made today is the plan you will want to follow
> tomorrow. With present bias (hyperbolic, $\beta\delta$ discounting) it is not, and a **sophisticated**
> decision maker treats her future self as another player and solves the problem by **backward
> induction**: a subgame-perfect equilibrium of a game with one person in it. This note also corrects a
> calculus slip in the book's worked example: with log utility the first-period choice is $K/2$, not
> $2K/3$.
> Prev: [[L03-07-stackelberg]] · Next: [[L03-09-formulas]] · Map: [[L03-00-map]]

---

## 1 · C — exponential discounting is time consistent (pp. 166–167)

A stream $x_1,\dots,x_T$ is worth, in period 1,

$$v(x_1,\dots,x_T)=u(x_1)+\delta u(x_2)+\dots+\delta^{T-1}u(x_T)=\sum_{t=1}^{T}\delta^{t-1}u(x_t)\qquad(8.3)$$

With $u=\ln$, budget $K$ over three periods and $x_1=K-x_2-x_3$:

$$\max_{x_2,x_3}\ \ln(K-x_2-x_3)+\delta\ln x_2+\delta^2\ln x_3 .$$

First-order conditions:
$-\tfrac{1}{K-x_2-x_3}+\tfrac{\delta}{x_2}=0$ and $-\tfrac{1}{K-x_2-x_3}+\tfrac{\delta^2}{x_3}=0$, so
$x_2=\delta x_1$ and $x_3=\delta^2x_1$. With $x_1+x_2+x_3=K$:

$$x_1=\frac{K}{1+\delta+\delta^2},\qquad x_2=\frac{\delta K}{1+\delta+\delta^2},\qquad x_3=\frac{\delta^2K}{1+\delta+\delta^2}\qquad(8.4)\text{–}(8.6)$$

**Will period-2 self follow the plan?** After consuming $x_1$ she has
$K_2=K-x_1=\tfrac{(\delta+\delta^2)K}{1+\delta+\delta^2}$ (8.7) and solves
$\max_{x_2}\ln x_2+\delta\ln(K_2-x_2)$, so $\tfrac1{x_2}=\tfrac{\delta}{K_2-x_2}$ and
$x_2=\tfrac{K_2}{1+\delta}$ (8.8). Substituting (8.7):

$$x_2=\frac{(\delta+\delta^2)K}{1+\delta+\delta^2}\cdot\frac{1}{1+\delta}=\frac{\delta K}{1+\delta+\delta^2},$$

**the same as (8.5).** Exponential discounting is **time consistent** (p. 167).

---

## 2 · C — present bias breaks it (pp. 167–168)

**Hyperbolic ($\beta\delta$) discounting**: the present is weighted 1 and *every* future period gets an
extra factor $\beta\in(0,1)$:

$$v(x_1,x_2,x_3)=\ln x_1+\beta\delta\ln x_2+\beta\delta^2\ln x_3\qquad(8.9)$$

Between today and tomorrow the discount is $\beta\delta$; between two future dates it is $\delta$.
Period-1 self wants to treat periods 2 and 3 alike (relative weight $\delta$); when period 2 arrives,
period-2 self discounts period 3 by $\beta\delta$ and wants more for herself. **Plans get revised.**

A sophisticated player 1 knows this and plays a game against "player 2", her period-2 self. Take
$\delta=1$, $\beta=\tfrac12$.

### 2.1 · Backward induction: period-2 self (p. 168)

With budget $K_2$:

$$\max_{x_2}\ \ln x_2+\tfrac12\ln(K_2-x_2),\qquad \frac1{x_2}-\frac{1/2}{K_2-x_2}=0
\ \Rightarrow\ K_2-x_2=\tfrac12x_2\ \Rightarrow\ x_2(K_2)=\tfrac23K_2,\quad x_3(K_2)=\tfrac13K_2 .$$

This is player 2's strategy: a reply for each of the continuum of subgames indexed by $K_2$.

### 2.2 · Period-1 self (p. 169), and a correction

Player 1 substitutes the reply, with $K_2=K-x_1$:

$$v_1(x_1)=\ln x_1+\tfrac12\ln\!\Bigl(\tfrac23(K-x_1)\Bigr)+\tfrac12\ln\!\Bigl(\tfrac13(K-x_1)\Bigr).$$

The constants $\tfrac23$ and $\tfrac13$ sit inside logarithms, so they drop out of the derivative:
$\tfrac{d}{dx_1}\ln\!\bigl(c(K-x_1)\bigr)=-\tfrac1{K-x_1}$ for any $c>0$. Hence

$$v_1'(x_1)=\frac1{x_1}-\frac{1/2}{K-x_1}-\frac{1/2}{K-x_1}=\frac1{x_1}-\frac1{K-x_1}=0
\quad\Rightarrow\quad \boxed{x_1=\tfrac K2},\quad x_2=\tfrac23\cdot\tfrac K2=\tfrac K3,\quad x_3=\tfrac K6 .$$

> *Source detail.* The book prints the first-order condition as
> $\tfrac1{x_1}-\tfrac23\times\tfrac{0.5}{K-x_1}-\tfrac13\times\tfrac{0.5}{K-x_1}=0$, multiplying each
> term by the constant inside the logarithm, and concludes $x_1=\tfrac23K$ (p. 169). That is not the
> derivative of the objective printed one line above it. A grid search of $v_1$ ([[L03-11-python]] §4)
> peaks at $x_1=0.5K$, and $v_1(\tfrac K2)>v_1(\tfrac{2K}3)$. If you are examined on this example,
> state the objective and differentiate it; do not reproduce the printed number.

![Left: self 1's payoff as a function of x1 over K, a concave curve peaking at x1 = K/2, with the printed value 2K/3 marked lower on the curve. Right: grouped bars of x1, x2, x3 as shares of K for four plans: exponential with delta 1 (one third each), self 1's ideal under commitment (1/2, 1/4, 1/4), the correct sophisticated equilibrium (1/2, 1/3, 1/6), and the printed one (2/3, 2/9, 1/9)](figures/L03-hyperbolic-discounting.png)
*Figure — the sophisticated three-period problem with $\beta=\tfrac12$, $\delta=1$, $u=\ln$. Left: self 1's objective given self 2's reply. Right: four consumption plans. Source: Tadelis §8.3.4, eqs. (8.4)–(8.9), pp. 166–169; corrected optimum computed here.*

The right panel separates the two effects. Self 1's *own* ideal plan (what she would lock in if she
could) is $(\tfrac12,\tfrac14,\tfrac14)$: present bias alone already moves consumption to period 1. The
sophisticated equilibrium keeps $x_1=\tfrac12$ but splits the rest $\tfrac23:\tfrac13$ instead of
$\tfrac12:\tfrac12$, because period-2 self grabs more than self 1 wants her to.

### 2.3 · What survives of the book's story

| Claim on p. 169 | With the correct derivative |
|---|---|
| Player 2 overconsumes relative to player 1's wishes | **yes**: $x_2=\tfrac K3$ against the $\tfrac K4$ player 1 would choose for her |
| Player 1 overconsumes to leave player 2 less | **not with log utility**: $x_1=\tfrac K2$ either way. With $\ln$, the ratio $x_2/x_3$ chosen by self 2 does not change self 1's marginal value of the remaining budget, so self 1 has no reason to shrink it |
| The result differs from the exponential benchmark ($\tfrac K3$ each) | **yes**, but because of $\beta$, not because of the game |

> **The structure is the lesson, not the number**: a time-inconsistent decision maker who anticipates
> her future choices is solving for a subgame-perfect equilibrium, and **she would pay to commit**
> (exercise 8.16 asks how much; not solved here). Naive players (who do not anticipate) and sophisticated
> ones (who do) are distinguished in the behavioural literature: Laibson (1997) on savings,
> O'Donoghue and Rabin (1999) on procrastination (p. 169).

---

## Links

- Previous: commitment as a source of value, [[L03-06-credibility-entry-commitment]] §3.
- Discounting in repeated games: [[../L05/L05-00-map|Lecture 5]].
- Python: `v1` and the commitment plan, [[L03-11-python]] §4; figure code
  `figures/make_figures.py::hyperbolic`.
- Exercises: Tadelis 8.14, 8.15, 8.16 (p. 174).
