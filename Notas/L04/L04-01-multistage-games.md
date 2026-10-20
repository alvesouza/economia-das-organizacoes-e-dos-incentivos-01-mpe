---
tags: [notes, lecture-04, multistage-games, histories, strategies]
date: 2026-10-16
status: estimated
source: "Tadelis (2013) Ch. 9 intro and §9.1–9.3, printed pp. 175–180 (Prisoner-Revenge Game pp. 176–177, Figure 9.1 p. 178, the n-firm pricing example p. 179); Gibbons (1992) §2.2.A, pp. 71–73"
---

# 9.1–9.3 · A multistage game is one extensive form: payoffs, histories, strategies

> **Claim.** Playing one game after another, with each outcome observed before the next stage,
> is **one** extensive-form game. Payoffs add up with discounting, and a strategy is a plan that
> names an action **for every history**. That richer strategy space lets later play be made to
> depend on earlier play, and that is where the economics of the chapter comes from.

Prev: — · Next: [[L04-02-carrot-and-stick]] · Map: [[L04-00-map]]

---

## 1 · U — why bother with stages

Tadelis opens with two firms that compete in one market and later meet in another, and with
lawmakers who sit on one committee and then, if re-elected, on the next (p. 175). Two questions
follow, and the chapter answers both:

| Question (p. 175) | Answer (pp. 175–176) |
|---|---|
| Should rational, forward-looking players treat the sequence as **one grand game**? | **Yes.** They anticipate future games and use them. |
| Must they play a **stage-game Nash equilibrium in every stage**? | **No.** If future behaviour can be conditioned on past outcomes, they can create **credible, self-enforcing incentives** for early-stage behaviour that is not a stage-game equilibrium. |

> **The core insight of multistage games (p. 176): if players can condition future behaviour on
> past outcomes, the set of self-enforcing outcomes becomes richer.**

---

## 2 · C — the definition (§9.1, p. 176)

A **multistage game** is a **finite** sequence of normal-form **stage-games**, each a
simultaneous-move game of complete but imperfect information, played by the **same players** in
periods $t=1,2,\dots,T$. Two conventions:

1. after each stage **all players observe its outcome**, and this is common knowledge;
2. total payoffs are evaluated from the **sequence** of stage outcomes (§2 below).

Infinite sequences of the **same** stage-game are repeated games, Chapter 10
([[../L05/L05-00-map|Lecture 5]]); games in which some stages are played before earlier outcomes
are revealed are outside the text (footnotes 1–2, p. 176).

**Gibbons's version (§2.2.A, p. 72).** Players 1 and 2 choose $a_1,a_2$ simultaneously; players
3 and 4 observe $(a_1,a_2)$ and then choose $a_3,a_4$ simultaneously; payoffs are
$u_i(a_1,a_2,a_3,a_4)$. Players 3 and 4 may be players 1 and 2 again (a multistage game in
Tadelis's sense), or different people (the boss and the workers of a tournament,
[[L04-04-two-stage-applications]] §3).

### 2.1 · The running example: the Prisoner-Revenge Game (pp. 176–177)

**Stage 1 ($t=1$), the Prisoner's Dilemma**, mum ($M$/$m$) or fink ($F$/$f$), uppercase for
player 1:

| | $m$ | $f$ |
|---|---|---|
| $M$ | $4,\ 4$ | $-1,\ 5$ |
| $F$ | $5,\ -1$ | $\mathbf{1,\ 1}$ |

**Stage 2 ($t=2$), the Revenge Game**, loner ($L$/$l$) or join a gang ($G$/$g$): two loners get 0
each; two gang members fight, $-3$ each; a loner facing a gang member gets $-4$ and the gang member
$-1$:

| | $l$ | $g$ |
|---|---|---|
| $L$ | $\mathbf{0,\ 0}$ | $-4,\ -1$ |
| $G$ | $-1,\ -4$ | $\mathbf{-3,\ -3}$ |

**Each stage on its own.**

- Stage 1: $F$ strictly dominates $M$ ($5>4$, $1>-1$), so the unique NE is $(F,f)$.
- Stage 2: two pure NE. $(L,l)$: against $l$, $L$ pays $0>-1$. $(G,g)$: against $g$, $G$ pays
  $-3>-4$. And a mixed NE. **Worked:** let player 2 play $l$ with probability $q$. Player 1 is
  indifferent when
  $$u_1(L)=0\cdot q+(-4)(1-q)=4q-4,\qquad u_1(G)=-1\cdot q+(-3)(1-q)=2q-3,$$
  $$4q-4=2q-3\iff q=\tfrac12 .$$
  By symmetry player 1 also plays $L$ with probability $\tfrac12$ — Tadelis's "(verify this!)",
  p. 177. Each then expects $4(\tfrac12)-4=-2$.

> **The two pure equilibria of stage 2 are what makes this game interesting: a friendly one
> worth 0 and a gang war worth $-3$.** Note 02 turns the gap between them into a carrot and a
> stick.

---

## 3 · C — payoffs: the discounted sum (§9.2, p. 177)

With $v_{it}$ player $i$'s payoff from the stage-$t$ outcome and a common discount factor
$\delta\in[0,1]$,

$$\boxed{\;v_i=v_{i1}+\delta v_{i2}+\delta^2v_{i3}+\dots+\delta^{T-1}v_{iT}=\sum_{t=1}^{T}\delta^{t-1}v_{it}\;}$$

