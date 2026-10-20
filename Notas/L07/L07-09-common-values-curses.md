---
tags: [notes, lecture-07, common-values, winners-curse, swing-voters-curse, jury]
date: 2026-10-16
status: estimated
source: "Tadelis (2013) §12.4 'Committee Voting' (jury game, posteriors, signal table, pp. 261–264) and §13.2 'Common Values and the Winner's Curse' (oil field, E[v|L] = 15, E[v|H] = 25, payoff -1.25, pp. 282–284); Cabral (2017) §6.4, p. 142"
---

# 12.4 · 13.2 · Common values: condition on the event in which your choice matters

> **Claim.** When the others' information bears on what an outcome is worth to you, **your action
> matters only in particular states — and those states are informative**. A juror is decisive only
> when the other juror votes to convict; a bidder wins only when the other bidder's signal was low.
> Ignoring that conditioning makes **voting your signal** and **bidding your expected value** fail as
> equilibria. Same mechanics as adverse selection: the event "trade happens" is bad news about quality.
>
> Prev: [[L07-08-revenue-equivalence]] · Next: [[L07-10-formulas]] · Map: [[L07-00-map]]

---

## 1 · C — the jury game (§12.4, pp. 261–264)

### 1.1 · Without private information

Two jurors vote Acquit ($A$) or Convict ($C$); conviction needs **both** $C$. The defendant is guilty
($G$) with prior $q>\tfrac12$. Each juror gets 1 for the right verdict, 0 for the wrong one.

| | $A$ | $C$ |
|---|---|---|
| $A$ | $1-q,\;1-q$ | $1-q,\;1-q$ |
| $C$ | $1-q,\;1-q$ | $q,\;q$ |

With $q>\tfrac12$, $C$ is weakly dominant (p. 261).

### 1.2 · Private signals

Each juror privately sees $\theta_i\in\{\theta_G,\theta_I\}$, independent given the truth:
$\Pr\{\theta_G\mid G\}=\Pr\{\theta_I\mid I\}=p>\tfrac12$. The type is **information about the state**,
not a taste — and since the state enters everyone's payoff, this is a **common-values** game (p. 262).
Strategies $xy\in\{AA,AC,CA,CC\}$: $x$ after $\theta_G$, $y$ after $\theta_I$.

**Alone, a juror follows his signal iff $p>q$** (p. 262):
$$\Pr\{G\mid\theta_G\}=\frac{qp}{qp+(1-q)(1-p)}>q,\qquad
\Pr\{G\mid\theta_I\}=\frac{q(1-p)}{q(1-p)+(1-q)p}<q,$$
and acquitting after $\theta_I$ is right iff $\Pr\{G\mid\theta_I\}<\tfrac12\iff q(1-p)<(1-q)p\iff q<p$.
At $p=\tfrac12$ the signal is noise and the posterior stays $q$.

### 1.3 · Is "vote your signal" ($CA$, $CA$) an equilibrium? (pp. 263–264)

**Signal probabilities** (p. 263):

| | $\theta_2=\theta_G$ | $\theta_2=\theta_I$ |
|---|---|---|
| $\theta_1=\theta_G$ | $qp^2+(1-q)(1-p)^2$ | $p(1-p)$ |
| $\theta_1=\theta_I$ | $p(1-p)$ | $q(1-p)^2+(1-q)p^2$ |

(Off-diagonal: $qp(1-p)+(1-q)(1-p)p=p(1-p)$.)

**Pivotality.** Under unanimity, juror $i$'s vote changes the verdict **only if $j$ votes $C$**; if $j$
plays $CA$, that means $\theta_j=\theta_G$. So $i$ must evaluate his vote **conditional on $\theta_j=\theta_G$**:

$$\Pr\{G\mid\theta_i=\theta_G,\theta_j=\theta_G\}=\frac{qp^2}{qp^2+(1-q)(1-p)^2}>q\;\Rightarrow\;C,$$

$$\Pr\{G\mid\theta_i=\theta_I,\theta_j=\theta_G\}=\frac{q(1-p)p}{p(1-p)}=q>\tfrac12\;\Rightarrow\;C,\ \text{not }A .$$

The two opposite signals **cancel**, leaving the prior. A $\theta_I$ juror who is pivotal should
convict, so **$CA$ is not a best response to $CA$**: voting one's signal is not a BNE.

> **The swing voter's curse** (Feddersen–Pesendorfer 1996; Austen-Smith–Banks 1996; p. 264): *"When
> a voter believes that his vote counts, he must condition this on the situation in which his vote
> counts."* It cuts against the **Condorcet jury theorem**, whose assumption that voters act as they
> would alone is exactly what strategic conditioning breaks.

**A check before exercise 12.8 (p. 268).** Tadelis states (p. 264) that both jurors playing $CC$ is a
BNE and leaves it to exercise 12.8(a). Run the pivotal logic on it: if $j$ always convicts, $i$ is
always decisive and conditions on his own signal only — so by §1.2 a $\theta_I$ juror prefers to acquit
whenever $p>q$ (e.g. $q=0.6$, $p=0.7$: $\Pr\{G\mid\theta_I\}=0.391<\tfrac12$). Work the exercise keeping the
case $p\le q$ versus $p>q$ explicit ([[L07-12-python]] §4 computes both).

