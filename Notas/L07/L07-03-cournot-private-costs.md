---
tags: [notes, lecture-07, bayesian-nash-equilibrium, cournot, private-costs]
date: 2026-10-16
status: estimated
source: "Gibbons (1992) §3.1.A 'Cournot Competition under Asymmetric Information', printed pp. 144–146, and §3.1.B–C, pp. 147, 150–151; Tadelis (2013) Ch. 12 opening (p. 241) and exercise 12.2 (p. 266, cited only). Numerical calibration illustrative."
---

# Gibbons 3.1.A · Cournot with a privately known cost: one quantity for firm 1, two for firm 2

> **Claim.** When firm 2 alone knows its marginal cost, its strategy is **a pair of quantities**
> $(q_2^*(c_H),q_2^*(c_L))$ and firm 1 best-responds to their **expectation**. Solving three
> first-order conditions gives the BNE in closed form, and it differs from complete-information
> Cournot in a definite direction: **the high-cost type produces more, the low-cost type less**,
> because each type also responds to firm 1 *not* knowing which one it is.
>
> Prev: [[L07-02-bayesian-nash-equilibrium]] · Next: [[L07-04-threshold-strategies-purification]] · Map: [[L07-00-map]]

---

## 1 · C — the game as a static Bayesian game (Gibbons pp. 144, 147)

