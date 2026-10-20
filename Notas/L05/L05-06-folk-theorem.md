---
tags: [notes, lecture-05, repeated-games, folk-theorem, feasible-payoffs, convex-hull, individual-rationality]
date: 2026-10-16
status: estimated
source: "Tadelis (2013) §10.6, Definitions 10.6–10.7, Figures 10.3–10.5, Theorem 10.1, the alternating-path example and the Remark, pp. 209–214; Gibbons (1992) §2.3.B, feasible payoffs, average payoff, Friedman's Theorem, Fudenberg–Maskin, pp. 96–99, Appendix 2.3.B, pp. 100–102; MWG App. A to Ch. 12, Props. 12.AA.3 (p. 420) and 12.AA.5 (p. 422), minimax payoff (p. 421)"
---

# 10.6 · The folk theorem: with enough patience, almost anything goes

> **Claim.** Every payoff vector that is **feasible** (a weighted average of stage-game payoffs) and
> gives **each player more than a stage Nash equilibrium** can be approximated by a subgame-perfect
> equilibrium of $G(\delta)$ once $\delta$ is close enough to 1 (Theorem 10.1). Cooperation is one
> of a continuum of equilibria — so is perpetual defection, and so is a lopsided path that gives one
> player $4.6$ and the other $1$. **Repetition explains how cooperation *can* be sustained; it does
> not predict that it *will* be.**
>
> Prev: [[L05-05-critical-discount-factor]] · Next: [[L05-07-formulas]] · Map: [[L05-00-map]]

---

## 1 · C — feasible payoffs: convex combinations and the convex hull

**Definition 10.6** (p. 209). *Consider two vectors $v=(v_1,\dots,v_n)$ and $v'=(v_1',\dots,v_n')$ in
$\mathbb R^n$. We say that the vector $\hat v=(\hat v_1,\dots,\hat v_n)$ is a convex combination of $v$
and $v'$ if there exists some number $\alpha\in[0,1]$ such that $\hat v=\alpha v+(1-\alpha)v'$, or
$\hat v_i=\alpha v_i+(1-\alpha)v_i'$ for all $i$.*

**Worked (Figure 10.3, p. 210).** $\alpha=0.6$, $v=(4,4)$, $v'=(5,-1)$:
$$\hat v=0.6(4,4)+0.4(5,-1)=(2.4+2.0,\ 2.4-0.4)=(4.4,\ 2).$$

**Definition 10.7** (p. 210). *Given a set of vectors $V=\{v^1,\dots,v^k\}$ in $\mathbb R^n$, the
convex hull of $V$ is*
$$\mathrm{CoHull}(V)=\Big\{v\in\mathbb R^n:\ \exists(\alpha_1,\dots,\alpha_k)\in\mathbb R_+^k,\ \sum_{j=1}^k\alpha_j=1,\ \text{such that } v=\sum_{j=1}^k\alpha_jv^j\Big\}.$$

Apply it to **average payoffs**. Repeating a pure profile $s$ forever gives average payoff $u(s)$
([[L05-03-discounting-histories-strategies]] §3), so the pure-profile payoff vectors are achievable
averages, and their convex hull is the set of **feasible payoffs** (p. 211). For Tadelis's PD,
$V=\{(4,4),(5,-1),(-1,5),(1,1)\}$ (Figure 10.4, p. 211).

Gibbons (p. 96) calls a payoff feasible if it is a convex combination of the pure-strategy payoffs,
and notes how to *get* one exactly: a **public randomizing device** — flip a fair coin to choose
between $(L_1,R_2)$ and $(R_1,L_2)$ and the expected payoff is $(2.5,2.5)$. Without the device,
Tadelis gets there **over time**, by alternating (§3).

---

## 2 · C — Theorem 10.1

