---
quiz: "Topic T5 · Hard conceptual quiz — Oligopoly and continuous games"
tags:
  cournot: "Cournot competition"
  bertrand: "Bertrand competition"
  commons: "Tragedy of the commons"
  space: "Spatial and electoral competition"
---

## cournot

Q: Cournot duopolists choose quantities and Bertrand duopolists choose prices, and in both models the firms sell substitute products. Which statement about strategic substitutes and strategic complements is correct?
- Cournot quantities are strategic substitutes, Bertrand prices complements: the terms refer to best-response slopes, not products
- Both games involve strategic substitutes, since in both of them the firms sell products that consumers treat as substitutes
- Cournot quantities are strategic complements, since a rival's larger output raises the market price each firm takes as given
- Bertrand prices are strategic substitutes, since a rival's higher price lets a firm sell more, so it wants to cut its own price
<!-- YW5zOjA= -->
> The terms describe how a player's best response moves with the rival's choice. In Cournot $q_i(q_j)=q^m-\tfrac12q_j$ slopes down: strategic substitutes (the commons is another example). In Bertrand, between cost and the monopoly price the best reply is to undercut the rival slightly, so it rises with $p_j$: strategic complements.
> Product substitutability holds in both models and does not settle the slope. A larger rival output lowers the price, and with it the best reply. A higher rival price lets a firm raise its own price and still undercut, so the best reply rises.
> Ref: Lecture 2 slides 23, 34; Tadelis (2013), §5.2.4 Remark (p. 93)

Q: In a Cournot duopoly with inverse demand $P=a-bQ$ and constant unit costs $c_1$ and $c_2$, the equilibrium is interior. Firm 2's unit cost rises by $\Delta$. What happens in the new equilibrium?
- Firm 2's output falls by $\Delta/(2b)$ and firm 1's stays put, since firm 1's own cost and the demand curve did not move at all
- Both outputs fall by $\Delta/(3b)$, since firm 2's higher cost raises the market price that firm 1 also faces, which deters it
- Firm 2's output falls by $2\Delta/(3b)$, firm 1's rises by $\Delta/(3b)$, total output falls and the price rises by $\Delta/3$
- Firm 2's output falls by $2\Delta/(3b)$ and firm 1's rises by just as much, so total output and the price stay put
<!-- YW5zOjI= -->
> Solving the two best responses gives $q_1^*=(a-2c_1+c_2)/(3b)$, $q_2^*=(a-2c_2+c_1)/(3b)$ and $P^*=(a+c_1+c_2)/3$. Raising $c_2$ by $\Delta$ lowers $q_2^*$ by $2\Delta/(3b)$ and raises $q_1^*$ by $\Delta/(3b)$, so $Q^*$ falls by $\Delta/(3b)$ and $P^*$ rises by $\Delta/3$.
> Firm 1's best-response function does not move, but firm 1 moves along it: quantities are strategic substitutes, so less from firm 2 means more from firm 1. That response offsets only half of firm 2's cut, so total output falls; a higher price follows from lower output and gives firm 1 no reason to produce less.
> Ref: Lecture 2 slides 21–24; Tadelis (2013), §5.2.3 (pp. 87–88); Notas/L01/L01-10-pitfalls.md, True/False item 18

Q: In the symmetric linear Cournot duopoly, in what sense is the Nash equilibrium inefficient?
- It is Pareto dominated for everyone, consumers included, by the cartel outputs, since the cartel saves on the firms' production costs
- For the two firms, the players, it is Pareto dominated by splitting the monopoly output; counting consumers, the cartel lowers surplus
- It is efficient for the firms, since each produces its best response, and inefficient only for consumers, who face a price over cost
- It is inefficient because total output exceeds the competitive level, so both firms and consumers would gain from producing less
<!-- YW5zOjE= -->
> Each firm produces $\tfrac23q^m$, so total output $\tfrac43q^m$ lies between the monopoly output $q^m$ and the competitive $2q^m$. The firms, who are the game's players, would both earn more by producing $\tfrac12q^m$ each, as in a prisoner's dilemma; consumers lose from that cut, and total surplus rises with output up to the competitive level.
> Consumers prefer more output, not the cartel. Mutual best responses can be Pareto dominated for the players, as here. Cournot output is below the competitive level, not above it.
> Ref: Lecture 2 slides 22–25; Tadelis (2013), §5.1.2 (p. 83), §5.2.3 (pp. 87–88)

## bertrand

