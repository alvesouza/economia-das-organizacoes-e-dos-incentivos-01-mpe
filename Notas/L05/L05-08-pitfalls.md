---
tags: [notes, lecture-05, pitfalls, true-false, self-test, repeated-games]
date: 2026-10-16
status: estimated
source: "Tadelis (2013) §10.1–10.3, 10.6, pp. 190–214; Gibbons (1992) §2.3.A–B, pp. 82–102; Cabral (2017) §7.3, pp. 172–174. True/False items are original, in the macro-1 style (rules/00_estilo_avaliacao.md)"
---

# Lecture 5 · Pitfalls and a True/False self-test

> Prev: [[L05-07-formulas]] · Next: [[L05-09-python]] · Map: [[L05-00-map]]

---

## Part I — the confusions this material produces

### 1 · "A long finite game is almost an infinite one"

It is not, when the stage equilibrium is unique. **500 rounds and 2 rounds have the same unique
SPE** (Prop. 10.1, p. 192): the induction never uses the length. What saves cooperation is the
absence of a *known* last period (or a second stage equilibrium), not a large $T$.
**Minimal counterexample:** the 500-round PD — fink in every period is the only SPE.
→ [[L05-01-finite-repetition-unraveling]] §4.

### 2 · "Finitely repeated games can never support non-Nash play"

Only with a **unique** stage NE. With two Pareto-ranked equilibria, $(M,m)$ in stage 1 of Tadelis's
two-stage game is subgame-perfect for $\delta\geq1/2$ (p. 191). The last period, though, must always
be a stage NE. → [[L05-02-two-stage-carrot-stick]].

### 3 · Infinite horizon as "the game lasts forever"

$\delta$ can be a continuation probability; the game then ends in finite time with probability 1
(p. 194). What matters is that **at every period another period is possible**, so there is never a
last period from which to unravel. → [[L05-03-discounting-histories-strategies]] §2.

### 4 · Nash vs subgame-perfect in the repeated game

A threat that is not an equilibrium of the subgame where it would be carried out is not credible.
Grim trigger works because its punishment, $(F,f)$ forever, *is* an SPE (Prop. 10.2). **Minimal
counterexample:** a profile whose off-path behaviour is not a best response there can be a Nash
equilibrium for high $\delta$ and an SPE for no $\delta$ — Tadelis Exercise 10.4 (p. 216) asks for
exactly such a profile in the trust game of §10.5 ([[../L06/L06-00-map|Lecture 6]]). The off-path
plays are never reached, so Nash equilibrium does not test them; subgame perfection does.

### 5 · Checking only the equilibrium path

The one-stage deviation principle needs the check **in every state**, off the path included. For
grim trigger the off-path check is trivial ($-2$ today, nothing gained), but in other profiles it
binds: in the alternating path of §10.6 the binding constraint is the **bad period**, not the
punishment. → [[L05-06-folk-theorem]] §3.

### 6 · Comparing today's gain with one period's loss

The loss from deviating is **every future period's** loss, discounted: $(R-P)\delta/(1-\delta)$, not
$(R-P)\delta$. With Tadelis's numbers the first gives $\delta\geq1/4$, the second would give
$\delta\geq1/3$. (The one-period version *is* right in the two-stage game, because there is only one
future period.)

### 7 · Thinking the sucker payoff matters for grim trigger

On the grim-trigger path nobody is ever the sucker and the punishment is $(F,f)$, so
$\delta^*=(T-R)/(T-P)$ has no $S$ in it: Tadelis ($S=-1$) and Gibbons ($S=0$) both get $1/4$. $S$
does matter for the **feasible set** and for the **alternating** path, whose bad period needs
$\delta\geq(P-S)/(T-P)$.

### 8 · Reading the folk theorem as a prediction of cooperation

It says a whole region of payoffs is supportable — **including the non-cooperative** $(1,1)$ and
lopsided points like $(4.6,1)$. It is an existence result about possibilities, and it raises the
equilibrium-selection problem rather than solving it. → [[L05-06-folk-theorem]] §5.

