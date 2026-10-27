---
quiz: "Lecture 3 · Quiz 3 of 3 — Credibility, commitment, Stackelberg and time inconsistency (estimated before the lecture: no slides yet, follows Tadelis §8.3 and Cabral §7.2)"
tags:
  cred: "Credible threats, entry deterrence and the value of commitment"
  stack: "Stackelberg competition and first-mover advantage"
  timeinc: "Time-inconsistent preferences as a game against one's future self"
---

## cred

P: An entrant stays out, which leaves the incumbent a payoff $M$, or enters. After entry the incumbent accommodates, giving itself $D_I$ and the entrant $E_a > 0$, or fights, giving itself $F_I$ and the entrant $E_f < 0$, with $F_I < D_I < M$. Before the entrant moves, the incumbent may post an enforceable bond $B \ge 0$ that it forfeits if it accommodates after entry.

Q: Which bonds make fighting the incumbent's strict best reply after entry, and what is the value of commitment (the incumbent's gain from posting such a bond)?
- Any $B > M - D_I$, and the value is $D_I - F_I$, the loss the incumbent avoids by not having to fight after entry
- Any $B > D_I$, and the value is $M - F_I$, the gap between monopoly and the payoff the incumbent gets in a price war
- Any $B > D_I - F_I$, and the value is $M - D_I + B$, since the bond is collected back in full once the entrant stays out
- Any $B > D_I - F_I$, and the value is $M - D_I$, since the entrant then stays out and the bond is never forfeited
<!-- YW5zOjM= -->
> After entry the bonded incumbent compares $F_I$ with $D_I - B$, so fighting is strictly better iff $B > D_I - F_I$. The entrant, anticipating the fight, compares $E_f < 0$ with $0$ and stays out, so the incumbent gets $M$; without the bond it would accommodate and get $D_I$. The bond is a penalty, never a payment when it is not triggered, so nothing is "collected back". At Cabral's numbers ($M = 50$, $D_I = 20$, $F_I = 10$) the threshold is 10 and the value 30; with the text's $F_I = -10$ the threshold is 30.
> Ref: Cabral (2017), §7.2, "The value of credible commitment" (pp. 169–170), Figs. 7.7–7.8; MWG Example 9.B.1 (pp. 268–269)
> Similar: Tadelis (2013), Exercise 8.8, pp. 171–172; Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 4 Ex. 2, p. 156

Q: Suppose the bond satisfies $0 < B < D_I - F_I$. What is the incumbent's subgame-perfect payoff if it posts the bond, and does it post it?
- $M$, and it posts it, since any bond signals resolve and the entrant, seeing it, prefers to stay out of the market
- $D_I - B$, and it does not post it, since the entrant still enters and the incumbent still accommodates, now paying $B$
- $F_I$, and it does not post it, since the bond makes the incumbent fight after entry, which pays less than accommodating
- $D_I$, and it is indifferent, since the bond is never forfeited when the incumbent accommodates the entrant after entry
<!-- YW5zOjE= -->
> Below the threshold, $D_I - B > F_I$: accommodating is still the best reply after entry, so the entrant still enters and the incumbent forfeits $B$. Its payoff $D_I - B$ is below the $D_I$ it gets without a bond, so it does not post one. A bond works only by changing behaviour at the node it targets; a "signal" that leaves the post-entry comparison unchanged is ignored by a rational entrant.
> Ref: Cabral (2017), §7.2 (pp. 169–170)
> Similar: Tadelis (2013), Exercise 8.9, p. 172

