---
quiz: "Topic T19 · Signaling and refinements — hard conceptual quiz (10 questions; estimated unit, no slides: Tadelis Ch. 16, Gibbons §4.2 and §4.4, MWG §13.C–13.D and App. 13.AA, M&R Ch. 5)"
tags:
  sig: "Separating, pooling and the cost of signals"
  scr: "Screening versus signaling"
  lp: "Limit pricing as a signal"
  ic: "The intuitive criterion"
---

## sig

Q: In the two-type Spence model with unproductive education, productivities $\theta_H > \theta_L$ and unit costs $c_H < c_L$, the separating education levels form the interval from $(\theta_H - \theta_L)/c_L$ to $(\theta_H - \theta_L)/c_H$. What happens as the low type's unit cost $c_L$ falls toward $c_H$?
- The least-cost level $(\theta_H - \theta_L)/c_L$ falls, since a cheaper signal for the low type means less education is needed before mimicking stops paying
- The least-cost level $(\theta_H - \theta_L)/c_L$ rises toward the upper bound, so separation gets costlier and the interval shrinks to a point as the costs meet
- The interval widens, since a lower $c_L$ reduces the low type's loss from education and so leaves more levels at which both types are content to separate
- Nothing changes, since only the high type buys education and the two bounds $(\theta_H - \theta_L)/c_L$ and $(\theta_H - \theta_L)/c_H$ move together
<!-- YW5zOjE= -->
> The lower bound is the education that makes the low type indifferent to mimicking, $\theta_H - c_L e = \theta_L$; the cheaper education is for him, the more of it the high type must buy to deter him. With M&R's numbers ($\theta_H - \theta_L = 30$, $c_H = 10$): at $c_L = 20$ the interval is $[1.5, 3]$, at $c_L = 15$ it is $[2, 3]$, at $c_L = 12$ it is $[2.5, 3]$, and at $c_L = c_H$ it is the single point 3, with the high type indifferent to signaling; for $c_L < c_H$ it is empty. The first option reverses the logic; the third confuses the low type's cost with his willingness to mimic; the upper bound $(\theta_H-\theta_L)/c_H$ does not move with $c_L$.
> Ref: Milgrom & Roberts (1992), Ch. 5, pp. 155–156 (the two self-selection constraints, and why they cannot both hold unless the low type's cost is higher); Gibbons (1992), §4.2.B (pp. 199–202)
> Similar: Gibbons (1992), Problem 4.7, p. 249; Milgrom & Roberts (1992), Ch. 5, Question 5.2, p. 164

Q: Both Tadelis's MBA game and Spence's job-market model use education that adds nothing to productivity. Which statement about the social value of separation is correct?
- Separation is pure waste in both, because whatever education the high type buys is a cost that changes nobody's output and only reshuffles the wage bill
- Separation has social value in both, because firms learn each worker's type, and better information always raises total surplus net of signaling costs
- Separation has social value in Spence's model only, because competitive firms pay each type its productivity there, while the MBA employer keeps the surplus
- Separation can have social value in the MBA game only, since it puts the high type in the job where it is more productive; in Spence wages are mere transfers
<!-- YW5zOjM= -->
> In Spence's model output is $\theta$ whatever the education and whoever is believed what; wages only split a fixed output, so the education is, in M&R's words, "a pure social waste". In the MBA game the employer's information changes the job assignment: a high type is worth 10 as a manager and 5 in blue-collar work, so revealing him moves him to where he produces more. At Tadelis's numbers (prior 1/4) total surplus per worker is 11.25 with separation, net of the MBA cost of 2, against 9.5 when everyone is pooled in blue-collar jobs. Information is not always worth its cost, so the second option overreaches; and who keeps the surplus does not decide whether it is created.
> Ref: Tadelis (2013), §16.1, Fig. 16.1 and the employer's payoffs (pp. 319–323); Milgrom & Roberts (1992), Ch. 5, p. 156; Gibbons (1992), §4.2.B (pp. 190–194)
> Similar: Tadelis (2013), Exercise 16.4 "School Choice", pp. 336–337

Q: In Spence's model, suppose a single employer hires all workers and pays each the lowest wage he accepts, which is zero for both types, whatever it believes about ability. What happens to education signaling?
- It becomes stronger, because the single employer can commit to a wage schedule rising with education, which makes the high type's investment more profitable
- It is unchanged, because the employer still learns ability from education, and the separating levels depend only on productivities and the costs of education
- It disappears, because no wage rises with the employer's belief, so no type gains from being believed able and no type will pay to change that belief
- It survives only as pooling, because both types still want the job, so they pick a common education level that the employer reads as the population average
<!-- YW5zOjI= -->
> A signal pays only if the receiver's belief moves the sender's payoff. In Spence the link is competition: firms bid wages up to expected productivity given the belief, eq. 4.2.1, so being believed able is worth $\theta_H - \theta_L$. A monopsonist who pays the reservation wage whatever it believes cuts that link, so every type chooses zero education. A wage schedule chosen by the uninformed side to sort workers would be screening, a different game, and is excluded by the stem. Pooling at positive education is pointless when nothing depends on beliefs; the separating bounds are derived from a wage premium that no longer exists.
> Ref: Gibbons (1992), §4.2.B, eq. 4.2.1 (p. 193); MWG (1995), §13.C (pp. 450–452)
> Similar: Gibbons (1992), Problem 4.16, p. 253

Q: With a continuum of types $\theta \in [\underline\theta, \bar\theta]$, $\underline\theta > 0$, and education cost $e^2/\theta$, the separating wage schedule solves $w(e)\,w'(e) = 2e$, so $w(e)^2 = 2e^2 + k$. A solutions manual reports $w(e) = \sqrt{2}\,e$. What is wrong with it?
- It sets $k = 0$, that is $w(0) = 0$, but the lowest type is paid $\underline\theta$ whatever the beliefs and chooses $e = 0$, so $k = \underline\theta^2$
- It solves the wrong equation: the first-order condition gives $w'(e) = 2e/\underline\theta$ for every type, as only the lowest cost matters at the margin
- Nothing: $k$ only shifts every wage by the same constant, so incentives are unchanged and $w(e) = \sqrt{2}\,e$ supports the same education choices
- It forgets that the lowest type must buy some education to separate from types below it, which pins $k$ through $w'(0) = 1$ rather than $w(0)$
<!-- YW5zOjA= -->
> Type $\theta$ maximizes $w(e) - e^2/\theta$, so $w'(e(\theta)) = 2e(\theta)/\theta$, and separation with zero profit means $w(e(\theta)) = \theta$; substituting gives $w w' = 2e$, hence $w^2 = 2e^2 + k$. The lowest type is paid at least $\underline\theta$ under any belief, so it buys no education: $w(0) = \underline\theta$ and $w(e) = \sqrt{2e^2 + \underline\theta^2}$, $e(\theta) = \sqrt{(\theta^2 - \underline\theta^2)/2}$. The manual's formula is the case $\underline\theta = 0$. The first-order condition involves each type's own $\theta$, not $\underline\theta$; $k$ sits under the square root, so it is not a constant shift and changes every $e(\theta)$; and there are no types below $\underline\theta$.
> Ref: MWG (1995), §13.C (pp. 450–459), Exercise 13.C.4 (p. 475); project errata note `.agent/notes/errata-game-theory-books.md`; worked solution in `Listas/pratica-lecture-08-solutions.pdf` (MWG 13.C.4)
> Similar: MWG (1995), Exercise 13.C.4, p. 475

## scr

Q: In MWG's competitive screening model, firms first offer wage–task contracts, where tasks are unproductive and costlier at the margin for the low type, and workers of two types then choose among them. How does its outcome compare with Spence's signaling game?
- Pooling and separating contracts can both be equilibria, as in Spence, since firms can sustain any break-even contract by holding pessimistic beliefs off the path
- The outcome is first best: since the uninformed firms move first, they can design the menu so that each type is identified at zero task and paid its productivity
- Only pooling contracts survive, because any separating menu invites a rival firm to offer a single contract that attracts both types and breaks even on average
- No pooling contract survives, and when an equilibrium exists it is the least-cost separating outcome, though for some priors no equilibrium exists at all
<!-- YW5zOjM= -->
> With firms moving first there are no off-path beliefs to exploit: the solution concept is subgame perfection. A pooling contract is always broken by a rival offering a contract with a slightly higher task and wage that only high types accept (Lemma 13.D.2). In a separating equilibrium each contract breaks even and the high type's task just deters the low type, the same outcome as Spence's least-cost separating equilibrium. But if high types are numerous, a pooling contract can attract both types profitably and break that menu, so no equilibrium exists (Fig. 13.D.7). Paying each type its productivity at zero task is not self-selecting: the low type would take the high type's contract. The third option has the logic of Fig. 13.D.7 but draws the wrong conclusion from it.
> Ref: MWG (1995), §13.D, Lemmas 13.D.1–13.D.3 (pp. 461–464) and Fig. 13.D.7 (p. 465); Milgrom & Roberts (1992), Ch. 5, screening (pp. 156–159)
> Similar: MWG (1995), Exercise 13.D.1, p. 476

## lp

Q: Compare the separating PBE of Tadelis's two-period limit-pricing game with the complete-information benchmark, in which the entrant sees the incumbent's cost. Which statement is correct?
- Entry is deterred more often than under complete information, because the high-cost incumbent's low first-period price persuades the entrant to stay out
- Entry is the same as under complete information, because the entrant enters only against the high-cost type; the cost is the low type's extra first-period output
- Entry is the same as under complete information, because both types produce their monopoly outputs in period one and the entrant reads costs from the prices
- Entry is deterred less often than under complete information, because the low-cost incumbent's output above monopoly reveals its cost too late to stop entry
<!-- YW5zOjE= -->
> In any separating PBE the entrant learns the cost, enters after the high type's output and stays out after the low type's (Claim 16.1): exactly the complete-information entry pattern, since entry pays only against a high-cost incumbent. What changes is period 1: the low type must produce at least 2.62, above its monopoly output 2, so that the high type would not mimic; the high type produces its monopoly output 1.5 (Claim 16.2). Limit pricing here deters no extra entry and lowers the first-period price, which benefits buyers. The third option is the one output level the low type cannot use: at 2 the high type mimics ($4.25 > 3.25$).
> Ref: Tadelis (2013), §16.2.1, Claims 16.1–16.2 and Step 5 (pp. 325–329)
> Similar: Tadelis (2013), Exercise 16.3, pp. 335–336

Q: In any separating PBE of Tadelis's limit-pricing game, the high-cost incumbent produces its one-period monopoly output in the first period. Why?
- Because it wants to be recognized as high cost, and its monopoly output is the cheapest way to show the entrant that its marginal cost is high
- Because the low type's output is fixed by the separating constraint, and the high type must stay as far from it as it can to avoid being read as a deviator
- Because it faces entry anyway once identified, so distorting its first-period output only lowers its profit and cannot make the entrant's beliefs any worse
- Because the entrant's off-path beliefs treat every other output as low cost, so a deviation would deter entry and the high type would lose its duopoly profit
<!-- YW5zOjI= -->
> In a separating PBE the high type is identified and faces Cournot entry whatever it does. Switching its first-period output to the monopoly level raises period-1 profit, and the entrant's belief after that switch is either still "high cost" (same continuation) or more favourable, which can only help the incumbent: Tadelis's Claim 16.2. The high type does not want to be recognized: it would rather be taken for low cost, which is why the low type must over-produce. Distance from the low type's output plays no role. Deterring entry would raise the high type's profit, so a belief "low cost" off the path would be a reason to deviate, not to stay.
> Ref: Tadelis (2013), §16.2.1, Claim 16.2 (pp. 325–327)
> Similar: Tadelis (2013), Exercise 16.7, p. 338

## ic

Q: The intuitive criterion's second condition asks whether some type not in the excluded set $\Theta'$ does strictly better by sending the unused action $a_1$ than in equilibrium, whatever best reply the receiver makes to beliefs concentrated outside $\Theta'$. A textbook writes the payoff inside that minimum as $v_2$, the receiver's. Why must it be $v_1$?
- It need not be: the receiver must gain from believing the deviator, and the condition checks this by asking whether the receiver's payoff rises after the deviation
- Because the test is about the sender's incentive to deviate: it compares the deviating type's equilibrium payoff with the sender's worst payoff from $a_1$
- Because $v_2$ would make the condition depend on the prior, while the intuitive criterion must hold for every prior, so only the sender's payoff can enter it
- Because the receiver's payoffs already enter through the first condition, which would count them twice if the second condition also used the receiver's payoff
<!-- YW5zOjE= -->
> Both conditions of Def. 16.1 compare a sender type's equilibrium payoff $v_1^*(\theta)$ with the sender's payoff from $a_1$: condition 1 with the best payoff under any reply in $BR_2(\Theta, a_1)$, condition 2 with the worst under replies in $BR_2(\Theta \setminus \Theta', a_1)$. The receiver's payoffs enter only through the best-reply sets $BR_2$, in both conditions. Tadelis prints $v_2$ in condition 2; his own explanation and the "speech" of the high type are about the sender's gain (8 against 6 in the MBA game). The receiver's gain is not what the test asks, and the prior plays no role in either condition.
> Ref: Tadelis (2013), §16.3, Def. 16.1 and the discussion around it (pp. 333–334); Gibbons (1992), §4.4, Signaling Requirement 6 (p. 239); project errata note `.agent/notes/errata-game-theory-books.md`
> Similar: Tadelis (2013), Exercise 16.7, p. 338

Q: For which kind of PBE of a signaling game can the intuitive criterion never have any bite?
- A pooling PBE in which the receiver's reply to the pooled message is strict, because then no deviation can change the receiver's behaviour after it
- A PBE in which the sender has only two types, because with two types the excluded set and its complement leave nothing to test after a deviation
- A PBE in which every message is sent by some type, because the criterion only restricts beliefs after messages that no type sends in equilibrium
- A PBE in which the receiver has only two actions, because then the best replies to any belief are fixed and no type can gain for sure by deviating
<!-- YW5zOjI= -->
> The criterion is a restriction on off-path beliefs: it looks for an unused action that some types could never gain from and that another type gains from for sure once those types are excluded. If every message is used, beliefs are pinned by Bayes' rule everywhere and there is nothing to restrict; so the MBA game's separating PBE passes "trivially". Two types are where it bites hardest: it kills every pooling PBE in Spence, the MBA game and limit pricing. A strict reply to the pooled message says nothing about the reply to an unused one. Two receiver actions are enough for the MBA pooling equilibrium to fail.
> Ref: Tadelis (2013), §16.3 (pp. 333–335); Gibbons (1992), §4.4 (pp. 233–239)
> Similar: Tadelis (2013), Exercise 16.8, p. 338

Q: In Gibbons's Beer–Quiche game the sender is wimpy with probability 0.1 and surly with 0.9; each type gets 1 from its preferred breakfast, Quiche for wimpy and Beer for surly, and 2 from avoiding a duel; the receiver wants to duel only a wimpy sender. In a PBE both types drink Beer, there is no duel after Beer, and Quiche is met with a duel. Does it survive the intuitive criterion?
- Yes: Quiche gives the surly type at most 2, below his payoff of 3, so he is excluded; with the belief on the wimpy type the receiver duels, and wimpy gains nothing
- No: Quiche gives the wimpy type up to 3, above his payoff of 2, so the wimpy type can persuade the receiver to hold off the duel and gains by switching to Quiche
- No: Quiche gives the surly type at most 2, below his payoff of 3, so he is excluded; the receiver then believes wimpy, and the wimpy type deviates to escape the duel
- Yes: neither type is excluded, since Quiche gives each type at most 3, so the receiver's belief after Quiche stays unrestricted and the duel can be kept as a reply
<!-- YW5zOjA= -->
> Equilibrium payoffs: wimpy $0 + 2 = 2$ (Beer, no duel), surly $1 + 2 = 3$. From Quiche the surly type gets at most $0 + 2 = 2 < 3$: equilibrium-dominated, so excluded. The wimpy type gets up to $1 + 2 = 3 > 2$, so he is kept, and a belief concentrated on him makes the receiver duel, the very reply the equilibrium uses; the wimpy type then gets $1 + 0 = 1 < 2$. No type gains for sure, so this pooling PBE passes, unlike pooling on Quiche. The second option forgets that a receiver who believes "wimpy" duels; the third draws the wrong conclusion from the right exclusion; the fourth miscounts the surly type's best payoff from Quiche.
> Ref: Gibbons (1992), §4.4, Beer and Quiche, Fig. 4.4.3 (pp. 237–239); Tadelis (2013), §16.3, Def. 16.1 (pp. 333–334)
> Similar: Tadelis (2013), Exercise 16.8, p. 338
