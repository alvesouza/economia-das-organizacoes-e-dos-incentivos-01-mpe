---
tags: [notes, lecture-01, static-games, common-knowledge, complete-information, strategy]
date: 2026-10-16
status: taught
source: "Aula/Lecture01.pdf slides 15-18; Tadelis (2013) Ch. 3 pp. 44-47 (static games, games of complete information, Def. 3.1 p. 45, Def. 3.2 p. 46); Gibbons §1.1.A (p. 4) and §1.1.B (p. 7); MWG §7.D (p. 228)"
---

# Slides 15–18 · Static vs dynamic, complete information, and what a strategy is

> **Claim.** Three words in the lecture title carry assumptions that the solution concepts will
> lean on. **Static** means no one observes anyone else's choice before choosing. **Complete
> information** means the game itself (players, actions, how outcomes map to payoffs) is
> **common knowledge**: everyone knows it, everyone knows everyone knows it, *ad infinitum*.
> And a **strategy** is a complete contingent plan, which is why even long dynamic interactions
> can be written as one simultaneous choice of strategies.
>
> Prev: [[L01-01-games-normal-form]] · Next: [[L01-03-solution-concepts]] · Map: [[L01-00-map]]

---

## 1 · C — static vs dynamic (slide 15)

| | Static (normal form) | Dynamic |
|---|---|---|
| What a player sees before choosing | nothing of the others' choices | some earlier moves |
| Defining test | choices made **without observing** the others' choices — timing is irrelevant (Tadelis p. 44; Gibbons p. 4) | someone conditions on an observed move |
| Natural representation | matrix / normal form | game tree (extensive form, [[../L03/L03-00-map|Lecture 3]]) |

Tadelis's example (p. 44): you study two days before the exam, I study the day before; if I do
not learn how much you studied, **moving later gives me no informational advantage**, and the
game is static.

> **Key fact (slide 15): any situation, static or dynamic, can be represented as a normal-form
> game by suitably defining strategies.** The trick is §3 below.

## 2 · C — complete information and common knowledge (slide 16)

In a game of **complete information** the game being played is common knowledge: all players
know who is playing, which actions each has, and how outcomes translate into payoffs (slide
16). Tadelis lists four components that must be common knowledge (p. 45): all players' possible
actions, all possible outcomes, how each action profile maps into an outcome, and every
player's preferences over outcomes.

**Definition 3.1 (Tadelis p. 45; slide 16).** An event $E$ is *common knowledge* if (1) everyone
knows $E$, (2) everyone knows that everyone knows $E$, and so on *ad infinitum*.

### 2.1 · Worked — the levels, written out

Let $K(E)$ be "everyone knows $E$". Then

$$K^1(E)=K(E),\qquad K^{m+1}(E)=K\bigl(K^m(E)\bigr),\qquad \text{CK}(E)\iff K^m(E)\ \text{for every } m\ge1 .$$

| Situation (Tadelis p. 45) | $K^1$ | $K^2$ | CK? |
|---|---|---|---|
| Walking in the rain together: "it is raining" | yes | yes (each sees the other getting wet) | **yes** |
| Professor announces an exam; you may have been daydreaming | I know it | I am not sure **you** know it | **no** — fails at level 2 |

> **Mutual knowledge ($K^1$) is not common knowledge.** The gap matters immediately: each round
> of iterated elimination ([[L01-06-iesds]]) uses one more level of knowledge **of rationality**.
> Gibbons states the same requirement for IESDS in words (p. 7).

Common knowledge is a strong assumption (Tadelis p. 45: "by no means innocuous"); Lecture 7
drops part of it by letting payoffs be private information
([[../L07/L07-00-map|Lecture 7]]).

## 3 · C — a strategy is a complete contingent plan (slide 17)

A strategy prescribes **what to do in every contingency that may arise** — the chess player
who decides in advance a move for every board position (slide 17). Tadelis's candidate going
to a meeting (p. 46): "if they ask $q_1$ I answer $a_1$; if they ask $q_2$ I answer $a_2$; …".
MWG (§7.D): the fact that a strategy is a complete contingent plan "cannot be overemphasized".