Q: Why does the bond lose its force if, after entry, the incumbent can renegotiate it with the party that would collect the penalty?
- Because the entrant could then buy the bond for $B$ and cancel it, so entering becomes profitable whatever the incumbent plans
- Because a renegotiable bond is not observed by the entrant, so the incumbent's commitment has no effect on the entry decision
- Because after entry both gain from cancelling the penalty for a payment below $D_I - F_I$, so the entrant expects accommodation
- Because renegotiation raises the incumbent's payoff $F_I$ from fighting, so the threat is credible without any bond at all
<!-- YW5zOjI= -->
> After entry, the bonded incumbent would fight and get $F_I$, and the bond holder would get nothing. If instead the holder waives the penalty for a payment $x$ with $0 < x < D_I - F_I$, the incumbent accommodates and gets $D_I - x > F_I$, and the holder gets $x > 0$: both gain. The entrant anticipates the deal and enters. That is why Cabral requires the contract to be non-renegotiable, and why he flags that most real contracts are renegotiable; the theme returns with relational contracts in Lecture 6.
> Ref: Cabral (2017), §7.2 (pp. 169–170) and footnote on renegotiation (p. 169)
> Similar: Tadelis (2013), Exercise 8.7, p. 171

P:

Q: Cabral models an incumbent that is credibly committed in two equivalent ways. Which pair is it, and why do they agree?
- Changing its payoffs, by a bond, or letting it pick fight or accommodate before entry; either way its reply is fixed and seen
- Changing its payoffs, or hiding the entrant's move from it; either way the incumbent loses the option to react to the entry
- Adding a move of Nature, or repeating the game; either way the incumbent builds a reputation that makes the threat believed
- Letting it move with the entrant, or giving it a mixed strategy; either way the entrant can no longer anticipate its reply
<!-- YW5zOjA= -->
> A commitment turns a later move into an earlier one. Lowering the payoff from accommodating until fighting is the best reply (Fig. 7.8), or letting the incumbent choose fight or accommodate before the entrant moves, observed by it (Fig. 7.9), gives the same backward-induction answer: the entrant stays out. Hiding the entry or moving simultaneously removes observation, which destroys the commitment rather than creating it; reputation is a repeated-game mechanism (Lectures 5–6).
> Ref: Cabral (2017), §7.2 (pp. 170–171), Figs. 7.8–7.9
> Similar: Tadelis (2013), Exercise 8.13, pp. 173–174

## stack

Q: Inverse demand is $P = a - Q$ and both firms have marginal cost $c < a$. Firm 1 chooses $q_1$; firm 2 observes it and chooses $q_2$. What are the subgame-perfect profits of the leader and of the follower?
- $(a-c)^2/9$ each, since observing $q_1$ changes nothing when the follower's reply is the Cournot best-response function
- $(a-c)^2/4$ and $(a-c)^2/16$, since the leader produces the monopoly output and earns the monopoly profit on it
- $(a-c)^2/8$ and $(a-c)^2/16$, since the leader sells $(a-c)/2$ and the follower $(a-c)/4$ at a margin of $(a-c)/4$
- $(a-c)^2/8$ each, since the follower matches the leader's margin and the two firms split the reduced output equally
<!-- YW5zOjI= -->
> The follower replies $R_2(q_1) = (a - c - q_1)/2$. The leader maximizes $q_1 (a - c - q_1)/2$, so $q_1^* = (a-c)/2$ and $q_2 = (a-c)/4$. Total output is $3(a-c)/4$, price minus cost is $(a-c)/4$, and profits are $(a-c)^2/8$ and $(a-c)^2/16$, against $(a-c)^2/9$ each in Cournot. The leader does produce the monopoly quantity, but the follower's output lowers the price, so it does not earn the monopoly profit. At $a = 100$, $c = 10$: 1012.5 and 506.25 against 900.
> Ref: Tadelis (2013), §8.3.2, eqs. (8.1)–(8.2) (pp. 160–161); Gibbons (1992), §2.1.B (pp. 61–63)
> Similar: Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 4 Ex. 11, p. 180; Ex. 12, pp. 185–186

