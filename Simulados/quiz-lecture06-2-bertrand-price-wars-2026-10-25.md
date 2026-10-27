---
quiz: "Lecture 6 · Quiz 2 of 3 — Price collusion, market structure and price wars (estimated before the lecture: built from the books and the L06 notes, no slides yet)"
tags:
  bertrand: "Repeated Bertrand: all or nothing"
  factors: "What the discount factor is made of, and market structure"
  punish: "Sharper sticks and renegotiation"
  wars: "Price wars under imperfect monitoring and demand shocks"
---

## bertrand

Q: $n$ identical firms sell a homogeneous good at constant marginal cost $c$ with no capacity limits, set prices simultaneously every period forever, and discount with $\delta$. Under grim strategies they charge the monopoly price, sharing the monopoly profit $\pi_M$ equally, and price at $c$ forever after any deviation. When is this an equilibrium?
- $\delta\ge1/n$, from $\frac{\pi_M/n}{1-\delta}\ge\pi_M$: each member's market share sets the patience it needs to stay loyal
- $\delta\ge1-1/n$, from $\frac{\pi_M/n}{1-\delta}\ge\pi_M$: an undercutter takes the whole market and the punishment pays zero
- $\delta\ge1/2$ for every $n$, from $\frac{\pi_M/2}{1-\delta}\ge\pi_M$: an undercutter faces one rival at a time, whatever $n$ is
- $\delta\ge\frac{(n+1)^2}{n^2+6n+1}$, from (10.5) with a punishment that leaves each firm the Cournot profit after a deviation
<!-- YW5zOjE= -->
> Conforming is worth $\frac{\pi_M/n}{1-\delta}$; undercutting by $\varepsilon$ wins (almost) $\pi_M$ today and zero forever, so $\frac1n\ge1-\delta$. In (10.5) terms, $v^c=\pi_M/n$, $v^d=\pi_M$, $v^p=0$. The share falls with $n$ while the temptation stays at $\pi_M$, which is why the cutoff rises with $n$. The last option is the Cournot cutoff, where punishment profit is positive and the deviator does not take the whole market.
> Ref: Cabral (2017), §9.1 eqs. (9.1)–(9.4) (pp. 218–219), §9.3 (p. 227); MWG (1995), Prop. 12.D.1 (p. 401)
> Similar: Gibbons (1992), Problem 2.13, p. 135; MWG (1995), Exercise 12.D.2, p. 405

Q: In the infinitely repeated Bertrand duopoly with constant marginal cost $c$, monopoly price $p_M$ and discount factor $\delta$, what happens to collusion when $\delta$ is below the grim-trigger cutoff of $1/2$?
- Firms can still sustain a price strictly between $c$ and $p_M$, because a lower collusive price cuts the deviation gain faster than it cuts the share
- Firms can still collude by switching to a one-period price war after each deviation, which deters undercutting at any $\delta$ in this game
- Firms can still sustain the monopoly price, because the threat of pricing at $c$ forever is harsh enough to deter undercutting at any $\delta$
- No price above $c$ survives, because for any collusive price $p$ the condition $\frac{\pi(p)/2}{1-\delta}\ge\pi(p)$ does not depend on $p$
<!-- YW5zOjM= -->
> Replace $p_M$ by any $p\in(c,p_M]$: conforming yields $\frac12\pi(p)/(1-\delta)$, undercutting yields $\pi(p)$, and $\pi(p)$ cancels, leaving $\delta\ge\frac12$. MWG Prop. 12.D.2 goes further: for $\delta<\frac12$ every subgame-perfect equilibrium has all sales at $c$ in every period, so no punishment scheme helps, since zero profit is already the harshest stick. Cournot is different: a cartel short of patience colludes less instead of not at all.
> Ref: MWG (1995), Props. 12.D.1–12.D.2 (pp. 401–403); Cabral (2017), §9.1 (pp. 218–219)
> Similar: Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 5 Ex. 5, p. 231; Gibbons (1992), Problem 2.13, p. 135

