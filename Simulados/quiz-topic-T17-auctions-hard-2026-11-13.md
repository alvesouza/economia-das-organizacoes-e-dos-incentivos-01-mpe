---
quiz: "Topic T17 · Auctions — hard conceptual quiz (10 questions; estimated unit, no slides: Tadelis Ch. 13, Gibbons §3.2.B, Cabral §6.4)"
tags:
  spa: "Second-price auctions and weak dominance"
  fpa: "First-price auctions and bid shading"
  rev: "Revenue equivalence and its assumptions"
  wc: "Common values and the winner's curse"
---

## spa

Q: In a second-price sealed-bid auction, bidding one's value is weakly dominant under independent private values. Which modification removes that property?
- Making the object's value common, so that each bidder's value depends on the signals the rivals hold, which his bid cannot condition on
- Adding a reserve price below which the object is not sold, so that a bidder must also weigh the chance of no sale against that of winning
- Letting private values be correlated across bidders, so that a bidder's own value is informative about the bids the rivals will submit
- Dropping the common prior, so that a bidder no longer knows the distribution of the rivals' values and cannot compute his odds of winning
<!-- YW5zOjA= -->
> The dominance argument compares bids pointwise in the highest rival bid: your bid decides only whether you win, never what you pay, and bidding your value wins exactly when the price is below it. That needs you to know your value. With a reserve price the same pointwise comparison goes through (the reserve acts as one more rival bid). Correlation and the absence of a common prior do not matter either: Tadelis stresses that the argument uses no beliefs about rivals and survives correlated private values. With common values your value depends on what the rivals know, so "your value" is not something you can bid, and bidding $E[v \mid \theta_i]$ even loses money in Tadelis's oil-field example.
> Ref: Tadelis (2013), §13.1.1, Prop. 13.1 and the remarks after its proof (pp. 273–274); §13.2 (pp. 282–284)
> Similar: Tadelis (2013), Exercise 13.1, p. 285

Q: Under complete information, two bidders with values 10 and 6 play a second-price sealed-bid auction. Consider the profile in which the value-10 bidder bids 0 and the value-6 bidder bids 100. What does this profile show?
- Nothing new: it is not a Nash equilibrium, since the value-10 bidder gains by outbidding the rival, so play collapses back to truthful bidding by both
- That weak dominance is special to the uniform case: with values known to all the auction has no dominant strategy, so any bid can be a best reply
- That truthful bidding, though weakly dominant, is not the only equilibrium: this profile is a Nash equilibrium with the wrong winner and zero revenue
- That second-price auctions are inefficient under complete information, since with known values each bidder bids the other's value and the low one wins
<!-- YW5zOjI= -->
> The value-6 bidder wins and pays the rival's bid, 0, earning 6, which he cannot improve on. To win, the value-10 bidder must bid above 100 and pay 100, a loss of 90; losing gives 0, so bidding 0 is a best reply. So this is a Nash equilibrium: the object goes to the lower value and the seller gets nothing. It rests on the weakly dominated bid 100 > 6. Weak dominance selects the truthful equilibrium; it does not make it unique. Bidding one's value stays weakly dominant with known values (the proof never uses the distribution), and in the truthful equilibrium the high-value bidder wins, so the auction is not inherently inefficient.
> Ref: Tadelis (2013), §13.1.1 (pp. 273–274), Exercise 13.2 (p. 285)
> Similar: Tadelis (2013), Exercise 13.2, p. 285

## fpa

