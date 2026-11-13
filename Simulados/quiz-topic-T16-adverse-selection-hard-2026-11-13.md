---
quiz: "Topic T16 · Adverse selection — hard conceptual quiz (10 questions; estimated unit, no slides: Tadelis §12.3–12.4, M&R Ch. 5, MWG §13.B, Gibbons §3.2.C, Cabral §7.4)"
tags:
  unravel: "Unravelling: what a single price buys"
  limits: "When adverse selection bites and when it stops"
  screen: "Screening, signaling and moral hazard"
  cv: "Common values and the pivotal event"
---

## unravel

Q: A buyer of used machines knows that every machine is worth more to her than to its owner, and reasons: "if I offer the average of the owners' valuations over all machines, I gain on average, because my valuation of each machine exceeds its owner's." Owners know their machine's quality; she does not. What is wrong with the argument?
- It fails only if the buyer is risk averse: with risk neutrality an average gain from trade guarantees that some single price leaves her a positive expected surplus
- The relevant average is over the owners who accept, and at any price only those who value their machine below it sell, so the pool she buys is worse than average
- It ignores that owners bargain the price up: once an offer is made, each owner counters with his own valuation, so the buyer ends up paying the average plus a premium
- It is right when qualities are spread out and fails only when they are close together, since then many owners sit exactly at the price and reject on indifference
<!-- YW5zOjE= -->
> The price selects the pool: at any offer only owners whose value lies below it sell, so the buyer must compare the price with her value of the *accepting* sellers, not of the population. In Tadelis's grove the population averages are 24 (buyer) and 20 (seller), yet at 20 only low and medium sell and that pool is worth 19. Risk aversion plays no role: the buyer there is risk neutral and still only the lowest type trades (Prop. 12.1). There is no haggling: the buyer makes a take-it-or-leave-it offer and the failure is pure selection. The last option has the comparative static backwards: the $k$-th quality can join only if the gain $\Delta$ is at least $(k-1)s/2$, so a *wider* spread $s$ of privately known quality makes unravelling worse.
> Ref: Tadelis (2013), §12.3, Prop. 12.1 (pp. 258–261); Milgrom & Roberts (1992), Ch. 5, adverse selection (pp. 149–151)
> Similar: Tadelis (2013), Exercises 12.5–12.6, pp. 267–268

Q: Worker productivity $\theta$ is uniform on $[0,2]$ and privately known; a worker's home value is $\alpha\theta$ with $0<\alpha<1$, so every worker is more productive in a firm. Competitive firms pay a single wage $w$ equal to the average productivity of the workers who accept it. For $\alpha>1/2$, what is the set of competitive equilibrium wages?
- Every $w \in [0, 1]$, since any wage below the population mean attracts a pool whose average productivity can be matched by some lower wage
- Only $w = 1$, since $\alpha < 1$ makes employment efficient for every worker, and at that wage the whole population accepts and is paid its mean
- Only $w = \alpha$, since at that wage the marginal worker's home value equals the wage and the pool's average productivity exactly covers it
- Only $w = 0$, since at any $w>0$ the accepting workers have $\theta \le w/\alpha$ and average $w/(2\alpha) < w$, so the market unravels entirely
<!-- YW5zOjM= -->
> A worker accepts $w$ iff $\alpha\theta \le w$, i.e. $\theta \le w/\alpha$; while $w/\alpha \le 2$ the accepting pool averages $w/(2\alpha)$, which is below $w$ for every $w>0$ when $\alpha>1/2$. So no positive wage breaks even and $w^*=0$: complete unravelling although all trade is efficient (MWG Example 13.B.1). At $w=1$ only $\theta\le 1/\alpha<2$ accept, averaging $1/(2\alpha)<1$; at $w=\alpha$ only $\theta\le1$ accept, averaging $1/2<\alpha$. The interval claim confuses "some pool" with the pool a wage actually attracts. (For $\alpha<1/2$ the wage 1, employing everyone, is an equilibrium.)
> Ref: MWG (1995), §13.B, Def. 13.B.1 (p. 439), eq. 13.B.6 (p. 441), Example 13.B.1 (p. 442)
> Similar: MWG (1995), Exercises 13.B.1–13.B.2, p. 473

## limits