**Theorem 10.1 (The Folk Theorem)** (p. 211). *Let $G$ be a finite, simultaneous-move game of
complete information, let $(v_1^*,\dots,v_n^*)$ denote the payoffs from a Nash equilibrium of $G$,
and let $(v_1,\dots,v_n)$ be a feasible payoff of $G$. If $v_i>v_i^*$ for all $i\in N$, and if
$\delta$ is sufficiently close to 1, then there exists a subgame-perfect equilibrium of the
infinitely repeated game $G(\delta)$ that achieves an average payoff arbitrarily close to
$(v_1,\dots,v_n)$.*

Gibbons's **Friedman (1971) Theorem** (p. 97) is the same statement with "achieves $(x_1,\dots,x_n)$
as the average payoff" (exact, with the randomizing device), $e_i$ the Nash payoffs and $x_i$ the
target.

**The intuition in four steps** (pp. 211–212):

1. The target $v$ is a weighted average of pure-profile payoffs (it is feasible).
2. With $\delta$ near 1, a deterministic **sequence** of pure profiles can mimic those weights, so its
   average payoff is (close to) $v$.
3. Because $v_i>v_i^*$ for everyone, reverting to the stage Nash equilibrium is a **punishment for
   every player** — the "wedge".
4. As $\delta\to1$, even the largest one-period gain "is dwarfed by an infinite series of even small
   losses", so the wedge deters every deviation.

**The proof for a stationary target** (Gibbons, Appendix 2.3.B, pp. 100–102). Play the profile
$a_x$ that yields $x$; after any deviation, play the stage NE $a_e$ forever. Let $d_i$ be $i$'s best
one-shot deviation payoff against $a_x$, so $d_i\geq x_i>e_i$. By the computation of
[[L05-05-critical-discount-factor]] §1, $i$ conforms iff $\delta\geq(d_i-x_i)/(d_i-e_i)$; so the
profile is a Nash equilibrium iff
$$\delta\;\geq\;\max_i\frac{d_i-x_i}{d_i-e_i}\;<\;1 .$$
Subgame perfection: after an all-$a_x$ history the continuation is the same trigger profile (a Nash
equilibrium of the game); after any other history it is $a_e$ forever (also one). $\blacksquare$

