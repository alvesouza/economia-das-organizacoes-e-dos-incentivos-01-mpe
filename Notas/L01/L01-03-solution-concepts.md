---
tags: [notes, lecture-01, solution-concepts, existence, uniqueness, invariance]
date: 2026-10-16
status: taught
source: "Aula/Lecture01.pdf slides 21-22; Tadelis (2013) §3.3 (pp. 52-56: solution concept and equilibrium p. 54, assumptions §3.3.1 pp. 54-55, criteria §3.3.2 pp. 55-56, Battle of the Sexes p. 54), §4.1.3 (p. 62 invariance of strict dominance), §4.2.3 (pp. 67-68); Cabral §7.1 (p. 163, Figure 7.3)"
---

# Slides 21–22 · What a solution concept must deliver

> **Claim.** A solution concept is a rule that maps every game into a set of profiles, its
> **equilibria** — the theory's prediction. It is judged on three criteria that pull against
> each other: **existence** (does it say something in most games?), **uniqueness** (does it say
> something sharp?), and **invariance** (does the answer survive a tiny change in payoffs?).
> "Anything can happen" always exists and is useless; "everyone plays a dominant strategy" is
> sharp and robust but rarely exists. Every concept in the course is a different point on that
> frontier.
>
> Prev: [[L01-02-information-and-strategies]] · Next: [[L01-04-dominance]] · Map: [[L01-00-map]]

---

## 1 · C — solution concept and equilibrium (slide 21)

- A **solution concept** is a method for analysing games that singles out their most
  reasonable outcomes (slide 21; Tadelis p. 54: it restricts "the set of all possible outcomes
  to those that are more reasonable than others").
- An **equilibrium** is a strategy profile selected by a solution concept: the prediction.
- To be useful, a theory must apply to a wide range of strategic situations.

> **Caveat (Tadelis p. 61): an equilibrium is a profile of strategies, never a profile of
> payoffs.** "(F, F) is the equilibrium; (−4, −4) are the equilibrium payoffs."

### 1.1 · The four maintained assumptions (Tadelis §3.3.1, pp. 54–55)

| # | Assumption | Content | First used by |
|---|---|---|---|
| 1 | **Rational** | each player chooses $s_i$ to maximize payoff given his beliefs | strict dominance ([[L01-04-dominance]]) |
| 2 | **Intelligent** | each player knows the whole game | strict dominance (to see that a strategy is dominated) |
| 3 | **Common knowledge** | rationality and intelligence are common knowledge | IESDS ([[L01-06-iesds]]) |
| 4 | **Self-enforcement** | a prediction must be one each player is happy to follow on his own | every concept (noncooperative game theory) |

Self-enforcement is why a third-party enforcer (a mafia code, a contract) has to be **modelled as
part of the game**, not assumed (Tadelis p. 55; [[L01-05-pareto-social-dilemmas]] §4).

## 2 · C — the three criteria (slide 22; Tadelis §3.3.2, pp. 55–56)

| Criterion | Question | A concept that passes trivially but is useless | A concept that is sharp but often fails |
|---|---|---|---|
| **Existence** | how often does it apply? | "anything can happen" | "players choose what they think the opponent chooses" — undefined when action sets differ (p. 55) |
| **Uniqueness** | how much does it restrict behaviour? | — | strict dominance: unique when it exists (Prop. 4.1) but often does not |
| **Invariance** | is it robust to payoff changes of size at most $\varepsilon$? | — | weak dominance (§3.2 below) |

**Why uniqueness is hard** (slide 22; p. 56): each player's best action depends on the others'
actions, so several combinations of strategies can support each other. The Battle of the Sexes
(p. 54) is the canonical case:

| Alex \ Chris | O | F |
|---|---|---|
| O | 2, 1 | 0, 0 |
| F | 0, 0 | 1, 2 |

No strategy is "always best" for either player (O against O, F against F), so the
always-best rule offers no guidance at all — a failure of **existence** for strict dominance
(Tadelis p. 62), and IESDS can only say "anything can happen" here (p. 68).

**What counts as a small change** (p. 56): adding a player or a strategy is not small; only the
payoff functions may move. Formally, if every payoff of every player moves by at most a small
$\varepsilon>0$, the prediction should not change.

## 3 · Worked — invariance, checked with numbers

### 3.1 · Strict dominance passes (Tadelis §4.1.3, p. 62)

In the prisoner's dilemma (Tadelis p. 48; [[L01-04-dominance]] §3) F strictly dominates M for
player 1 with the margins

$$v_1(F,M)-v_1(M,M)=-1-(-2)=1,\qquad v_1(F,F)-v_1(M,F)=-4-(-5)=1 .$$

Perturb every payoff by some $\delta$ with $|\delta|\le\varepsilon$. Each margin is a difference of
two perturbed payoffs, so it moves by at most $2\varepsilon$:

$$\tilde v_1(F,\cdot)-\tilde v_1(M,\cdot)\ \ge\ 1-2\varepsilon\ >\ 0\quad\text{whenever}\ \varepsilon<\tfrac12 .$$

The same holds for player 2, so (F, F) remains the strict dominant-strategy equilibrium. Tadelis's
own perturbation (5 years becoming 5.01 for one player and 4.99 for the other, p. 56) has
$\varepsilon=0.01$. In general: **if $g>0$ is the smallest strict margin, any perturbation with
$\varepsilon<g/2$ keeps every strict inequality** — the argument behind Tadelis's sentence "because
the inequality is strict, we can find a small enough value $\varepsilon>0$" (p. 62).

### 3.2 · Weak dominance fails

Player 1's payoffs (player 2's are irrelevant here):