Q: Two Bertrand firms with the same unit cost $c$ sell a homogeneous good, ties split the market, and prices must be multiples of a tick $\varepsilon>0$, with $c$ on the grid. Which profiles are pure Nash equilibria?
- Only $(c,c)$, as with continuous prices, since at any common price over $c$ each firm gains by undercutting one tick
- Every common price from $c$ up to the monopoly price, since on a grid a one-tick cut never pays more than sharing
- Both $(c,c)$ and $(c+\varepsilon,c)$: the firm at $c+\varepsilon$ sells nothing, and no other price on the grid helps it
- Both $(c,c)$ and $(c+\varepsilon,c+\varepsilon)$: from $c+\varepsilon$ the only undercut is to $c$, which earns nothing
<!-- YW5zOjM= -->
> At $(c+\varepsilon,c+\varepsilon)$ each firm earns half the market at margin $\varepsilon$; cutting to $c$ earns 0 and raising the price sells nothing, so neither deviates. At a common price $c+k\varepsilon$ with $k\ge2$, cutting one tick earns $(k-1)\varepsilon$ on the whole market instead of $k\varepsilon$ on half of it, which pays since $k-1\ge k/2$ and demand is higher at the lower price. Tadelis's cents example gives exactly (10, 10) and (10.01, 10.01).
> The undercut from $c+\varepsilon$ lands on $c$, where profit is zero, so the continuous-price argument breaks at the bottom of the grid; higher up, a one-tick cut does pay. At $(c+\varepsilon,c)$ the firm at $c$ earns 0 and gains by moving up to $c+\varepsilon$ to share the market at a positive margin.
> Ref: Lecture 2 slides 35–38; Tadelis (2013), §5.2.4 (pp. 89–90)

Q: Two Bertrand firms sell a homogeneous good with demand $100-p$; firm 1's unit cost is 1, firm 2's is 2, and ties split the market. Which statement about pure-strategy Nash equilibria is correct?
- With real prices the unique equilibrium is $p_1=p_2=2$, the limit of the cent equilibria as the price grid becomes finer and finer
- With real prices the unique equilibrium is $p_1=p_2=1$, since the low-cost firm sets the price and firm 2 then has to match it
- In whole cents one exists, such as firm 1 at 1.99 and firm 2 at 2.00; with real prices none does, as firm 1 has no best reply to 2
- No equilibrium exists either way, since each firm always wants to undercut the other, and in both cases the undercutting never stops
<!-- YW5zOjI= -->
> With cents, (1.99, 2.00) is an equilibrium: firm 2 cannot sell profitably below its cost of 2, and firm 1 takes the whole market at the highest price that still undercuts. With real prices, against $p_2=2$ firm 1's profit rises as $p_1$ approaches 2 from below and halves at 2, so no best price exists, and Tadelis shows that no profile is an equilibrium.
> The limit (2, 2) is not an equilibrium: firm 1 gains by cutting slightly. At (1, 1) firm 2 sells half the market at a loss and firm 1 could raise its price towards 2. On a grid the undercutting stops at firm 2's cost, so an equilibrium exists there; with real prices the payoff discontinuity at $p_1=p_2$ is what destroys existence.
> Ref: Lecture 2 slides 32–34; Tadelis (2013), §5.2.4 (pp. 91–93)
> Similar: Listas/pratica-lecture-02.md, item 20 (Tadelis 5.12, p. 98)

