---
quiz: "Topic T9 · Commitment and credibility — hard conceptual quiz (10 questions; Lectures 3–4, Tadelis §8.3, Brexit case)"
tags:
  cred: "Credibility, commitment and observability"
  strat: "Strategic moves in oligopoly"
  timeinc: "Time inconsistency"
---

## cred

Q: Suppose the EU cannot observe whether the UK has prepared for a hard Brexit, while everything else in the Lecture 4 Brexit game stays the same. What happens to the equilibrium?
- No pure equilibrium is left: the UK prepares and the EU offers the favourable deal only with some probability, and the UK ends up worse off
- The subgame-perfect outcome is unchanged, since the EU anticipates that a rational UK prepares and so offers it the favourable deal as before
- The UK stops preparing altogether, since a sunk cost the EU cannot see can never move its offer, and the EU offers the unfavourable deal
- The UK prepares for sure and the EU randomizes, since preparation still makes rejecting a bad deal credible at the UK's own reply nodes
<!-- YW5zOjA= -->
> Once the EU's offer cannot depend on preparation, the best responses cycle: against preparation the EU offers F, against F the UK would rather save the 5, against no preparation the EU offers U, and against U the UK prepares. The case's mixed equilibrium has the UK preparing with probability 8/13 and the EU offering F with probability 11/36; the UK's expected cost rises from 24.7 to about 26.64, while the EU's stays at 14, and a hard Brexit becomes far more likely. The second option fails because, expecting F, the UK would not prepare; the third because, facing U for sure, the UK would prepare; the fourth because, facing a prepared UK for sure, the EU would offer F for sure.
> Ref: Cases/Brexit/brexit-game.pdf, "The unobservable variant: commitment must be seen"; Lecture 4 slide 11 ("Observability matters")
> Similar: Simulados/quiz-lecture03-3-commitment-stackelberg-2026-10-25, section stack (unobserved leader)

Q: Why does the UK's sunk preparation move the EU's offer in the Brexit game, while a public statement that the UK will reject a bad deal does not?
- Because the outlay signals the UK's private resolve, and the EU revises its beliefs about the UK's type after seeing it, as in a signaling game
- Because sunk costs bind future behavior legally while statements can be withdrawn, so it is the contract, not the payoff, that the EU relies on
- Because preparation lowers the UK's cost of a hard Brexit, so rejecting becomes a best reply, while a statement leaves every payoff unchanged
- Because the EU discounts statements by the chance that Parliament overrules the government, while preparation is beyond Parliament's reach
<!-- YW5zOjI= -->
> Preparation mitigates 12.5 of the 35 a hard Brexit costs, so a prepared UK compares $-27.5$ from rejecting with $-27.9$ from accepting the neutral deal and rejects; an unprepared UK compares $-35$ with $-25.4$ and accepts. The EU reads these payoffs, not words: "Talk is cheap. Announcing 'I will reject a bad deal' without preparing is not credible." The game has complete information, so there is no type to signal (first option); nothing in the game is legally binding (second option); and Parliament votes on a deal after the UK accepts it, which plays no role in the threat (fourth option).
> Ref: Lecture 4 slides 9 and 11; Tadelis (2013), §8.2 (pp. 153–159)
> Similar: Listas/pratica-lecture-04 #1 (Tadelis 8.8, Entry Deterrence 1)

Q: In the Brexit game both sides would gain if the EU could promise a generous deal to a UK that does not prepare, saving the 5 spent on preparation. Why does this not happen in the subgame-perfect equilibrium?
- Because the generous deal would be rejected by Parliament more often, which makes it worth less to the UK than the favourable deal after preparing
- Because the UK's preparation is sunk before the EU can speak, so the promise would come too late to change the UK's choice at the first node
- Because a deal that saves both sides money must lie beyond the frontier of feasible deals, so no offer the EU could make would deliver it
- Because the promise is not credible: once the UK is unprepared, the unfavourable deal is the EU's best reply, and the UK knows it in advance
<!-- YW5zOjM= -->
> The case computes a deal on the same frontier (UK and EU costs summing to 32) that leaves an unprepared UK as well off as in the SPE and costs the EU about 11.5 instead of 14, so both would gain. But the EU moves after the UK's preparation decision, and once the UK has not prepared, offering U is the EU's best reply; the UK anticipates this and prepares. The inefficiency is a commitment problem on the EU's side, the mirror image of the UK's credible threat. Parliament's pass probability does not depend on the deal in the base case (first option); the promise would be made before the UK chooses (second option); and the deal lies on the frontier, not beyond it (third option).
> Ref: Cases/Brexit/brexit-game.pdf, "Efficiency: preparation as rent-shifting" ("A bargain the parties cannot strike"); Lecture 4 slides 10–11
> Similar: Listas/pratica-lecture-04 #10 (Tadelis 8.7, Debt and Repayment)