Q: In Tadelis's orange-grove game, quality is low, medium or high with equal probability, the seller values the three at 10, 20 and 30 and the buyer at 14, 24 and 34, and the buyer makes a take-it-or-leave-it offer. Only the low quality can trade. Which change, keeping every valuation, lets every quality trade?
- A free inspection whose verdict both parties see before the offer, because the buyer can then make a separate offer equal to the seller's value for each quality
- A rule letting the seller make the take-it-or-leave-it offer, because each type can then ask the buyer's value for its own quality and the buyer will accept it
- A second buyer bidding against the first, because competition between buyers raises the offer to the buyer's average value of 24 and brings in the medium sellers
- A rule that the seller must state the quality before the offer, because a stated quality makes the buyer's offer conditional and so removes the lemons problem
<!-- YW5zOjA= -->
> Tadelis names two ingredients: common values (the seller's type enters the buyer's payoff) and cheap talk (no credible way to reveal the type). A verifiable inspection removes the second: with known quality each grove is an ultimatum game whose SPE trades at the seller's value. A seller who sets the price faces the same problem in reverse: every type would ask 34, a pooled ask is accepted only if it is at most 24, and the high type needs at least 30, so not all can trade. Competition among uninformed buyers bids the price up only to the value of the pool that accepts it; at 24 only low and medium sell, a pool worth 19. An unverifiable statement is cheap talk: every type claims high quality.
> Ref: Tadelis (2013), §12.3 (pp. 258–261, footnote 5 on p. 259, "talk is cheap" on pp. 260–261); MWG (1995), §13.B (pp. 439–443)
> Similar: Tadelis (2013), Exercise 12.5, pp. 267–268

Q: Change the orange-grove game so that the buyer values every grove at 25 whatever its quality, while the seller privately values low, medium and high quality, each with probability 1/3, at 10, 20 and 30. The buyer makes a take-it-or-leave-it offer. What happens, and why?
- The buyer offers 20 and buys low and medium groves, because without common values the accepting pool's quality no longer matters and adverse selection disappears
- The buyer offers 25 and buys every grove the seller values below 25, because with private values the outcome is efficient whatever offer the buyer happens to make
- The buyer offers 10 and only low groves trade, because raising the offer to 20 means paying more for the low groves too, not because the accepting pool gets worse
- The buyer offers 10 and only low groves trade, because the medium sellers who accept at 20 are worth less to the buyer than the price that it takes to bring them in
<!-- YW5zOjI= -->
> Offering 10 buys the low grove with probability 1/3 and earns $\tfrac13(25-10)=5$; offering 20 buys low and medium and earns $\tfrac23(25-20)=\tfrac{10}{3}<5$; offering 30 loses. So the buyer offers 10 and the efficient sale of the medium grove (worth 25 against 20) is lost. The cause is not adverse selection: the buyer's value does not depend on who accepts, so the last option's reason is false (the medium grove is worth 25 to her). It is the monopsony trade-off of a price-setter facing private reservation values: a higher price buys more units but pays a rent to the units it already bought. The first two options get the offer wrong (20 and 25 both earn less than 10). This is why Tadelis lists common values as one of the two ingredients of adverse selection.
> Ref: Tadelis (2013), §12.3, the discussion after Prop. 12.1 (pp. 260–261); Milgrom & Roberts (1992), Ch. 5 (pp. 149–151)
> Similar: Tadelis (2013), Exercise 12.6, p. 268

Q: Two insurance markets have the same mix of high- and low-risk customers, the same costs and the same valuations of cover. In the first, each customer knows his own risk; in the second, neither customers nor insurers know any individual's risk. Which statement is correct?
- Both markets suffer the same adverse selection, because the insurer faces the same uncertainty about each customer's cost in both and prices to the same average
- The second market fares worse, because customers who do not know their risk cannot pick the cover suited to them, and so the low-risk ones stay out of the market
- Only the first can unravel, because there low-risk customers drop out at a pooled premium, while in the second each customer values cover at the population mean
- Only the second can unravel, because uninformed customers value cover at the average, which an insurer charging average cost plus a margin will always exceed
<!-- YW5zOjI= -->
> Adverse selection needs asymmetric information, not uncertainty. In Cabral's numbers, a premium of 4.5 lies between average cost 3.9 and average value 4.7; when patients know their risk only the high risks (value 20, cost 30) buy, the insurer loses 2.55 per patient and ends up selling to nobody. When patients do not know their risk, each values cover at 4.7, buys at 4.5, and the insurer earns 0.6: same numbers, only who knows what changed. The first option treats the insurer's uncertainty as the problem; the second has it backwards; the fourth fails because the average value exceeds the average cost here, so a premium between them sells.
> Ref: Cabral (2017), §7.4, pp. 174–176 (Figs. 7.11–7.12); Milgrom & Roberts (1992), Ch. 5 (pp. 149–152)
> Similar: Cabral (2017), Exercises 7.9–7.10, pp. 180–181