Q: Why does product differentiation remove the Bertrand paradox, even with two firms choosing prices simultaneously?
- A slightly lower price no longer wins the whole market, so demand is continuous in own price and the best reply stays over cost
- Differentiated products let each firm commit to a capacity first, which turns the price game into a Cournot game played in quantities
- Differentiation makes prices strategic substitutes, so each firm answers a rival's price cut by raising its own price, not matching it
- Differentiated products are sold in separate markets, so each firm becomes a local monopolist and simply sets its own monopoly price
<!-- YW5zOjA= -->
> The paradox comes from the jump in demand when one homogeneous price falls just below the other, which drives undercutting down to cost. With differentiated products each firm keeps some customers when it charges more, its profit is smooth in its own price, and its best reply is an interior price over cost that rises with the rival's price, so equilibrium prices exceed marginal cost.
> Capacity commitment is a different route to Cournot-like outcomes (the slides' 'what is harder to adjust'), not what differentiation does. Prices remain strategic complements. Demand for each product still depends on the rival's price, so neither firm is a monopolist.
> Ref: Lecture 2 slides 39–40; Gibbons (1992), §1.2.B (pp. 21–22); Tadelis (2013), §5.2.4 Remark (p. 93)

## commons

Q: $n$ players share a resource of size $K$; player $i$ consumes $k_i\ge0$ and earns $\ln k_i+\ln(K-\sum_j k_j)$. Which statement about the symmetric Nash equilibrium and the symmetric efficient profile is correct?
- Each consumes $K/(2n)$ in equilibrium and $K/(n+1)$ at the optimum, so with many players too much of the resource is left unused
- Each consumes $K/(n+1)$ in equilibrium and $K/(2n)$ at the optimum, but the gap closes as $n$ grows, since each share becomes negligible
- Each consumes $K/(n+1)$ in equilibrium and at the optimum, since log payoffs make each player internalize the stock she shares
- Each consumes $K/(n+1)$ in equilibrium and $K/(2n)$ at the optimum, so total use $nK/(n+1)$ nears $K$ while efficient use is $K/2$
<!-- YW5zOjM= -->
> Player $i$'s first-order condition $1/k_i=1/(K-\sum_jk_j)$ counts only her own loss from a smaller stock, giving $k_i=K/(n+1)$ in the symmetric equilibrium. A planner maximizing the sum of payoffs counts all $n$ losses, $1/k=n/(K-nk)$, giving $k=K/(2n)$. Total equilibrium use $nK/(n+1)$ tends to $K$ while efficient use stays $K/2$.
> Equilibrium consumption is the larger of the two, not the smaller. The gap widens with $n$, since each player ignores the harm to $n-1$ others. Log payoffs do not make anyone internalize the shared stock: for $n=2$ the equilibrium $K/3$ exceeds the efficient $K/4$.
> Ref: Tadelis (2013), §5.2.2 (pp. 84–87), Exercise 5.7 (p. 96)

## space

Q: Two candidates care only about winning and choose platforms on a line; each voter votes for the nearer platform, ties are settled by a coin, and the five voters' ideal points are 0, 1, 2, 9 and 10. Which profile is the Nash equilibrium?
- Both at 4.4, the mean ideal point, since that platform minimizes the total distance between the voters and the winner
- Both at 2, the median ideal point, since any other platform loses to a rival who stands at the median voter's position
- Both at 5, the midpoint of the range, since only the two extreme voters' positions decide how the others will vote
- One at 1 and one at 9, since each candidate secures one side of the electorate and neither gains by moving inward
<!-- YW5zOjE= -->
> A candidate at the median 2 gets voters 0, 1 and 2 against any rival to the right, and 2, 9 and 10 against any rival to the left, so she beats every other platform; hence the only equilibrium has both at 2, each winning with probability one half. A grid search over platforms confirms it is the unique equilibrium.
> Total distance to the voters is minimized at the median, not the mean, and candidates maximize winning anyway: a rival at 4 beats a candidate at 4.4 by taking 0, 1 and 2. Against a rival at 5, a platform at 4 also wins with 0, 1 and 2. From (1, 9), the candidate at 9 wins by moving to 2, taking 2, 9 and 10.
> Ref: Lecture 1 slides 32–33; Tadelis (2013), §5.2.5 (pp. 93–95)
> Similar: Tadelis (2013), Exercise 5.15 (p. 99); Gibbons (1992), Problem 1.8 (p. 50)

Q: In the Hotelling voting game with 101 citizens at the integers from −50 to +50, two candidates who care only about winning choose integer platforms, and each citizen votes for the nearer one. Candidate 2 stands at +10. What is candidate 1's best response?
- Every platform from −9 to +9, each of which wins outright; the best response is unique only against a rival at −1, 0 or +1
- Only +9, the platform just to the left of the rival, since it captures every voter from −50 up to +9 and maximizes the margin
- Only 0, the median voter's platform, since the median platform beats every other platform in a simple majority vote
- Every platform from −50 to +9, since any platform to the left of the rival wins all of the voters lying to its left
<!-- YW5zOjA= -->
> Against $a_2=+10$, a platform $a_1\in[-9,9]$ wins: the voters up to the midpoint of the two platforms, at least 51 of them, are nearer to $a_1$. $a_1=-10$ ties by symmetry and anything further left loses. Since candidates care only about winning, every winning platform is a best response, and the set collapses to {0} only when the rival stands at −1, 0 or +1.
> A larger margin is worth nothing to a candidate who cares only about winning, so +9 is not the unique best reply, and 0 wins but so do the others. Moving left of −9 gives up the centre: at −10 the candidates tie, and further left candidate 1 loses.
> Ref: Tadelis (2013), §5.2.5 (pp. 93–94), footnote 10 (p. 94)
> Similar: Listas/pratica-lecture-02.md, item 22 (Tadelis 5.15)

Q: In the pharmacy location game the two chains, with fixed and equal prices, both end on the middle block. Why would letting them also choose prices push them apart?
- With prices, the chains can split the market by agreement, and staying apart is the easiest way to enforce such a deal
- With prices, clustering stops being an IESDS outcome, because the middle block is no longer strictly dominant for them
- Sharing a block makes their offers identical, so price competition drives margins to cost, and moving apart softens it
- With prices, total walking distance enters each chain's profit, so each locates to minimize its customers' walking
<!-- YW5zOjI= -->
> With fixed prices the only thing to fight over is customers' location, so the chains crowd the centre. If they also set prices, two stores on the same block sell identical products and Bertrand logic pushes prices to cost; separation gives each store some customers who would rather pay a little more than walk, which lets it charge more.
> No agreement is needed: separation arises as a noncooperative outcome of the one-shot game. The middle block was never strictly dominant; it was the IESDS survivor. Walking distance matters to customers and shapes demand, but the chains maximize profit, not customers' welfare.
> Ref: Lecture 1 slides 32–33; Lecture 2 slide 3; Cabral (2017), §14.2 (pp. 358–360); Tadelis (2013), Exercise 5.16 (p. 99)
