---
tags: [notes, lecture-07, bayesian-nash-equilibrium, strategies, chicken]
date: 2026-10-16
status: estimated
source: "Tadelis (2013) §12.1.3 (Defs. 12.3–12.4, eq. 12.2, pp. 249–252) and §12.2.1 chicken with incomplete information (Fig. 12.3, R = 8, H = 16, L = 0, pp. 252–255); Gibbons (1992) §3.1.C, pp. 149–152; MWG Def. 8.E.1 and Prop. 8.E.1, pp. 255–256"
---

# 12.1.3 · 12.2.1 · A strategy is a plan for every type; a BNE is a Nash equilibrium of those plans

> **Claim.** In a Bayesian game a **strategy maps types to actions**, and a **Bayesian Nash
> equilibrium** is a profile of such maps in which **every type of every player** best-responds to
> his posterior over the others' types and their strategies. Checking it type by type is all the
> work; the chicken game shows the method end to end and gives a prediction ("children of lenient
> parents drive on") that **flips when the payoffs are reassigned**.
>
> Prev: [[L07-01-bayesian-games-harsanyi]] · Next: [[L07-03-cournot-private-costs]] · Map: [[L07-00-map]]

---

## 1 · C — strategies: Definition 12.3 (p. 249)

> **Definition 12.3.** A **pure strategy** for player $i$ is a function $s_i:\Theta_i\to A_i$ that
> specifies the action $s_i(\theta_i)$ he chooses when his type is $\theta_i$. A mixed strategy is a
> probability distribution over pure strategies.

**Counting.** With $|A_i|$ actions and $|\Theta_i|$ types, player $i$ has $|A_i|^{|\Theta_i|}$ pure
strategies: the entry game's incumbent, 2 actions × 2 types → $2^2=4$ ($AA,AF,FA,FF$); the chicken
players below, likewise 4 each.

**Why a plan for types that were not drawn** (Tadelis pp. 250–251; Gibbons pp. 150–151): once Nature
has drawn $\theta_i$, the other types of $i$ never move. But **$j$ cannot compute his expected payoff
without knowing what every type of $i$ would do**, weighted by $\phi_j$. A strategy that left some
types unspecified would make $j$'s best response undefined — the same reason a strategy in an
extensive game must cover unreached information sets ([[../L03/L03-00-map|Lecture 3]]).

> **Types are information sets.** Learning one's type is arriving at an information set that
> Nature's move determines (p. 250). A type-contingent strategy is a complete contingent plan,
> exactly as in Lecture 1's definition of a strategy.

**A pure strategy of $i$ looks mixed to $j$** (p. 250): if the incumbent plays $AF$ and is rational
with probability $p$, the entrant faces "A with probability $p$, F with probability $1-p$". This is
the seed of Harsanyi's reading of mixed strategies ([[L07-04-threshold-strategies-purification]] §3).

Gibbons's vocabulary (p. 150), needed in [[../L08/L08-00-map|Lecture 8]]: a **separating** strategy
gives each type a different action; a **pooling** strategy gives all types the same action.

---

## 2 · C — Bayesian Nash equilibrium: Definition 12.4 (p. 251)

> **Definition 12.4.** A strategy profile $s=(s_1(\cdot),\dots,s_n(\cdot))$ is a **pure-strategy
> Bayesian Nash equilibrium** if, for every player $i$, for each of $i$'s types $\theta_i\in\Theta_i$,
> and for every $a_i\in A_i$,
> $$\sum_{\theta_{-i}\in\Theta_{-i}}\phi_i(\theta_{-i}\mid\theta_i)\,u_i\big(s_i(\theta_i),s_{-i}(\theta_{-i});\theta_i\big)
> \;\ge\;\sum_{\theta_{-i}\in\Theta_{-i}}\phi_i(\theta_{-i}\mid\theta_i)\,u_i\big(a_i,s_{-i}(\theta_{-i});\theta_i\big).\tag{12.2}$$

Read (12.2) left to right:

| Piece | Meaning |
|---|---|
| $\phi_i(\theta_{-i}\mid\theta_i)$ | what type $\theta_i$ believes about the others' types (from the common prior) |
| $s_{-i}(\theta_{-i})$ | what each of those types does — the others' **strategies** |
| left side | type $\theta_i$'s expected payoff from his prescribed action |
| right side | his expected payoff from any single alternative action |

**Two simplifications the book makes explicit (p. 251):**

1. It suffices to check deviations to **actions**, one type at a time, not to whole alternative
   strategies $s_i'(\cdot)$: if no type gains by switching his action, no rearrangement across types
   gains either.
2. The general form, valid for a continuum of types (Remark, p. 251):
   $$E_{\theta_{-i}}\big[u_i(s_i(\theta_i),s_{-i}(\theta_{-i});\theta_i)\mid\theta_i\big]\;\ge\;
   E_{\theta_{-i}}\big[u_i(a_i,s_{-i}(\theta_{-i});\theta_i)\mid\theta_i\big]\quad\forall a_i\in A_i .$$

> **A BNE is a Nash equilibrium of the Harsanyi game** (Gibbons p. 151: *"a Bayesian Nash
> equilibrium is simply a Nash equilibrium in a Bayesian game"*). Two equivalent ways to find one:
> **ex ante** — build the matrix of prior-expected payoffs over type-contingent strategies and find
> its Nash equilibria (the entry game, [[L07-01-bayesian-games-harsanyi]] §2.3); **interim** — check
> (12.2) for each type separately. MWG Prop. 8.E.1 (p. 256) is the statement that the two coincide
> for every type that occurs with positive probability.

**Existence** (Gibbons pp. 151–152): a finite static Bayesian game has a BNE, possibly in mixed
strategies — the proof is Nash's existence theorem applied to the Harsanyi game.

---

## 3 · Worked — chicken with incomplete information (§12.2.1, pp. 252–255)

### 3.1 · The game

Two teenagers drive at each other; each chooses chicken ($C$/$c$) or drive ($D$/$d$).

| Outcome | Payoff to $i$ |
|---|---|
| $i$ chickens | $0$ (whatever $j$ does) |
| $i$ drives, $j$ chickens | $R$ (all the respect) |
| both drive | $R/2-k_i$ (split respect, accident cost $k_i$) |

$k_i$ is $i$'s **type**: harsh parents $H$ or lenient parents $L<H$, each with probability $\tfrac12$,
**independently** across players. Each kid knows his own parents only. Four equally likely states
$\theta_1\theta_2\in\{LL,LH,HL,HH\}$ (Fig. 12.3, p. 253). Strategies: $xy\in\{CC,CD,DC,DD\}$ for
player 1, $x$ = action of type $L$, $y$ = action of type $H$; likewise $\{cc,cd,dc,dd\}$ for player 2.

### 3.2 · One cell by hand: $(CD,dd)$ (p. 254)

Player 1's $L$-type chickens, $H$-type drives; both types of player 2 drive. Average over the four
states, each with weight $\tfrac14$:

$$E u_1=\tfrac14\underbrace{u_1(C,d;L)}_{0}+\tfrac14\underbrace{u_1(C,d;L)}_{0}+\tfrac14\underbrace{u_1(D,d;H)}_{R/2-H}+\tfrac14\underbrace{u_1(D,d;H)}_{R/2-H}=\frac R4-\frac H2 .$$

$$E u_2=\tfrac14\underbrace{u_2(C,d;L)}_{R}+\tfrac14\underbrace{u_2(C,d;H)}_{R}+\tfrac14\underbrace{u_2(D,d;L)}_{R/2-L}+\tfrac14\underbrace{u_2(D,d;H)}_{R/2-H}=\frac{3R}4-\frac L4-\frac H4 .$$

### 3.3 · The whole matrix at $R=8$, $H=16$, $L=0$ (p. 254)

| P1 \ P2 | $cc$ | $cd$ | $dc$ | $dd$ |
|---|---|---|---|---|
| $CC$ | $0,0$ | $0,4$ | $0,4$ | $0,8$ |
| $CD$ | $4,0$ | $-1,-1$ | $-1,3$ | $-6,2$ |
| $DC$ | $4,0$ | $3,-1$ | $\mathbf{3,3}$ | $2,2$ |
| $DD$ | $8,0$ | $2,-6$ | $2,2$ | $-4,-4$ |

Check against §3.2: $(CD,dd)$ gives $8/4-16/2=-6$ and $3\cdot8/4-0-16/4=2$. ✓

**Best responses.** Player 1's best row in each column: $cc\to DD$ (8); $cd\to DC$ (3); $dc\to DC$ (3);
$dd\to DC$ (2). Player 2's best column in each row: $CC\to dd$ (8); $CD\to dc$ (3); $DC\to dc$ (3);
$DD\to dc$ (2). The only cell that is a best response both ways:

$$\boxed{(DC,\;dc)}\quad\text{— the unique pure-strategy BNE (p. 254).}$$

### 3.4 · The same answer type by type (the interim check)

Take player 2 playing $dc$ (lenient drives, harsh chickens). Player 1 believes each with probability
$\tfrac12$.

| Player 1's type | $C$ | $D$ | Best |
|---|---|---|---|
| $L$ ($k=0$) | $0$ | $\tfrac12\underbrace{(4-0)}_{\text{vs. }d}+\tfrac12\underbrace{8}_{\text{vs. }c}=6$ | $D$ |
| $H$ ($k=16$) | $0$ | $\tfrac12(4-16)+\tfrac12\cdot8=-2$ | $C$ |

So $DC$ is player 1's best reply to $dc$, and by symmetry $dc$ to $DC$. The ex-ante payoff is
$\tfrac12\cdot6+\tfrac12\cdot0=3$, the matrix's $(3,3)$. ✓

> **The prediction is only as good as the payoffs** (p. 255). With $R=8$, $H=16$, $L=0$, "harsh
> upbringing" yields fewer crashes. Tell the story the other way — lenient parents' children respect
> the car ($L=16$), harsh parents' children do not ($H=0$) — and the unique BNE flips to
> $(CD,cd)$. Same game form, opposite policy advice.

---

## 4 · U — reading a BNE

- **Each type is effectively a separate player** maximizing against his conditional distribution of
  the others' actions (MWG's gloss on Prop. 8.E.1, p. 256).
- **Uncertainty about the opponent's type acts like a mixed strategy by the opponent.** Player 1 of
  type $L$ above faces "drive with probability $\tfrac12$" although player 2 plays a pure strategy.
- **A BNE is a consistency condition**, not a learning story: beliefs about types are given by the
  prior, beliefs about strategies must be correct ([[../../rules/game-theory|rules/game-theory]]
  item 17).

---

## Links

- Prev: the Harsanyi transformation and the entry game → [[L07-01-bayesian-games-harsanyi]].
- Next: the same definition with a continuum of actions → [[L07-03-cournot-private-costs]].
- Nash equilibrium of a complete-information game: [[../L02/L02-00-map|Lecture 2]].
- Separating vs pooling strategies, and what changes when actions are observed before others move:
  [[../L08/L08-00-map|Lecture 8]].
- Code: [[L07-12-python]] §2 (`pure_nash` on the chicken matrix, both parameter sets).
- **Exercises (number + page only):** Tadelis 12.1 (p. 266), 12.3 (pp. 266–267), 12.4 (p. 267);
  Gibbons 3.4 (pp. 169–170); MWG 8.E.1 (p. 265); Muñoz-Garcia Ch. 7 Ex. 3 (p. 327), Ex. 4
  (p. 331), Ex. 7 (p. 343).
