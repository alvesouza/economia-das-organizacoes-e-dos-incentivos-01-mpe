---
tags: [notes, lecture-06, repeated-games, pitfalls, true-false, review]
date: 2026-10-16
status: estimated
source: "Original items built on Tadelis (2013) §10.4–10.5; Gibbons (1992) §2.3.C–D; Cabral (2017) Ch. 9; Milgrom & Roberts (1992) Ch. 8; MWG §12.D. True/False format of rules/00_estilo_avaliacao.md (macro-1)."
---

# Lecture 6 · Pitfalls and a True/False self-test

> Prev: [[L06-09-formulas]] · Next: [[L06-11-python]] · Map: [[L06-00-map]]

---

## Part I — the confusions this material produces

### 1 · "Any deviation" instead of the best one-period deviation

The cutoff (10.5) uses $v^d$, the **most tempting** deviation — the stage best response to
the others' cooperative play. A firm in Tadelis's cartel that deviates from 22 to 30 gains
$(100-30-23-10)\times30=1110$; to 33.5 it gains 1122.25. Using 30 gives
$\delta^*=(1110-990)/(1110-900)=0.571$ instead of 0.595 — an understated requirement.
→ [[L06-02-cournot-collusion]] §2.

### 2 · One cutoff for an asymmetric cartel

Each player has his own cutoff; the cartel survives iff $\delta\ge\max_i\delta_i^*$. In the
22/23 split the **smaller** firm binds (0.595 against 0.473). And copy the book with care: its
0.392 for firm 2 plugs in the wrong rival quantity.

### 3 · "Too little patience means back to the stage game" — true for Bertrand, false for Cournot

Bertrand: the condition $\frac{\pi(p)/n}{1-\delta}\ge\pi(p)$ does not depend on $p$, so below
$1-1/n$ nothing above cost survives (MWG Prop. 12.D.2). Cournot: below $9/17$ the cartel
**shrinks** to $q^*(\delta)$ and still beats Cournot. → [[L06-03-bertrand-market-structure]] §1.

### 4 · "Price competition makes collusion harder" — not at $n=2$

Bertrand needs $1/2$, Cournot $9/17>1/2$ with two firms; from $n=3$ the ranking flips
($0.667>0.571$). Harsher stick against bigger temptation.

### 5 · Reading a price war as proof that someone cheated

Under imperfect monitoring (Green–Porter) wars happen **on** the equilibrium path after bad
demand shocks, and nobody cheats. Under observed shocks (Rotemberg–Saloner) prices fall in
**booms**. → [[L06-04-punishments-price-wars]] §3–§4.

### 6 · Grim trigger as "the" punishment

It is the simplest, not the strongest: Abreu's one-period stick sustains the monopoly
outcome at $\delta=1/2<9/17$. And "forever" invites renegotiation.

### 7 · Forgetting the off-path half of a strategy

"Cooperate as long as player 1 trusts me" is a Nash equilibrium, not an SPE (Tadelis footnote
9). A repeated-game strategy specifies play after **every** history.

### 8 · Mixing the two $p$'s

Gibbons's $p$ = probability that **shirking goes undetected** (output still high); M&R's $p$ =
probability that **cheating is detected**. Gibbons's premium has $1-p$ in the denominator,
M&R's has $p$. Same economics, opposite letters. → [[L06-07-efficiency-wages]] §6.2.

### 9 · M&R's $NV>G$ taken literally

From the box, cheating yields $V+G$ in the round of cheating; the exact comparison is
$NV\ge V+G\iff\delta\ge G/(V+G)$. With $V=G=1$, $NV>G$ would give $N>1$, i.e. any $\delta>0$
— wrong; the exact form gives $\delta\ge1/2$.

### 10 · "Efficient, therefore sustainable"

$y-e>w_0$ makes the employment relation efficient; it is sustainable only if
$y\ge w^*$, i.e. $\delta\ge e/(e+(1-p)(y-e-w_0))$. With M&R's calibration and $y=41$, that is
$\delta\ge0.952$.

