---
tags: [notes, lecture-06, repeated-games, grim-trigger, one-shot-deviation]
date: 2026-10-16
status: estimated
source: "Tadelis (2013) §10.2–10.3, pp. 192–200 (Def. 10.2–10.3, Prop. 10.2–10.3, eq. (10.3)) and §10.4 eq. (10.5), p. 202; §10.5 opening, p. 204. Recap only — the full treatment is Lecture 5."
---

# 10.2–10.3 recap · One inequality runs the whole lecture

> **Claim.** Everything in Lecture 6 — a cartel, a trusted merchant, a well-paid worker — is
> the same check: **the one-period gain from cheating must not exceed the discounted loss of
> the relationship it destroys.** Written once, as Tadelis's (10.5), it is
> $\delta\ge (v^d-v^c)/(v^d-v^p)$; every later note only fills in $v^c$, $v^d$ and $v^p$.
> Prev: — · Next: [[L06-02-cournot-collusion]] · Map: [[L06-00-map]]

> **What this note is not.** Finite versus infinite repetition, the folk theorem and the
> proofs belong to [[../L05/L05-00-map|Lecture 5]]. Only what Lecture 6 uses is restated.

---

## 1 · U — why the future can discipline the present

A stage game with a unique Nash equilibrium repeated a **known, finite** number of times
unravels: in the last period only the stage Nash equilibrium can be played, so nothing that
happens earlier can be rewarded or punished, and backward induction repeats the argument to
period 1 (Tadelis Prop. 10.1, p. 192). Infinite repetition — or, equivalently, a probability
$\delta$ that the game goes on after every period — removes the last period. Then the
**proposed equilibrium itself** can serve as the reward ("carrot"), and the repeated stage
Nash equilibrium as the punishment ("stick"): Tadelis calls it a *bootstrap equilibrium*
(p. 197).

> **Two things are needed and both are examinable** (Tadelis p. 204): **no predetermined
> terminal period**, and **a discount factor that is not too small.** Drop either and
> cooperation that is not a stage-game best response cannot be sustained.

---

## 2 · C — the tools, as Tadelis states them

| Object | Statement | Page |
|---|---|---|
| Present value (Def. 10.2) | $v_i=\sum_{t=1}^{\infty}\delta^{t-1}v_i^t$ | p. 193 |
| Average payoff (Def. 10.3) | $\bar v_i=(1-\delta)\sum_{t=1}^{\infty}\delta^{t-1}v_i^t$ — a constant stream $v$ has average $v$ | p. 194 |
| Prop. 10.2 | playing a stage Nash equilibrium after **every** history is an SPE for any $\delta<1$ | p. 196 |
| Prop. 10.3 (one-stage deviation) | a profile is an SPE **iff** no player gains by deviating at **one** history and conforming afterwards | p. 198 |
| Grim trigger | play the cooperative action while every past outcome was cooperative; after any deviation play the stage Nash equilibrium forever | p. 198 |

**Why Prop. 10.3 makes the check finite.** Under grim trigger every history falls in one of
two classes (p. 199): *no deviation yet* (play cooperatively) or *some deviation* (play stage
Nash). Off the path the prescription is a stage Nash equilibrium followed by more of the same,
so a one-shot deviation only lowers today's payoff — **no condition**. On the path there is
one condition, the inequality of §3.

---

## 3 · C — the template, every step

Let $v_i^c$ be player $i$'s per-period payoff on the cooperative path, $v_i^d$ the best
payoff he can grab in one period by deviating, and $v_i^p$ his per-period payoff in the
punishment (the stage Nash equilibrium, $v_i^*$ in Tadelis). Conforming forever is worth

$$v_i^c+\delta v_i^c+\delta^2v_i^c+\dots=v_i^c+\frac{\delta v_i^c}{1-\delta}.$$

Deviating today and being punished forever after is worth

$$v_i^d+\delta v_i^p+\delta^2v_i^p+\dots=v_i^d+\frac{\delta v_i^p}{1-\delta}.$$

No profitable one-shot deviation requires

$$v_i^c+\frac{\delta v_i^c}{1-\delta}\ \ge\ v_i^d+\frac{\delta v_i^p}{1-\delta}.$$

Multiply by $1-\delta>0$:

$$(1-\delta)v_i^c+\delta v_i^c\ \ge\ (1-\delta)v_i^d+\delta v_i^p
\iff v_i^c\ \ge\ (1-\delta)v_i^d+\delta v_i^p .$$

