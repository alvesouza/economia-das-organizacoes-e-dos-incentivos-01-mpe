---
tags: [notes, lecture-07, bayesian-games, types, common-prior, harsanyi]
date: 2026-10-16
status: estimated
source: "Tadelis (2013) Ch. 12 opening and §12.1.1–12.1.2, printed pp. 241–249 (entry game Figs. 12.1–12.2, Def. 12.1, Def. 12.2 and the 1/6–1/3 prior); Gibbons (1992) §3.1.B, pp. 146–149; MWG §8.E, p. 255"
---

# 12 · 12.1.1–12.1.2 · Types, Nature and the common prior: incomplete information made playable

> **Claim.** A game of incomplete information cannot be solved as it stands: nobody knows the game.
> **Harsanyi's move** turns it into a game we already know how to solve: **Nature draws each
> player's type from a commonly known distribution, each player sees only his own type**, and the
> uncertainty about *payoffs* becomes uncertainty about *Nature's move* — a game of imperfect
> information. Everything after this note is Nash equilibrium applied to that game.
>
> Prev: — · Next: [[L07-02-bayesian-nash-equilibrium]] · Map: [[L07-00-map]]

**Notation.** The Lecture 1 slides write a game as $G=(I,\{S_i\}_{i\in I},\{u_i\}_{i\in I})$;
Tadelis Ch. 12 writes the player set $N$ and payoffs $v_i$. These notes keep the slides' $I$ and
$u_i$ and Tadelis's $\theta_i\in\Theta_i$ (types) and $\phi_i$ (beliefs). Gibbons writes $t_i\in T_i$
and $p_i$.

---

## 1 · U — what complete information assumed

Every game so far assumed that **the game itself is common knowledge**: who plays, what each can
do, and how outcomes map into payoffs ([[../L01/L01-00-map|Lecture 1]], Def. 3.1 p. 45). Tadelis
opens Ch. 12 (p. 241) with the Cournot duopoly: is it reasonable that each firm knows the other's
cost function exactly? Gibbons opens Ch. 3 (p. 143) with the **sealed-bid auction**: each bidder
knows her own valuation and not the others'.

> **Incomplete information = at least one player is uncertain about another player's payoff
> function** (Gibbons p. 143). It is a statement about *preferences*, not about moves.

The problem: to best-respond, player $i$ needs a belief about what $j$ will do; what $j$ does
depends on $j$'s payoffs; $i$ does not know them. And $j$ needs a belief about $i$'s belief about
$j$'s payoffs, and so on. Harsanyi cut the infinite regress with one modelling device.

---

## 2 · C — Harsanyi's transformation, worked on Tadelis's entry game

### 2.1 · The complete-information game (Fig. 12.1, p. 243)

Player 1 (entrant) chooses Out ($O$) or Enter ($E$); after $E$, player 2 (incumbent) chooses Fight
($F$) or Accommodate ($A$).

| Outcome | $u_1$ | $u_2$ |
|---|---|---|
| $O$ | 0 | 2 |
| $E$, then $F$ | $-1$ | $-1$ |
| $E$, then $A$ | 1 | 1 |

Backward induction: after $E$, player 2 compares $-1$ with $1$ and accommodates, so player 1
enters. The unique SPE is $(E,A)$; $(O,F)$ is a Nash equilibrium sustained by an incredible threat.

### 2.2 · Add a second type of incumbent (Fig. 12.2, p. 243)

Now player 2 is **rational** (payoffs as above) with probability $p$, or **crazy** with probability
$1-p$: the crazy type *enjoys* fighting, and $(E,F)$ pays him $2$ instead of $-1$. Everything else is
unchanged.

The three things that must be pinned down (pp. 243–244):

1. **Nature moves first** and picks player 2's type.
2. **Player 2 knows his own type** when he moves; player 1 does not — hence a single information set
   for player 1 across Nature's two branches.
3. **The probability $p$ is common knowledge** — the **common prior assumption**: everyone agrees on
   how Nature draws types. *"This is of course a strong assumption, but without it we will not be
   able even to discuss equilibrium behavior"* (p. 244).

### 2.3 · The induced normal form

A strategy for player 2 must say what **each type** does: $xy\in\{AA,AF,FA,FF\}$, with $x$ the
rational type's action and $y$ the crazy type's. Player 1 has $\{O,E\}$. Each strategy pair
produces a lottery over outcomes, and expected payoffs fill the matrix. For $(E,AF)$:

$$u_1=p\cdot1+(1-p)\cdot(-1)=2p-1,\qquad u_2=p\cdot1+(1-p)\cdot2=2-p.$$

For $(E,FA)$ each type plays the action he likes less (rational fights, crazy accommodates):
$u_1=p(-1)+(1-p)(1)=1-2p$ and $u_2=p(-1)+(1-p)(1)=1-2p$. For $(E,FF)$: $u_1=-1$,
$u_2=p(-1)+(1-p)2=2-3p$. After $O$ every cell is $(0,2)$.

| | $AA$ | $AF$ | $FA$ | $FF$ |
|---|---|---|---|---|
| $O$ | $0,2$ | $0,2$ | $0,2$ | $0,2$ |
| $E$ | $1,1$ | $2p-1,\;2-p$ | $1-2p,\;1-2p$ | $-1,\;2-3p$ |

**At $p=2/3$** (the book's choice, p. 244):

| | $AA$ | $AF$ | $FA$ | $FF$ |
|---|---|---|---|---|
| $O$ | $0,2$ | $0,2$ | $0,2$ | $0,2$ |
| $E$ | $1,1$ | $\tfrac13,\tfrac43$ | $-\tfrac13,-\tfrac13$ | $-1,0$ |

**Solve it like any bimatrix game.** Player 1's best responses: against $AA$ or $AF$ enter
($1>0$, $\tfrac13>0$); against $FA$ or $FF$ stay out ($0>-\tfrac13$, $0>-1$). Player 2's best
responses: against $O$ every column pays 2 (all are best responses); against $E$ the column payoffs
are $1,\tfrac43,-\tfrac13,0$, so only $AF$. Mutual best responses:

$$\boxed{(O,FA),\quad(O,FF),\quad(E,AF)}\qquad\text{(p. 245)}$$

Only $(E,AF)$ survives the extensive-form check that each type moves optimally at his own node
(rational accommodates, crazy fights); the other two rest on types who would not carry out $F$ or $A$.

### 2.4 · Why the "meta-player" gets it right (p. 245)

The matrix averages player 2's types into one player who maximizes the **prior-weighted** sum of his
types' payoffs. That meta-player's best response coincides with each type's best response
**because a strategy specifies an action per type**: against $E$, moving from $AA$ to $AF$ changes
only the crazy type's action and raises only his payoff, so the average rises. $AA$ is not a best
response to $E$ precisely because it asks the crazy type to play a dominated action.

> **The device is not free.** Before, equilibrium asked players to hold correct beliefs about
> *actions*. Now it asks, in addition, that **everyone agree on how types are drawn** (p. 245–246).
> Predictions are only as good as that leap.

---

## 3 · C — the general object: Definition 12.1 (p. 246)

> **Definition 12.1.** The normal-form representation of an $n$-player static Bayesian game of
> incomplete information is
> $$\langle I,\{A_i\}_{i=1}^n,\{\Theta_i\}_{i=1}^n,\{u_i(\cdot;\theta_i),\theta_i\in\Theta_i\}_{i=1}^n,\{\phi_i\}_{i=1}^n\rangle$$
> where $A_i$ is $i$'s action set; $\Theta_i=\{\theta_{i1},\dots,\theta_{ik_i}\}$ is $i$'s **type
> space**; $u_i:A\times\Theta_i\to\mathbb R$ is the **type-dependent payoff**; and
> $\phi_i(\theta_{-i}\mid\theta_i)$ is $i$'s (posterior) belief about the other players' types given
> his own.

**Timing** (pp. 246–247), the four steps every Bayesian game in this lecture follows:

| Step | What happens |
|---|---|
| 1 | Nature draws a type profile $(\theta_1,\dots,\theta_n)$ |
| 2 | Each $i$ learns **only** $\theta_i$ and forms $\phi_i(\theta_{-i}\mid\theta_i)$ from the prior |
| 3 | Players choose $a_i\in A_i$ **simultaneously** (static game) |
| 4 | Payoffs $u_i(a;\theta_i)$ are realized |

### 3.1 · Private values versus common values

| | Payoff depends on | Examples in this lecture |
|---|---|---|
| **Private values** | own type only: $u_i(a;\theta_i)$ | chicken, study groups, IPV auctions ([[L07-06-second-price-english]]) |
| **Common values** | others' types too: $u_i(a;\theta_1,\dots,\theta_n)$ | the orange grove ([[L07-05-adverse-selection-lemons]]), the jury and the oil field ([[L07-09-common-values-curses]]) |

> **Every "curse" in this lecture — adverse selection, the swing voter's curse, the winner's curse
> — needs common values.** With private values, learning another player's type changes what you
> expect him to *do*, never what the outcome is *worth to you*.

Gibbons makes the same extension in two lines (p. 149): when one player's private information
enters another's payoff, write $u_i(a_1,\dots,a_n;t_1,\dots,t_n)$.

---

## 4 · C — beliefs from the common prior: Definition 12.2 (pp. 247–249)

Each player learns his own type; if types are **correlated**, his type is evidence about the
others'. Bayes' rule converts the common prior into his interim belief.

> **Definition 12.2.** Conditional on event $S$, the probability of event $H$ is
> $$\Pr\{H\mid S\}=\frac{\pi(S\cap H)}{\pi(S)}.\tag{12.1}$$

### 4.1 · Worked — the book's correlated prior (p. 249)

Types $\theta_1\in\{a,b\}$, $\theta_2\in\{c,d\}$, prior:

| | $\theta_2=c$ | $\theta_2=d$ | row sum |
|---|---|---|---|
| $\theta_1=a$ | $1/6$ | $1/3$ | $1/2$ |
| $\theta_1=b$ | $1/3$ | $1/6$ | $1/2$ |

Player 1 learns $\theta_1=a$:

$$\phi_1(c\mid a)=\frac{1/6}{1/6+1/3}=\frac{1/6}{1/2}=\frac13,\qquad
\phi_1(d\mid a)=\frac{1/3}{1/2}=\frac23 .$$

Had he learned $b$: $\phi_1(c\mid b)=\frac{1/3}{1/2}=\frac23$, $\phi_1(d\mid b)=\frac13$. **His type
moved his belief**: before learning it, $\Pr\{c\}=\tfrac16+\tfrac13=\tfrac12$.

**Independent types** (every application in Gibbons §3.2, p. 148): the prior factors,
$\pi(\theta_1,\theta_2)=\pi_1(\theta_1)\pi_2(\theta_2)$, so $\phi_i(\theta_{-i}\mid\theta_i)=\pi_{-i}(\theta_{-i})$
— the posterior equals the prior and does not depend on one's own type. Then the other players
also *know* $i$'s belief (Gibbons p. 149).

> **Correlation is where conditioning bites.** In the oil-field auction of
> [[L07-09-common-values-curses]] the signals are correlated, and it is exactly the update "I won,
> so the other signal was low" that bidders who ignore Bayes' rule get wrong.

---

## 5 · G — formal side (not examinable unless the lecture brings it)

- **The belief hierarchy.** A type must encode beliefs about beliefs about … payoffs. Harsanyi's
  argument that a rich enough type space captures the whole hierarchy was made precise by Mertens and
  Zamir (1985) and Brandenburger and Dekel (1993) (Tadelis's Remark, p. 247). Named only.
- **MWG §8.E** (p. 255) writes a Bayesian game as $[I,\{S_i\},\{u_i(\cdot)\},\Theta,F(\cdot)]$, with
  the joint distribution $F$ of the types as the common prior; Example 8.E.1 (p. 254) is a
  two-type prisoner's dilemma solved exactly like §2 above.
- **Gibbons's version** (p. 148): $G=\{A_1,\dots,A_n;T_1,\dots,T_n;p_1,\dots,p_n;u_1,\dots,u_n\}$,
  beliefs by Bayes' rule $p_i(t_{-i}\mid t_i)=p(t_{-i},t_i)/\sum_{t_{-i}'}p(t_{-i}',t_i)$ (p. 149).
  Different letters, same object.

---

## Links

- Next: strategies as type-contingent plans and the equilibrium concept →
  [[L07-02-bayesian-nash-equilibrium]].
- The entry game's complete-information version and SPE: [[../L03/L03-00-map|Lecture 3]].
- Common knowledge (Def. 3.1) and the normal form (Def. 3.3): [[../L01/L01-00-map|Lecture 1]].
- Rules: [[../../rules/game-theory|rules/game-theory]] items 1, 5, 9.
- Code: [[L07-12-python]] §1 (`harsanyi_normal_form`, `posterior`).
- **Exercises (number + page only):** Tadelis 12.1 (p. 266); Gibbons 3.1 (p. 169);
  Muñoz-Garcia Ch. 7 Ex. 1 (p. 318), Ex. 2 (p. 323).