Q: With linear demand and constant marginal cost, compare the grim-trigger cutoffs for colluding on the monopoly outcome under Bertrand, $1-1/n$, and under Cournot, $(n+1)^2/(n^2+6n+1)$, where $n$ is the number of firms. Which statement is correct?
- Bertrand needs less patience at $n=2$ and more from $n=3$ on: the zero-profit stick wins with two firms, the whole-market temptation after that
- Bertrand needs more patience for every $n$: undercutting captures the whole market, while a Cournot deviator still leaves its rivals some sales
- Bertrand needs less patience for every $n$: its punishment drives profit to zero, while Cournot reversion leaves every firm a positive profit
- Bertrand and Cournot need equal patience at $n=2$ and Bertrand more after: the two sticks coincide when the market has only two firms
<!-- YW5zOjA= -->
> At $n=2$, $1/2<9/17$; at $n=3$, $2/3>16/28$; at $n=10$, $0.9>0.752$. Bertrand has both the harshest punishment (zero, which lowers the cutoff) and the largest temptation (the whole monopoly profit, which raises it). With two firms the harsher stick wins by a small margin; with three or more the larger temptation dominates. Each one-sided option keeps only one of the two effects.
> Ref: Cabral (2017), §9.3 (p. 227); Gibbons (1992), §2.3.C (p. 103); Lecture 6 notes L06-03 §2
> Similar: Tadelis (2013), Exercise 10.8, p. 218

## factors

Q: Cabral builds the effective discount factor as $\delta=\frac{(1+g)(1-h)}{1+r/f}$, with $r$ the annual interest rate, $f$ the number of price revisions per year, $h$ the per-period probability that the industry ends and $g$ the per-period demand growth. With $h=g=0$, how large can a Bertrand cartel colluding under grim strategies be?
- $n\le1+r/f$, so the largest sustainable cartel shrinks as the firms revise their prices more often within a year
- $n\le f/r$, so the largest sustainable cartel grows in proportion to the number of price revisions within a year
- $n\le1+f/r$, so the largest sustainable cartel grows linearly with the number of price revisions within a year
- $n\le(1+f/r)/2$, so the largest sustainable cartel grows at half the rate of the price revisions within a year
<!-- YW5zOjI= -->
> The Bertrand condition $\delta\ge1-1/n$ reads $n\le1/(1-\delta)$. With $\delta=1/(1+r/f)$, $1-\delta=\frac{r/f}{1+r/f}$, so $1/(1-\delta)=1+f/r$. Cabral's example, 10 per cent a year with monthly prices, gives 121 firms; annual prices give 11. The model now over-predicts collusion, which is why Cabral turns to antitrust, turnover, renegotiation and imperfect observation of prices.
> Ref: Cabral (2017), eq. (9.5) (p. 220), p. 221; Lecture 6 notes L06-03 §3.1
> Similar: Cabral (2017), Exercise 9.1, p. 242; Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 6 Ex. 5, p. 290

Q: In Cabral's effective discount factor $\delta=\frac{(1+g)(1-h)}{1+r/f}$ ($r$ interest rate, $f$ price revisions per year, $h$ hazard that the industry ends, $g$ demand growth), which comparative statics are right, and what do they imply for collusion?
- $\delta$ rises with $f$ and $g$ and falls with $h$ and $r$: frequent interaction and a stable, growing market make collusion easier
- $\delta$ rises with $f$ and $h$ and falls with $g$ and $r$: frequent interaction and a market likely to end make collusion easier
- $\delta$ rises with $g$ and $r$ and falls with $f$ and $h$: rare interaction and a growing market with dear credit make collusion easier
- $\delta$ rises with $f$, $g$ and $h$ and falls with $r$ only: a risky market lowers what a price war costs, so collusion gets easier
<!-- YW5zOjA= -->
> A higher $f$ shortens the period, so $r/f$ falls; growth makes tomorrow's profit larger; the hazard multiplies tomorrow's payoff by $1-h$. A higher $h$ makes the future punishment matter less, so collusion is harder, not easier. Hence gas stations that reprice daily collude more easily than resorts that set annual rates, and a fast-obsolescence market less easily than cement.
> Ref: Cabral (2017), §9.1 (pp. 219–220); MWG (1995), §12.D (p. 403)
> Similar: Cabral (2017), Exercise 9.1, p. 242