---

## 2 · C — the oil field and the winner's curse (§13.2, pp. 282–284)

### 2.1 · Pure common value

Two identical firms bid for an oil field worth the **same** $v$ to both:

| $v$ | 10 | 20 | 30 |
|---|---|---|---|
| $\Pr$ | $\tfrac14$ | $\tfrac12$ | $\tfrac14$ |

Each firm explores and sees $\theta_i\in\{L,H\}$: $v=10\Rightarrow LL$; $v=30\Rightarrow HH$; $v=20\Rightarrow LH$ or
$HL$ with equal chance. Every signal pair has probability $\tfrac14$ — and the signals are **correlated**
through $v$.

### 2.2 · Posteriors and conditional values (pp. 283–284)

A firm with $L$ knows the pair is $LL$ ($v=10$) or $LH$ ($v=20$), each with prior $\tfrac14$:
$\Pr\{\theta_j=L\mid\theta_i=L\}=\tfrac{1/4}{1/2}=\tfrac12$. So

$$E[v\mid\theta_i=L]=\tfrac12\cdot10+\tfrac12\cdot20=15,\qquad E[v\mid\theta_i=H]=\tfrac12\cdot20+\tfrac12\cdot30=25 .$$

### 2.3 · "Bid your expected value" in a second-price auction fails (p. 284)

Suppose firm 2 bids $s_2(\theta_2)=E[v\mid\theta_2]$, and firm 1 with $L$ bids 15.

| Firm 2's signal (prob.) | Firm 2's bid | Outcome for firm 1 | True $v$ | Firm 1's payoff |
|---|---|---|---|---|
| $L$ ($\tfrac12$) | 15 | tie: wins with prob. $\tfrac12$, pays 15 | 10 | $\tfrac12(10-15)=-2.5$ |
| $H$ ($\tfrac12$) | 25 | loses | 20 | 0 |

$$E u_1=\tfrac12\cdot\tfrac12\cdot(10-15)+\tfrac12\cdot0=-1.25<0 .$$

Firm 1 would rather bid below 15 and never win. **The truthful-looking strategy is not a BNE.**

> **The winner's curse** (p. 284): *"a player wins when his signal is the most optimistic, which in
> the common-values setting means that he has overestimated the value of the good."* The equilibrium
> bid must condition on **winning**, not just on one's own signal: $E[v\mid\theta_1=L,\ \text{I win}]=
> E[v\mid LL]=10<15$.

The BNE of this auction is Tadelis exercise 13.8 (p. 287). The curse exists in first- and second-price
formats alike (p. 284).

### 2.4 · Why private-value logic does not transfer

| | Private values ([[L07-06-second-price-english]]) | Common values (here) |
|---|---|---|
| Your value | known to you: $\theta_i$ | $E[v\mid\text{all signals}]$ — you see one |
| Winning tells you | nothing about your value | that the rival's signal was lower |
| Second-price advice | bid $\theta_i$, weakly dominant | bidding $E[v\mid\theta_i]$ loses money |
| English vs sealed second-price | same outcome | not the same: quitting prices reveal signals (named, Krishna 2002, Milgrom 2004) |

---

## 3 · U — the curse in the field (Cabral p. 142)

A domestic telecom operator and a foreign one bid for spectrum; values are correlated (a small market is
small for both) and the domestic firm is better informed. **The uninformed bidder must shade more** — if
it wins, it is probably because the informed rival bid low. Seasoned bidders learn this, so the
uninformed bid less and win less often. In US offshore oil-lease auctions the winner is most often the
firm already drilling the **adjacent** tract — the better-informed bidder.

---

## 4 · U — one lesson, three settings

| Setting | Your choice matters when … | … which tells you | Naive behaviour | Note |
|---|---|---|---|---|
| Lemons | the seller **accepts** your price | quality is below the price | pay for the average | [[L07-05-adverse-selection-lemons]] |
| Jury | the other juror **convicts** | his signal said guilty | vote your signal | §1 |
| Common-value auction | you **win** | the rival's signal was lower | bid $E[v\mid\theta_i]$ | §2 |

> **Common thread: Bayes' rule applied to the event in which your action is decisive.** In each case
> the naive strategy is optimal for a decision taken alone and fails in the game.

---

## Links

- Prev: [[L07-08-revenue-equivalence]] · Next: [[L07-10-formulas]].
- Posterior beliefs from a correlated prior: [[L07-01-bayesian-games-harsanyi]] §4.
- Signaling as the informed side's attempt to escape the pool: [[../L08/L08-00-map|Lecture 8]].
- Rules: [[../../rules/game-theory|rules/game-theory]] items 5 and 19; [[../../rules/07_selecao_adversa|Topic 7]].
- Code: [[L07-12-python]] §4 (jury posteriors) and §9 (`cond_value`, the $-1.25$).
- **Exercises (number + page only):** Tadelis 12.8 (pp. 268–269), 13.8, 13.10 (p. 287);
  Muñoz-Garcia Ch. 7 Ex. 4 (p. 331).