![Payoff space for Tadelis's Prisoner's Dilemma: the grey feasible quadrilateral with corners (-1,5), (4,4), (5,-1), (1,1); the green folk-theorem region where both payoffs exceed 1, with corners (1,1), (1,4.6), (4,4), (4.6,1); the point (4.4,2); and an orange segment from (3,1) at delta = 1/2 to (2,2) as delta tends to 1, the alternating path's average payoffs, with the delta = 0.9 point (2.158, 1.842) marked](figures/L05-folk-theorem.png)
*Figure — feasible set (grey), its strictly individually rational part (green), Definition 10.6's $(4.4,2)$, and the alternating path's averages for $\delta\in[1/2,1)$. Source: Figures 10.3–10.5 and pp. 209–214.*

The green region's top-left corner is where the edge from $(-1,5)$ to $(4,4)$ — the line
$v_2=5-(v_1+1)/5$ — meets $v_1=1$: $v_2=5-2/5=4.6$. Every point in the green interior, including
lopsided ones near $(1,4.6)$, is an SPE average for $\delta$ high enough. The orange segment starts
at $(3,1)$: at $\delta=1/2$ player 2's average on the alternating path is exactly the punishment
payoff $1$, the edge of the region — which is why §3 finds $\delta\geq1/2$.

> **Interactive companion.** [The Patience Threshold](companions/companion-grim-trigger.html) — the right panel redraws the feasible set and the folk-theorem region as $T$, $R$, $P$, $S$ move, and plots the alternating path at the current $\delta$.

---

## 3 · Worked — reaching $(2,2)$ by alternating (pp. 212–214)

$(2,2)=\tfrac12(5,-1)+\tfrac12(-1,5)$ — **not** a payoff of any pure profile, but feasible
(Figure 10.5, p. 212).

**Strategies** (p. 212):

- **Player 1:** in period 1 play $F$. In even periods play $M$ iff the pattern so far was $(F,m),(M,f),(F,m),\dots$; otherwise $F$. In odd periods $t=3,5,\dots$ play $F$.
- **Player 2:** in period 1 play $m$. In odd periods $t=3,5,\dots$ play $m$ iff the pattern was respected; otherwise $f$. In even periods play $f$.

On the path the outcomes alternate $(F,m),(M,f),(F,m),\dots$, paying $(5,-1),(-1,5),\dots$

**Average payoffs, every step.** Split player 1's stream by parity:
$$\bar v_1=(1-\delta)\big[5+\delta(-1)+\delta^2(5)+\delta^3(-1)+\dots\big]
=(1-\delta)\big[5(1+\delta^2+\delta^4+\dots)+(-1)(\delta+\delta^3+\delta^5+\dots)\big].$$
Both brackets are geometric series in $\delta^2$: $1+\delta^2+\dots=\dfrac1{1-\delta^2}$ and
$\delta+\delta^3+\dots=\dfrac{\delta}{1-\delta^2}$. With $1-\delta^2=(1-\delta)(1+\delta)$,
$$\bar v_1=(1-\delta)\,\frac{5-\delta}{(1-\delta)(1+\delta)}=\boxed{\frac{5-\delta}{1+\delta}},\qquad
\bar v_2=\boxed{\frac{-1+5\delta}{1+\delta}}\ \text{(same steps, roles swapped)}.$$
As $\delta\to1$: $\bar v_1\to4/2=2$ and $\bar v_2\to4/2=2$.

**Subgame perfection: three kinds of history** (one-stage deviation principle, Prop. 10.3):

| State | Follow | Best one-stage deviation | Condition |
|---|---|---|---|
| **Punishment** ($(F,f)$ forever) | $1$ per period | $M$ or $m$: $-1$ today, punishment continues | always holds (loses 2) |
| **Player 1's good period** (he gets 5) | average $\dfrac{5-\delta}{1+\delta}$ | $M$ against $m$: $4$ today, then $1$ forever: $(1-\delta)4+\delta$ | holds for **all** $\delta\in(0,1)$ |
| **Player 1's bad period** (he gets $-1$) | average $\dfrac{-1+5\delta}{1+\delta}$ | $F$ against $f$: $1$ today, then $1$ forever: average $1$ | $\delta\geq\tfrac12$ |

*Good period, every step.* Multiply $\frac{5-\delta}{1+\delta}\geq4-3\delta$ by $1+\delta$:
$5-\delta\geq(4-3\delta)(1+\delta)=4+\delta-3\delta^2$, i.e. $3\delta^2-2\delta+1\geq0$. The
discriminant is $4-12<0$, so the quadratic is always positive: **the condition always holds**.

*Bad period, every step.* $\frac{-1+5\delta}{1+\delta}\geq1\iff-1+5\delta\geq1+\delta\iff4\delta\geq2\iff\delta\geq\tfrac12$.

Player 2's checks are the mirror images. **So the alternating path is an SPE iff $\delta\geq1/2$,
and its averages approach $(2,2)$ as $\delta\to1$.**

> **The binding constraint is the bad period**: a player taking $-1$ today must be held there by the
> promise of $5$ tomorrow. In general the bad period needs $\dfrac{S+\delta T}{1+\delta}\geq P$, i.e.
> $\delta\geq\dfrac{P-S}{T-P}$ — here the **sucker payoff matters**, unlike grim trigger on $(R,R)$.

### 3.1 · The Remark: fine-tuning without $\delta\to1$ (p. 214)

At $\delta=0.9$ the alternating path gives $\bar v_1=\frac{5-0.9}{1.9}=2.158$ and
$\bar v_2=\frac{-1+4.5}{1.9}=1.842$. Tadelis then alters single far-off periods to pull the averages
toward $(2,2)$: a change at $t=26$ moves them by $0.151$ and $0.076$ (to $2.007$, $1.918$), one at
$t=36$ by $0.013$ and $0.066$ (to $1.994$, $1.984$).

*Reading note.* Those four adjustments equal $\Delta\cdot\delta^{t-1}/(1+\delta)$ — e.g.
$4\times0.9^{25}/1.9=0.151$ — which is the effect of changing the outcome **in period $t$ and in
every second period after it** ($(1-\delta)\Delta(\delta^{t-1}+\delta^{t+1}+\dots)$). A one-off change
in period 26 alone moves player 1's average by $(1-\delta)\delta^{25}\cdot4=0.029$. The point of the
Remark is unaffected: **far-off periods are a fine dial on the average**, so targets can be hit even
at a fixed $\delta<1$. (Verified in [[L05-09-python]] §6.)

---

## 4 · U/G — what the threshold is: Nash payoffs or minimax payoffs

Tadelis's and Friedman's theorem punishes with a stage **Nash** equilibrium, so it covers payoffs
above $v_i^*$. Gibbons (pp. 98–99) defines the **reservation payoff** $r_i$, the largest payoff $i$ can
guarantee whatever the others do; necessarily $r_i\leq e_i$. In the PD $r_i=e_i=1$ (fink guarantees
at least 1). In Cournot $r_i=0<e_i$ (only producing nothing guarantees anything).

- **Fudenberg and Maskin (1986):** for two players, $r_i$ can replace $e_i$ — any feasible payoff with
  $x_i>r_i$ is an SPE average for $\delta$ near 1 (Gibbons, p. 99).
- **MWG**: Prop. 12.AA.3 (p. 420) is the **Nash-reversion folk theorem**; the **minimax payoff**
  $\underline v_i$ (p. 421) is the lowest payoff the rivals can hold $i$ to, payoffs above it are
  **individually rational**, and Prop. 12.AA.5 (p. 422), *the* Folk Theorem, supports every feasible
  individually rational payoff as $\delta\to1$.

**G**, not examinable unless the lecture brings it. In Tadelis's PD the two versions draw the same
green region.

---

## 5 · U — what "almost anything goes" means for prediction

Tadelis's own word for the result is "rather disturbing" (p. 209), and the section title is "Almost
Anything Goes".

| What the folk theorem delivers | What it does not |
|---|---|
| a proof that cooperation **can** be self-enforcing among patient players | a prediction of **which** equilibrium is played |
| a whole region of SPE payoffs, efficient ones included | a reason to rule out $(1,1)$ — fink forever is still an SPE (Prop. 10.2) |
| conditions: patience and **observable** deviations | anything about settings where deviations cannot be seen (price wars, Tadelis p. 203 → [[../L06/L06-00-map|Lecture 6]]) |

> **"A prediction that does not select among equilibria is not a prediction"**
> ([[../../rules/game-theory|rules/game-theory]] item 3). The folk theorem moves the
> question from *can they cooperate?* to *which of many equilibria will they coordinate on, and how?*
> — focal points, communication, institutions. Lecture 6's applications (tacit collusion,
> reputation, relational contracts) are cases where the context picks the equilibrium.

---

## Links

- Previous: the threshold that the folk theorem drives to 1 — [[L05-05-critical-discount-factor]].
- Support: [[L05-07-formulas]], [[L05-08-pitfalls]], [[L05-09-python]].
- Applications of the same machinery: [[../L06/L06-00-map|Lecture 6]].
- Mixed strategies and Nash payoffs of the stage game: [[../L02/L02-00-map|Lecture 2]].
- Rules: [[../../rules/game-theory|rules/game-theory]] items 3, 4 and 14.
- Exercises: Tadelis 10.12 (p. 219; uses §10.5's trust game, so after [[../L06/L06-00-map|Lecture 6]]), 10.9 (pp. 218–219); MWG Exercise 12.AA.1 (p. 420).