| | L | R |
|---|---|---|
| U | 1 | 1 |
| D | 1 | 0 |

U weakly dominates D ($1\ge1$, $1>0$). Raise $u_1(D,L)$ by any $\varepsilon/2>0$: now
$u_1(D,L)=1+\varepsilon/2>1=u_1(U,L)$, so U no longer weakly dominates D, **however small $\varepsilon$
is**. A tie is not robust; a strict inequality is. (This is the counterexample used in
`Listas/lista-lecture-01.tex` Q1(c) and checked in `Listas/lista-lecture-01-check.py`.)

## 4 · C — the lecture's concepts on the scorecard

| Concept | Assumptions | Existence | Uniqueness | Invariance | Pareto optimal? |
|---|---|---|---|---|---|
| Strict dominant-strategy equilibrium ([[L01-04-dominance]]) | rationality (1–2) | rare (fails in BoS) | **yes**, Prop. 4.1 | **yes** | not necessarily — PD |
| IESDS ([[L01-06-iesds]]) | + common knowledge of rationality (3) | **always** in finite games | often fails (BoS: nothing removed) | yes (strict inequalities) | not necessarily — (4.1), Cournot |
| Nash equilibrium ([[../L02/L02-00-map|Lecture 2]]) | + correct beliefs | pure: not always; mixed: always (finite games) | often fails | — | not necessarily |

> **Robustness to the assumptions themselves** (Cabral p. 163, Figure 7.3): when a player's best
> choice hinges on the *other* player being rational, a tiny doubt about that rationality can
> overturn it if the downside is large (Cabral's $-100$). The more rounds of "I know that you
> know" a prediction uses, the more fragile it is in practice.

---

## Links

- Prev / next: [[L01-02-information-and-strategies]] · [[L01-04-dominance]].
- The criteria applied: strict dominance → [[L01-04-dominance]] §5; IESDS → [[L01-06-iesds]] §5.
- Rules pack: [[../../rules/game-theory|rules/game-theory]] rules 2–3 (name the concept; check existence and multiplicity).
- Practice: Tadelis 4.1, 4.2 (p. 76) = `Listas/pratica-lecture-01.md` items 11–12; `Listas/lista-lecture-01.tex` Q1(c); quiz `Simulados/quiz-lecture01-1-normal-form-2026-10-13.md` (section `nf`).
