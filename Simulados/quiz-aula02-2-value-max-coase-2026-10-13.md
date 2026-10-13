---
quiz: "Aula 2 · Quiz 2 of 3 — Value maximization and the Coase theorem"
tags:
  vmp: "The value maximization principle"
  shares: "Fixed shares versus free transfers"
  coase: "The Coase theorem"
  tc: "Transaction costs and the theorem's limits"
---

## vmp

Q: Two people have utilities $U_i = x_i + v_i(y)$, $i = 1, 2$, where $x_i$ is money and $y$ a joint decision that generates cash $P(y)$, split as $x_1 + x_2 = P(y)$; let $W(y) = P(y) + v_1(y) + v_2(y)$. What does the utility possibility frontier look like?
- The line $U_1 + U_2 = \max_y W(y)$, since each $y$ gives a $-45°$ line $U_1 + U_2 = W(y)$ and the highest line lies above all others
- A concave curve through the points $(W(y), 0)$ and $(0, W(y))$, since each $y$ fixes one utility pair and transfers trace out the rest
- The line $U_1 + U_2 = \max_y P(y)$, since only cash can be transferred and the personal values $v_i(y)$ cannot move between people
- The envelope of the lines $U_1 = W(y) - U_2$, which bends outward wherever two decisions $y$ give the same total $W(y)$
<!-- YW5zOjA= -->
> Summing utilities gives $U_1 + U_2 = P(y) + v_1(y) + v_2(y) = W(y)$: the shares $x_i$ drop out. Each $y$ therefore yields a straight line at $-45°$ (moving one unit of money moves one unit of utility), and the frontier is the highest of these, at $\max_y W$ (M&R Figure 2.1). The curved frontier is the wealth-effects case. Maximizing $P$ alone ignores the personal costs $v_i$.
> Ref: Milgrom & Roberts (1992), Ch. 2, pp. 36–37, Figure 2.1; Aula 2 notes §3.1
> Similar: M&R Mathematical Exercise 2.3, p. 53

Q: Two people have utilities $U_i = x_i + v_i(y)$, $i = 1, 2$, with $x_1 + x_2 = P(y)$ and total value $W(y) = P(y) + v_1(y) + v_2(y)$. They start at decision $y^0$ with utilities $U_1^0, U_2^0$; $y^*$ maximizes $W$ and $W(y^*) > W(y^0)$. Which money payment $x_1$ at $y^*$ (person 2 receiving $P(y^*) - x_1$) gives each person the old utility plus half of the gain?
- $x_1 = U_1^0 + \tfrac12[W(y^*) - W(y^0)] + v_1(y^*)$
- $x_1 = U_1^0 + \tfrac12[W(y^*) - W(y^0)] - v_1(y^0)$
- $x_1 = U_1^0 + \tfrac12[W(y^*) - W(y^0)] - v_1(y^*)$
- $x_1 = U_1^0 + [W(y^*) - W(y^0)] - v_1(y^*)$
<!-- YW5zOjI= -->
> Person 1's utility at $y^*$ is $x_1 + v_1(y^*)$; setting it equal to $U_1^0 + \tfrac12[W(y^*) - W(y^0)]$ gives the third option. Person 2 then gets $W(y^*) - U_1 = U_2^0 + \tfrac12[W(y^*) - W(y^0)]$, since $U_1^0 + U_2^0 = W(y^0)$. Both are strictly better off, so any allocation that does not maximize $W$ is inefficient. The personal cost is the one at the new decision, $v_1(y^*)$, not at $y^0$.
> Ref: Milgrom & Roberts (1992), Ch. 2, p. 37; Aula 2 notes §3.1–§3.2
> Similar: M&R Mathematical Exercises 2.1–2.2, p. 53

Q: When preferences display wealth effects, how does maximizing the sum of the parties' utilities relate to efficiency?
- It remains necessary and sufficient, since any allocation off the maximum can be improved by a transfer from the gainer to the loser
- It remains sufficient but not necessary, since the frontier is curved and its different points can use different decisions
- It becomes necessary but not sufficient, since a maximum of the sum can leave one person worse off than at the starting point
- It becomes neither, since with wealth effects utilities cannot be added, so efficiency has to be checked pair by pair instead
<!-- YW5zOjE= -->
> Maximizing any sum of utilities still gives a point on the frontier (sufficient). But with wealth effects the frontier is curved, and points on it that do not maximize the unweighted sum are efficient too, often with a different $y$ (M&R n. 10). So there is no single "efficient decision"; the value maximization principle's "if and only if" needs quasi-linearity.
> Ref: Milgrom & Roberts (1992), Ch. 2, p. 37 n. 10; Aula 2 notes §3.1, §8
> Similar: M&R Mathematical Exercise 2.3, p. 53