Q: A country installs an automatic retaliation device that it cannot switch off and that its rival can inspect. How does the device's threat differ from the same threat made by a leader who would decide after an attack?
- The device's threat is credible only if retaliating is a best reply after an attack, as for the leader, since a machine inherits its owner's payoffs
- The device removes the later choice, so retaliation needs no sequential rationality, while the leader's threat holds only if retaliating is then optimal
- The two threats are equivalent, since the rival's best reply depends only on its beliefs about retaliation, and those beliefs are the same in both cases
- The leader's threat is more credible, since a leader can tailor the response to the attack, while a device must respond the same way every time
<!-- YW5zOjE= -->
> Credibility is a property of a choice that remains open: a threat is credible if carrying it out is a best reply when the moment comes. Commitment changes the tree itself: the device deletes the post-attack decision node, so there is nothing left to be sequentially rational about, and because the rival can inspect it, the deletion is observed. The leader's threat is credible only if retaliation is optimal after an attack, which in mutually assured destruction depends on which equilibrium the post-escalation subgame selects. Beliefs in a subgame-perfect equilibrium are not free, so the two cases differ (third option), and flexibility is exactly what makes the leader's threat weaker (fourth option).
> Ref: Tadelis (2013), §8.3.3 (pp. 163–166); Lecture 3 slide 38; Cabral (2017), §7.2 (pp. 167–172)
> Similar: Simulados/quiz-lecture03-3-commitment-stackelberg-2026-10-25, section cred

## strat

Q: In the linear Stackelberg game with inverse demand $P = a - q_1 - q_2$ and common marginal cost $c$, the leader produces $(a-c)/2$ and the follower $(a-c)/4$. Is the leader's output a best reply to the follower's output?
- Yes, since every subgame-perfect profile is a Nash equilibrium of the game, so each firm's quantity is a best reply to the other firm's quantity
- Yes, since the leader maximizes profit given the follower's reaction, and at the optimum her marginal revenue equals marginal cost as in Cournot
- No: against $(a-c)/4$ the leader would rather produce $3(a-c)/8$; she produces more only because it moves the follower along its reaction curve
- No: against $(a-c)/4$ the leader would rather produce more than $(a-c)/2$, since a timid follower leaves residual demand that pays to fill
<!-- YW5zOjI= -->
> The leader's best reply to $q_2$ is $(a-c-q_2)/2$, which at $q_2=(a-c)/4$ is $3(a-c)/8 < (a-c)/2$. Given the follower's actual output, the leader overproduces; her quantity is optimal only against the follower's strategy $q_2(q_1)$, because a larger $q_1$ makes the follower shrink. The first option is the subtle trap: the SPE is a Nash equilibrium in strategies, and the follower's strategy is a function, not a number, so the leader best-replies to the function. The second option ignores that the leader's marginal revenue includes the follower's induced response, so it does not match the Cournot condition.
> Ref: Tadelis (2013), §8.3.2 (pp. 160–163); Lecture 3 slide 37; Gibbons (1992), §2.1.B (pp. 61–64)
> Similar: Listas/pratica-lecture-04 #4 (Muñoz-Garcia Ch. 4 Ex. 11, Stackelberg with two firms)

Q: Before competing, firm 1 makes an observable investment that lowers its own marginal cost. Through its effect on the rival's later choice, is this strategic effect good or bad for firm 1?
- Good under Cournot quantities, where the rival cuts output in reply, and bad under differentiated prices, where the rival cuts its price too
- Good in both, since a lower cost makes firm 1 more aggressive, and a rival facing a more aggressive firm always backs off in its own strategic variable
- Bad under Cournot quantities, where the rival expands output to keep its share, and good under price competition, where the rival raises its price
- Neutral in both, since the rival's best reply depends only on its own costs, so the investment helps firm 1 only through its own margin
<!-- YW5zOjA= -->
> A lower cost makes firm 1 more aggressive in stage 2 in both models: more output, or a lower price. Quantities are strategic substitutes (the rival's best reply slopes down), so the rival produces less, which helps firm 1. Prices with differentiated products are strategic complements (the rival's best reply slopes up), so the rival cuts its price too, which hurts firm 1. The direct cost saving is always good; only the strategic effect changes sign. The second option assumes every rival backs off; the third reverses both slopes; the fourth ignores that the rival's best reply depends on firm 1's anticipated action, which the investment shifts.
> Ref: MWG §12.G, Example 12.G.1 and Fig. 12.G.2 (pp. 414–416); Cabral (2017), §7.2 (pp. 167–172)
> Similar: Listas/pratica-lecture-04 #6 (Tadelis 8.6, Investment in the Future)

Q: In the linear Stackelberg game, firm 1 announces $q_1$ first, but after firm 2 chooses $q_2$, firm 1 can revise $q_1$ at no cost before the market clears. What is the subgame-perfect outcome?
- The Stackelberg outcome with firm 1 leading, since firm 1 still moves first and firm 2 sees its announced quantity before committing to its own
- The Stackelberg outcome with firm 2 leading, since firm 1's first move is cheap talk and firm 2's quantity is fixed before firm 1's final choice
- The Cournot outcome, since both firms can now adjust to each other, and the only profile from which neither wants to move is the mutual best reply
- The monopoly split, since the possibility of revision lets the firms punish each other and so sustain the output that maximizes their joint profit
<!-- YW5zOjE= -->
> Work backwards. At the last move firm 1 picks its best reply to the $q_2$ it sees, whatever it announced, so the announcement affects no payoff. Firm 2 anticipates this and chooses $q_2$ to maximize its profit along firm 1's reaction curve: firm 2 is the real leader. Commitment needs irreversibility as well as observability; an output that can be revised for free commits to nothing, which is the logic of "talk is cheap". Cournot would need the two final choices to be simultaneous (third option), and a one-shot game with one revision offers no future in which to punish (fourth option).
> Ref: Tadelis (2013), §8.3.2 (pp. 160–163); Lecture 4 slide 11; Lecture 3 slide 37
> Similar: Listas/pratica-lecture-04 #8 (Muñoz-Garcia Ch. 4 Ex. 12)