### 9 · "Feasible" means "a payoff of some pure profile"

Feasible means a **convex combination** of those payoffs: $(2,2)$ and $(4.4,2)$ in the PD are
feasible though no cell pays them. They are reached by alternating over time (Tadelis) or by a public
randomizing device (Gibbons, p. 96).

### 10 · Mixing present values and average payoffs

Compare like with like: $4/(1-\delta)$ (PV) against $5+\delta/(1-\delta)$ (PV), or $4$ (average)
against $(1-\delta)5+\delta$ (average). Comparing $4$ with $5+\delta/(1-\delta)$ is the classic slip.

### 11 · The stage-$t$ game is a subgame

It is not: a subgame includes all moves that follow (Gibbons, p. 95). Treating stage $t$ as a
one-shot game assumes it is the last one.

### 12 · Notation: $T$ the horizon vs $T$ the temptation

Tadelis writes $G(T,\delta)$ with $T$ the number of periods; the PD label $T$ is the temptation
payoff. Context decides; these notes use $T$ for the horizon in notes 01–02 and for the temptation
in notes 04–06.

---

## Part II — True/False self-test (original items)

**1.** In the Prisoner's Dilemma repeated 1,000 times with $\delta=0.99$, there is a
subgame-perfect equilibrium in which both players cooperate in the first period.
**False.** The stage game has a unique NE, so by Prop. 10.1 the unique SPE plays $(F,f)$ in every
period; neither the horizon nor $\delta$ enters the argument.

**2.** In a finitely repeated game, behaviour in the last period of any subgame-perfect equilibrium
must be a Nash equilibrium of the stage game.
**True.** At $T$ nothing in the future depends on today's action, so each player best-responds in the
stage game (Prop. 9.2, p. 181) — whether the stage NE is unique or not.

**3.** In Tadelis's two-stage game (p. 191), the strategy profile that rewards $(M,m)$ with $(R,r)$
and punishes everything else with $(F,f)$ is subgame-perfect for every $\delta\in(0,1)$.
**False.** Stage-2 play is a stage NE after every history, but stage 1 requires $4+3\delta\geq5+\delta$,
i.e. $\delta\geq1/2$.

**4.** If a stage game has two Nash equilibria that give every player the same payoff, repetition a
finite number of times cannot support any non-Nash first-period behaviour through rewards and
punishments.
**True.** A carrot and a stick must differ in payoff; with $r=p$ the loss from deviating is zero and
the one-period temptation is never offset.

**5.** Reading $\delta$ as the probability that the game continues, the infinitely repeated game ends
in finite time with probability one.
**True.** The probability of reaching period $t$ is $\delta^{t-1}\to0$ (p. 194); the analysis only
needs a future to exist at each period.

**6.** The average payoff of the stream $(4,4,4,\dots)$ is $4/(1-\delta)$.
**False.** That is its present value; the average payoff is $(1-\delta)\cdot4/(1-\delta)=4$ (Def. 10.3).

**7.** In the infinitely repeated PD, playing fink after every history is a subgame-perfect
equilibrium only if $\delta$ is small.
**False.** By Prop. 10.2 it is an SPE for every $\delta<1$: history-independent play makes each
period a one-shot game.

**8.** With Tadelis's payoffs, grim trigger is a subgame-perfect equilibrium of the infinitely
repeated PD if and only if $\delta\geq1/4$.
**True.** Off the path $(F,f)$ forever is an SPE; on the path $4+\frac{4\delta}{1-\delta}\geq5+\frac{\delta}{1-\delta}\iff\delta\geq\frac14$ (10.3).

**9.** To verify that grim trigger is subgame-perfect, it is enough to check that no player gains
from a single deviation on the cooperative path.
**False.** The one-stage deviation principle requires checking every history, including those
after a deviation; grim trigger passes the off-path check, but it has to be made.