Q: Two firms are Bertrand duopolists, with discount factor $\delta$, in two markets. Under grim strategies a deviation in either market triggers marginal-cost pricing in both. How does multimarket contact change the cutoff for monopoly pricing?
- It halves the cutoff to $1/4$ when the markets are identical, because a deviation is punished in two markets at once while it pays in only one
- It raises the cutoff to $3/4$ when the markets are identical, because a firm that cheats in both markets doubles its one-period gain from cheating
- It lowers the cutoff below $1/2$ when the markets are identical, because each firm faces the same rival twice and so meets it more frequently
- It leaves the cutoff at $1/2$ when the markets are identical, and it helps only when the markets differ, as when each firm has its own cost edge
<!-- YW5zOjM= -->
> With identical markets the best deviation is to cheat in both (any deviation triggers war everywhere): $2\pi_M$ today and zero after, against $2\cdot\frac12\pi_M/(1-\delta)$ from colluding. Both sides double and the cutoff stays $1/2$. Contact matters when the markets differ: a threat to retaliate in the market where the rival is strong sustains collusion in the market where it is weak (Cabral pp. 228–230). The half-cutoff option forgets that the best deviation exploits both markets.
> Ref: Cabral (2017), §9.3 (pp. 228–230); Lecture 6 notes L06-03 §4
> Similar: Cabral (2017), Exercise 9.15, p. 244

## punish

Q: In a Cournot duopoly ($P=a-Q$, marginal cost $c$, discount factor $\delta$), Abreu's two-phase strategy is: produce $q_m/2$; after any deviation both produce $x$ for one period; if both did, return to $q_m/2$. Let $\pi_m/2$ be the collusive profit, $\pi_d$ the best deviation from it, $\pi(x)$ the profit when both produce $x$, and $\pi_{dp}(x)$ the best deviation from the punishment. Which two conditions must hold?
- $\delta\bigl(\pi_m/2-\pi(x)\bigr)\ge\pi_d-\pi_m/2$ and $\delta\bigl(\pi_m/2-\pi_{dp}(x)\bigr)\ge\pi_d-\pi(x)$, one per phase with the deviation payoffs swapped
- $\delta\bigl(\pi_m/2-\pi(x)\bigr)\ge\pi_d-\pi_m/2$ and $\delta\bigl(\pi_m/2-\pi(x)\bigr)\ge\pi_{dp}(x)-\pi(x)$, one for the collusive phase, one for the stick
- $\delta\bigl(\pi_m/2-\pi(x)\bigr)\ge\pi_d-\pi_m/2$ only, since a firm that deviates from the stick just restarts the same punishment it faced
- $\frac{\delta}{1-\delta}\bigl(\pi_m/2-\pi(x)\bigr)\ge\pi_d-\pi_m/2$ and $\delta\bigl(\pi_m/2-\pi(x)\bigr)\ge\pi_{dp}(x)-\pi(x)$, a permanent loss in the first phase
<!-- YW5zOjE= -->
> (2.3.3): $\frac{\pi_m/2}{1-\delta}\ge\pi_d+\delta V(x)$ with $V(x)=\pi(x)+\frac{\delta}{1-\delta}\frac{\pi_m}{2}$ simplifies to the first inequality: the gain today against one period of punishment tomorrow, so no $1/(1-\delta)$ factor. (2.3.4): $V(x)\ge\pi_{dp}(x)+\delta V(x)$ simplifies to the second. Deviating from the stick is a real temptation, which is why the stick cannot be too harsh. At $\delta=1/2$ the two give $x/(a-c)\in[3/8,1/2]$, so the monopoly outcome is sustained where grim trigger needs $9/17$.
> Ref: Gibbons (1992), §2.3.C eqs. (2.3.3)–(2.3.4) (pp. 104–106)
> Similar: Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 6 Ex. 3, p. 282

