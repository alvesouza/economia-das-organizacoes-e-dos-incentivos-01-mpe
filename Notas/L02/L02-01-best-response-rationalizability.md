---
tags: [notes, lecture-02, best-response, beliefs, rationalizability, cournot, beauty-contest]
date: 2026-10-16
status: estimated
source: "Tadelis (2013) §4.3.1–4.3.6, printed pp. 69–76 (Defs. 4.5–4.8, Claim 4.2, Props. 4.3–4.4; Battle of the Sexes p. 69; the 3×3 game p. 72; Cournot p. 73–74; p-beauty contest pp. 74–75); Gibbons (1992) §1.2.A pp. 18–21 (graphical IESDS); MWG §8.C pp. 242–245 (G)"
---

# 4.3 · Best responses, beliefs and rationalizability: asking what a rational player *might* do

> **Claim.** Lecture 1 removed what a rational player would **never** do (dominance, IESDS). Rationalizability asks
> the mirror question: what **might** a rational player do? The answer is a best response **to some belief**.
> Iterating "only strategies that are a best response to some belief about strategies that are themselves
> rationalizable" under common knowledge of rationality is the **same machine as IESDS in two-player games**
> ([[L02-08-iesds-rationalizability-revisited]]). It has bite in Cournot (it converges to 30) and in the
> beauty contest (it ends at {0, 1}), and none at all in the Battle of the Sexes.
>
> Prev: [[../L01/L01-00-map|Lecture 1 map]] · Next: [[L02-02-nash-equilibrium]] · Map: [[L02-00-map]]

---

## 1 · U — why beliefs enter

In a decision problem the best action depends only on the problem. In a game it depends on **what the others do**,
and in a static game a player cannot see that, so the player must hold a **belief** (Tadelis p. 71). Tadelis's test
of whether someone is irrational is to ask *"What were you thinking?"*: if some belief about the others makes the
choice optimal, the choice is **rationalized** (p. 69).

The Battle of the Sexes (p. 69; Alex picks the row, Chris the column):

| Alex \ Chris | O | F |
|---|---|---|
| **O** | 2, 1 | 0, 0 |
| **F** | 0, 0 | 1, 2 |

Alex's best choice is O if Chris goes to O and F if Chris goes to F. Nothing is dominated, so Lecture 1's tools say
"anything can happen"; the best choice **flips with the belief**.

---

## 2 · C — the definitions, exactly