## timeinc

Q: A decision maker with present-biased preferences splits a budget over three periods: from any period on, she weighs the next period by $\beta\delta$, with $\beta<1$. Who would pay at period 1 to fix the split between periods 2 and 3 in advance?
- Both a naive and a sophisticated self 1 would pay the same, since each disagrees with self 2 about the split and each expects the same deviation
- Neither would pay, since self 2 maximizes the same lifetime utility as self 1 and so chooses exactly the split that self 1 would have chosen
- Only a naive self 1 would pay, since a sophisticated self 1 already accounts for self 2's choice and so cannot gain anything by restricting it
- Only a sophisticated self 1 would pay, since she foresees self 2 tilting the budget toward period 2, while a naive one expects her plan to hold
<!-- YW5zOjM= -->
> Self 1 weighs periods 2 and 3 by $\beta\delta$ and $\beta\delta^2$, a ratio of $\delta$; self 2 weighs them by $1$ and $\beta\delta$, a ratio of $\beta\delta$, so self 2 spends more of what is left in period 2 than self 1 wants. A sophisticated self 1 foresees this and gains from tying self 2's hands; a naive one believes her plan will be carried out and sees nothing to buy. Tadelis: "What is interesting about sophisticated players is that they would choose to constrain their" future choices. Anticipating the deviation does not remove its cost (third option); self 2 does not share self 1's weights (second option); and only the sophisticated self expects the deviation (first option).
> Ref: Tadelis (2013), §8.3.4, eq. (8.9) and the discussion of naive and sophisticated players (pp. 166–169)
> Similar: Listas/pratica-lecture-04 #12 (Tadelis 8.16, The Value of Commitment); #9 (Tadelis 8.15)

Q: A central bank with unchanging preferences announces zero inflation, yet once wages are set it prefers surprise inflation. How does this time inconsistency differ from that of a present-biased consumer?
- It needs no change in tastes: the plan stops being optimal because wage setters' choices are sunk by then, which is a sequential-rationality problem
- It is the same mechanism, since the bank discounts the future more steeply at each date and so revises its plans as a present-biased consumer does
- It arises only if the bank is naive about its future self, since a sophisticated bank would foresee the temptation and so resist it when it arrives
- It disappears once wage setters hold rational expectations, since they then expect zero inflation and the bank has no reason to surprise them
<!-- YW5zOjA= -->
> In the Barro–Gordon stage game employers set expected inflation, then the bank chooses inflation with the same preferences throughout; given any expectation it inflates, so the subgame-perfect outcome has positive inflation, and the bank "would be better off if it could commit to having no inflation." The plan is time-inconsistent because others' choices become sunk, not because tastes change, unlike $\beta\delta$ preferences. Rational expectations are what produce the inflation bias, not what cure it (fourth option); a sophisticated bank foresees the bias but cannot escape it without commitment (third option).
> Ref: Gibbons (1992), §2.3.E (pp. 112–115); Tadelis (2013), §8.3.4 (pp. 166–169)
> Similar: Simulados/quiz-lecture03-3-commitment-stackelberg-2026-10-25, section timeinc

Q: Why does Tadelis model a sophisticated present-biased consumer as a game between her period-1 and period-2 selves, solved by subgame perfection, rather than as one decision problem?
- Because her two selves hold different information about the budget, so their choices must be modeled with information sets as in a Bayesian game
- Because a single decision maker always discounts exponentially by definition, and present bias can only be expressed as a conflict between players
- Because her later self ranks the remaining plans differently, so her plan for later periods counts only if it is a best reply for that later self
- Because the budget constraint couples the periods, and only an equilibrium concept can allocate a fixed budget across several decision dates
<!-- YW5zOjI= -->
> With $\beta\delta$ preferences, the self at period 2 ranks continuation plans differently from the self at period 1, so self 1 cannot simply choose the whole path: whatever she plans for periods 2 and 3 will be carried out only if it is optimal for self 2. Treating each self as a player and solving by backward induction imposes exactly this sequential-rationality requirement. Information is complete (first option); a single decision maker can perfectly well have non-exponential discounting, which is what creates the conflict (second option); and a budget constraint alone is handled by ordinary optimization, as in the exponential case (fourth option).
> Ref: Tadelis (2013), §8.3.4 (pp. 167–169); Notas/L03/L03-08-time-inconsistency
> Similar: Tadelis (2013), Exercises 8.14–8.16, p. 174
