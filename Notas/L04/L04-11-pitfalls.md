---
tags: [notes, lecture-04, pitfalls, true-false, review]
date: 2026-10-16
status: estimated
source: "Confusions drawn from Tadelis (2013) Ch. 9, 11; Gibbons (1992) §2.1.D, §2.2; MWG 9.AA; the distractors of Listas/lista-aulas-01-02.tex Block 3. True/False items are original, in the macro-1 style of rules/00_estilo_avaliacao.md"
---

# Lecture 4 · Pitfalls and an original True/False self-test

> Prev: [[L04-10-formulas]] · Next: [[L04-12-python]] · Map: [[L04-00-map]]

---

## Part I — the confusions this material produces

### 1 · "An SPE plays a stage Nash equilibrium in every stage"

**Only the last stage must be a stage NE** (Proposition 9.2). Earlier stages can be anything the
continuation can enforce. *Counterexample:* $(M,m)$ in stage 1 of the Prisoner-Revenge Game, an
SPE path for $\delta\ge\frac13$, although $(M,m)$ is not a NE of the Prisoner's Dilemma.
→ [[L04-02-carrot-and-stick]] §3.

### 2 · "Two equilibria in stage 2 are enough"

They are necessary, not sufficient: the gap must also beat the one-shot gain after discounting,
$g\le\delta(c-s)$. *Counterexample:* at $\delta=0.2$ only $(F,f)$ survives in stage 1. And with a
**unique** stage-2 NE nothing can be enforced at all (Proposition 9.3). → note 02 §2, §4.

### 3 · "Punish with any threat that hurts"

A punishment must be a **Nash equilibrium of the subgame** where it is carried out. "I play gang
while you play loner" is not one ($-1$ for the gang member, but the loner would switch to $G$ for
$-3>-4$). Only the switch from $(L,l)$ to $(G,g)$ is credible. → note 02 §4.

### 4 · Testing a deviation with the wrong continuation

A one-stage deviation changes the action at **one** information set; afterwards the deviator
follows **his own** strategy, which may itself prescribe the punishment. *Example:* the stage-1
fink is followed by $G$, so the deviation payoff is $5-3\delta$, not $5+0$. → [[L04-03-one-stage-deviation]] §3.

### 5 · Two-stage games: substituting a non-equilibrium, or reading dominance as efficiency

Stage 2 is replaced by its **Nash equilibrium**, never by the jointly best outcome. And a dominant
tariff is not a good tariff: $(t^*,t^*)$ gives $65/162$ each against $72/162$ under free trade. Nor does
the bank-run model predict runs; it shows they *can* be an equilibrium. → [[L04-04-two-stage-applications]].

### 6 · Nash vs subgame perfect in the ultimatum game

"Any split is an equilibrium" is true **for Nash** (Proposition 11.1) and false for SPE
(Proposition 11.2). The Nash strategies rely on a responder who would reject a positive offer, a
threat never tested on the path. → [[L04-05-ultimatum-game]].

### 7 · "The experiments refute the theory"

They refute *money = utility*. With a payoff that falls with the proposer's advantage, rejecting a
low offer is sequentially rational, and the SPE changes accordingly. → note 05 §4.

### 8 · Mixing the two advantages

The **last** mover's advantage comes from the deadline; the **first** mover's from discounting.
With $\delta=1$ only the **last** word matters ($x_1=1$ for odd $T$, $0$ for even). With
$T\to\infty$ only the **first** move matters, and it is worth $\frac1{1+\delta}$.
→ [[L04-06-finite-alternating-offers]] §5.

### 9 · Offering the responder the discounted *pie* instead of her discounted *continuation*

The responder gets $\delta\times$ what she would obtain **as next round's proposer**, not
$\delta\times1$. With two rounds those coincide ($\delta$), with three they do not
($\delta(1-\delta)$ to player 2). → note 06 §3; [[L04-07-rubinstein-infinite-horizon]] §3.

### 10 · The order of limits

$\lim_{\delta\to1}\lim_{T\to\infty}v_1=\frac12$ but $\lim_{T\to\infty}\lim_{\delta\to1}v_1=1$ (odd $T$).
"Patient players split equally" needs the horizon to go first (footnote 2, p. 227).

### 11 · Swapping the discount factors

$x^*=\frac{1-\delta_2}{1-\delta_1\delta_2}$ has the **responder's** factor in the numerator. Your own
patience raises your share, the opponent's lowers it. The swapped formula
$\frac{1-\delta_1}{1-\delta_1\delta_2}$ is a standard wrong answer (it is distractor D of Listas Block 3,
Question 5a). → note 07 §4.

### 12 · "The infinite game is the limit of the finite games"

Here the answers coincide, but that is a **theorem**, proved by stationarity, not a definition. In
repeated games ([[../L05/L05-00-map|Lecture 5]]) the infinite game supports cooperation that every
finite version rules out (MWG p. 298). → note 07 §1.

### 13 · Legislative bargaining: $v=1/N$ is not the proposer's share

$v=1/N$ is the *ex ante* value of the game; the proposer keeps $k=1-\delta\frac{N-1}{2N}$, more than
$1/N$. And an open rule hurts the proposer: $\frac1{1+2\delta}<1-\frac\delta3$. → [[L04-08-legislative-bargaining]].

---

## Part II — True or False (original, 20 items)

Scoring as in the course style: $\max\{0,\ \text{correct}-\text{wrong}/2\}$ per item value; blanks
do not count.