Q: Inverse demand is $P = a - bQ$; the leader's marginal cost is $c_1$ and the follower's $c_2$, with $c_1 < a$. For which $c_2$ does the follower produce a positive quantity under simultaneous Cournot but zero in the subgame-perfect equilibrium of the Stackelberg game?
- $(a+c_1)/2 \le c_2 < a$, since the follower stays in Cournot until its cost reaches the monopoly price of the leader
- $c_1 < c_2 < (a+2c_1)/3$, since any cost disadvantage lets the leader's commitment push the follower out of the market
- $(a+2c_1)/3 \le c_2 < a$, since the follower is out of Stackelberg above that threshold and Cournot never shuts it out
- $(a+2c_1)/3 \le c_2 < (a+c_1)/2$, since the leader's commitment shuts the follower out before Cournot competition does
<!-- YW5zOjM= -->
> In Stackelberg the interior solution gives $q_2^S = (a + 2c_1 - 3c_2)/(4b)$, which is zero once $c_2 \ge (a + 2c_1)/3$; beyond that the leader sits at the kink $q_1 = (a - c_2)/b$, where the follower is just priced out. In Cournot $q_2^C = (a - 2c_2 + c_1)/(3b)$, positive iff $c_2 < (a + c_1)/2$, which is the leader's monopoly price. Since $(a + 2c_1)/3 < (a + c_1)/2$ whenever $c_1 < a$, the window is non-empty: commitment deters a rival that simultaneous competition would let in.
> Ref: Gibbons (1992), §2.1.B (pp. 61–64); Tadelis (2013), §8.3.2 (pp. 160–163)
> Similar: Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 4 Ex. 11, p. 180; Tadelis (2013), Exercise 8.6, pp. 170–171

Q: In the Stackelberg game with $P = a - Q$ and common marginal cost $c > 0$, firm 2 may use any strategy $q_2(q_1)$, including threats to flood the market. Which outcomes $(\hat q_1, \hat q_2)$ can be supported by some Nash equilibrium?
- Every $(\hat q_1, (a-c-\hat q_1)/2)$ with $0 \le \hat q_1 \le a-c$, each held up by a threat to flood if $q_1 \ne \hat q_1$
- Only $((a-c)/2, (a-c)/4)$, since a Nash equilibrium of this game must have firm 2 best-responding at every value of $q_1$
- Every $(\hat q_1, \hat q_2)$ on firm 1's reaction curve, since firm 1 then best-responds to firm 2's quantity on the path
- Only $((a-c)/2, (a-c)/4)$ and $((a-c)/3, (a-c)/3)$, the Stackelberg and Cournot points, both lying on firm 2's curve
<!-- YW5zOjA= -->
> Let firm 2 play $R_2(\hat q_1)$ if $q_1 = \hat q_1$ and flood the market otherwise, driving the price to zero. Any deviation by firm 1 earns at most $0$, while $\hat q_1$ earns $\hat q_1 (a - c - \hat q_1)/2 \ge 0$ iff $\hat q_1 \le a - c$; and firm 2 best-responds on the path. So every point of firm 2's reaction curve in that range is a Nash outcome; only the Stackelberg point is subgame perfect, because flooding is not a best reply after a deviation. Best-responding at every $q_1$ is the SPE requirement, not the Nash one.
> Ref: Tadelis (2013), §8.3.2 and Remark (pp. 162–163); note the printed reply "40" on p. 163 should read 35
> Similar: Tadelis (2013), Exercise 8.4, p. 170; Exercise 8.6, pp. 170–171

Q: Firm 1 chooses $q_1$ first, but firm 2 cannot observe it before choosing $q_2$; demand is $P = a - Q$ and both have marginal cost $c$. Why is $((a-c)/2, (a-c)/4)$ not an equilibrium of this game?
- Because firm 2's best reply to $(a-c)/2$ is $(a-c)/3$, so the follower would raise its output and the pair unravels to Cournot
- Because firm 1's best reply to $(a-c)/4$ is $3(a-c)/8$, so it would cut its output unseen; the unique equilibrium is Cournot
- Because firm 1's best reply to $(a-c)/4$ is $(a-c)/2$, but firm 2 cannot verify it, so it plays its Cournot output instead
- Because firm 2 moves later and so best-responds to the actual $q_1$, which makes this game the same as Stackelberg
<!-- YW5zOjE= -->
> Without observation firm 2 has one information set, so the game is simultaneous whatever the clock says. If firm 2 expects $(a-c)/2$ and replies $(a-c)/4$, firm 1's best reply is $(a - c - (a-c)/4)/2 = 3(a-c)/8$: the leader's quantity is no longer a commitment, because cutting it goes unseen. The unique Nash equilibrium is Cournot, $(a-c)/3$ each. Firm 2's reply to $(a-c)/2$ really is $(a-c)/4$, so the first option misstates it. Moving first is worth nothing unless the move is observed.
> Ref: Gibbons (1992), §2.1.B (pp. 63–64); Tadelis (2013), §7.1 (p. 131)
> Similar: MWG Exercise 9.B.5, p. 302