**10.** Raising the sucker payoff $S$ of a Prisoner's Dilemma lowers the critical discount factor
for grim trigger.
**False.** $\delta^*=(T-R)/(T-P)$ does not contain $S$.

**11.** Making the stage Nash payoff $P$ closer to the cooperative payoff $R$ makes cooperation
harder to sustain with grim trigger.
**True.** $\partial\delta^*/\partial P=(T-R)/(T-P)^2>0$: a milder punishment needs more patience.

**12.** In Cabral's game, where cooperating pays 5, deviating 6 and the stage equilibrium 4,
cooperation is sustainable by trigger strategies if the continuation probability is at least $1/2$.
**True.** $5/(1-\alpha)\geq6+4\alpha/(1-\alpha)\iff\alpha\geq1/2$ (pp. 172–173).

**13.** If two players have different critical discount factors under a grim-trigger profile, the
profile is an SPE when the common $\delta$ exceeds the smaller one.
**False.** Each player must be deterred: $\delta$ must exceed the **larger** threshold,
$\max_i(d_i-x_i)/(d_i-e_i)$ (Gibbons, p. 101).

**14.** With $\delta=1/(1+r)$, grim trigger in Tadelis's PD survives any per-period interest rate up
to 300%.
**True.** $\delta\geq1/4\iff1+r\leq4\iff r\leq3$.

**15.** The payoff vector $(2,2)$ is feasible in Tadelis's PD even though no pure profile yields it.
**True.** $(2,2)=\frac12(5,-1)+\frac12(-1,5)$, a convex combination (Def. 10.7, Fig. 10.5).

**16.** By the folk theorem, the average payoff $(0.5,\,3)$ can be supported in Tadelis's repeated PD
for $\delta$ close enough to 1.
**False.** It is feasible, but player 1 gets less than the stage Nash payoff $1$; Theorem 10.1 needs
$v_i>v_i^*$ for every player.

**17.** In the alternating path $(F,m),(M,f),\dots$ of Tadelis's PD, the binding incentive
constraint is a player's "bad" period.
**True.** The good-period condition holds for all $\delta$; the bad period needs
$\frac{-1+5\delta}{1+\delta}\geq1$, i.e. $\delta\geq1/2$.

**18.** The folk theorem predicts that patient players in a repeated Prisoner's Dilemma will
cooperate.
**False.** It shows that cooperation is one of many SPE outcomes, alongside perpetual defection and
lopsided paths; it does not select among them.

**19.** The one-stage deviation principle for infinitely repeated games relies on discounting.
**True.** Discounting makes payoffs continuous at infinity, so a profitable infinite deviation implies
a profitable finite one (fn. 6, p. 199).

**20.** In a two-stage game with stage-game equilibria worth $(3,3)$ and $(1,1)$, punishing with
$(1,1)$ is immune to renegotiation.
**False.** After a deviation both players prefer $(3,3)$; "bygones are bygones" undermines the threat
(Gibbons, p. 87). Renegotiation-proof punishments need equilibria the punisher does not want to
leave (Figure 2.3.5).

**21.** In the infinitely repeated game, every subgame is identical to the whole game.
**True.** Gibbons (p. 94); it is what makes the bootstrap — the cooperative equilibrium serving as
its own reward — consistent rather than circular.

**22.** Increasing the number of rounds $T$ in Tadelis's three-action stage game can increase the
number of rounds in which $(M,m)$ is played in an SPE, but never to all $T$ rounds.
**True.** Longer games allow longer reward phases (useful when $1/3<\delta<1/2$), and the final round
must be a stage NE, which $(M,m)$ is not ([[L05-02-two-stage-carrot-stick]] §4).

---

## Links

- Map: [[L05-00-map]] · Formulas: [[L05-07-formulas]] · Python: [[L05-09-python]].
- Rules: [[../../rules/game-theory|rules/game-theory]] items 4, 14, 15; exam style [[../../rules/00_estilo_avaliacao|rules/00_estilo_avaliacao]].