In a static game each player has a single, unconditional decision, so **strategies coincide
with actions** (Tadelis p. 47: the change of focus "may seem redundant"). The distinction pays
off as soon as someone observes something.

### 3.1 · Worked — counting strategies when the pair can see your sheet

Take the grade game of [[L01-01-games-normal-form]] §3, but let Pair read your letter before
writing (a dynamic version; original example).

- You still have one decision: $S_1=\{\alpha,\beta\}$.
- Pair has **two contingencies** (you wrote $\alpha$; you wrote $\beta$) and two actions in each,
  so a strategy is a pair (reply to $\alpha$, reply to $\beta$):
  $S_2=\{\alpha\alpha,\ \alpha\beta,\ \beta\alpha,\ \beta\beta\}$, $|S_2|=2^2=4$.

With the slide-12 payoffs, the normal form is the 2×4 matrix

| You \ Pair | $\alpha\alpha$ | $\alpha\beta$ | $\beta\alpha$ | $\beta\beta$ |
|---|---|---|---|---|
| $\alpha$ | 0, 0 | 0, 0 | 3, −1 | 3, −1 |
| $\beta$ | −1, 3 | 1, 1 | −1, 3 | 1, 1 |

Cell by cell: against $\alpha\beta$ (copy the reply "α to α, β to β"), You's $\alpha$ meets
$\alpha$ (0, 0) and You's $\beta$ meets $\beta$ (1, 1). **The dynamic game is now a static choice
of plans** — exactly slide 15's key fact. Solving it properly needs backward induction
([[../L03/L03-00-map|Lecture 3]]).

> **Count, then draw.** With $m$ contingencies and $a$ actions in each, a player has $a^m$ pure
> strategies. Forgetting a contingency (writing $S_2=\{\alpha,\beta\}$ here) is the most common
> modelling error with sequential moves.

## 4 · C — what a payoff is (slide 18)

$u_i:S\to\mathbb R$ is player $i$'s utility over **outcomes (strategy profiles)**; it represents
$i$'s preferences over outcomes. Stronger conditions (the expected-utility axioms) enter only
"in some lectures" — when players randomize ([[../L02/L02-00-map|Lecture 2]]).

### 4.1 · Worked — why dominance only needs the ranking

Let $f:\mathbb R\to\mathbb R$ be strictly increasing and replace $u_i$ by $f\circ u_i$. Then for
any $s_i,s_i',s_{-i}$:

$$u_i(s_i',s_{-i})>u_i(s_i,s_{-i})\iff f\bigl(u_i(s_i',s_{-i})\bigr)>f\bigl(u_i(s_i,s_{-i})\bigr).$$

Every comparison in the definitions of [[L01-04-dominance]] is of this form (one player, two of
her strategies, a fixed $s_{-i}$), so **strict and weak dominance, dominant-strategy equilibrium
and IESDS are unchanged by any strictly increasing transformation of each player's payoffs**.
That is why the grade game only needs the *order* A ≻ B+ ≻ B− ≻ C (plus how much you care about
the pair) — and why the numbers 3, 1, 0, −1 on slide 12 are one choice among many with the same
predictions. Cardinal payoffs matter only once expectations over mixed strategies appear.

---

## Links

- Prev / next: [[L01-01-games-normal-form]] · [[L01-03-solution-concepts]].
- Where common knowledge of rationality does its work: [[L01-06-iesds]] §2.
- Rules pack: [[../../rules/game-theory|rules/game-theory]] rule 5 (common vs mutual knowledge).
- Practice: `Listas/pratica-lecture-01.md` items 3–4 (Muñoz-Garcia Ch. 1 Ex. 2 p. 4, Ex. 5 p. 8: trees to matrices); quiz `Simulados/quiz-lecture01-1-normal-form-2026-10-13.md` (sections `strategy`, `ck`).