## timeinc

Q: A sophisticated decision maker splits a budget $K$ over three periods with utility $\ln x_t$ and $\beta\delta$ discounting with $\delta = 1$, $\beta \in (0,1)$: self 1 maximizes $\ln x_1 + \beta \ln x_2 + \beta \ln x_3$, and self 2, with budget $K_2$, maximizes $\ln x_2 + \beta \ln x_3$. What is self 1's equilibrium consumption?
- $x_1 = K/(1+\beta)$, from weighting each of self 2's reply terms by the share of $K_2$ that it allocates
- $x_1 = K/3$, since with $\delta = 1$ all three periods carry the same weight and $\beta$ only alters self 2's split
- $x_1 = K/(1+\beta+\beta^2)$, since present bias compounds and every later period is discounted again by $\beta$
- $x_1 = K/(1+2\beta)$, since self 2's split of $K - x_1$ only adds constants inside the logs in self 1's objective
<!-- YW5zOjM= -->
> Self 2 sets $x_2 = K_2/(1+\beta)$ and $x_3 = \beta K_2/(1+\beta)$. Substituting with $K_2 = K - x_1$, self 1's objective is $\ln x_1 + 2\beta \ln(K - x_1)$ plus constants, so $1/x_1 = 2\beta/(K - x_1)$ and $x_1 = K/(1+2\beta)$: $K/2$ at Tadelis's $\beta = 1/2$. The first option multiplies each derivative by the constant inside the log, which is the slip behind the printed $2K/3$ on p. 169. The third is an exponential-style formula that confuses $\beta$ with $\delta$.
> Ref: Tadelis (2013), §8.3.4, eq. (8.9) and the sophisticated example (pp. 167–169)
> Similar: Tadelis (2013), Exercises 8.14 and 8.16, p. 174

Q: With $\beta\delta$ discounting and log utility, self 1 values $\ln x_1 + \beta\delta \ln x_2 + \beta\delta^2 \ln x_3$ and self 2 values $\ln x_2 + \beta\delta \ln x_3$, where $\beta \in (0,1)$ and $\delta \in (0,1]$. What ratio $x_2/x_3$ does self 1 want, and which does self 2 choose?
- Self 1 wants $1/(\beta\delta)$ and self 2 chooses $1/\delta$, since the planner is the one who weighs the present more
- Self 1 wants $1/\delta$ and self 2 chooses $1/(\beta\delta)$, so self 2 tilts the remaining budget towards period 2
- Both want $1/\delta$, since the factor $\beta$ multiplies both future periods equally and so cancels out of the ratio
- Self 1 wants $1/\delta$ and self 2 chooses $\beta/\delta$, so self 2 tilts the remaining budget towards period 3
<!-- YW5zOjE= -->
> With log utility the optimal ratio of two consumptions equals the ratio of their weights. Self 1 weighs periods 2 and 3 by $\beta\delta$ and $\beta\delta^2$, so she wants $x_2/x_3 = 1/\delta$; self 2 weighs them by $1$ and $\beta\delta$, so she chooses $1/(\beta\delta) > 1/\delta$. The factor $\beta$ cancels from self 1's ratio but not from self 2's, because for self 2 period 2 is the present: that asymmetry is the time inconsistency, and with $\beta = 1$ the two ratios coincide.
> Ref: Tadelis (2013), §8.3.4, eqs. (8.3)–(8.9) (pp. 166–169)
> Similar: Tadelis (2013), Exercise 8.15, p. 174
