---
quiz: "Topic T14 · Hard conceptual quiz — Reputation and relational contracts"
tags:
  finite: "Reputation with a finite horizon: types, beliefs and Bayes' rule"
  relational: "Relational contracts: observability, judgment and the end game"
---

## finite

Q: A prisoner's dilemma is repeated a known number $T$ of times. With probability $p > 0$, possibly very small, player 1 is a commitment type who plays grim trigger; otherwise he is strategic, and player 2 is strategic. What did Kreps, Milgrom, Roberts and Wilson show about long games?
- The number of periods with any defection is bounded by a constant that depends on $p$ but not on $T$, so cooperation fills almost all of a long game
- Cooperation lasts for a fraction $p$ of the periods, since player 2 cooperates exactly as often as he expects to be facing the commitment type
- Cooperation is possible only if $p > 1/2$, since below that player 2 defects in period 1 and the strategic type then reveals himself at once
- Cooperation lasts until the strategic type reveals himself, which happens with probability $1 - p$ in period 1, so it does not grow with the horizon $T$
<!-- YW5zOjA= -->
> Right (Tadelis's Proposition 17.1): if the strategic type ever defects before the end, he reveals himself and both defect until $T$; so he mimics the commitment type to keep player 2 cooperating, and player 2, anticipating this, cooperates too. Reputational incentives fade only near $T$, and the number of periods with defection is bounded independently of $T$. Even a tiny $p$ is enough in a long game. Wrong: cooperation is not proportional to $p$; the $p > 1/2$ condition belongs to Tadelis's short two- and three-period examples, not to the long-game result; and the strategic type does not reveal himself early, because pooling is what pays.
> Ref: Tadelis (2013), §17.1, Proposition 17.1 (pp. 341–342); Gibbons (1992), §4.3.C (pp. 224–226)
> Similar: Tadelis (2013), Exercise 17.1, pp. 354–355

Q: A prisoner's dilemma pays $1$ to each for mutual cooperation, $0$ to each for mutual defection, and $2$ to a defector facing a cooperator, who gets $-1$. Player 1 is a grim-trigger type with probability $p > 1/2$, otherwise strategic; player 2 is strategic. Why does the strategic type cooperate in period 1 when the game lasts three periods but defect in period 1 when it lasts two?
- With two periods player 2 defects in period 1 whatever he believes, so there is no one to cooperate with, while with three periods player 2 cooperates in period 1
- With three periods the strategic type is more patient, having two future periods to protect, so he plays grim trigger himself until the very last period
- With three periods, pooling keeps player 2's belief at the prior, so he cooperates in period 2 and can be exploited then; with two periods no later belief matters
- With two periods the grim-trigger type defects in period 2 after any cooperation, so cooperating in period 1 would earn the strategic type a sucker payoff later
<!-- YW5zOjI= -->
> Right: with three periods, if the strategic type cooperates in period 1, player 2's belief stays at $p > 1/2$, so by the two-period analysis player 2 cooperates in period 2 and the strategic type defects then: $1 + 2 + 0 = 3$, against $2 + 0 + 0 = 2$ from defecting at once and revealing himself. With two periods, player 2 defects in period 2 whatever he believes, so period-1 behaviour buys nothing and the strategic type defects. Wrong: in the two-period game player 2 does cooperate in period 1 when $p > 1/2$; the strategic type defects in period 2 of the three-period game, so he does not play grim trigger; and the grim-trigger type cooperates after cooperation.
> Ref: Tadelis (2013), §17.1, Claims 17.1–17.2 (pp. 340–341)
> Similar: Tadelis (2013), Exercise 17.1, pp. 354–355

Q: In the finitely repeated prisoner's dilemma, which kind of incomplete information did Kreps, Milgrom, Roberts and Wilson find not to be enough for cooperation, so that both defect in every stage, as under complete information?
- One-sided uncertainty about strategies, where with probability $p$ the row player can only play tit-for-tat, since the column player then exploits it in every stage
- One-sided uncertainty about stage payoffs, where with probability $p$ the row player's best response to cooperation is cooperation, with nothing unknown about column
- Two-sided uncertainty about stage payoffs, where each player's best response to cooperation is cooperation with some probability, since each waits for the other
- One-sided uncertainty about the horizon, where the row player alone knows the number of stages, since column then defects in the last stage he thinks possible
<!-- YW5zOjE= -->
> Right: Gibbons reports that one-sided uncertainty of this payoff kind still leaves finking in every stage, while two-sided uncertainty of the same kind supports cooperation until the last few stages. The one-sided tit-for-tat type works because a deviation from tit-for-tat makes it common knowledge that row is rational, so the rational row has a strong reason to mimic. Wrong: the tit-for-tat formulation is precisely the one-sided case that does produce cooperation; two-sided payoff uncertainty is the case that works; and uncertainty about the horizon is not part of the model.
> Ref: Gibbons (1992), §4.3.C (pp. 225–226)

Q: Reputation models of the finitely repeated prisoner's dilemma add a small probability that a player is a commitment type with fixed behaviour. What happens to their predictions when the modeller is free to choose which commitment types are possible?
- The predictions do not depend on that choice, since any commitment type gives the strategic type a reason to mimic it, and so produces the same cooperative path
- Cooperation becomes the unique prediction, since the strategic type mimics whichever commitment type yields the highest payoff, and that type always cooperates
- Defection becomes the unique prediction, since with many possible types no single reputation is credible, and backward induction from the last stage takes over
- Almost anything can be supported: with all conceivable types allowed for both players, a folk-theorem result obtains, so the prediction rests on the types assumed
<!-- YW5zOjM= -->
> Right: Tadelis's remark cites Fudenberg and Maskin (1986): if all conceivable types are possible for both players, any conceivable path of play can be an equilibrium. The gang-of-four result is driven by the grim-trigger (or tit-for-tat) type; a different commitment type would be mimicked differently. Wrong: the path depends on the type the strategic player imitates; nothing makes the best type to imitate a cooperative one; and many possible types multiply equilibria rather than restoring backward induction.
> Ref: Tadelis (2013), §17.1, Remark (p. 342); Gibbons (1992), §4.3.C (p. 226)

Q: Cooperation in the infinitely repeated prisoner's dilemma under grim trigger is often called a "reputation" equilibrium. In what sense does it differ from reputation in the Kreps–Milgrom–Roberts–Wilson model?
- It does not differ: in both, a player cooperates to keep the other's posterior belief about his type high, and loses that belief after a single defection
- In the infinite game reputation is a belief about the horizon, while in the finite model it is a belief about payoffs, and both are updated by Bayes' rule
- In the infinite game nothing is learned: payoffs are common knowledge and cooperation rests on threats and promises, while the finite model puts a type at stake
- In the infinite game reputation needs a commitment type with positive probability, while in the finite model cooperation rests only on threats and promises
<!-- YW5zOjI= -->
> Right: Gibbons suggests calling the complete-information equilibrium one of "threats and promises" and reserving "reputation" for games in which at least one player has something to learn about another. Under grim trigger everyone knows everyone's payoffs; the history matters only because strategies condition on it. In KMRW the history moves a posterior about a type. Wrong: no posterior exists under complete information; the horizon is known in both settings; the last option swaps the two models.
> Ref: Gibbons (1992), §4.3.C, footnote 7 (p. 225); Tadelis (2013), §10.5.1 (p. 204) and §17.1 (p. 339)

## relational

Q: Milgrom and Roberts's elementary theory of reputation applies to relational contracts, which leave what must be done unspecified. Which informational condition does that theory need for the relationship to enforce good behaviour?
- The parties must be able to tell afterwards whether the right thing was done, even if a court cannot verify it, so punishment can depend on what they see
- A court must be able to verify afterwards whether the right thing was done, since otherwise the injured party has no credible way to impose a punishment
- The parties must be able to specify in advance what the right thing will be in each contingency, since otherwise there is nothing for a reputation to be about
- Each party must know the other's type, since a reputation can discipline behaviour only when both sides know whether they are dealing with an honest partner
<!-- YW5zOjA= -->
> Right: the elementary theory assumes that contracts cannot specify what to do, but that the parties can tell afterwards whether the right thing was done; observability by the parties, not verifiability by a court, is what the trigger needs. If a court could verify, an explicit contract would do, and no reputation would be needed. Wrong: the second option describes formal enforcement; the third removes the reason for a relational contract, which exists because contingencies cannot be specified in advance; and the repeated-game reputation needs no uncertainty about types.
> Ref: Milgrom & Roberts (1992), Ch. 8, "Reputations as contract enforcers" (pp. 259–261)

Q: On the Western Front in 1914–1918, opposing battalions settled into "live and let live": fire in earnest only if fired upon. Commanders broke these truces by ordering raids. Why did the raids work, in repeated-game terms?
- Raids changed the stage payoffs, making shooting first strictly dominant, so the cooperative profile was no longer a Nash equilibrium of the repeated game
- Raids shortened each battalion's expected horizon, lowering its discount factor below the cutoff, so the cooperative profile stopped being self-enforcing
- Raids revealed that the other side had been preparing to attack anyway, so the truce collapsed as each side updated its belief about the other's type
- Raids injected deviations the other side could not tell from intentional ones, so the retaliation the equilibrium prescribes set off endless cycles of fire
<!-- YW5zOjM= -->
> Right: the truce was sustained by reciprocity, so a raid looked like a deviation and called for retaliation, which in turn called for retaliation; as with tit-for-tat after a single deviation, the punishment echoes. Milgrom and Roberts note that each side also showed it could retaliate, since the punishment must be visibly feasible. Wrong: a raid did not change what shooting paid; the battalions' horizon was unchanged; and the logic needs no types, only an equilibrium that conditions on observed fire.
> Ref: Milgrom & Roberts (1992), Ch. 8, "live and let live" (p. 264); Lecture 5 slides, slide 31 (a single deviation echoes under tit-for-tat)

Q: Milgrom and Roberts note that a reputation disciplines behaviour only if outsiders can judge whether the right thing was done, which ambiguity often prevents. How do simple, widely known corporate rules help, such as a football team's rule that an injured starter always gets his place back?
- They replace the repeated game with an explicit contract that a court enforces, so the firm no longer needs to rely on its reputation for fair treatment
- They make "the right thing" unambiguous in the cases they cover, so any departure is recognized by all and can be punished by a loss of reputation
- They raise the discount factor of the firm's managers, since a rule kept for many years lengthens the horizon over which the relationship is valued
- They lower the temptation to cheat by fixing payoffs in advance, so the firm's gain from breaking its word falls to zero in every contingency
<!-- YW5zOjE= -->
> Right: a reputation conditions on observed behaviour, so it fails when no one can tell whether a choice was honourable. A simple rule, communicable to all, turns a judgment call into a checkable fact, and the injured player has no reason to hide his injury. That is how corporate culture extends the reach of reputation. Wrong: the rule is not a court-enforceable contract, which is why reputation is still needed; it does not change the horizon or the discount factor; and it does not remove the gain from breaking it, it makes breaking it visible.
> Ref: Milgrom & Roberts (1992), Ch. 8, "Ambiguity, complexity, and limits of reputations" and corporate culture (pp. 264–265)

Q: A supplier is known to be closing down in a few months. Its customers, who have paid promptly for years, start claiming that recent deliveries were defective and withhold part of their payments. Which reading fits the theory of reputation?
- The customers have learned that the supplier's quality is low, since a closing firm cuts costs, so they rationally withhold payment for goods that are now worse
- The supplier has lost its incentive to monitor deliveries, so defects really increase, and the customers' claims simply reflect a genuine fall in quality
- The future that made prompt payment worth more than cheating is ending, so the customers' own honesty, not the supplier's, is no longer self-enforcing
- The customers fear that the supplier will cheat them first, so they withhold payment as insurance against defective goods they have not yet received
<!-- YW5zOjI= -->
> Right: this is Milgrom and Roberts's end game. Prompt payment was disciplined by the value of the continuing relationship to the customers; as the relationship ends, that value vanishes and their attitudes harden, exactly the unravelling of a known last period. The point is that the customers, not the supplier, are now the ones whose good behaviour is no longer enforced. Wrong: the story needs no change in quality, real or inferred; and fear of being cheated first is not what the claims about past deliveries reflect.
> Ref: Milgrom & Roberts (1992), Ch. 8, the end game and bankruptcy (p. 266); Lecture 5 slides, slide 9 (the endgame effect)
> Similar: Milgrom & Roberts (1992), Ch. 8, Quantitative Exercise 4, p. 286

Q: A firm has honoured trust for years: honouring earns it $V$ per period, a single betrayal earns $V + G$ once and nothing after, and it discounts at $\delta$, so it stays honest iff $G \le \delta V/(1-\delta)$. Which change is most likely to make it betray its customers?
- A rise in $V$, since more valuable business makes each betrayal pay more as well, raising the one-time gain relative to the stream of honest earnings
- A one-off order much larger than usual, since it raises $G$ for that period alone, while the stream $\delta V/(1-\delta)$ it puts at risk stays the same
- A fall in the interest rate, since a lower rate makes the future less certain, which reduces the weight $\delta$ that the firm puts on its future business
- A rise in the frequency of trade, since meeting customers more often multiplies the occasions to cheat, each worth $G$, so betrayal becomes more tempting
<!-- YW5zOjE= -->
> Right: the condition compares the one-time gain $G$ with the value of the future relationship; an unusually large order raises the temptation for one period without raising what honesty protects, so the inequality can fail once. Wrong: a higher $V$ raises the right-hand side, so it helps honesty (only $G$ is the extra gain); a lower interest rate raises $\delta$; and more frequent trade also raises $\delta$ per meeting, which is why frequent relationships sustain more trust.
> Ref: Milgrom & Roberts (1992), Ch. 8, the trust box and its multiplier (pp. 261–263); Tadelis (2013), §10.5.1 (p. 205)