Q: After a deviation, grim trigger prescribes the stage Nash equilibrium forever, while Abreu's two-phase strategy prescribes one harsh period and then a return to collusion. Why is the second less exposed to renegotiation?
- Because the harsh period is a Nash equilibrium of the stage game, so neither firm can gain by proposing to skip it and restart collusion at once
- Because a one-period punishment hurts only the deviator, so the punishing firm has no reason to ask for it to be cancelled and restarted
- Because grim trigger leaves both firms worse off forever, so both gain by restarting collusion, while the short stick restores collusion anyway
- Because renegotiation needs an explicit agreement, which antitrust law forbids, while the return to collusion under the short stick is automatic
<!-- YW5zOjI= -->
> Under grim trigger, once a deviation has happened both firms prefer to return to collusion, so the deviator can propose "let bygones be bygones"; if both expect that, the threat is empty. The two-phase punishment also hurts the punisher, but only for one period, after which collusion resumes: the gain from skipping it is small. The stick is not a stage Nash equilibrium (it is harsher than Cournot), and it hurts both firms, not only the deviator.
> Ref: Gibbons (1992), §2.3.C (pp. 104–106), p. 111; Cabral (2017), §9.1 (p. 222)
> Similar: Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 6 Ex. 3, p. 282

## wars

Q: Cartel members observe only the market price, which depends on both their outputs and an unobserved demand shock. In a trigger-price equilibrium (Green and Porter), a price below a critical level starts a punishment phase. Which statement is correct?
- Price wars on the path reveal that some member cheated, so a cartel that observed none would be one that had stopped punishing
- The cartel should never punish after a low price, because low demand is the likelier cause, and punishing would destroy surplus
- Infinite punishments are optimal, because the harshest threat minimizes the temptation to cut output in secret in every period
- Price wars occur on the path even though no one cheats, and finite punishments beat infinite ones because they are set off by luck
<!-- YW5zOjM= -->
> If low prices were never punished, each firm would expand output in secret and blame demand. So bad shocks must trigger punishment, and in equilibrium nobody deviates, yet wars happen: they are the price of incentive compatibility under noise. Because punishments are triggered by accident, a permanent war would eventually be set off for sure, so finite wars are better. Cabral's Joint Executive Committee railroad cartel (1880–1886) fits the pattern.
> Ref: Gibbons (1992), §2.3.C (pp. 106–107); Tadelis (2013), §10.4 (pp. 203–204); Cabral (2017), §9.2 (pp. 223–224)
> Similar: Cabral (2017), Exercise 9.19, p. 245; Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 6 Ex. 10, p. 310

Q: Demand shocks are independent over time and every firm observes the current shock before setting prices (Rotemberg and Saloner), so deviations are always detected. When is the no-deviation constraint tightest, and what does the cartel do?
- In booms: the gain from undercutting scales with current demand while the future loss does not, so the cartel lowers its price in booms
- In slumps: the future loss is smallest when demand is low, so the cartel lowers its price in slumps and prices move with the cycle
- In booms: the future loss scales with current demand while the gain does not, so the cartel can raise its price further in booms
- In slumps: with observed shocks a deviation is always detected, so the constraint binds only when the cartel's profit is at its lowest
<!-- YW5zOjA= -->
> With i.i.d. shocks the expected value of future collusion is the same in every state, while today's gain from undercutting is proportional to today's demand. The constraint binds when demand is high, so the cartel must accept a lower margin then: collusive prices are counter-cyclical. Cabral's cement evidence: a 1 per cent rise in GDP lowers the relative price by 0.5 to 1 per cent. Green and Porter instead predict wars after low demand.
> Ref: Gibbons (1992), §2.3.C (p. 106); Cabral (2017), §9.2 (p. 225)
> Similar: Gibbons (1992), Problem 2.14, pp. 135–136
