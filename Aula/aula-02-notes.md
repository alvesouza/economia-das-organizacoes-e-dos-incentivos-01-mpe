---
tags: [aula, aula-02, notes, topic/barganha]
date: 2026-10-13
---

# Aula 2 — Bargaining I: Value Maximization and the Coase Theorem

> **Syllabus item** · *Barganha* · [[rules/02_barganha|Topic 2]] · [[Map/study-guide#Aula 2 — Bargaining I: value maximization and the Coase theorem|class plan]]
> **Read** · Milgrom & Roberts (1992), Ch. 2 "Wealth Effects, Value Maximization and the Coase Theorem" (pp. 35–39) · Varian (2014, with Calculus) §35.2 "Quasilinear Preferences and the Coase Theorem" (p. 670) · Cabral (2017) §5.1, "The Coase Theorem" (pp. 96–99)
> **Next** · Aula 3 drops two of today's assumptions: full information (M&R Ch. 5, pp. 140–149) and costless bargaining; its formal supplement is alternating offers (MWG 9.AA, pp. 296–298)

Page numbers are M&R's printed pages unless another book is named. The worked examples are this
course's own, with numbers chosen to come out clean; they do not solve any book exercise.

---

## 0. The question

Two parties can create value together: a supplier and an assembler, a factory and the people
downstream, the divisions of one firm. Two things have to be decided: **what they do** (the
investment, the technology, who holds a right) and **how they split** what it produces. Does the
second decision affect the first?

M&R's answer has a sharp condition attached. When preferences show **no wealth effects**, "the
issue of the distribution of value is completely separable from the issue of how value is
created" (p. 38). Efficiency then pins down *what* is done; bargaining power, assets and patience
decide only *who gets what*. That is the **Coase theorem** (p. 38), and it is the foundation of
the transaction-costs approach to organization (p. 38). The class builds it up in four steps:

1. what "no wealth effects" means, and when it is a bad assumption (§1);
2. the utility form it implies, $x + v(y)$ (§2);
3. the value maximization principle: efficiency $\Leftrightarrow$ maximum total value (§3);
4. the Coase theorem, and the division of the surplus by bargaining (§4–§5).

Aula 1 already used this result without saying so: every "profit" there was a total value to be
maximized, as if the organization had one objective. §7 explains when that is legitimate.

---

## 1. Wealth effects (pp. 35–36)

A **wealth effect** is a change in choices caused by a change in wealth: a poorer person may not
afford some options, or may trade off risk and money differently (p. 35).

**No wealth effects** for a decision maker over a set of decisions requires three conditions
(p. 35):

1. **Compensability.** For any two decisions $y_1, y_2$ there is a definite amount of money that
   compensates for switching from one to the other.
2. **Independence from wealth.** Giving the decision maker more wealth first does not change that
   amount.
3. **Ability to pay.** The decision maker has enough money to absorb any payment needed to buy a
   switch to the preferred option.

Where each fails (pp. 35–36):

| Condition | Plausible | Fails |
|---|---|---|
| 1 Compensability | most business decisions | serious risk to life or limb, living far from family, freedom of religion |
| 2 Independence | a corporation whose assets unexpectedly gain value keeps its prices and hurdle rates | a lottery winner who keeps the same house and job (nobody does) |
| 3 Ability to pay | a pay cut in exchange for avoiding rush-hour traffic | holding a nuclear-plant worker financially liable for his or her mistakes |

M&R's rule of thumb: the assumption is most dangerous "when the decision makers are individuals
and when large cash transfers or significant changes in personal living conditions are involved"
(p. 36), and safest when transfers are small relative to the parties' resources.

---

## 2. The value index $u = x + v(y)$ (p. 36)

Let $x$ be money and $y$ everything else the decision affects (job assignment, effort, a risky
income component, social approval). In general $u(x, y)$ mixes the two in complicated ways. With
no wealth effects there is a **cash-equivalent value** $v(y)$ such that

$$u(x, y) = x + v(y),$$

which M&R call the decision maker's **value index** (p. 36). Two checks against §1's conditions
(the logic of M&R's n. 7, p. 36):

- **Compensation for a switch.** From $y_1$ to $y_2$ at initial wealth $M$, the amount $\Delta x$
  solves $M + \Delta x + v(y_2) = M + v(y_1)$, so $\Delta x = v(y_1) - v(y_2)$. It exists
  (condition 1) and **does not depend on $M$** (condition 2).
- **Ability to pay.** Condition 3 holds when $M$ exceeds the largest difference
  $|v(y) - v(y')|$, so no required payment exceeds what the person has.

**A counterexample, worked.** Take $u(x, c) = \ln x + \theta c$, where $c \in \{0, 1\}$ marks
clean water and $\theta > 0$. Starting from wealth $M$:

| Question | Equation | Answer |
|---|---|---|
| Willingness to **pay** to get clean water ($c$: 0 → 1) | $\ln(M - p) + \theta = \ln M$ | $p = M(1 - e^{-\theta})$ |
| Willingness to **accept** to give it up ($c$: 1 → 0) | $\ln(M + a) = \ln M + \theta$ | $a = M(e^{\theta} - 1)$ |

Both amounts are **proportional to $M$** (condition 2 fails), and $a > p$ always, because
$e^\theta - 1 > 1 - e^{-\theta}$ for $\theta > 0$. With $M = 100$ and $\theta = \ln 2$:
$p = 50$, $a = 100$. With the quasi-linear $u = x + \theta c$ instead, $p = a = \theta$. The gap
between willingness to pay and willingness to accept is the signature of a wealth effect; §4.2
shows what it does to the Coase theorem.

M&R's footnote 6 (p. 35) is worth keeping in mind for the whole course: an assumption in a model
is "a working hypothesis used to abstract from the complexity of the real economic world", not a
claim that it is true.

---

## 3. The value maximization principle (pp. 36–38)

> **The Value Maximization Principle:** "An allocation among a group of people whose preferences
> display no wealth effects is efficient only if it maximizes the total value of the affected
> parties. Moreover, for any inefficient allocation, there exists another (total value
> maximizing) allocation that all of the parties strictly prefer." (p. 36)

Total value is "also sometimes called the total (consumer and/or producer) surplus" (p. 36, n. 8).

### 3.1 The logic (p. 37)

Two people, $U_i(x_i, y) = x_i + v_i(y)$, $i = 1, 2$. The decision $y$ generates cash income
$P(y)$, divided as $x_1 + x_2 = P(y)$. Here $v_i(y)$ can be read as the personal cost of the
inputs $i$ supplies, negative for positive $y$ (p. 37). The sum of utilities is

$$[x_1 + v_1(y)] + [x_2 + v_2(y)] = P(y) + v_1(y) + v_2(y) \equiv W(y).$$

**The shares $x$ have dropped out.** Varying $x_1$ moves value from one person to the other one
for one, leaving $W(y)$ fixed. In utility space each $y$ gives a straight line
$U_1 + U_2 = W(y)$ at $-45°$ (M&R Figure 2.1, p. 37).

- If $y$ does not maximize $W$, pick $y^*$ with $W(y^*) > W(y)$, and set the transfers so that
  each person gets his or her old utility plus half the gain $W(y^*) - W(y)$. Both are
  **strictly** better off: the allocation was not efficient.
- If $y^*$ maximizes $W$, no allocation can raise one utility without lowering the other,
  because every feasible pair lies on or below the line $U_1 + U_2 = W(y^*)$.

So $(x_1, x_2, y)$ is efficient **if and only if** $y$ maximizes $W$ (p. 37). The $N$-person proof
is M&R Mathematical Exercise 2.3 (p. 53).

**The converse that fails with wealth effects** (n. 10, p. 37): an allocation that maximizes the
sum of utilities is still efficient, but there may be efficient allocations that do not. With
wealth effects the utility possibility frontier is curved and different points on it use
different $y$s; no single "efficient decision" exists.

### 3.2 Worked example: a supplier and an assembler

A supplier (S) and an assembler (A) choose a joint quality level $y \ge 0$. Revenue
$P(y) = 6y$; personal costs $v_S(y) = -y^2$ and $v_A(y) = -\tfrac{1}{2} y^2$.

$$W(y) = 6y - \tfrac{3}{2}y^2, \qquad W'(y) = 6 - 3y = 0 \;\Rightarrow\; y^* = 2, \quad W(y^*) = 6.$$

- **Any** split of the 12 of revenue is efficient as long as $y = 2$: $(x_S, x_A) = (4, 8)$ gives
  utilities $(0, 6)$; $(10, 2)$ gives $(6, 0)$. Distribution is a separate question.
- Start instead at $y = 1$ with $(x_S, x_A) = (3, 3)$: utilities $(2, 2.5)$, total $4.5$. Move to
  $y = 2$ and hand each party half of the gain $6 - 4.5 = 1.5$: utilities $(2.75, 3.25)$, so
  $x_S = 2.75 + 4 = 6.75$ and $x_A = 3.25 + 2 = 5.25$ (they sum to 12). Both strictly prefer it.
- **Why transfers matter.** Suppose instead the revenue must be split in fixed shares $s$ and
  $1 - s$, with no side payments. S wants $\max_y\, 6sy - y^2$, i.e. $y = 3s$; A wants
  $\max_y\, 6(1-s)y - \tfrac12 y^2$, i.e. $y = 6(1 - s)$. At $s = \tfrac12$ they want 1.5 and 3.
  Only $s = \tfrac23$ (each party's revenue share equal to its share of the marginal cost) makes
  both want $y^* = 2$. The value maximization principle needs the money to move freely; take
  that away and how value is split starts to shape how much is created.

### 3.3 How general the principle is (p. 38)

The variable $y$ can be almost anything (p. 38): resources for a public good (parks,
libraries), **who** works overtime, **who** holds water rights, the **brand** of computer, the
**location** of a new office. In each case, with no wealth effects, efficiency picks $y$ by
total value, and the money settles the rest.

---

## 4. The Coase theorem (p. 38)

### 4.1 Statement

The division of value depends on "what assets each brings to the bargaining table, how patient
each party is, what outside opportunities are available, and so on" (p. 38). But if the parties
bargain **efficiently** (no further mutual gain is left) and the value maximization principle
applies, $y$ maximizes total value whatever cash changes hands (p. 38):

> **The Coase Theorem:** "If the parties bargain to an efficient agreement (for themselves) and if
> their preferences display no wealth effects, then the value-creating activities ($y$) that they
> will agree upon do not depend on the bargaining power of the parties or on what assets each
> owned when the bargaining began. Rather, efficiency alone determines the activity choice. The
> other factors can affect only decisions about how the costs and benefits are to be shared
> ($x$)." (p. 38)

Its two hypotheses, and the one M&R add in application (p. 39):

| Hypothesis | What breaks without it | Where the course deals with it |
|---|---|---|
| Efficient bargaining | haggling, delay, failed deals | Aula 3 (bargaining costs, M&R pp. 147–149) |
| No wealth effects | the efficient $y$ depends on who owns what (§4.2) | today |
| Unlimited transfers between the parties | the party who should pay cannot | today (p. 39) |
| *(implicit)* full information about values | efficient trade can fail | Aula 3 (M&R pp. 140–147) |

Cabral's version reads the same result through property rights: "if property rights are
properly assigned and negotiations are costless, then all externalities will be
'internalized'" (Cabral 2017, p. 97).

### 4.2 The river, with and without wealth effects

A factory upstream gains $G$ from dumping waste; the residents downstream value clean water.
Cabral's steel-plant example (pp. 97–98) runs on quasi-linear values. Run it both ways.

**No wealth effects** ($u_R = x + \theta c$). If residents hold the right, the factory buys it
iff $G > \theta$. If the factory holds it, residents buy it back iff $\theta > G$. Either way:
**dumping iff $G > \theta$**. Only the direction of the payment changes. This is Coase.

**With wealth effects** ($u_R = \ln x + \theta c$, §2). Now residents would pay at most
$p = M(1 - e^{-\theta})$ to stop dumping, but would accept no less than $a = M(e^\theta - 1)$ to
allow it. With $M = 100$, $\theta = \ln 2$, $G = 70$:

| Right held by | Who must pay | Maximum the payer will pay vs. minimum the other accepts | Outcome |
|---|---|---|---|
| Residents | factory pays $\ge a = 100$ | factory gains only 70 | **clean water** |
| Factory | residents pay $\le p = 50$ | factory needs 70 | **dumping** |

The allocation of the right now decides **what happens**, not only who pays. Both outcomes are
Pareto efficient (n. 10, p. 37): there is no single efficient $y$ to converge to. Whenever
$p < G < a$, the initial assignment is decisive.

### 4.3 What the theorem buys: the transaction-costs approach (pp. 38–39)

With no wealth effects, "all real activities are determined to maximize the total value of the
parties, taking into account the costs of organization (transaction costs) along with all other
kinds of costs" (p. 38). For a given production plan, **the efficient organization is the one
that minimizes transaction costs**: the costs of writing contracts, supervising workers,
enforcing contracts, resolving disputes (p. 38).

M&R set this against two rival views (p. 39):

- **Marxian:** organization reflects power and class interests. The transaction-costs view says
  the choice of organization ($y$) does not depend on the prior distribution of power. Evidence
  cited: worker-controlled Yugoslav firms hired managers who organized factories much like
  capitalist firms.
- **Harvard school of IO/antitrust:** business arrangements are attempts to manipulate prices.
  The transaction-costs reading of resale price maintenance: it stops discounters from
  free-riding on other dealers' service, which would push service below efficient levels.

M&R's own caution: decide between hypotheses "with detailed evidence" (p. 39).

### 4.4 Where not to apply it (p. 39)

The theorem "depend[s] on restrictive hypotheses regarding preferences and, perhaps more
importantly, on the ability to make unlimited transfer payments between the parties" (p. 39).
Reasonable for a contract between General Motors and Toyota; a mistake, applied uncritically, to
land tenure in a developing country or to slavery in the pre-Civil War South (p. 39). In both,
the side that would have to pay for an efficient change cannot.

---

## 5. Threat points and the division of the surplus

M&R say what determines the split (assets, patience, outside opportunities, p. 38) without
giving a formula. Two standard formulas, both consistent with §4.

### 5.1 The Nash bargaining solution under transferable utility

Let $d_i$ be party $i$'s **threat point** (disagreement payoff: what $i$ gets if no agreement is
reached, e.g. selling to another buyer). Agreement is worth having iff
$W(y^*) > d_1 + d_2$. The (symmetric) Nash solution maximizes the product of gains:

$$\max_{y,\, u_1,\, u_2}\; (u_1 - d_1)(u_2 - d_2) \quad \text{s.t.} \quad u_1 + u_2 = W(y).$$

For any $y$ the product is largest at equal gains, where it equals $\big((W(y) - d_1 - d_2)/2\big)^2$,
increasing in $W(y)$. Hence

$$y = y^*, \qquad u_i = d_i + \tfrac12\big[W(y^*) - d_1 - d_2\big].$$

With bargaining weights $\beta$ and $1 - \beta$ (maximize $(u_1 - d_1)^\beta (u_2 - d_2)^{1-\beta}$):
$u_1 = d_1 + \beta S$, with $S = W(y^*) - d_1 - d_2$ the **surplus**. Two points:

- The Nash solution **chooses $y^*$ by itself**: the Coase theorem holds inside it. Threat points
  and $\beta$ move only $u$, i.e. the transfers $x$.
- A better outside option raises a party's payoff, but by less than one for one, and the
  opponent's lowers it: $\partial u_1/\partial d_1 = 1 - \beta$, $\partial u_1/\partial d_2 = -\beta$.

Varian §30.7 (p. 581) notes the axiomatic Nash model and calls its full treatment beyond its
scope; the course uses only the formula above.

**Back to §3.2.** Suppose S could sell its capacity elsewhere for $d_S = 1$, and A could buy from
another supplier for $d_A = 2$. Surplus $S = 6 - 3 = 3$; symmetric split: $u_S = 2.5$,
$u_A = 3.5$. In money: $x_S = u_S + y^{*2} = 6.5$, $x_A = 12 - 6.5 = 5.5$, and
$u_A = 5.5 - 2 = 3.5$. Raise A's outside option to $d_A = 3$: $y^*$ is still 2, $u_A = 4$,
$u_S = 2$.

### 5.2 Where the weights come from: alternating offers (preview of Aula 3)

The non-cooperative route (MWG 9.AA, pp. 296–298; Varian §30.7, pp. 581–582): players
alternate offers over a surplus $v$, with discount factors $\delta_1, \delta_2 \in (0,1)$.

- **Ultimatum (one round).** The proposer keeps (almost) everything.
- **Finite horizon** (MWG Example 9.AA.1, equal $\delta$): solve by backward induction; the
  first proposer's share alternates around the limit and converges to it as $T \to \infty$.
- **Infinite horizon** (Rubinstein; MWG Example 9.AA.2): a unique subgame-perfect equilibrium,
  immediate agreement, first proposer's share
  $$\frac{1 - \delta_2}{1 - \delta_1 \delta_2} \quad \Big(= \frac{1}{1 + \delta} \text{ when } \delta_1 = \delta_2 = \delta\Big).$$
  Varian's three-day version gives the same backward-induction logic (p. 582).

Patience is bargaining power: a more patient opponent ($\delta_2$ up) lowers player 1's share.
With $\delta_i = e^{-r_i \Delta}$ and the time between offers $\Delta \to 0$, player 1's share
tends to $r_2/(r_1 + r_2)$: the Nash split with weight $\beta = r_2/(r_1 + r_2)$. Agreement is
immediate, so no value is lost: under full information the bargaining game itself delivers
M&R's "efficient bargaining". Aula 3 asks what happens when it does not.

---

## 6. Organizational objectives (p. 39)

Firms are usually said to maximize profit. M&R are more careful: they treat organizational
decisions "as the outcomes either of strategic interplay among self-interested people … or of
collective or managerial attempts to compromise the interests of the parties affected" (p. 39).
And: "Only when the value maximization principle applies is there an objective that we can
ascribe to the firm that is implied by considerations of efficiency alone" (p. 39). Owners who
are also customers or suppliers may not want profit maximized (p. 40; FFT 2.2, p. 52).

---

## 7. Back to Aula 1

- **Why Aula 1 could talk about "the" profit of a system.** The complementarity models
  maximized one function $\pi(x, y)$ over practices. That presumes the parties can agree on
  total value, i.e. the value maximization principle. When it holds, the choice of system is a
  pure efficiency question and the split is settled by transfers.
- **When the split leaks into the system.** §3.2's fixed-share case is the Salomon and HBC
  problem in miniature: when pay is a fixed share and cannot be renegotiated freely, each
  party's chosen action follows its own share, not the total. Incentives and the size of the pie
  stop being separable. Aulas 13–16 study that case properly (moral hazard).
- **Coherent systems need someone to choose among them.** Coase says efficient bargainers find
  the value-maximizing $y$. Aula 1's valley says local adjustment may not: with complementary
  practices, getting from one coherent system to another needs a coordinated jump that no
  single party's marginal move produces. Coase assumes the bargain reaches it; organization is
  how real firms try to.

---

## 8. Common mistakes

| Mistake | Correction |
|---|---|
| "Coase says property rights don't matter" | They do not matter **for $y$** under its hypotheses; they always matter for who pays (§4.1). |
| Applying Coase with wealth effects or limited cash | The efficient $y$ can then depend on the initial assignment ($p < G < a$, §4.2; p. 39). |
| "Efficient = fair" | Efficiency picks $y$; fairness is about $x$, which efficiency leaves open (Cabral p. 99). |
| "Maximizing the sum of utilities is necessary for efficiency" | Only with no wealth effects. In general it is sufficient, not necessary (n. 10, p. 37). |
| "No wealth effects means money doesn't matter" | It means the **compensation** for a switch does not depend on wealth; money enters one for one. |
| "A stronger bargainer gets a better project" | A stronger bargainer gets a **bigger share** of the same project (Nash, §5.1). |
| Reading WTP = WTA as a general fact | It holds only with quasi-linear utility; with wealth effects $a > p$ for a normal good. |

---

## 9. Exercises (number and page only)

| Exercise | Where | Practises |
|---|---|---|
| M&R Food for Thought 2.2 | p. 52 | objectives of firms owned by lenders, customers and suppliers (§6) |
| M&R Food for Thought 2.3 | p. 52 | when wealth constraints stop arrangements from maximizing total value (§4.4) |
| M&R Mathematical Exercise 2.1 | p. 53 | the efficient level of a shared improvement (§3) |
| M&R Mathematical Exercise 2.2 | p. 53 | equal cost sharing vs. efficiency; a unanimous improvement (§3.2) |
| M&R Mathematical Exercise 2.3 | p. 53 | proof of the value maximization principle, $N$ people (§3.1) |
| M&R Mathematical Exercise 2.4 | p. 53 | deriving $x + v(y)$ from the no-wealth-effects conditions (§2) |
| Varian Ch. 35 Review Questions 1–2 | p. 687 | property rights and the Coase theorem |
| Cabral 5.1 "Front yards" | p. 117 | an externality between neighbours: is the outcome inefficient? |

Exam-style practice for Aulas 1–2: `Listas/lista-aulas-01-02.tex` (graduate level).

---

## Sources

- Milgrom, P. & Roberts, J. (1992). *Economics, Organization, and Management*. Prentice-Hall.
  Ch. 2, pp. 35–40, 52–53. Read from `Livros/` on 2026-10-13.
- Varian, H. (2014). *Intermediate Microeconomics with Calculus*, 1st ed. Norton. §30.7,
  pp. 581–583; §35.2, p. 670.
- Cabral, L. (2017). *Introduction to Industrial Organization*, 2nd ed. MIT Press. §5.1,
  pp. 96–99.
- Mas-Colell, A., Whinston, M. & Green, J. (1995). *Microeconomic Theory*. OUP. Ch. 9,
  Appendix A, pp. 296–298.