Q: A seller and a buyer each privately know their own valuation of an object, drawn independently and uniformly from $[0,1]$. A mediator wants a trading rule, which both would agree to play, under which trade happens exactly when the buyer's valuation exceeds the seller's. What does the theory say?
- No such rule exists: with private information on both sides every voluntary rule loses some efficient trades; the linear double-auction equilibrium loses those under 1/4
- Such a rule exists: a posted price of 1/2 makes trade voluntary for both sides, and as it is set before values are drawn neither party can manipulate it to block efficient trade
- Such a rule exists: the double auction that trades at the average of ask and offer has an equilibrium in which each side names its own value, so every efficient trade happens
- No such rule exists, but only because the double auction has many equilibria; selecting its linear equilibrium by a refinement would restore trade wherever it is efficient
<!-- YW5zOjA= -->
> Myerson and Satterthwaite show that no bargaining game both parties would willingly play trades iff $v_b \ge v_s$; among the double auction's equilibria the linear one, which trades iff $v_b \ge v_s + 1/4$, gives the largest expected gains (9/64 against the efficient 1/6). A posted price of 1/2 trades only when $v_s \le 1/2 \le v_b$ and misses every efficient trade on one side of 1/2. Truthful naming is not an equilibrium of the double auction: the buyer shades down and the seller up, as the linear strategies $\tfrac23 v + \text{const}$ show. The linear equilibrium is itself inefficient, so no selection among equilibria can fix the problem.
> Ref: Gibbons (1992), §3.2.C (pp. 158–163, Myerson–Satterthwaite on pp. 162–163)
> Similar: Gibbons (1992), Problem 3.8, p. 171

## screen

Q: An insurer finds that the buyers of its maternity cover have far more births per year than the population. Which observation would point to adverse selection rather than moral hazard?
- Buyers had birth rates like everyone else's before signing, and their rate rose only after the cover made having a child cheaper for them
- The excess vanishes once premiums are set by the buyer's age, which shows that the insurer's pricing, not the buyers' information, caused it
- Births among buyers vary at random from year to year, so the higher rate is noise that a larger pool of policies would wash out over time
- Buyers were already planning children when they signed, so the higher rate reflects who chose to buy, not what the cover led them to do
<!-- YW5zOjM= -->
> Adverse selection is pre-contractual hidden information (who you are); moral hazard is post-contractual hidden action (what you do once covered). M&R's own example: a family that buys maternity cover because it plans children is adverse selection; having more children because the cover pays is moral hazard. The first option is the moral-hazard pattern. If pricing on an observable such as age removes the excess, the gap came from a characteristic the insurer could see, not from private information. Random variation does not produce a systematic difference between buyers and non-buyers.
> Ref: Milgrom & Roberts (1992), Ch. 5, pp. 149–150
> Similar: Milgrom & Roberts (1992), Ch. 5, Questions 5.3–5.5, pp. 164–165

Q: Classify the two practices: (i) an insurer offers a menu with a cheap high-deductible policy and an expensive full-cover policy and lets each customer choose; (ii) job seekers earn a costly degree before applying, and employers read the degree as evidence of ability.
- Both are signaling, because in both the informed side ends up revealing its type through a costly choice that the uninformed side then interprets
- The menu is screening and the degree is signaling, because in the first the uninformed side moves first and in the second the informed side does
- The menu is signaling and the degree is screening, because the insurer signals its prices first, while employers screen applicants by their degrees
- Both are screening, because in both the uninformed side ends up sorting the informed by observing choices that the informed side would rather hide
<!-- YW5zOjE= -->
> M&R draw the line by who takes the lead: in signaling the privately informed act first (education, warranties, dividends); in screening the uninformed design a menu and the informed self-select. Both rely on self-selection constraints, which is why "the informed reveal themselves through a costly choice" is true of both and cannot be the distinction. The insurer's prices carry no private information about the insurer, so they signal nothing; the employer in (ii) designs nothing. The timing changes the game: MWG treat signaling as a PBE problem (§13.C) and screening as an SPNE of a game in which firms move first (§13.D).
> Ref: Milgrom & Roberts (1992), Ch. 5, "Signaling, Screening, and Self-Selection" (pp. 154–157); MWG (1995), §13.C (p. 450) and §13.D (pp. 460–461)
> Similar: MWG (1995), Exercise 13.D.2, p. 476