## shares

P: A supplier S and an assembler A choose a joint quality $y \ge 0$. Revenue is $P(y) = \rho y$ with $\rho > 0$; personal costs are $v_S(y) = -\tfrac12 c_S y^2$ and $v_A(y) = -\tfrac12 c_A y^2$, with $c_S, c_A > 0$. Revenue is split in fixed shares, $s$ to S and $1 - s$ to A, and each party would like $y$ set to maximize its own payoff.

Q: With no side payments possible, which share $s$ makes both parties want the efficient quality $y^*$?
- $s = c_A/(c_S + c_A)$, which gives S the larger share when A's cost is larger, so both want $y^* = \rho/(c_S + c_A)$
- $s = \tfrac12$ always, which splits the revenue equally, so both want $y^* = \rho/(c_S + c_A)$ whatever the two costs are
- $s = c_S/(c_S + c_A)$, which matches each party's revenue share to its share of marginal cost, so both want $y^* = 2\rho/(c_S + c_A)$
- $s = c_S/(c_S + c_A)$, which matches each party's revenue share to its share of marginal cost, so both want $y^* = \rho/(c_S + c_A)$
<!-- YW5zOjM= -->
> $W(y) = \rho y - \tfrac12(c_S + c_A)y^2$, so $y^* = \rho/(c_S + c_A)$. S maximizes $s\rho y - \tfrac12 c_S y^2$, wanting $y = s\rho/c_S$; A wants $(1 - s)\rho/c_A$. Both equal $y^*$ iff $s = c_S/(c_S + c_A)$. The $2\rho$ version forgets the $\tfrac12$ in the costs; equal shares work only when $c_S = c_A$.
> Ref: Aula 2 notes §3.2
> Similar: M&R Mathematical Exercise 2.2, p. 53

Q: Suppose $s = \tfrac12$ and $c_S > c_A$, still with no side payments. How do the levels preferred by S and A compare with $y^*$?
- $\rho/(2c_S) < y^* < \rho/(2c_A)$: S wants too little and A too much, so the split now shapes how much value is created
- $\rho/(2c_A) < y^* < \rho/(2c_S)$: S wants too much and A too little, so the split now shapes how much value is created
- $\rho/(2c_S) < \rho/(2c_A) < y^*$: both want too little, so the split lowers value but the parties still agree on $y$
- $\rho/c_S < y^* < \rho/c_A$: S wants too little and A too much, but bargaining over $y$ alone restores $y^*$
<!-- YW5zOjA= -->
> Preferred levels are $\rho/(2c_S)$ and $\rho/(2c_A)$, and $y^* = \rho/(c_S + c_A)$. With $c_S > c_A$, $2c_S > c_S + c_A > 2c_A$, so $\rho/(2c_S) < y^* < \rho/(2c_A)$. Each party bears all of its own cost but receives only half the revenue, and the party with the higher cost wants less. Without transfers there is no way to compensate the side that would lose from $y^*$.
> Ref: Aula 2 notes §3.2, §7
> Similar: M&R Mathematical Exercise 2.2, p. 53

Q: Now suppose that, with the share $s$ still fixed, the parties may also agree on $y$ together with a lump-sum payment between them, bargaining efficiently. What do they choose?
- The level preferred by whichever party has the larger revenue share, with the lump sum compensating the other party for its extra cost
- A level between the two preferred levels, weighted by the revenue shares, since a lump sum cannot change anyone's marginal incentives
- $y^* = \rho/(c_S + c_A)$ whatever $s$ is, since the lump sum lets the gain from moving to $y^*$ be shared so that both gain
- $y^* = \rho/(c_S + c_A)$ only when $s = c_S/(c_S + c_A)$, since otherwise one party always vetoes the move to $y^*$ in bargaining
<!-- YW5zOjI= -->
> Once money moves freely, the value maximization principle applies: the parties choose $y$ to maximize $W$ and use the lump sum to divide the gain. The share $s$ then only shifts the split, which the lump sum can undo. A lump sum does not change marginal incentives when each party chooses alone; here $y$ is chosen jointly, so it does not need to.
> Ref: Milgrom & Roberts (1992), Ch. 2, pp. 37–38; Aula 2 notes §3.2
> Similar: M&R Mathematical Exercise 2.2, p. 53

## coase