Q: With $n$ risk-neutral bidders whose private values are independent and identically distributed, which interpretation of the symmetric first-price equilibrium bid $b(\theta)$ is correct?
- $b(\theta)$ is the unconditional expected value of the highest rival value, so every type bids the same expected price and differs only in whether it wins
- $b(\theta)$ is the expected highest rival value given that it lies below $\theta$, what type $\theta$ would expect to pay in a second-price auction if it won
- $b(\theta)$ is the expected second-highest value among all $n$ bidders, so the winner's bid in a first-price auction equals the second-price revenue in every draw
- $b(\theta)$ is $\theta$ minus type $\theta$'s expected surplus, so the amount shaded equals what the bidder expects to earn and shrinks as $\theta$ rises
<!-- YW5zOjE= -->
> With $Y$ the highest of the $n-1$ rival values, $b(\theta) = E[Y \mid Y < \theta]$: the first-price bid is the expected second-price payment conditional on winning, which is why revenue equivalence holds type by type. Uniform check: $E[Y \mid Y<\theta] = \frac{n-1}{n}\theta$, the familiar bid. The unconditional mean of $Y$ does not depend on $\theta$, so it cannot be an increasing bid. The expected second-highest value of all $n$ is the seller's expected revenue, $\frac{n-1}{n+1}$ in the uniform case; revenues agree only in expectation, not draw by draw. The last option fails on the uniform case: the expected surplus is $\theta^n/n$, not the shading $\theta/n$, and the shading rises with $\theta$.
> Ref: Tadelis (2013), §13.1.3, eqs. 13.1–13.8 (pp. 276–279) and §13.1.4 (pp. 279–282); Gibbons (1992), §3.2.B and Appendix 3.2.B (pp. 155–158)
> Similar: Tadelis (2013), Exercise 13.9 "Private Value Linear Bidding", p. 287

Q: Two bidders in a first-price auction have private values 4 or 8, each with probability 1/2, independently. The low type bids 4, and a textbook proposes that the high type mixes uniformly on $[4, 6]$. Why is that not an equilibrium?
- Because the high type should bid $6$ for sure: with the low type pinned at $4$, a bid below $6$ risks losing to a rival high type and is dominated by $6$
- Because the low type would deviate: against a high type mixing on $[4, 6]$, a low bid slightly above $4$ wins more often and earns a positive surplus
- Because the support is wrong: a high type bidding just above $4$ earns $2$ while one bidding $6$ earns less, so the support must stop well below $6$
- Because the high type is not indifferent: a bid of $5$ wins with probability $3/4$ and earns $9/4$, above the $2$ at each end; $G(b)=(b-4)/(8-b)$ is right
<!-- YW5zOjM= -->
> A high type bidding $b \in (4,6]$ beats every low rival and a high rival who bids less, so with the uniform cdf $(b-4)/2$ it earns $(8-b)\big(\tfrac12 + \tfrac12\cdot\tfrac{b-4}{2}\big) = (8-b)(b-2)/4$: 2 at both ends but $3 \cdot \tfrac34 = \tfrac94$ at $b=5$. A mixed strategy needs equal payoffs on its support, and $(8-b)\big(\tfrac12+\tfrac12 G(b)\big) = 2$ gives $G(b) = (b-4)/(8-b)$, whose revenue is 5, the English auction's. Tadelis's part (c) asks to show the uniform works; it does not. A pure bid 6 earns 2 but a pure high bid is undercut by a rival high type, which is why mixing is needed. A low type bidding above 4 pays more than its value. A bid of 6 wins for sure and earns exactly 2, not less.
> Ref: Tadelis (2013), §13.1.3 (pp. 276–279), Exercise 13.5 (p. 286); project errata note `.agent/notes/errata-game-theory-books.md`; worked solution in `Listas/pratica-lecture-07-solutions.pdf` (Tadelis 13.5)
> Similar: Tadelis (2013), Exercise 13.5, p. 286

## rev