### 11 · Reputation without observability or judgment

Reputation needs future partners to **see** the past and to **judge** it. Remove either (no
communication, ambiguous duties) and the incentive disappears — the case for law merchants,
credit bureaus and corporate culture. → [[L06-05-reputation-trust]] §6.

### 12 · Reproducing a finite-horizon argument in an infinite game, or vice versa

Known last period: unravels (end game, CEO near retirement). Indefinite continuation with
probability $\delta$: cooperation possible. The question always states which one.

---

## Part II — True/False (original items)

*Scoring as in `macro-1`: $\max\{0,\ \text{correct}-\text{wrong}/2\}$ × item value; blanks do
not count as wrong.*

**1.** In the infinitely repeated Cournot duopoly with $P=a-Q$ and constant marginal cost,
grim trigger sustains half the monopoly output for every player iff $\delta\ge9/17$.
**True.** $\pi_m/2=(a-c)^2/8$, $\pi_d=9(a-c)^2/64$, $\pi_c=(a-c)^2/9$; (10.5) gives
$(1/64)/(17/576)=9/17$; the symmetric game gives both firms the same cutoff.

**2.** If $\delta<9/17$ in that duopoly, the only subgame-perfect outcome of the repeated game
under Nash-reversion strategies is the Cournot outcome in every period.
**False.** Grim trigger still sustains any symmetric $q\ge q^*(\delta)=\frac{9-5\delta}{3(9-\delta)}(a-c)$,
strictly below Cournot for $\delta>0$ — e.g. $0.2549(a-c)$ at $\delta=1/2$.

**3.** In the repeated Bertrand duopoly with grim strategies, the cutoff discount factor
depends on the collusive price chosen.
**False.** Conform $\frac{\frac12\pi(p)}{1-\delta}$ versus deviate $\pi(p)$: $\pi(p)$ cancels
and the cutoff is $1/2$ for every $p\in(c,p_M]$ (MWG Prop. 12.D.2).

**4.** With $n$ symmetric Bertrand firms, collusion at the monopoly price is sustainable iff
$\delta\ge1-1/n$.
**True.** $\frac{\pi_M/n}{1-\delta}\ge\pi_M\iff1/n\ge1-\delta$.

**5.** With two firms, tacit collusion requires more patience under Bertrand than under
Cournot competition.
**False.** $1/2<9/17$: with two firms Bertrand needs less; the ranking reverses from three
firms on.

**6.** In Tadelis's 22/23 split of the monopoly output, the firm producing 22 needs a higher
discount factor than the firm producing 23.
**True.** It gains more by deviating (132.25 vs 121) and loses less per period from Cournot
(90 vs 135): 0.595 against 0.473.

**7.** By Cabral's (9.5), collusion is easier in an industry that reprices daily than in one
that reprices once a year, other things equal.
**True.** $\delta=\frac{(1+g)(1-h)}{1+r/f}$ rises with the frequency $f$.

**8.** An increase in the hazard that the industry disappears makes collusion easier because
firms have less to lose from a price war.
**False.** A higher $h$ lowers $\delta$: the future punishment matters less, so the
temptation wins more often — collusion is **harder**.

**9.** In Cabral's model, if two firms meet in two identical markets, multimarket contact
halves the discount factor needed to collude.
**False.** Both the gain from deviating and the punishment double; the cutoff stays $1/2$.
Contact helps only when the markets differ.

**10.** In a Green–Porter cartel with unobserved demand shocks, price wars occur on the
equilibrium path even though no firm ever deviates.
**True.** Low prices must trigger punishment or every firm would cut secretly; bad shocks then
start wars with nobody cheating.

**11.** If demand shocks are observed before pricing and are independent over time, a collusive
cartel's price tends to be lowest when demand is highest.
**True.** The deviation gain scales with current demand while the future loss does not; the
constraint binds in booms, so the cartel cuts its price there (Rotemberg–Saloner).