Q: Residents downstream have utility $x + \theta c$, where $x$ is money, $c \in \{0, 1\}$ indicates clean water and $\theta > 0$; a factory upstream gains $G$ from dumping, with $\theta > G$. The factory holds the right to dump, bargaining is costless and money moves freely. Which payments $t$ from residents to the factory leave both weakly better off, and what is the outcome?
- $0 \le t \le G$, with clean water as the outcome, the same as if the residents had held the right, though now they pay instead of being paid
- $G \le t \le \theta$, with clean water as the outcome, the same as if the residents had held the right, though now they pay instead of being paid
- $G \le t \le \theta$, with clean water as the outcome, which differs from the case where residents hold the right and the factory buys it to dump
- $\theta \le t \le G$, an empty range here, so the outcome is dumping, since the factory holds the right and residents cannot buy it back
<!-- YW5zOjE= -->
> The factory accepts any $t \ge G$ (what it gives up); residents pay any $t \le \theta$ (what they gain). Since $\theta > G$ the range $[G, \theta]$ is nonempty and the water is cleaned. Had residents held the right, the factory would need to pay at least $\theta > G$, so again no dumping. The outcome is the same; only the direction of payment changes. This is the Coase theorem with quasi-linear values.
> Ref: Milgrom & Roberts (1992), Ch. 2, p. 38; Cabral (2017), §5.1, pp. 96–98; Varian (2014), §35.2, p. 670; Aula 2 notes §4.2
> Similar: Varian (2014), Ch. 35 Review Questions 1–2, p. 687

Q: A reorganization gives one division of a firm the right to veto the other division's choice of technology. If the divisions bargain efficiently and their preferences display no wealth effects, what changes?
- The technology chosen, since the division holding the veto can now block any project that does not maximize its own payoff
- Nothing at all, since property rights are irrelevant under the Coase theorem, for the technology and for the payments alike
- Both the technology and the transfers, since bargaining power shapes the agreement and the agreement covers both decisions
- Only the transfers between the divisions, since the technology chosen is still the one that maximizes the divisions' total value
<!-- YW5zOjM= -->
> The veto is an asset that changes each division's position at the bargaining table, so it moves the split. But under efficient bargaining and no wealth effects the agreed $y$ maximizes total value whatever the assets (M&R p. 38). "Property rights don't matter" is the classic misreading: they do not matter for $y$, and they always matter for who pays.
> Ref: Milgrom & Roberts (1992), Ch. 2, p. 38; Aula 2 notes §4.1, §8
> Similar: M&R FFT 2.2, p. 52

## tc

Q: Three bargains fail to reach the value-maximizing decision. In (i) the parties haggle for months before agreeing; in (ii) each side knows only its own value, and some mutually beneficial deals never happen; in (iii) the side that should pay for the efficient change has too little cash. Which hypothesis behind the Coase theorem fails in each?
- (i) costless bargaining, (ii) no wealth effects, (iii) full information about values
- (i) full information about values, (ii) costless bargaining, (iii) no wealth effects
- (i) costless bargaining, (ii) full information about values, (iii) unlimited transfers
- (i) unlimited transfers, (ii) full information about values, (iii) costless bargaining
<!-- YW5zOjI= -->
> Delay and haggling are bargaining costs (M&R pp. 147–149); deals that fail because values are private are the full-information problem (pp. 140–147); a payer who cannot pay is M&R's "ability to make unlimited transfer payments" (p. 39), their main caveat. The first two are Aula 3's subject; the third is why land tenure and slavery are their examples of misapplying the theorem.
> Ref: Milgrom & Roberts (1992), Ch. 2, pp. 38–39; Ch. 5, pp. 140–149; Aula 2 notes §4.1, §4.4
> Similar: M&R FFT 2.3, p. 52

Q: Under the value maximization principle, the efficient organization is the one that minimizes transaction costs for a given production plan, regardless of the prior distribution of power. Which evidence and which rival view do M&R set this against?
- Worker-controlled Yugoslav firms hired managers and organized like capitalist ones, against the Marxian view that organization reflects power
- Resale price maintenance survived antitrust challenges for decades, against the Marxian view that organization reflects the interests of capital
- Worker-controlled Yugoslav firms abolished managers and organized as partnerships, against the Harvard view that arrangements manipulate prices
- Japanese manufacturers kept long-term suppliers despite owning no shares in them, against the Harvard view that arrangements manipulate prices
<!-- YW5zOjA= -->
> If organization reflected power, workers in control would build a different organization. M&R cite Yugoslav worker-controlled firms that hired managers and organized much as capitalist firms did. Resale price maintenance is their example against the Harvard school: read as a transaction-cost device, it stops discounters free-riding on other dealers' service. They add that the choice between hypotheses needs "detailed evidence".
> Ref: Milgrom & Roberts (1992), Ch. 2, pp. 38–39; Aula 2 notes §4.3
> Similar: M&R FFT 2.2, p. 52
