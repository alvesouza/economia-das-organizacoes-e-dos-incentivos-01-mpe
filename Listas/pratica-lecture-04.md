---
tags: [lista, pratica, lecture-04, topic/subgame-perfection, topic/credibility, topic/repeated-games]
date: 2026-11-12
status: aligned
---

# Practice plan — Lecture 4 (Credible threats and subgame perfection)

**Re-aligned on 2026-11-12** to the real slides `Aula/Lecture04.pdf` ("Lecture 4: Credible threats and
subgame perfection", 45 slides: Boris's Brexit dilemma, its extensive and strategic forms, "too many
Nash equilibria" and backward induction, slides 3–20; subgames and the subgame-perfect equilibrium,
21–38; finitely repeated games, definition, 39–44). The list replaces the estimated Lecture 4 list
(multistage games and bargaining) of 2026-10-25: the bargaining block moved to Lecture 6, the
multistage and repeated-game exercises to Lecture 5. It takes the credibility, commitment, Stackelberg
and time-inconsistency exercises of the old Lecture 3 list, the leader-and-two-followers problem
Gibbons 2.6 from the old Lecture 4 list, and Gibbons 2.12 (the definition of a strategy, a subgame and
an SPE in a repeated game) from the old Lecture 5 list. Every item keeps the verbatim statement block
verified on 2026-10-25, with a "Moved here from" line giving its old list and number.

12 existing book exercises in one sequence of rising complexity, each reproduced verbatim under its
tier table. Sources: Tadelis (2013), Ch. 8, the book the slides follow; Muñoz-Garcia & Toro-Gonzalez
(2019), Ch. 4, worked answers after every exercise; Gibbons (1992), Ch. 2. Lecture slides:
`Aula/Lecture04.pdf`. Class plan: [[Map/study-guide|study guide]]; book map:
[[Map/books-index|books-index]]; notes: [[Notas/L03/L03-00-map|Lecture 3 notes]] (credibility, Stackelberg
and time inconsistency are notes 06–08 there) and [[Notas/L04/L04-00-map|Lecture 4 notes]]. Worked
solutions: `Listas/pratica-lecture-04-solutions.pdf` (source `Listas/pratica-lecture-04-solutions/`),
every number asserted by `check_L04.py`.

**Answers in the books.** Muñoz-Garcia: a worked answer follows each exercise. Gibbons 2.6 and 2.12:
in an unofficial, unfinished manual (`D:/Livros/Mercado/Economia/`, not copied). Tadelis: none in the
book; the preface (p. xiii) says about half are solved on Princeton UP's website (not checked).

**Verification.** Statements were transcribed from the PDF text layers and checked against the
rendered page images on 2026-10-25 (the old lists), and are copied here unchanged. Pages: Tadelis
8.4 and 8.6 on pp. 170–171, 8.7 on p. 171, 8.8 on pp. 171–172, 8.12 on p. 173, 8.13 on pp. 173–174,
8.15–8.16 on p. 174 (PDF index = printed page + 18). Muñoz-Garcia Ch. 4 Ex. 11 on p. 180, Ex. 12 on
pp. 185–186 (offset 11). Gibbons Problem 2.6 on p. 133, 2.12 on p. 135 (offset 6).