**12.** In Abreu's two-phase strategy at $\delta=1/2$, any punishment output $x$ larger than the
Cournot quantity $(a-c)/3$ sustains the monopoly outcome.
**False.** The collusive-phase constraint needs $x\ge\frac38(a-c)$, and $\frac13<x<\frac38$ fails
it; the feasible band is $x/(a-c)\in[3/8,1/2]$.

**13.** A punishment that hurts the punisher as well as the deviator can never be part of a
subgame-perfect equilibrium.
**False.** Both grim trigger and Abreu's stick hurt the punisher; they are SPE because carrying
out the punishment is a best response given what follows. The issue they raise is
renegotiation, not subgame perfection.

**14.** In Tadelis's repeated trust game with payoffs $(1,1)$, $(-1,2)$ and $(0,0)$, cooperation
is sustainable by grim trigger iff $\delta\ge1/2$.
**True.** $\frac{1}{1-\delta}\ge2$.

**15.** In M&R's trust box, the decision maker's exact no-cheating condition is $NV\ge G$.
**False.** Cheating gives $V+G$ in the round of cheating; the exact condition is
$NV\ge V+G$, i.e. $\delta\ge G/(V+G)$.

**16.** Reputation can discipline a decision maker even if he never meets the same offeror
twice, provided each offeror observes how he treated earlier offerors.
**True.** M&R p. 263: the calculation is the same as with one offeror; that is what a
reputation is.

**17.** A guarantor who earns a fee of 0.1 per period and could pocket a bond of 2 keeps the
contract iff $\delta\ge0.95$.
**True.** $\frac{0.1}{1-\delta}\ge2\iff\delta\ge0.95$.

**18.** In Gibbons's efficiency-wage model, the wage premium needed to induce effort falls as the
probability that a shirker still produces high output rises.
**False.** The premium $\frac{(1-\delta)e}{\delta(1-p)}$ **rises** with $p$: shirking is
caught less often, so a larger rent is needed.

**19.** If shirking is always detected ($p=0$ in Gibbons), the firm can induce effort by paying
exactly $w_0+e$.
**False.** It must still pay $w_0+e/\delta$: the gain $e$ today must be covered by the rent from
tomorrow, which is discounted. Only as $\delta\to1$ does $w^*\to w_0+e$.

**20.** In the efficiency-wage model, $y-e>w_0$ guarantees that the high-wage, high-output
equilibrium exists for every $\delta$.
**False.** It also needs $y\ge w^*$, i.e. $\delta\ge e/\bigl(e+(1-p)(y-e-w_0)\bigr)$.

**21.** With M&R's numbers (rent USD 10,000, detection 5%, gain USD 1,000), a worker with
$N=1$ prefers to cheat.
**True.** Expected loss $0.05\times10{,}000=500<1{,}000$; the efficiency wage would be USD
60,000.

**22.** A longer expected relationship (higher $N$) leads, in M&R's minimum-cost implementation
problem, to more intensive monitoring.
**False.** $dp^*/dN<0$: a longer relationship substitutes for monitoring ("more trust and less
direct monitoring", p. 255).

**23.** A known final period weakens reputational incentives as it approaches.
**True.** The end-game problem (M&R p. 266): at the last date there is no future to protect,
and the argument creeps backwards; hence more explicit incentive pay for CEOs near retirement.

**24.** A firm's brand name can sustain cooperation by short-lived owners because the brand's
resale value is lost if trust is abused under it.
**True.** Kreps's brand acts as a bond (Tadelis pp. 207–208): the resale value above 1
exceeds the one-period gain from defecting.

---

## Links

[[L06-00-map]] · [[L06-09-formulas]] · [[L06-11-python]] · style:
[`rules/00_estilo_avaliacao.md`](../../rules/00_estilo_avaliacao.md).