Q: An insurer that cannot observe risk offers two policies designed so that high-risk customers take one and low-risk customers the other. In the standard screening solution, which customers are left with less than full coverage, and why?
- The low-risk ones, because a deductible costs a high-risk customer more in expected terms, so partial cover is what makes the cheap policy unattractive to high risks
- The high-risk ones, because they are the costly customers to insure, so the insurer limits their coverage to cap its expected losses on the riskier half of the pool
- Nobody, because once types self-select each policy is priced at its own type's expected cost, and at a fair price every risk-averse customer buys full coverage
- Both types, because each policy must be unattractive to the other type, so each one carries a deductible that the intended type tolerates and the other does not
<!-- YW5zOjA= -->
> Self-selection is achieved by varying coverage: the high risks get full coverage at a high price per unit, and the low risks get a cheaper policy with partial cover. Partial cover costs a high risk more because he expects more uncovered losses, so it is the device that keeps him out of the cheap policy. Capping the high risks' cover would push them toward the cheap policy, which is the wrong direction. Full cover for both at type-specific fair prices is the full-information outcome and is not self-selecting: high risks would buy the cheap full-cover policy. The high risks need no distortion because nobody wants to mimic them. M&R call the low risks' missing coverage the cost of the information asymmetry.
> Ref: Milgrom & Roberts (1992), Ch. 5, screening and insurance (pp. 158–159); MWG (1995), §13.D (pp. 460–466; Rothschild–Stiglitz on p. 461)
> Similar: MWG (1995), Exercise 13.D.2, p. 476

## cv

Q: Two jurors each privately observe a signal that is correct with probability $p>1/2$; the prior probability of guilt is $q>1/2$; conviction needs both votes, and each juror earns 1 for a correct verdict. A textbook states that both jurors always voting to convict is a Bayesian Nash equilibrium. When is that claim true?
- For every $p$ and $q$, since a juror who expects the other to convict knows his vote can matter only when the other juror has also seen a guilt signal
- Only when $p > q$, since then each juror's signal is precise enough to justify following the other juror's lead rather than his own innocence signal
- Never, since a juror who sees an innocence signal always prefers to acquit, and under unanimity a single acquittal vote is enough to block a conviction
- Only when $p \le q$, since against a juror who always convicts each vote decides every case, so an innocence signal must be too weak to beat the prior
<!-- YW5zOjM= -->
> If the other juror always convicts, your vote decides the verdict in every state, so you condition only on your own signal. After an innocence signal you still convict iff $\Pr\{G \mid \theta_I\} = \frac{q(1-p)}{q(1-p)+(1-q)p} \ge \frac12$, i.e. iff $p \le q$. Tadelis states the claim with no condition (p. 264, and Exercise 12.8(a)); with $q=0.6$, $p=0.7$ the posterior is $0.18/0.46 \approx 0.39$ and the juror acquits. The first option borrows the pivotal event of "vote your signal", where the other juror convicts only after a guilt signal; against an unconditional convictor that event is every state. The third ignores the case $p\le q$, where even an innocence signal leaves guilt more likely. For $p>q$ the pure equilibria are $(AA,AA)$, $(CA,CC)$ and $(CC,CA)$.
> Ref: Tadelis (2013), §12.4 (pp. 261–264), Exercise 12.8 (pp. 268–269); project errata note `.agent/notes/errata-game-theory-books.md`; worked solution in `Listas/pratica-lecture-07-solutions.pdf` (Tadelis 12.8)
> Similar: Tadelis (2013), Exercise 12.8, pp. 268–269