**1.** In a finite multistage game in which every stage-game has a unique Nash equilibrium, the
only subgame-perfect path plays that equilibrium in every stage.
**T.** Proposition 9.3: by backward induction the last stage is fixed after every history, so the
second-to-last stage cannot be linked to the future, and so on.

**2.** In the Prisoner-Revenge Game, $(M,m)$ in stage 1 can be part of an SPE path when
$\delta=0.4$.
**T.** The condition is $4\ge5-3\delta$, i.e. $\delta\ge\frac13$; $0.4$ qualifies ($4\ge3.8$).

**3.** In the same game, $(F,m)$ in stage 1 can be part of an SPE path when $\delta=0.6$.
**F.** Player 2 needs $-1\ge1-3\delta$, i.e. $\delta\ge\frac23$; at $0.6$ fink pays $1-1.8=-0.8>-1$.

**4.** If stage 2 has two Nash equilibria with the same payoffs for both players, history-dependent
strategies can still sustain a non-equilibrium outcome in stage 1.
**F.** Carrot minus stick is zero, so the discounted punishment $\delta(c-s)=0$ cannot offset any
positive one-shot gain.

**5.** A player in the Prisoner-Revenge Game has 32 pure strategies.
**T.** One stage-1 action plus one stage-2 action for each of the four stage-1 outcomes: $2^5=32$.

**6.** To check that a profile is subgame perfect in a finite game, it suffices to check that no
player gains by changing his action at a single information set while following his strategy
elsewhere.
**T.** Theorem 9.1, the one-stage deviation principle.

**7.** In Gibbons's bank-run model, both investors withdrawing at date 1 is the unique
subgame-perfect outcome.
**F.** After substituting date 2's $(R,R)$, the date-1 game has two pure NE: the run $(r,r)$ and
waiting $(R,R)$.

**8.** In Gibbons's tariff model, each government's equilibrium tariff depends on the other
government's tariff.
**F.** $W_i^*$ depends on $t_j$ only through the export-profit term, which does not involve $t_i$; so
$t_i^*=(a-c)/3$ is dominant.

**9.** In the tariff model, both governments would be better off committing to zero tariffs.
**T.** Each gets $72/162$ of $(a-c)^2$ at free trade against $65/162$ at the dominant tariffs: a
Prisoners' Dilemma.

**10.** In the ultimatum game, offering the responder 40% of the pie is a Nash equilibrium outcome.
**T.** Proposition 11.1: "accept iff offered at least 40%" against "offer 40%" are mutual best
responses. It is not subgame perfect.

**11.** In the ultimatum game's unique SPE, the responder rejects an offer of zero.
**F.** If she rejected zero, the proposer would have no best response (no largest $x<1$); in the SPE
she accepts every offer, including $x=1$ (Proposition 11.2).

**12.** With two rounds of bargaining and a common $\delta=0.7$, the first proposer receives 70% of
the pie.
**F.** She receives $1-\delta=30\%$; the responder can wait and take the whole pie in round 2,
worth $0.7$ now.

**13.** With $T=3$ and a common $\delta=0.5$, player 1 receives $0.75$.
**T.** $x_1=1-\delta+\delta^2=1-0.5+0.25=0.75$, equivalently $\frac{1+0.125}{1.5}=0.75$.

**14.** In the finite alternating-offer game with discounting, an agreement may be reached only in
the last round if players are very patient.
**F.** Proposition 11.3: any later agreement wastes pie that a slightly better round-1 offer could
share, so every SPE agrees in round 1, for any $\delta<1$.

**15.** In the finite game with $\delta=1$ and $T$ odd, player 1 receives the whole pie.
**T.** With no cost of delay the last proposer's take-it-or-leave-it power flows up the tree:
$x_1=\frac{1+1}{1+1}=1$.

**16.** In Rubinstein's infinite-horizon game with common $\delta$, the first proposer receives more
than half the pie for every $\delta\in(0,1)$.
**T.** $\frac1{1+\delta}>\frac12\iff\delta<1$.

**17.** In Rubinstein's game with $\delta_1=0.8$ and $\delta_2=0.5$, player 1's share is
$\frac{0.5}{0.6}$.
**T.** $\frac{1-\delta_2}{1-\delta_1\delta_2}=\frac{0.5}{1-0.4}=\frac{0.5}{0.6}\approx0.833$.

**18.** Raising the responder's discount factor raises the proposer's infinite-horizon share.
**F.** $\partial x^*/\partial\delta_2=-(1-\delta_1)/(1-\delta_1\delta_2)^2<0$: a patient responder must be paid
more.

**19.** Under Baron–Ferejohn's closed rule with three legislators, the proposer keeps $1-\delta/3$.
**T.** (11.8) with $N=3$: $k=1-\delta\frac{2}{6}$; she buys one partner at $\delta v=\delta/3$.

**20.** Under the open rule with three legislators, catering to a single partner gives the proposer
a higher expected payoff than the guaranteed-success proposal for every $\delta\in(0,1)$.
**F.** Only for $\delta>\sqrt3-1\approx0.732$; below that the guaranteed proposal $\frac1{1+2\delta}$
is better.

---

## Links

- Formulas: [[L04-10-formulas]]. Python checks of every number above: [[L04-12-python]].
- Quiz on the same ground from Aula 2: `Simulados/quiz-aula02-3-nash-offers-2026-10-13.md`.
