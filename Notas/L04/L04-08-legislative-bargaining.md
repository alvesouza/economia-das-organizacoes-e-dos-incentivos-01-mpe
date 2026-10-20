---
tags: [notes, lecture-04, bargaining, legislative-bargaining, baron-ferejohn]
date: 2026-10-16
status: estimated
source: "Tadelis (2013) §11.4, printed pp. 229–235: closed rule, eqs. (11.6)–(11.8); open rule with guaranteed success (11.9) and risky success (11.10)–(11.13); footnotes 7–8; §11.5 Summary pp. 235–236"
---

# 11.4 · Legislative bargaining: majority rule, random proposers, and amendments

> **Claim.** Replace "both must agree" by "a majority must agree" and "alternate" by "a random
> legislator proposes" (Baron and Ferejohn, 1989). In the symmetric stationary equilibrium the
> proposer buys the **cheapest** majority, paying each partner the discounted continuation value
> $\delta/N$. Under a **closed rule** (no amendments) that is worth $1-\delta\frac{N-1}{2N}$ to the
> proposer; an **open rule** destroys targeting and cuts the proposer to $\frac{1}{1+2\delta}$ when
> $N=3$, unless she gambles on a minimal coalition, which pays when $\delta>\sqrt3-1$.

Prev: [[L04-07-rubinstein-infinite-horizon]] · Next: [[L04-09-bargaining-private-information]] · Map: [[L04-00-map]]

> **Scope note.** §11.4 lies inside the study guide's page range (pp. 220–237). Whether the lecture
> covers it is unknown until the slides arrive; the section is tagged C on that basis and should be
> rechecked at reconcile.

---

## 1 · C — the two departures (pp. 229–230)

1. $N$ players, $N$ odd; $\frac{N+1}{2}$ votes pass a proposal.
2. Each period **every player is equally likely (prob. $1/N$) to be the proposer**. No fixed order,
   so no last mover.

With three or more players the game has many SPE (Herrero, 1985; footnote 4, p. 230). Baron and
Ferejohn select **symmetric stationary** equilibria: a proposer makes the same proposal whenever
called on, and responders vote on the current proposal against their expected continuation. Then
the game "starts over" after each rejection, and every player's expected value at the start of a
period is the same number $v$ (pp. 230–231).

---

## 2 · C — closed rule (§11.4.1, pp. 230–231)

**Responders.** Rejecting is worth $\delta v$, so responder $i$ accepts iff $x_i\ge\delta v$.

**Proposer.** She needs $\frac{N+1}{2}$ votes, her own plus $\frac{N-1}{2}$ others. She picks
$\frac{N-1}{2}$ partners at random, pays each exactly $\delta v$, gives the rest 0, and keeps

$$k=1-\frac{N-1}{2}\,\delta v.\tag{11.6}$$

**Value of the game.** With probability $\frac1N$ a player proposes ($k$); with probability
$\frac{N-1}{N}$ she responds, and then is chosen as a partner with probability $\frac12$ (getting $\delta v$),
else 0:

$$v=\frac{k}{N}+\frac{N-1}{2N}\,\delta v.\tag{11.7}$$

**Solve.** Substitute (11.6): $v=\frac1N-\frac{N-1}{2N}\delta v+\frac{N-1}{2N}\delta v=\frac1N$. Then

$$\boxed{\;v=\frac1N,\qquad k(N)=1-\delta\,\frac{N-1}{2N}\;}\tag{11.8}$$

$v=1/N$ is forced by symmetry and immediate agreement; the interesting object is $k$.

**Worked.**

| | $\delta=0.9$ | $\delta\to1$ |
|---|---|---|
| $N=3$: $k=1-\delta/3$ | $1-0.3=\mathbf{0.70}$; each partner $\delta/3=0.30$ | $2/3$ |
| $N=5$: $k=1-\delta\cdot4/10$ | $1-0.36=\mathbf{0.64}$; two partners at $0.18$ | $0.6$ |
| $N\to\infty$: $k\to1-\delta/2=\frac{2-\delta}{2}$ | $0.55$ | $1/2$ |

**Two readings (pp. 231–232).**

1. As in Rubinstein, $k$ **falls with $\delta$**: patient responders must be paid more.
2. As $N$ grows, each partner costs less ($\delta/N$) but more partners are needed; the second force
   wins and $k$ falls. Yet relative to a partner the proposer's share $k/(\delta/N)$ **rises without
   bound**: more players means more ways to form a coalition.

---

## 3 · C — open rule, guaranteed success (§11.4.2.1, pp. 232–233), $N=3$

After a proposal, one of the other two is drawn as **amender**. She can second it (then a majority
vote) or offer an amendment, which is voted against it and becomes the new baseline next period.

**Guaranteed success.** The proposer keeps $k$ and offers each of the others $\frac{1-k}{2}$, so whoever
is drawn seconds it. The amender's alternative is to propose herself next period, worth $\delta k$ by
symmetry. The proposer pays exactly that:

$$\frac{1-k}{2}=\delta k\iff1-k=2\delta k\iff\boxed{\;k=\frac{1}{1+2\delta}\;}\tag{11.9}$$

**Closed beats open (footnote 7, p. 233).**

$$\Bigl(1-\frac\delta3\Bigr)-\frac1{1+2\delta}=\frac{(3-\delta)(1+2\delta)-3}{3(1+2\delta)}=\frac{5\delta-2\delta^2}{3(1+2\delta)}=\frac{\delta(5-2\delta)}{3(1+2\delta)}>0 .$$

Under a closed rule the proposer can play some legislators against others; under an open rule a
shortchanged legislator amends at her expense. As $\delta\to1$, $k\to\frac13$: an equal split, against
$\frac23$ under the closed rule (p. 233).

---

## 4 · C — open rule, risky success (§11.4.2.2, pp. 233–235)

The proposer offers $1-k$ to **one** partner and 0 to the third. If the partner is drawn as amender
she seconds; if the excluded player is drawn she amends to $(k$ for herself, $1-k$ to the same
partner, $0$ to the original proposer$)$ and wins ("selective inclusion"). Let $v(k)$ be the
proposer's expected payoff and $v(0)$ the excluded player's.

$$v(k)=\tfrac12k+\tfrac12\,\delta v(0)\tag{11.10}$$
$$v(0)=\tfrac12\,\delta v(k)\tag{11.11}$$
$$1-k=\delta v(k)\tag{11.12}$$

(11.10): with prob. $\tfrac12$ the partner seconds and the proposer gets $k$; otherwise she is the
excluded one next period. (11.11): with prob. $\tfrac12$ the excluded player is drawn and becomes
proposer next period. (11.12): the partner could reject and stand in the proposer's shoes next period.

**Solve.** Put (11.11) in (11.10): $v(k)=\frac k2+\frac{\delta^2}{4}v(k)$, so $v(k)=\frac{2k}{4-\delta^2}$.
Then (11.12): $1-k=\frac{2\delta k}{4-\delta^2}$, so $k\,(4-\delta^2+2\delta)=4-\delta^2$:

$$\boxed{\;k=\frac{4-\delta^2}{4+2\delta-\delta^2},\qquad v(k)=\frac{2}{4+2\delta-\delta^2}\;}\tag{11.13}$$

**Closed still beats it (footnote 8, p. 235):**
$\bigl(1-\frac\delta3\bigr)-\frac{2}{4+2\delta-\delta^2}=\frac{6+2\delta-5\delta^2+\delta^3}{12+6\delta-3\delta^2}>0$
(numerator $(3-\delta)(4+2\delta-\delta^2)-6$; at $\delta=1$ it is $4$).

**Risky against guaranteed (p. 235).**

$$\frac{2}{4+2\delta-\delta^2}>\frac1{1+2\delta}\iff2+4\delta>4+2\delta-\delta^2\iff\delta^2+2\delta-2>0\iff\boxed{\;\delta>\sqrt3-1\approx0.732\;}$$

![Proposer's expected payoff against delta for three legislators: closed rule 1 - delta/3 on top, open-rule guaranteed 1/(1+2 delta) falling steeply, open-rule risky 2/(4+2 delta - delta^2) falling gently and crossing the guaranteed curve at delta = sqrt(3) - 1](figures/L04-legislative-shares.png)
*Figure — (11.8) with $N=3$, (11.9) and (11.13). The closed rule dominates both open-rule payoffs; the risky strategy beats the guaranteed one to the right of $\sqrt3-1$. Source: Tadelis pp. 231–235.*

**Worked, $\delta=0.9$:** closed $0.700$; guaranteed $1/2.8=0.357$; risky $k=3.19/4.99=0.639$ with
expected payoff $2/4.99=0.401>0.357$. Patient legislators make buying off **both** potential amenders
too expensive, so the proposer caters to one and accepts a 50% chance of failure and **delay**,
which, unlike in Rubinstein's game, now happens in equilibrium (p. 235).

---

## 5 · U — what the chapter summary asks you to keep (§11.5, pp. 235–236)

| Summary point | Where |
|---|---|
| The discount factor drives the split; more patience, more equal shares | notes 06–07, §2 here |
| Protocol and agreement rules matter a lot | closed vs open rule, §3–§4 |
| Finite alternating games: last-mover advantage; discounting: first-mover advantage | note 06 |
| Infinite horizon or random proposers: **no last-mover advantage**, only the first-mover one | note 07, §2 here |

---

## Links

- Previous / next: [[L04-07-rubinstein-infinite-horizon]] · [[L04-09-bargaining-private-information]].
- Python: [[L04-12-python]] §4 (closed and open rule, the $\sqrt3-1$ threshold).
- Pitfalls: [[L04-11-pitfalls]] item 13.
- **Exercises (number and page only):** Tadelis 11.7 (p. 237); Muñoz-Garcia Ch. 6 Ex. 8 (p. 303).