Q: Bidders have independent private values but are risk averse; everything else satisfies the revenue equivalence theorem. How do the first- and second-price sealed-bid auctions rank in expected revenue?
- They still tie, because risk aversion lowers bids in both formats by the same risk premium, so the expected price falls equally in the two auctions
- The second-price one raises more, because risk-averse bidders fear overpaying and bid below value in it, but shade less there than in the first-price one
- The first-price one raises more, because bidding one's value stays dominant in the second-price one, while risk-averse bidders shade less to avoid losing
- The first-price one raises less, because a risk-averse bidder dislikes paying his own bid when he wins and shades more to protect his surplus in that event
<!-- YW5zOjI= -->
> Risk neutrality is condition 2 of Tadelis's statement. In the second-price auction the dominance argument never uses attitudes to risk, so bids stay at values and revenue is unchanged. In the first-price auction shading trades a larger margin against a higher risk of losing, and a risk-averse bidder buys insurance against losing by shading less, so bids and revenue rise. Tadelis's Exercise 13.7 makes this concrete: the equilibrium bid share rises above $\frac{n-1}{n}$. The "same risk premium" story fails because there is no risk premium in a dominant-strategy bid; the other two options reverse the direction of the first-price effect.
> Ref: Tadelis (2013), §13.1.4, the four conditions and footnote 7 (p. 280), Exercise 13.7 (p. 287)
> Similar: Tadelis (2013), Exercise 13.7, p. 287

Q: Two bidders have independent private values, but one's values are drawn from a distribution that favours higher values than the other's. Why can the first- and second-price auctions then yield different expected revenues?
- Because in the first-price auction the two shade differently, so the lower-value bidder sometimes wins and the highest type need not get the object
- Because the second-price auction loses its dominant strategy: the weaker bidder must now bid above its value to have any chance against the stronger bidder
- Because the lowest type of the weaker bidder earns a positive expected payoff, which breaks the condition that the lowest possible type expects zero surplus
- Because asymmetric bidders are in effect risk averse, since each faces a rival whose bids are more spread out, which breaks the condition of risk neutrality
<!-- YW5zOjA= -->
> Revenue equivalence compares formats that allocate the object the same way. In the second-price auction everyone still bids his value, so the higher value wins. In the first-price auction the weak bidder, facing a strong rival, bids more aggressively relative to its value than the strong one, so for some draws the lower value wins: Tadelis's condition 3, that the highest type wins, fails. Dominance in the second-price auction never depends on the rivals' distribution. The lowest type of each bidder never wins, so it still earns zero. Asymmetry in distributions has nothing to do with the bidders' attitude to risk.
> Ref: Tadelis (2013), §13.1.4, condition 3 (p. 280); §13.1.1, Prop. 13.1 (pp. 273–274)
> Similar: Tadelis (2013), Exercise 13.6 "Third-Price Sealed-Bid Auction", pp. 286–287

Q: A seller adds the same reserve price $r>0$ to a first-price and to a second-price sealed-bid auction with independent private values and risk-neutral bidders. Which statement about their expected revenues is correct?
- They now differ, because the reserve binds only in the second-price auction, where it replaces the second-highest bid whenever that bid falls below $r$
- They now differ, because some draws leave the object unsold, which breaks the condition that the highest type wins and so voids revenue equivalence
- They now differ, because a reserve makes bidders in the first-price auction shade less, while bids in the second-price auction stay at value as before
- They stay equal, because both formats still sell to the highest value above $r$ and give the lowest type zero, even if the reserve changes both revenues
<!-- YW5zOjM= -->
> What revenue equivalence needs is that the two formats share the allocation rule and the lowest type's payoff (Myerson's general version, of which Tadelis's four conditions are the no-reserve case). With a common reserve both formats sell iff the highest value is at least $r$, to that bidder, and a bidder of the lowest type gets zero in both, so their expected revenues stay equal to each other, although the reserve moves both away from the no-reserve level. Reading condition 3 literally ("the highest type wins") makes the second option tempting, but the comparison is between two auctions with the same unsold draws. The reserve binds in the first-price auction too: no bid below $r$ is accepted, and bidders just above $r$ bid close to it. A reserve does change first-price shading, but revenue equivalence is precisely the statement that such changes wash out in expectation.
> Ref: Tadelis (2013), §13.1.4, the four conditions and the Vickrey–Myerson–Riley–Samuelson attribution (p. 280); note `Notas/L07/L07-08-revenue-equivalence.md` §1, §6
> Similar: Tadelis (2013), Exercises 13.3–13.4 "Reserve Prices", pp. 285–286

## wc