**Definition 4.5 (p. 70).** $s_i\in S_i$ is player $i$'s **best response** to $s_{-i}\in S_{-i}$ if
$$v_i(s_i,s_{-i})\ \ge\ v_i(s_i',s_{-i})\qquad\forall s_i'\in S_i .$$

**Claim 4.2 (p. 70).** A rational player who believes the opponents play $s_{-i}$ always chooses a best response to
$s_{-i}$.

Worked (p. 70): if Chris believes Alex goes to the opera, $v_2(O,O)=1>0=v_2(O,F)$, so Chris's best response is O.

**Proposition 4.3 (p. 70).** If $s_i$ is strictly dominated, it is not a best response to any $s_{-i}$.

*Proof, every step.* Strict dominance gives some $s_i'$ with $v_i(s_i',s_{-i})>v_i(s_i,s_{-i})$ for **all** $s_{-i}$.
A best response to a particular $s_{-i}$ needs $v_i(s_i,s_{-i})\ge v_i(s_i',s_{-i})$ for that $s_{-i}$. The two
inequalities contradict each other at every $s_{-i}$, so no such $s_{-i}$ exists. ∎

**Proposition 4.4 (p. 70).** In a finite game, if $s^*$ is a strict dominant-strategy equilibrium, or the unique
survivor of IESDS, then $s_i^*$ is a best response to $s_{-i}^*$ for every $i$.

*Proof (Tadelis's contradiction, pp. 70–71).* A strict dominant-strategy equilibrium uniquely survives IESDS (Lecture 1),
so it suffices to treat the unique survivor. Suppose $s_i^*$ is **not** a best response to $s_{-i}^*$: some $s_i'$ has
$v_i(s_i',s_{-i}^*)>v_i(s_i^*,s_{-i}^*)$. That $s_i'$ was eliminated at some round, while $s_{-i}^*$ was never
eliminated, so the strategy $s_i''$ that eliminated it does even better against $s_{-i}^*$:
$v_i(s_i'',s_{-i}^*)>v_i(s_i',s_{-i}^*)>v_i(s_i^*,s_{-i}^*)$. Repeat; finiteness ends the chain at a strategy that
beats $s_i^*$ against $s_{-i}^*$ and **is never eliminated**, contradicting uniqueness of the survivor. ∎

**Definition 4.6 (p. 72).** A **belief** of player $i$ is a profile of opponents' strategies $s_{-i}\in S_{-i}$.
(Here a belief is a *pure* profile; Lecture 2's §6 replaces it by a probability distribution, Def. 6.4, p. 105.)

**Definition 4.7 (p. 72).** The **best-response correspondence** selects, for each $s_{-i}$, the set
$BR_i(s_{-i})\subseteq S_i$ of best responses.

> **It is a correspondence, not a function, because a belief can have several best responses.**

Worked: the 3×3 game of p. 72.

| P1 \ P2 | L | C | R |
|---|---|---|---|
| **U** | 3, 3 | 5, 1 | 6, 2 |
| **M** | 4, 1 | 8, 4 | 3, 6 |
| **D** | 4, 0 | 9, 6 | 6, 8 |

Against R, player 1's payoffs are U 6, M 3, D 6, so $BR_1(R)=\{U,D\}$. Against L: U 3, M 4, D 4, so
$BR_1(L)=\{M,D\}$. Against C: 5, 8, 9, so $BR_1(C)=\{D\}$.

**Definition 4.8 (p. 73).** $s_i$ is **never a best response** if there is no belief $s_{-i}$ with
$s_i\in BR_i(s_{-i})$.

**Rationalizability (p. 73).** Remove every strategy that is never a best response; in the reduced game, remove
again; iterate. The survivors are the **rationalizable** strategies. Tadelis postpones the formal definition until
beliefs can be mixed (§6.3, p. 114, Def. 6.8) because with pure beliefs only the elimination is too weak
([[L02-08-iesds-rationalizability-revisited]] §2 shows a strategy that is a best response only to a *mixed*
belief).

| Concept | Question asked | Assumption |
|---|---|---|
| Strict dominance | is there something always better? | rationality |
| IESDS | what would a rational player never do, iterated? | common knowledge of rationality |
| **Rationalizability** | what can a rational player justify by some belief, iterated? | common knowledge of rationality |

---

## 3 · Worked — Cournot revisited (§4.3.4, pp. 73–74)

$p(q)=100-q$, $c_i(q_i)=10q_i$. Firm 1 maximizes $v_1=(100-q_1-q_2)q_1-10q_1$.

$$\frac{\partial v_1}{\partial q_1}=100-2q_1-q_2-10=90-2q_1-q_2=0\ \Longrightarrow\ q_1=\frac{90-q_2}{2}.$$

The second derivative is $-2<0$, so this is the maximum. Truncated at zero:

$$BR_1(q_2)=\begin{cases}\dfrac{90-q_2}{2}&0\le q_2<90\\[4pt]0&q_2\ge 90\end{cases}$$

(for $q_2\ge90$ the price is below 10 at any $q_1>0$, so producing loses money). It is a **function**: one best
reply per belief.

| Round | Beliefs about $q_j$ | Best replies $q_i$ | Why |
|---|---|---|---|
| 1 | $[0,\infty)$ | $[0,45]$ | $BR_i$ is largest, 45, at $q_j=0$ |
| 2 | $[0,45]$ | $[22.5,45]$ | $BR_i(45)=22.5$, $BR_i(0)=45$ |
| 3 | $[22.5,45]$ | $[22.5,33.75]$ | $BR_i(45)=22.5$, $BR_i(22.5)=33.75$ |
| 4 | $[22.5,33.75]$ | $[28.125,33.75]$ | $BR_i(33.75)=28.125$ |
| $\infty$ | | $\{30\}$ | fixed point of $q=(90-q)/2$: $3q=90$ |

Each round halves the width (the slope of $BR$ is $-1/2$), so the intervals shrink to the point $q_i=30$, which is
the Nash equilibrium of [[L02-03-cournot]]. Lecture 1 reached the same point by IESDS (Tadelis p. 65; Gibbons
pp. 18–20). Gibbons p. 20–21 adds the warning: with **three** firms the process stops after the first round, because
$Q_{-i}$ can range over $[0,a-c]$ and every $q_i\in[0,(a-c)/2]$ is the best reply to $Q_{-i}=a-c-2q_i$.

![Cournot best-response lines with the rationalizability squares, the Nash equilibrium at (30, 30) and the collusive split](figures/L02-cournot-best-responses.png)
*The shaded squares are rounds 1 and 2 of rationalizability, $[0,45]^2$ and $[22.5,45]^2$; they close in on the crossing at (30, 30). Source: Tadelis §4.3.4, pp. 73–74, and Fig. 5.2, p. 88.*

Read the figure as a staircase: a belief anywhere in the outer square implies a reply inside the inner one, and so on.
The crossing is the only point that survives every round, which is why rationalizability is "unique" here.

> **Interactive companion.** [The Cournot Crossing](companions/companion-cournot-best-responses.html) — move $c_1$
> and $c_2$ apart and watch the crossing move along both lines; the rationalizability argument works for any
> crossing of two lines with slope $-1/2$.

---

## 4 · Worked — the p-beauty contest (§4.3.5, pp. 74–75)

$n$ players choose integers in $\{0,\dots,20\}$; the winners are those closest to $\tfrac34$ of the average; each
player pays 1 and winners split the pot. Tadelis's example: $n=3$, choices $1,5,18$; average 8; $\tfrac34\cdot8=6$;
player 2 (at 5) is closest and wins.

**Round 1: 20 is never a best response.** If you believe the average is below 20, a lower number is closer to
$\tfrac34$ of it. If you believe everyone else plays 20, then choosing 20 ties with everyone, while 19 wins alone:
the average is $\frac1n[(n-1)20+19]\in[19.5,20)$, so $\tfrac34$ of it lies in $[14.625,15)$, and 19 is closer
than 20 (footnote 6, p. 75). So 20 is beaten under **every** belief.

**Rounds 2–19.** In the reduced game the same argument removes the new top number each time, leaving
$S_i^{19}=\{0,1\}$. For $n>2$ both survive (each is a best response to "everyone else plays it"); for $n=2$ only
0 survives (p. 75; the proofs are Tadelis exercises 4.8–4.9, p. 78).

> **Common knowledge of rationality is doing all the work.** Tadelis notes that real classes rarely produce a
> winning number below 4 (footnote 7, p. 75): the prediction is only as good as the assumption that everyone
> reasons all 19 rounds deep.

---

## 5 · C — evaluating rationalizability (§4.3.6, p. 76)

| Criterion | Verdict |
|---|---|
| Existence | always (as IESDS) |
| Uniqueness | sometimes sharp (Cournot, beauty contest); in the Battle of the Sexes **"anything can happen"** |
| Pareto | survivors need not be Pareto optimal (the prisoner's dilemma survives intact) |

> **Rationalizability lets each player hold *some* belief; it never asks the beliefs to be right.** In the Battle of
> the Sexes, Alex can rationally go to O believing Chris goes to O while Chris rationally goes to F believing Alex
> goes to F. Removing that dissonance is the step to Nash equilibrium ([[L02-02-nash-equilibrium]]).

---

## 6 · G — the formal version (MWG §8.C, pp. 242–245)

MWG Def. 8.C.1 (p. 243) defines a best response among **mixed** strategies and "never a best response" against all
mixed profiles of the rivals; Def. 8.C.2 (p. 243) calls the survivors of the iterated removal the **rationalizable
strategies** (Bernheim 1984, Pearce 1984). The set of rationalizable strategies is no larger than the set surviving
IESDS, and the removal order does not matter. Not examinable unless the lecture states it.

---

## Links

- Neighbours: [[L02-02-nash-equilibrium]] (the beliefs made correct), [[L02-08-iesds-rationalizability-revisited]]
  (the equivalence with IESDS once beliefs can be mixed).
- Lecture 1 (dominance and IESDS, the same Cournot game by elimination): [[../L01/L01-00-map|Lecture 1]].
- Rules pack: [[../../rules/game-theory|rules/game-theory]] items 2, 6.
- Practice (statements in the books): Tadelis 4.6 (p. 77), 4.8, 4.9 and 4.10 (p. 78); Gibbons 1.2 (p. 48);
  MWG 8.C.1 (p. 263).