**Not in this list on purpose.** The Brexit case itself (slides 3–20) and the slides' Examples 1–2
(counting subgames; the voluntary battle of the sexes) are in-class work; their closest book
exercises are Tadelis 8.1 (the voluntary Battle of the Sexes, which refers to Fig. 8.2, p. 154) and
8.5, 8.10 (already in Lecture 3's list). Repeated games beyond their definition are Lecture 5. No
optional new Tadelis Ch. 8 exercise was added: 8.9 (entry deterrence with a fixed cost, p. 172)
and 8.14 (p. 174) are listed under optional extras.

**Fit to the slides.** Items 3, 4, 6, 7, 8 are Stackelberg or Cournot games with an observed first
mover, which the slides introduce in Example 4 of Lecture 3 (slide 71) and use again for the sunk,
observable commitment of the Brexit case (slide 19); they are the continuous-action counterpart of
subgame perfection here. Items 9 and 12 (time inconsistency, Tadelis §8.3.4) are not in either lecture's
slides; they stay in this list as reading, as the plan assigns them.

## Weighting

| Block | Subtopic | Items | Weight | Why |
|---|---|---|---|---|
| B1 | Credibility and commitment: non-credible threats, entry deterrence, hold-up, sunk investment, a legal system | 4 | 33% | slides 3–20 and 22–23: the Brexit case, "too many Nash equilibria" and the lessons from the case |
| B2 | Subgames and SPE in multistage and Stackelberg games: proper subgames, SPE, Nash equilibria that are not SPE | 5 | 42% | slides 21–38; continuous-action leader-follower games are where subgames are infinite in number |
| B3 | The definition of a repeated game: strategy, subgame, SPE | 1 | 8% | slides 39–44 (6 of 43 content slides), definitions only |
| B4 | Time inconsistency and the value of commitment (reading) | 2 | 17% | Tadelis §8.3.4; not in the slides, kept as reading |

| Level | Items | Count |
|---|---|---|
| Foundations (entry deterrence with numbers, a first Stackelberg game, definitions) | 1–4 | 4 |
| Exam (hold-up and commitment, investment before Cournot, three firms, naive present bias) | 5–9 | 5 |
| Advanced (legal system and credibility of suing, agenda setting with a continuum of Nash equilibria, the value of commitment) | 10–12 | 3 |


---

## Tier 1 — Foundations

| # | Block | Source | Ch./Sec. | Exercise | Page | What it trains |
|---|---|---|---|---|---|---|
| 1 | B1 | Tadelis | Ch. 8, Exercises | 8.8 | 171–172 | The entry game with numbers: the price-war threat is not credible |
| 2 | B3 | Gibbons | §2.3, Problems | 2.12 | 135 | Defining strategy, subgame and SPE in a repeated game |
| 3 | B2 | Gibbons | §2.2, Problems | 2.6 | 133 | One leader and two simultaneous followers: solve stage 2 as a Nash equilibrium, then stage 1 |
| 4 | B2 | Muñoz-Garcia | Ch. 4 | Ex. 11 | 180 | Stackelberg with asymmetric costs; comparison with monopoly, Cournot and Bertrand |

### Statements

#### 1. Tadelis 8.8


<!-- id: Tadelis 8.8 -->
**Source.** Tadelis (2013), *Game Theory: An Introduction*, Exercise 8.8 "Entry Deterrence 1", pp. 171–172 [PDF 190–191]. Reproduced verbatim. Answer in the source: none in the book (the preface, p. xiii, says about half are solved on Princeton UP's website; not checked).

**Moved here from:** old Lecture 3 list, item 6.

> **Entry Deterrence 1:** NSG Corporation is considering entry into the local phone market in the San Francisco Bay Area. The incumbent, S&P Corporation, predicts that a price war will result if NSG enters. If NSG stays out, S&P earns monopoly profits valued at \$10 million (net present value of profits) while NSG earns zero. If NSG enters, it must incur irreversible entry costs of \$2 million. If there is a price war, each firm earns \$1 million. S&P always has the option of accommodating entry (i.e., not starting a price war). In such a case both firms earn \$4 million (net present value). Suppose that the timing is such that NSG first has to choose whether or not to enter the market. Then S&P decides whether to "accommodate entry" or "engage in a price war." What is the subgame-perfect equilibrium outcome to this sequential game? Set up a game tree.

#### 2. Gibbons 2.12


<!-- id: Gibbons 2.12 -->
**Source.** Gibbons (1992), *Game Theory for Applied Economists*, §2.3 Problems, Problem 2.12, p. 135 [PDF 142]. Reproduced verbatim. Answer in the source: none (Gibbons prints no answers).

**Moved here from:** old Lecture 5 list, item 1.

> 2.12. What is a strategy in a repeated game? What is a subgame in a repeated game? What is a subgame-perfect Nash equilibrium?

#### 3. Gibbons 2.6


<!-- id: Gibbons 2.6 -->
**Source.** Gibbons (1992), *Game Theory for Applied Economists*, Ch. 2 Problems (Section 2.2), Problem 2.6, p. 133 [PDF 140]. Reproduced verbatim. Answer in the source: none (Gibbons prints no answers).

**Moved here from:** old Lecture 4 list, item 4.

> 2.6. Three oligopolists operate in a market with inverse demand given by $P(Q) = a - Q$, where $Q = q_1 + q_2 + q_3$ and $q_i$ is the quantity produced by firm $i$. Each firm has a constant marginal cost of production, $c$, and no fixed cost. The firms choose their quantities as follows: (1) firm 1 chooses $q_1 \ge 0$; (2) firms 2 and 3 observe $q_1$ and then simultaneously choose $q_2$ and $q_3$, respectively. What is the subgame-perfect outcome?

#### 4. Muñoz-Garcia Ex. 11


<!-- id: Muñoz-Garcia Ch. 4 Ex. 11 -->
**Source.** Muñoz-Garcia & Toro-Gonzalez (2019), *Strategy and Game Theory: Practice Exercises with Answers*, Ch. 4, Exercise 11 "Stackelberg with Two Firms", p. 180 [PDF 192]. Reproduced verbatim (statement only; the book's worked answer follows it).

**Moved here from:** old Lecture 3 list, item 8.

> Consider a leader and a follower in a Stackelberg game of quantity competition. Firms face an inverse demand curve $p(Q) = 1 - Q$, where $Q = q_L + q_F$ denotes aggregate output. The leader faces a constant marginal cost $c_L > 0$ while the follower's constant marginal cost is $c_F > 0$, where $1 > c_F \geq c_L$, indicating that the leader has access to a more efficient technology than the follower.
>
> **Part (a)** Find the follower's best response function, $BRF_F$, i.e., $q_F(q_L)$.
>
> **Part (b)** Determine each firm's output strategy in the subgame perfect equilibrium (SPNE) of this sequential-move game.
>
> **Part (c)** Under which conditions on $c_L$ can you guarantee that both firms produce strictly positive output levels?
>
> **Part (d)** Assuming cost symmetry, i.e., $c_L = c_F = c$, determine the aggregate equilibrium output level in the Stackelberg game, and its associated equilibrium price. Then compare them with those arising in (1) a monopoly; in (2) the Cournot game of quantity competition; and (3) in the Bertrand game of price competition (which, under cost symmetry, is analogous to a perfectly competitive industry) [*Hint*: For a more direct and visual comparison, depict the inverse demand curve $p(Q) = 1 - Q$, and locate each of these four aggregate output levels in the horizontal axis (with its associated prices in the vertical axis).].


---

## Tier 2 — Exam level

| # | Block | Source | Ch./Sec. | Exercise | Page | What it trains |
|---|---|---|---|---|---|---|
| 5 | B1 | Tadelis | Ch. 8, Exercises | 8.13 | 173–174 | Hold-up after a sunk trip, and a posted price as a commitment |
| 6 | B1 | Tadelis | Ch. 8, Exercises | 8.6 | 170–171 | Investment before Cournot: the threshold cost $F^*$ and a Nash equilibrium that is not SPE |
| 7 | B2 | Tadelis | Ch. 8, Exercises | 8.4 | 170 | A leader and two simultaneous followers: subgames, the unique SPE, a Nash equilibrium that is not SPE (also Gibbons 2.6, p. 133) |
| 8 | B2 | Muñoz-Garcia | Ch. 4 | Ex. 12 | 185–186 | Stackelberg with two and with three sequential firms |
| 9 | B4 | Tadelis | Ch. 8, Exercises | 8.15 | 174 | A naive present-biased planner, and how the period-2 self revises the plan |

### Statements

#### 5. Tadelis 8.13


<!-- id: Tadelis 8.13 -->
**Source.** Tadelis (2013), *Game Theory: An Introduction*, Exercise 8.13 "Junk Mail Advertising", pp. 173–174 [PDF 192–193]. Reproduced verbatim. Answer in the source: none in the book (the preface, p. xiii, says about half are solved on Princeton UP's website; not checked).

**Moved here from:** old Lecture 3 list, item 15.

> **Junk Mail Advertising:** Suppose a single good is owned by a single seller who values it at $c > 0$ (he can consume the good and get a payoff of $c$). There is a single buyer who has a small transportation cost $k > 0$ to get to and back from the seller's store, and he values the good at $v > c + k$. The buyer first decides whether to make the commute or stay at home, not buy the good, and receive a payoff of 0. If the buyer commutes to the store, the seller can then make the buyer a take-it-or-leave-it price offer $p \geq 0$. The buyer can then accept the offer, pay $p$, and get the good, or he can walk out and not buy the good. Assume that $c$, $v$, and $k$ are common knowledge.
>
> a. As best you can, draw the extensive form of this game. What is the best response of the buyer at the node at which he decides whether to accept or reject the seller's offer?
>
> b. Find the subgame-perfect equilibrium of the game and show that it is unique. Is it Pareto optimal?
>
> c. Are there Nash equilibria that yield a higher payoff to both players as compared to the subgame-perfect equilibrium you found in (b)?
>
> d. Now assume that before the game is played the seller can, at a small cost $\varepsilon < (v - c - k)$, send the buyer a postcard that commits the seller to a certain price at which the buyer can buy the good (e.g., "bring this coupon and get the good at a price $p$"). Would the seller choose to do so? Justify your answer with an equilibrium analysis.

#### 6. Tadelis 8.6


<!-- id: Tadelis 8.6 -->
**Source.** Tadelis (2013), *Game Theory: An Introduction*, Exercise 8.6 "Investment in the Future", pp. 170–171 [PDF 189–190]. Reproduced verbatim. Answer in the source: none in the book (the preface, p. xiii, says about half are solved on Princeton UP's website; not checked).

**Moved here from:** old Lecture 3 list, item 16.

> **Investment in the Future:** Consider two firms that play a Cournot competition game with demand $p = 100 - q$ and costs for each firm given by $c_i(q_i) = 10q_i$. Imagine that before the two firms play the Cournot game firm 1 can invest in cost reduction. If it invests the costs of firm 1 will drop to $c_1(q_1) = 5q_1$. The cost of investment is $F > 0$. Firm 2 does not have this investment opportunity.
>
> a. Find the value $F^*$ for which the unique subgame-perfect equilibrium involves firm 1 investing.
>
> b. Assume that $F > F^*$. Find a Nash equilibrium of the game that is not subgame perfect.

#### 7. Tadelis 8.4


<!-- id: Tadelis 8.4 -->
**Source.** Tadelis (2013), *Game Theory: An Introduction*, Exercise 8.4 "Industry Leader", p. 170 [PDF 189]. Reproduced verbatim. (Gibbons Problem 2.6, p. 133, poses the same game and asks only for the subgame-perfect outcome.) Answer in the source: none in the book (the preface, p. xiii, says about half are solved on Princeton UP's website; not checked).

**Moved here from:** old Lecture 3 list, item 23.

> **Industry Leader:** Three oligopolists operate in a market with inverse demand given by $P(Q) = a - Q$, where $Q = q_1 + q_2 + q_3$, and $q_i$ is the quantity produced by firm $i$. Each firm has a constant marginal cost of production, $c$, and no fixed cost. The firms choose their quantities dynamically as follows: Firm 1, which is the industry leader, chooses $q_1 \geq 0$. Firms 2 and 3 observe $q_1$ and then simultaneously choose $q_2$ and $q_3$, respectively.
>
> a. How many proper subgames does this dynamic game have? Explain briefly.
>
> b. Is it a game of perfect or imperfect information? Explain briefly.
>
> c. What is the subgame-perfect equilibrium of this game? Show that it is unique.
>
> d. Find a Nash equilibrium that is not a subgame-perfect equilibrium.

#### 8. Muñoz-Garcia Ex. 12


<!-- id: Muñoz-Garcia Ch. 4 Ex. 12 -->
**Source.** Muñoz-Garcia & Toro-Gonzalez (2019), *Strategy and Game Theory: Practice Exercises with Answers*, Ch. 4, Exercise 12 "Stackelberg Competition with 2, or 3 Firms", pp. 185–186 [PDF 197–198]. Reproduced verbatim (statement only; the book's worked answer follows it).

**Moved here from:** old Lecture 3 list, item 17.

> Consider a Stackelberg model of output competition where firm 1 is the industry leader and firm 2 is the follower. Firms face a linear inverse demand curve $p(Q) = 10 - Q$, where $Q = q_1 + q_2$ denotes the aggregate output sold by both firms. In addition, consider that firms are cost symmetric, facing a common marginal cost of $MC_i = 2$ for every firm $i = \{1, 2\}$ and no fixed costs.
>
> (a) Find the equilibrium in this Stackelberg game.
>
> (b) Assume now that a new firm (firm 3) joins the industry, acting last (after firm 2 chooses its output). Find the equilibrium in this Stackelberg game. Compare your results with those in part (a). How is the output of firm 1 and 2 affected by firm 3's entry?

#### 9. Tadelis 8.15


<!-- id: Tadelis 8.15 -->
**Source.** Tadelis (2013), *Game Theory: An Introduction*, Exercise 8.15 "Time Inconsistency", p. 174 [PDF 193]. Reproduced verbatim. *Note (not in the book):* the example of Section 8.3.4 is on pp. 166–169; its printed first-period choice $x_1 = \frac{2}{3}K$ (p. 169) does not follow from the objective printed there (the maximum is at $\frac{K}{2}$); see `Notas/L03/L03-08-time-inconsistency.md` §2.2. Answer in the source: none in the book (the preface, p. xiii, says about half are solved on Princeton UP's website; not checked).

**Moved here from:** old Lecture 3 list, item 18.

> **Time Inconsistency:** Consider the three-period example of a player with hyperbolic discounting described in Section 8.3.4 with utility $\ln(x)$ in each of the three periods, with initial budget $K$ and with discount factors $\delta = 1$ and $\beta = \frac{1}{2}$.
>
> a. Solve the optimal plan of action of a naive player 1 who does not take into account how his future self, player 2, will alter the plan. What is player 1's optimal plan $x_1^*$, $x_2^*$, and $x_3^*$ as a function of $K$?
>
> b. Let $K_2$ be the amount left from the solution to (a) after player 1 consumes his planned choice of $x_1^*$. Given $K_2$, what is the optimal plan of player 2? In what way does it differ from the optimal plan set out by player 1?


---

## Tier 3 — Advanced

| # | Block | Source | Ch./Sec. | Exercise | Page | What it trains |
|---|---|---|---|---|---|---|
| 10 | B1 | Tadelis | Ch. 8, Exercises | 8.7 | 171 | Credibility of suing: how the cost and design of a legal system change the SPE of a lending game |
| 11 | B2 | Tadelis | Ch. 8, Exercises | 8.12 | 173 | Agenda setting with a continuum of proposals: SPE vs a continuum of Nash equilibria |
| 12 | B4 | Tadelis | Ch. 8, Exercises | 8.16 | 174 | The value of commitment for a sophisticated present-biased planner |

### Statements

#### 10. Tadelis 8.7


<!-- id: Tadelis 8.7 -->
**Source.** Tadelis (2013), *Game Theory: An Introduction*, Exercise 8.7 "Debt and Repayment", p. 171 [PDF 190]. Reproduced verbatim. Answer in the source: none in the book (the preface, p. xiii, says about half are solved on Princeton UP's website; not checked).

**Moved here from:** old Lecture 3 list, item 21.

> **Debt and Repayment:** A project costing \$100 yields a gross return of \$110. A lender (player 1) is approached by a debtor (player 2) requesting a standard loan contract to complete the project. If the lender chooses *not to offer* a loan, then both parties earn nothing. If the lender chooses to *offer* a loan of \$100, the debtor can realize the project's gains and is obliged by contract to repay \$105. For simplicity assume that money is continuous and that the debtor can choose to return any amount of money $x \leq 110$. Ignore the time value of money. Assume first that no legal system is in place that can compel the debtor to repay, so that default on the loan (less than full repayment) carries no repercussions for the debtor.
>
> a. Model this as an extensive-form game tree as best you can and find a subgame-perfect equilibrium of this game. Is it unique?
>
> b. Now assume that there is a legal system in place that allows the lender to *voluntarily* choose whether or not to sue when the debtor defaults and repays an amount $x < 105$. Furthermore assume that it is *costless* to use the legal system (it is supplied by the state), and if the lender sues a debtor that defaulted, the lender will get the \$105 repaid in full. After paying the lender, the borrower will pay a fine of \$5 to the court, above and beyond the repayment. Model this as an extensive-form game tree as best you can and find a subgame-perfect equilibrium of this game. Is it unique?
>
> c. Are there Nash equilibria in the game described in (b) that are not subgame-perfect equilibria?
>
> d. Now assume that using the legal system is *costly:* if the lender sues, he pays lawyers a *legal fee* of \$105 (this is the lawyers' price; it is unrelated to the contract). The rest of the game proceeds as before. (If the lender sues a debtor that defaulted, the lender will get repaid in full; after paying the lender, the borrower will pay a fine of \$5 above and beyond the repayment.) Model this as an extensive-form game tree as best you can and find a subgame-perfect equilibrium of this game. Is it unique?
>
> e. Are there Nash equilibria in the game described in (d) that are not subgame-perfect equilibria?
>
> f. Now assume that a change in the law is proposed: upon default, if a debtor is sued he has to first repay the lender \$105 and then pay the legal fees of \$105 above and beyond repayment of the loan, and no extra fine is imposed. Should the lender be willing to pay to have this change in the law enacted? If so, how much?
>
> g. If you were a social planner, would you implement the suggested law?

#### 11. Tadelis 8.12


<!-- id: Tadelis 8.12 -->
**Source.** Tadelis (2013), *Game Theory: An Introduction*, Exercise 8.12 "Agenda Setting", p. 173 [PDF 192]. Reproduced verbatim. Answer in the source: none in the book (the preface, p. xiii, says about half are solved on Princeton UP's website; not checked).

**Moved here from:** old Lecture 3 list, item 22.

> **Agenda Setting:** An agenda-setting game is described as follows. The "issue space" (set of possible policies) is an interval $X = [0, 5]$. An agenda setter (player 1) proposes an alternative $x \in X$ against the status quo $q = 4$. After player 1 proposes $x$, the legislator (player 2) observes the proposal and selects between the proposal $x$ and the status quo $q$. Player 1's most-preferred policy is 1, and for any final policy $y \in X$ his payoff is given by
>
> $$v_1(y) = 10 - |y - 1|,$$
>
> where $|y - 1|$ denotes the absolute value of $(y - 1)$. Player 2's most preferred policy is 3, and for any final policy $y \in X$ his payoff is given by
>
> $$v_2(y) = 10 - |y - 3|.$$
>
> That is, each player prefers policies that are closer to his most-preferred policy.
>
> a. Write the game down as a normal-form game. Is this a game of perfect or imperfect information?
>
> b. Find a subgame-perfect equilibrium for this game. Is it unique?
>
> c. Find a Nash equilibrium that is not subgame perfect. Is it unique? If yes, explain. If not, show all the Nash equilibria for this game.

#### 12. Tadelis 8.16


<!-- id: Tadelis 8.16 -->
**Source.** Tadelis (2013), *Game Theory: An Introduction*, Exercise 8.16 "The Value of Commitment", p. 174 [PDF 193]. Reproduced verbatim. *Note (not in the book):* "We solved the optimal consumption plan" refers to pp. 168–169, whose printed $x_1 = \frac{2}{3}K$ is a slip; with the objective as printed the sophisticated plan is $(\frac{1}{2}, \frac{1}{3}, \frac{1}{6})K$ (`Notas/L03/L03-08-time-inconsistency.md` §2.2). Use the corrected plan as the no-commitment benchmark in (b). Answer in the source: none in the book (the preface, p. xiii, says about half are solved on Princeton UP's website; not checked).

**Moved here from:** old Lecture 3 list, item 25.

> **The Value of Commitment:** Consider the three-period example of a player with hyperbolic discounting described in Section 8.3.4 with utility $\ln(x)$ in each of the three periods and with discount factors $\delta = 1$ and $\beta = \frac{1}{2}$. We solved the optimal consumption plan of a sophisticated player 1.
>
> a. Imagine that an external entity can enforce any plan of action that player 1 chooses in $t = 1$ and will prevent player 2 from modifying it. What is the plan that player 1 would choose to enforce?
>
> b. Assume that $K = 90$. Up to how much of his initial budget $K$ will player 1 be willing to pay the external entity in order to enforce the plan you found in (a)?

**Optional extras.**
- Tadelis 8.1 and 8.2 (p. 170): mixed-strategy SPE of the voluntary Battle of the Sexes (read Fig. 8.2, p. 154; the slides' Example 2) and of mutually assured destruction (read §8.3.3, pp. 163–166, Fig. 8.11).
- Tadelis 8.9 (entry deterrence with a fixed cost, p. 172) and 8.14 (hyperbolic discounting with general $\delta$, $\beta$, p. 174): harder versions of items 1 and 9.
- Muñoz-Garcia Ch. 4 Ex. 2 (entry-predation, p. 156), Ex. 5–6 (sequential Pareto coordination and chicken, pp. 166, 169), Ex. 13–15 (Stackelberg variants, pp. 189, 192, 195): all with worked answers.

---

## Suggested study order

1. **Credible threats.** Read Tadelis §8.1 (pp. 151–153) and Cabral §7.2 (pp. 167–171) with slides 3–20, then do items **1**, then **5, 6**.
2. **Subgames and subgame perfection.** Read Tadelis §8.2 (pp. 153–159) and Gibbons §2.4.B (pp. 122–129) with slides 21–38, then do **3, 4**, then **7, 8**, then **11**.
3. **Credibility and the law.** Do **10** after item 5: the same logic, with a legal system.
4. **Repeated games, definition.** Read Gibbons §2.3.A (pp. 82–88) with slides 39–44, then do **2**.
5. **Time inconsistency (reading).** Read Tadelis §8.3.4 (pp. 166–169) with the correction in `Notas/L03/L03-08-time-inconsistency.md`, then do **9, 12**.

---

## Consolidated Reading by Book

### Tadelis — Tadelis (2013)
| Topic | Chapter / Section | Pages | Priority |
|---|---|---|---|
| Sequential rationality and backward induction; Zermelo | Ch. 8, §8.1 | p. 151–153 | Foundations |
| Subgame-perfect equilibrium | Ch. 8, §8.2 | p. 153–159 | Foundations |
| Centipede, Stackelberg, mutually assured destruction, time inconsistency | Ch. 8, §8.3 | p. 159–169 | Exam |
| Exercises 8.4, 8.6, 8.7, 8.8, 8.12, 8.13, 8.15, 8.16 | Ch. 8, Exercises | p. 170–174 | Exam |

### Gibbons — Gibbons (1992)
| Topic | Chapter / Section | Pages | Priority |
|---|---|---|---|
| Repeated games: definitions | §2.3.A | p. 82–88 | Foundations |
| Extensive form; subgame-perfect Nash equilibrium | §2.4 | p. 115–129 | Exam |
| Problems 2.6, 2.12 | §2.6, Problems | p. 133, 135 | Foundations |

### Cabral — Cabral (2017)
| Topic | Chapter / Section | Pages | Priority |
|---|---|---|---|
| Entry deterrence, commitment and credibility | §7.2 | p. 167–171 | Exam |

### Muñoz-Garcia — Muñoz-Garcia & Toro-Gonzalez (2019)
| Topic | Chapter / Section | Pages | Priority |
|---|---|---|---|
| Sequential-move games with complete information: Stackelberg exercises with worked answers | Ch. 4 | p. 153–214 | Exam |

## Consolidated Exercises

| # | Exercise | Book | Page | Topic | Level |
|---|---|---|---|---|---|
| 1 | 8.8 | Tadelis | p. 171–172 | Entry deterrence with numbers | Foundations |
| 2 | 2.12 | Gibbons | p. 135 | Strategy, subgame and SPE in a repeated game | Foundations |
| 3 | 2.6 | Gibbons | p. 133 | Leader and two followers, SPE outcome | Foundations |
| 4 | Ex. 11 | Muñoz-Garcia | p. 180 | Stackelberg, asymmetric costs | Foundations |
| 5 | 8.13 | Tadelis | p. 173–174 | Hold-up and a posted price | Exam |
| 6 | 8.6 | Tadelis | p. 170–171 | Investment before Cournot | Exam |
| 7 | 8.4 | Tadelis | p. 170 | Leader and two followers | Exam |
| 8 | Ex. 12 | Muñoz-Garcia | p. 185–186 | Stackelberg with two and three firms | Exam |
| 9 | 8.15 | Tadelis | p. 174 | Naive present bias (reading) | Exam |
| 10 | 8.7 | Tadelis | p. 171 | Debt, repayment and the legal system | Advanced |
| 11 | 8.12 | Tadelis | p. 173 | Agenda setting | Advanced |
| 12 | 8.16 | Tadelis | p. 174 | Value of commitment (reading) | Advanced |

## Study roadmap

| Priority | Topic | Reading | Exercises | Suggested time |
|:---:|---|---|---|:---:|
| 1 | Credible threats | Tadelis §8.1 p. 151–153; Cabral §7.2 p. 167–171; slides 3–20 | Tadelis 8.8, 8.13, 8.6 | 2 h |
| 2 | Subgames and SPE | Tadelis §8.2 p. 153–159; Gibbons §2.4 p. 115–129; slides 21–38 | Gibbons 2.6; Muñoz-Garcia Ex. 11, 12; Tadelis 8.4, 8.12 | 2.5–3 h |
| 3 | Credibility and the law | Tadelis §8.2 | Tadelis 8.7 | 1 h |
| 4 | Repeated games, definition | Gibbons §2.3.A p. 82–88; slides 39–44 | Gibbons 2.12 | 0.5 h |
| 5 | Time inconsistency (reading) | Tadelis §8.3.4 p. 166–169 | Tadelis 8.15, 8.16 | 1 h |