Q: Which statement about the winner's curse in a common-value auction is correct?
- In equilibrium the winner pays more than the object's value on average, which is why experienced bidders tend to stay away from common-value auctions
- In equilibrium bidders shade below their value given their own signal, and the winner does not overpay on average; the curse hits those who ignore it
- It arises only in first-price auctions, because in a second-price auction the winner pays the rival's bid, which already corrects the winner's optimism
- It arises whenever there are many bidders, even with private values, because the winner of a large auction is likely to hold the most extreme value
<!-- YW5zOjE= -->
> Winning tells a bidder that his signal was the most optimistic, which is bad news about a common value. A bidder who conditions on that event, as an equilibrium bidder does, bids below $E[v \mid \theta_i]$ and does not lose on average; the curse is the loss of one who bids his signal-based estimate (in Tadelis's oil field, $-1.25$ for a low-signal firm bidding 15). Tadelis notes it exists in both first- and second-price formats. With private values winning carries no news about one's own value, so no curse arises however many bidders there are.
> Ref: Tadelis (2013), §13.2 (pp. 282–284), the definition of the curse and the remark on both formats (p. 284); Cabral (2017), §6.4 (p. 142)
> Similar: Tadelis (2013), Exercise 13.8, p. 287

Q: Holding fixed a bidder's own signal, how does the number of rivals affect the winner's-curse correction he must apply to his signal-based estimate in a common-value auction, and how does that compare with private values?
- More rivals call for less correction in both settings, because competition pushes every bid closer to the bidder's own estimate of the object's value
- More rivals matter only with private values, because in a common-value auction the object is worth the same to everyone and so is the right bid
- With common values more rivals call for a larger correction, since winning means beating more signals; with private values a win carries no such news
- More rivals call for a smaller correction with common values, since a larger sample of rival signals makes the winner's own estimate more precise
<!-- YW5zOjI= -->
> The correction is the gap between $E[v \mid \theta_i]$ and the value conditional on winning, which conditions on every rival signal being lower. Beating more rivals is worse news, so the gap grows with their number. A check with a value of 0 or 1, equally likely, and signals with density $2s$ if it is 1 and $2(1-s)$ if it is 0: at signal 0.8 the estimate is 0.8 on the signal alone, but given that every rival signal is lower it is 0.73 with one rival, 0.64 with two and 0.44 with four. With private values winning says nothing about one's own value, so there is no correction to make; more rivals then only reduce first-price shading. The winner does not learn the rival signals, so a larger sample sharpens nothing for him; and a common value does not imply a common bid, since bids depend on signals.
> Ref: Tadelis (2013), §13.2 (p. 284: in equilibrium players must condition on "their signal is higher than everyone else's"); Cabral (2017), §6.4 (p. 142)
> Similar: Tadelis (2013), Exercise 13.10, p. 287

Q: With private values, the English auction and the second-price sealed-bid auction give the same outcome. With common values, which statement is correct?
- With three or more bidders they can differ, because in the English auction those still in see the prices at which others quit and infer their signals
- They still give the same outcome, because both make the winner pay the second-highest bid, and that payment rule alone fixes who wins and what is paid
- They differ even with two bidders, because in the English auction each bidder sees the other stay in and keeps revising his estimate as the price rises
- They differ only if bidders are risk averse, because the open format lets a bidder stop at a price he is sure of, which the sealed format does not allow
<!-- YW5zOjA= -->
> Proposition 13.2's equivalence uses private values: then no one cares what the others know. With common values a quit reveals the quitter's signal, and the bidders still in should use it. With two bidders, though, the first exit ends the auction, and "the rival is still in" is already the event a sealed-bid strategy conditions on at each price, so the two formats coincide; only with three or more bidders does information arrive in time to matter. The payment rule alone does not fix bids when values are common, and risk attitudes are beside the point here.
> Ref: Tadelis (2013), §13.1.2, Prop. 13.2 (pp. 275–276); §13.2 (p. 284, pointing to Krishna 2002 and Milgrom 2004); note `Notas/L07/L07-09-common-values-curses.md` §2.4
> Similar: Tadelis (2013), Exercise 13.10, p. 287