| Element | Here |
|---|---|
| Players | firms 1 and 2 |
| Actions | $q_1\ge0$, $q_2\ge0$, chosen simultaneously |
| Types | $T_1=\{c\}$ (firm 1's cost is common knowledge); $T_2=\{c_H,c_L\}$, $c_L<c_H$ |
| Prior | $\Pr\{c_H\}=\theta$, $\Pr\{c_L\}=1-\theta$, common knowledge |
| Payoffs | $\pi_1=[(a-q_1-q_2)-c]q_1$; $\pi_2(q_1,q_2;c_k)=[(a-q_1-q_2)-c_k]q_2$ |
| Strategies | firm 1: a number $q_1$; firm 2: a **function** $c_k\mapsto q_2(c_k)$, i.e. a pair |

Demand $P(Q)=a-Q$, $Q=q_1+q_2$. Firm 2 could be a new entrant or have a new technology
(p. 144). *Gibbons writes $\theta$ for the probability of the high cost — not a type.*

> **Why firm 2's strategy must be a pair** (Gibbons pp. 150–151): firm 1 cannot check that $q_1$ is
> a best response unless it knows what firm 2 would produce **at each cost**. A single number for
> firm 2 would leave firm 1's expected profit undefined.

---

## 2 · C — the three optimization problems and their FOCs (p. 145)

**Firm 2, high cost:**
$$\max_{q_2}\;[(a-q_1^*-q_2)-c_H]\,q_2\quad\Rightarrow\quad a-q_1^*-2q_2-c_H=0\quad\Rightarrow\quad
q_2^*(c_H)=\frac{a-q_1^*-c_H}{2}.$$

**Firm 2, low cost:**
$$q_2^*(c_L)=\frac{a-q_1^*-c_L}{2}.$$

**Firm 1** does not know which type it faces, so it maximizes **expected** profit:
$$\max_{q_1}\;\theta[(a-q_1-q_2^*(c_H))-c]q_1+(1-\theta)[(a-q_1-q_2^*(c_L))-c]q_1 .$$
Differentiate:
$$\theta\,[a-2q_1-q_2^*(c_H)-c]+(1-\theta)[a-2q_1-q_2^*(c_L)-c]=0$$
$$\Rightarrow\quad q_1^*=\frac{\theta[a-q_2^*(c_H)-c]+(1-\theta)[a-q_2^*(c_L)-c]}{2}=\frac{a-c-E[q_2^*]}{2},$$
with $E[q_2^*]=\theta q_2^*(c_H)+(1-\theta)q_2^*(c_L)$.

> **Firm 1's problem is linear in $q_2$, so only the mean of firm 2's quantity matters to it.**
> That is special to linear demand (see §5).

---

## 3 · C — solving, every step

Write $\bar c=\theta c_H+(1-\theta)c_L$ for firm 2's expected cost. Average firm 2's two FOCs with
weights $\theta,1-\theta$:
$$E[q_2^*]=\frac{a-q_1^*-\bar c}{2}.$$
Substitute into firm 1's FOC:
$$q_1^*=\frac{a-c-\tfrac12(a-q_1^*-\bar c)}{2}\;\Rightarrow\;2q_1^*=\tfrac a2-c+\tfrac{q_1^*}2+\tfrac{\bar c}2
\;\Rightarrow\;\tfrac32q_1^*=\tfrac{a-2c+\bar c}{2}$$
$$\boxed{\;q_1^*=\frac{a-2c+\theta c_H+(1-\theta)c_L}{3}\;}$$

Back into firm 2's high-cost FOC, using $\bar c=c_H-(1-\theta)(c_H-c_L)$:
$$q_2^*(c_H)=\frac{a-c_H}{2}-\frac{a-2c+\bar c}{6}=\frac{2a+2c-\bar c-3c_H}{6}
=\frac{2a+2c-4c_H+(1-\theta)(c_H-c_L)}{6}$$
$$\boxed{\;q_2^*(c_H)=\frac{a-2c_H+c}{3}+\frac{1-\theta}{6}(c_H-c_L)\;}$$

Likewise, with $\bar c=c_L+\theta(c_H-c_L)$:
$$\boxed{\;q_2^*(c_L)=\frac{a-2c_L+c}{3}-\frac{\theta}{6}(c_H-c_L)\;}$$

(Gibbons assumes the FOCs characterize the solutions, i.e. all three quantities positive; he leaves
a sufficient condition as an exercise on p. 145.)

---

## 4 · C — comparison with complete information (p. 146)

Under complete information with costs $c_1,c_2$, firm $i$ produces $q_i=(a-2c_i+c_j)/3$.

| Firm 2's cost | Complete information $q_2$ | BNE $q_2^*$ | Direction |
|---|---|---|---|
| $c_H$ | $(a-2c_H+c)/3$ | $+\frac{1-\theta}{6}(c_H-c_L)$ more | **produces more** |
| $c_L$ | $(a-2c_L+c)/3$ | $-\frac{\theta}{6}(c_H-c_L)$ less | **produces less** |

> **Why.** Firm 2 "not only tailors its quantity to its cost but also responds to the fact that
> firm 1 cannot do so" (p. 146). Facing a high-cost rival, firm 1 *would* expand; not knowing, it
> produces the average, which is **less** than it would against a known high-cost firm — so the
> high-cost type, facing less rival output than under complete information, produces more. The
> low-cost type faces more and produces less.

**The "potentially misleading feature"** (p. 146): here $q_1^*$ equals the average of firm 1's two
complete-information quantities,
$$\theta\frac{a-2c+c_H}{3}+(1-\theta)\frac{a-2c+c_L}{3}=\frac{a-2c+\bar c}{3}=q_1^*,$$
but only because costs enter linearly. Gibbons's counterexample: total cost $c_iq_i^2$.

---

## 5 · Worked — an illustrative calibration

Gibbons states the model in letters only. Take $a=10$, $c=2$, $c_H=3$, $c_L=1$, $\theta=\tfrac12$
(illustrative), so $\bar c=2$:

| | Formula | Value |
|---|---|---|
| $q_1^*$ | $(10-4+2)/3$ | $8/3\approx2.667$ |
| $q_2^*(c_H)$ | $(10-6+2)/3+\tfrac{1/2}{6}\cdot2=2+\tfrac16$ | $13/6\approx2.167$ |
| $q_2^*(c_L)$ | $(10-2+2)/3-\tfrac{1/2}{6}\cdot2=\tfrac{10}3-\tfrac16$ | $19/6\approx3.167$ |
| $E[q_2^*]$ | $\tfrac12(13/6+19/6)$ | $8/3$ |

**Check each FOC.** $(10-8/3-3)/2=(13/3)/2=13/6$ ✓; $(10-8/3-1)/2=(19/3)/2=19/6$ ✓;
$(10-2-8/3)/2=(16/3)/2=8/3$ ✓.

**Complete-information benchmarks.** Against $c_H$: $q_1=(10-4+3)/3=3$, $q_2=(10-6+2)/3=2$. Against
$c_L$: $q_1=(10-4+1)/3=7/3$, $q_2=(10-2+2)/3=10/3$. Indeed $13/6>2$ and $19/6<10/3$, and
$q_1^*=\tfrac12(3+7/3)=8/3$.

**Profits.** With linear demand each FOC says *margin = quantity* (e.g. $a-q_1-q_2^*(c_H)-c_H=q_2^*(c_H)$),
so each profit is a square:

| | BNE | Complete information | Who gains from the asymmetry |
|---|---|---|---|
| Firm 1 (expected) | $(8/3)^2=64/9\approx7.111$ | $\tfrac12\cdot3^2+\tfrac12(7/3)^2=65/9\approx7.222$ | firm 1 **loses** |
| Firm 2, $c_H$ | $(13/6)^2\approx4.694$ | $2^2=4$ | high-cost type **gains** |
| Firm 2, $c_L$ | $(19/6)^2\approx10.028$ | $(10/3)^2\approx11.111$ | low-cost type **loses** |

![Best-response lines in (q1, q2): firm 2's two lines for high and low cost, firm 1's line against the expected rival quantity; the BNE has one q1 = 8/3 with q2 = 13/6 (high cost) and 19/6 (low cost); hollow complete-information points at (3, 2) and (7/3, 10/3)](figures/L07-cournot-private-costs.png)
*Figure — one $q_1^*$, two $q_2^*$'s: the filled points sit on the vertical $q_1=8/3$, the hollow complete-information points sit where firm 1's line would cross each of firm 2's lines if firm 1 knew the cost. Source: Gibbons pp. 145–146; calibration $a=10$, $c=2$, $c_H=3$, $c_L=1$, $\theta=\tfrac12$ illustrative.*

Firm 1's line is drawn against $E[q_2]$, so it crosses the vertical only at the mean $8/3$. The
high-cost point lies to the **left** of its complete-information twin (firm 1 produces less than
the 3 it would against a known high-cost rival) and therefore **higher** on firm 2's high-cost line.

---

## Links

- Prev: the BNE definition → [[L07-02-bayesian-nash-equilibrium]].
- Complete-information Cournot (and its IESDS solution): [[../L01/L01-00-map|Lecture 1]],
  [[../L02/L02-00-map|Lecture 2]].
- Code: [[L07-12-python]] §3 (`cournot_bne`, checked against best-response iteration).
- **Exercises (number + page only):** Tadelis 12.2 (p. 266); Gibbons 3.2 and 3.3 (p. 169);
  MWG 8.E.3 (p. 265); Muñoz-Garcia Ch. 7 Ex. 5 (p. 336).