A higher $\delta$ means more patient players; $\delta=0$ means only the current stage matters.

**Worked (p. 177).** Play $(F,m)$ then $(L,g)$:

$$v_1=5+\delta(-4),\qquad v_2=-1+\delta(-1).$$

With $\delta=\tfrac12$: $v_1=5-2=3$ and $v_2=-1-0.5=-1.5$.

Figure 9.1 (p. 178) draws the whole game as one tree whose 16 terminal nodes carry these
discounted sums. That the payoffs "arrive" only at the end of the tree is harmless: strategically
only the sum matters (p. 177).

> **Notation.** Tadelis writes $v_i$ for total payoffs in multistage games, while the Lecture 1
> slides write $u_i$ for the payoff function of a normal-form game
> $G=\langle I,\{S_i\},\{u_i\}\rangle$. These notes keep Tadelis's $v_i$ for the discounted total
> and $v_{it}$ for the stage payoff. Reconcile with the slides when they arrive.

---

## 4 · C — strategies condition on histories (§9.3, pp. 178–180)

Because each stage's outcome is revealed before the next, **the number of information sets of a
player at stage $t$ equals the number of possible outcomes of stages $1,\dots,t-1$** (p. 178).
Inside a stage the players still move without seeing each other, so each information set holds
several nodes.

**Prisoner-Revenge (p. 179).** Stage 1 has four outcomes $Mm,Mf,Fm,Ff$, so each player has
**four** stage-2 information sets. A pure strategy is a quintuple

$$s_i=\bigl(s_{i1},\ s_{i2}(Mm),\ s_{i2}(Mf),\ s_{i2}(Fm),\ s_{i2}(Ff)\bigr).$$

**Counting.** Each of the five entries takes one of two values, so

$$|S_i|=2^5=32,\qquad |S_1\times S_2|=32\times32=1024$$

pure-strategy profiles (p. 179). That is why the extensive form, not a $32\times32$ matrix, is the
tool.

**In general (p. 179).** A pure strategy is

$$s_i=\{s_{i1},\ s_{i2}(h_1),\ \dots,\ s_{it}(h_{t-1}),\ \dots,\ s_{iT}(h_{T-1})\},$$

where $h_{t-1}\in H_{t-1}$ is a **history**, the sequence of outcomes before $t$. A behavioural
strategy replaces each action by a randomization $\sigma_{it}(h_{t-1})$ (p. 179).

**Worked: $n$ firms pricing in $T$ markets (p. 179).** Firm $i$'s pure strategy is a list of
prices $p_{i1},p_{i2}(h_1),\dots,p_{iT}(h_{T-1})$, with
$h_{t-1}=((p_{11},\dots,p_{n1}),\dots,(p_{1,t-1},\dots,p_{n,t-1}))$. **Each entry after the first is
a function from a continuum of histories to a price.** Strategy spaces in multistage games are
huge even when every stage is simple.

> **A strategy is a complete contingent plan** (the Lecture 1 slides' definition): in a
> multistage game "complete" means *one action for every history, including histories the plan
> itself rules out.* Off-path entries are not decoration; note 02 shows they carry the threats.

---

## 5 · C — the solution concept: subgame perfection, worked stage by stage (Gibbons §2.2.A)

Gibbons solves the two-stage class "in the spirit of backwards induction" (pp. 72–73):

1. **Stage 2 first.** For each first-stage outcome $(a_1,a_2)$, find the NE
   $(a_3^*(a_1,a_2),a_4^*(a_1,a_2))$ of the game that remains. Here the first step is a *game*, not
   a one-person optimization as in Lecture 3.
2. **Substitute it back.** Players 1 and 2 then play the simultaneous game with payoffs
   $u_i(a_1,a_2,a_3^*(a_1,a_2),a_4^*(a_1,a_2))$.
3. If that game has NE $(a_1^*,a_2^*)$, the **subgame-perfect outcome** is
   $(a_1^*,a_2^*,a_3^*(a_1^*,a_2^*),a_4^*(a_1^*,a_2^*))$.

Gibbons assumes stage 2 has a **unique** NE for every $(a_1,a_2)$ (p. 72). Then step 1 is
well defined and the method needs no choice. **Tadelis's Prisoner-Revenge Game deliberately
breaks that assumption**, and that is the whole of note 02.

> **Why not threats that are not stage-2 equilibria?** Gibbons, p. 73: when play reaches stage 2,
> at least one of players 3 and 4 will not carry out such a threat, exactly because it is not a NE
> of the game that remains. **This is subgame perfection
> ([[../L03/L03-00-map|Lecture 3]]) applied to stages.**

---

## Links

- Next: [[L04-02-carrot-and-stick]] (Propositions 9.1–9.3, the carrot and the stick).
- Applications of the two-stage method: [[L04-04-two-stage-applications]].
- Subgame perfection and backward induction: [[../L03/L03-00-map|Lecture 3]]; repeated games
  (same stage-game, possibly forever): [[../L05/L05-00-map|Lecture 5]].
- Rules pack: [[../../rules/game-theory|rules/game-theory]] items 1–2 (specify the game,
  name the concept).
- **Exercises (number and page only):** Tadelis 9.1 (p. 186), 9.2 (pp. 186–187).