Collect $\delta$: $v_i^c-v_i^d\ge -\delta v_i^d+\delta v_i^p=-\delta(v_i^d-v_i^p)$, and
divide by $v_i^d-v_i^p>0$:

$$\boxed{\;\delta\ \ge\ \delta_i^*\equiv\frac{v_i^d-v_i^c}{v_i^d-v_i^p}\;}\qquad\text{(Tadelis (10.5), p. 202)}$$

> **Read the fraction as temptation over stake.** The numerator is the **one-period gain from
> cheating**; the denominator is the gain from cheating **plus** the per-period loss the
> punishment inflicts ($v^c-v^p$). Rearranged once more:
> $$\underbrace{v^d-v^c}_{\text{gain today}}\ \le\ \frac{\delta}{1-\delta}\,\underbrace{(v^c-v^p)}_{\text{loss per period, from tomorrow}} .$$
> **This second form is the one Milgrom & Roberts and the efficiency-wage model use**
> ([[L06-05-reputation-trust]], [[L06-07-efficiency-wages]]).

The middle line, $v^c\ge(1-\delta)v^d+\delta v^p$, is the **average-payoff form**: the
cooperative payoff must beat a weighted average of the deviation and punishment payoffs. Every
"conform vs deviate" figure in this unit plots exactly those two sides against $\delta$.

### 3.1 · Worked — Tadelis's repeated Prisoner's Dilemma (pp. 197–200)

Stage game: $(M,m)$ pays $(4,4)$; $F$ against $m$ pays $5$ to the finker and $-1$ to the
other; $(F,f)$ pays $(1,1)$. So $v^c=4$, $v^d=5$, $v^p=1$:

$$4+\frac{4\delta}{1-\delta}\ \ge\ 5+\frac{\delta}{1-\delta}\quad\text{(10.3)}
\iff \delta\ge\frac{5-4}{5-1}=\frac14 .$$

| $\delta$ | conform: $4/(1-\delta)$ | deviate: $5+\delta/(1-\delta)$ | verdict |
|---|---|---|---|
| 0.20 | 5.000 | 5.250 | deviate |
| **0.25** | **5.333** | **5.333** | **indifferent — the cutoff** |
| 0.50 | 8.000 | 6.000 | conform |

---

## 4 · C — what $\delta$ stands for

$\delta$ is not only impatience. Tadelis reads it as the **probability that the game is played
again** (p. 200); Cabral turns it into a formula with the interest rate, the **frequency** of
price changes, the **hazard** that the industry ends and its **growth** — eq. (9.5), worked in
[[L06-03-bertrand-market-structure]] §3. Everything that raises $\delta$ makes every
relational contract in this lecture easier to sustain.

---

## 5 · C — the checklist for any application

1. **Name the cooperative path** and its per-period payoff $v^c$ for **each** player
   (asymmetric splits give different cutoffs — [[L06-02-cournot-collusion]] §2).
2. **Find the best one-period deviation** $v^d$: the stage best response to the others'
   cooperative actions (not "any" deviation — the most tempting one).
3. **Name the punishment** and its value $v^p$; check that it is itself an equilibrium
   (stage Nash forever is, by Prop. 10.2) — otherwise the threat is not credible.
4. **Apply (10.5)** for every player; the cooperative path survives iff
   $\delta\ge\max_i\delta_i^*$.
5. **Check off-path behaviour** with Prop. 10.3 (automatic under Nash reversion).

---

## Links

- Next: [[L06-02-cournot-collusion]] (the first application). Map: [[L06-00-map]].
- The basics in full: [[../L05/L05-00-map|Lecture 5]]; subgame perfection and the one-stage
  deviation principle for finite games: [[../L03/L03-00-map|Lecture 3]],
  [[../L04/L04-00-map|Lecture 4]] (Tadelis §9.5).
- Rules: [[../../rules/game-theory|rules/game-theory]] item 4 ("repeated games are not
  one-shot games").
- Code: [[L06-11-python]] §1. Formal side: MWG §12.D (pp. 400–405), named in
  [[L06-03-bertrand-market-structure]].
- Exercises: Tadelis 10.2 and 10.3 (p. 215) drill the cutoff; Muñoz-Garcia Ch. 6 Ex. 2
  (from p. 278).
