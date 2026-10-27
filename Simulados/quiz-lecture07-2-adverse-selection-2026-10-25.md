---
quiz: "Lecture 7 · Quiz 2 of 3 — Adverse selection, two-sided private information and common values"
tags:
  lemons: "Lemons: unravelling under one-sided private information"
  insurance: "Insurance and credit: the informed buyer"
  double: "The double auction: two-sided private information"
  cv: "Common values: conditioning on the decisive event"
---

## lemons

Q: A seller knows the quality $k \in \{1,\dots,K\}$ of his asset, each equally likely; the buyer does not. The seller values quality $k$ at $v_1+(k-1)s$, with spread $s>0$, and the buyer values it at that plus a premium $\Delta>0$. The buyer makes a take-it-or-leave-it price offer. When can qualities $1$ to $k$ all trade at one price?
- If and only if $\Delta \ge (k-1)s$, so that the premium covers the gap between the lowest and the highest quality
- If and only if $\Delta \ge (k-1)s/2$, so that the pool's mean buyer value covers the price that brings in quality $k$
- If and only if $\Delta \ge ks/2$, so that the pool's mean buyer value covers the price that brings in quality $k+1$
- If and only if $\Delta \ge v_1+(k-1)s/2$, so that the premium covers the mean seller value of the whole pool
<!-- YW5zOjE= -->
> To bring in quality $k$ the price must be at least $v_k = v_1+(k-1)s$. All qualities up to $k$ then accept, and the buyer's mean value of that pool is $v_1+(k-1)s/2+\Delta$. Trade does not lose money iff $\Delta \ge (k-1)s/2$. The level $v_1$ cancels: only the spread of quality that the seller knows about, relative to the gain from trade, decides. Tadelis's grove ($s=10$, $\Delta=4$) fails already at $k=2$, which needs $\Delta \ge 5$.
> Ref: Tadelis (2013), §12.3, Prop. 12.1 (pp. 258–261)
> Similar: Tadelis (2013), Exercise 12.5, pp. 267–268; Exercise 12.6, p. 268

Q: A grove's quality is $L$, $M$ or $H$, equally likely and known only to the seller, who values them at $v_L<v_M<v_H$; the buyer values each at the seller's value plus $\Delta>0$, and $\Delta$ is small enough that only quality $L$ can trade. The buyer makes a take-it-or-leave-it offer. Which prices can be supported as a Bayesian Nash equilibrium price?
- Every $p^* \in [v_L, v_M]$, since any price below $v_M$ is accepted by the lowest quality alone and costs the buyer nothing extra
- Every $p^* \in [v_L, \tfrac12(v_L+v_M)+\Delta]$, the range where the pool of the two lowest qualities is still worth the price
- Every $p^* \in [v_L+\Delta, v_M]$, since the buyer must pay his own value to make the lowest-quality seller willing to accept
- Every $p^* \in [v_L, v_L+\Delta]$, since the lowest quality accepts at or above $v_L$ and the buyer must not lose on it
<!-- YW5zOjM= -->
> Only $L$ trades, so the buyer pays $p^*$ for a grove worth $v_L+\Delta$ to him: he needs $p^* \le v_L+\Delta$, and the $L$ seller needs $p^* \ge v_L$. Any price in that band is supported by strategies in which the $L$ type accepts iff $p \ge p^*$; offers above $p^*$ but below $v_M$ buy the same $L$ for more. With Tadelis's numbers ($v_L=10$, $\Delta=4$) this is $[10,14]$.
> Ref: Tadelis (2013), §12.3, Prop. 12.1 (p. 260)
> Similar: Tadelis (2013), Exercise 12.5, pp. 267–268; MWG (1995), Exercise 13.B.1, p. 473

Q: Every quality of an asset is worth more to the buyer than to the seller, yet only the lowest quality trades. Which two features of the environment produce that outcome?
- The seller's quality enters the buyer's payoff, and the seller has no credible way to reveal it, since every type would claim high quality
- The buyer has all the bargaining power, and he is risk averse, so he refuses to pay more than the lowest value any seller might accept
- The seller's values are private while the buyer's are common knowledge, and the fixed costs of trading exceed the gains on high qualities
- The buyer cannot observe the quality, and he moves first, so any seller who rejects an offer reveals that his grove must be of low quality
<!-- YW5zOjA= -->
> Two things make adverse selection bite. First, common values: the buyer cares who accepts because quality enters his payoff; with private values the identity of the acceptor would not matter. Second, cheap talk does not help: "my soil is good" costs nothing, so every type would say it. A credible, costly revelation of type is signaling, the subject of Lecture 8. Risk aversion and transaction costs play no role in the example.
> Ref: Tadelis (2013), §12.3 (pp. 260–261); Milgrom & Roberts (1992), Ch. 5 (pp. 149–150)
> Similar: Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 7 Ex. 4, p. 331

## insurance

Q: Expected claims $x \sim U[0,\bar x]$ are privately known; a buyer of type $x$ also values risk reduction at $v>0$ and buys at price $P$ iff $P \le x+v$. The insurer pays $1+c$ per unit of claims, $0<c<1$, and breaks even on the pool of buyers. When does the private market break down, and when is mandatory coverage worthwhile?
- Breakdown iff $c\bar x > 2v$; mandatory coverage iff $v > c\bar x$, so the market fails only when insurance is not worth having
- Breakdown iff $v < c\bar x/2$; mandatory coverage iff $v > c\bar x$, so the market fails only when insurance is not worth having
- Breakdown iff $c\bar x > v$; mandatory coverage iff $v > c\bar x/2$, so a band exists where it is efficient but no market survives
- Breakdown iff $(1+c)\bar x/2 > v$; mandatory coverage iff $v > c\bar x/2$, so a band exists where it is efficient but no market survives
<!-- YW5zOjI= -->
> With marginal buyer $x$, the insurer needs $P_s(x) = \tfrac12(x+\bar x)(1+c)$ and the buyer accepts $P_b(x) = x+v$. The gap $P_b-P_s$ rises in $x$ and peaks at $x=\bar x$, where it equals $v-c\bar x$: a market exists iff $v \ge c\bar x$. Covering everyone gives mean benefit $v+\bar x/2$ against mean cost $(1+c)\bar x/2$, worthwhile iff $v > c\bar x/2$. In $c\bar x > v > c\bar x/2$ insurance is efficient and no individual market survives, the case for group insurance.
> Ref: Milgrom & Roberts (1992), Ch. 5, eqs. (5.1)–(5.2) (pp. 150–152)
> Similar: Milgrom & Roberts (1992), Questions 5.3–5.5, pp. 164–165

Q: Safe borrowers repay a loan for sure and earn a modest return; risky borrowers earn a high or a low return and default in the low state. Why can a bank's expected return fall when it raises its loan rate?
- Because a higher rate lowers total loan demand, and the bank's fixed costs are then spread over fewer loans of the same average quality
- Because a higher rate encourages each borrower to switch to a riskier project after borrowing, which raises the default rate of every loan
- Because a higher rate pushes the bank's own funding costs up one for one, so its margin on each loan is unchanged while its volume falls
- Because a higher rate drives the safe borrowers out first, since their return cannot cover it, so the pool of borrowers gets riskier
<!-- YW5zOjM= -->
> The rate is a price that selects the customers. Safe borrowers stop borrowing once the repayment exceeds their sure return; risky borrowers keep borrowing because limited liability caps their loss in the bad state. The pool shifts toward default risk and the bank's expected return can fall: this is credit rationing by adverse selection (Stiglitz–Weiss). The second option is a moral-hazard story, a different mechanism and outside this course's scope.
> Ref: Milgrom & Roberts (1992), Ch. 5 (p. 153); Cabral (2017), §7.4 (pp. 174–176)
> Similar: Cabral (2017), Exercises 7.9 and 7.10, pp. 180–181

## double

Q: A seller with value $v_s$ and a buyer with value $v_b$, independent $U[0,1]$ and private, simultaneously name an ask $p_s$ and an offer $p_b$; they trade at $(p_s+p_b)/2$ if $p_b \ge p_s$. In the linear Bayesian Nash equilibrium, what are the strategies, and when does trade occur?
- $p_b = \tfrac23 v_b + \tfrac14$ and $p_s = \tfrac23 v_s + \tfrac1{12}$, so trade occurs if and only if $v_b \ge v_s - \tfrac14$
- $p_b = \tfrac23 v_b + \tfrac1{12}$ and $p_s = \tfrac23 v_s + \tfrac14$, so trade occurs if and only if $v_b \ge v_s + \tfrac14$
- $p_b = \tfrac12 v_b + \tfrac18$ and $p_s = \tfrac12 v_s + \tfrac38$, so trade occurs if and only if $v_b \ge v_s + \tfrac12$
- $p_b = v_b$ and $p_s = v_s$, by the dominance argument of sealed bids, so trade occurs if and only if $v_b \ge v_s$
<!-- YW5zOjE= -->
> Against a linear seller the buyer's condition gives $p_b = \tfrac23 v_b + \tfrac13 a_s$, and against a linear buyer the seller's gives $p_s = \tfrac23 v_s + \tfrac13(a_b+c_b)$. The fixed point is $a_s = \tfrac14$, $a_b = \tfrac1{12}$. Then $p_b \ge p_s$ iff $\tfrac23(v_b-v_s) \ge \tfrac16$, i.e. $v_b \ge v_s+\tfrac14$. Truthful bidding fails because each side's own price moves the trading price.
> Ref: Gibbons (1992), §3.2.C, eqs. (3.2.5)–(3.2.8) (pp. 158–161)
> Similar: Gibbons (1992), Problem 3.8, pp. 171–172

Q: In a double auction between a seller and a buyer (independent $U[0,1]$ values, trade at the average of ask and offer when the offer is at least the ask), consider the one-price equilibrium at $x \in [0,1]$: the buyer offers $x$ iff $v_b \ge x$, the seller asks $x$ iff $v_s \le x$. What are the expected gains from trade, and how do they compare with the efficient benchmark?
- $x(1-x)/2$, maximized at $x=\tfrac12$ with $\tfrac18$, short of the efficient $\tfrac16$ of trading whenever $v_b \ge v_s$
- $x(1-x)$, maximized at $x=\tfrac12$ with $\tfrac14$, above the linear equilibrium's level since every trade at $x$ is profitable
- $x(1-x)/2$, maximized at $x=\tfrac12$ with $\tfrac18$, equal to the efficient level since every trade at $x$ has $v_b \ge v_s$
- $(1-x)^2/2$, maximized at $x=0$ with $\tfrac12$, the efficient level, since at $x=0$ every buyer is willing to make an offer
<!-- YW5zOjA= -->
> Trade happens iff $v_s \le x \le v_b$, so the gains are $\int_0^x\int_x^1 (v_b-v_s)\,dv_b\,dv_s = x(1-x)\big[\tfrac{1+x}{2}-\tfrac x2\big] = x(1-x)/2$, at most $\tfrac18$. The efficient benchmark integrates over the whole triangle $v_b \ge v_s$ and gives $\tfrac16$; the linear equilibrium reaches $\tfrac9{64}$. Every trade at $x$ is efficient, but many efficient trades (both values above, or both below, $x$) are missed.
> Ref: Gibbons (1992), §3.2.C, Fig. 3.2.1 (pp. 159–160)
> Similar: Gibbons (1992), Problem 3.8, pp. 171–172

## cv

Q: Two jurors vote to acquit or convict, and conviction needs both votes. The defendant is guilty with prior $q>\tfrac12$; each juror privately sees a signal that is correct with probability $p>\tfrac12$, independently given the truth. Juror $j$ convicts iff his signal says guilty. What is juror $i$'s posterior of guilt when his own signal says innocent and he conditions on being pivotal?
- $\frac{q(1-p)}{q(1-p)+(1-q)p}$, his posterior from his own signal alone, below $\tfrac12$ when $p>q$, so he acquits
- $\frac{qp^2}{qp^2+(1-q)(1-p)^2}$, the posterior after two guilty signals, above $q$, so he convicts
- $q$, since the pivotal event means $j$ saw a guilty signal, which cancels his own, so he convicts
- $\tfrac12$, since the pivotal event means $j$ saw a guilty signal, which cancels his own, so he is indifferent
<!-- YW5zOjI= -->
> Under unanimity $i$'s vote matters only if $j$ votes to convict, i.e. if $j$'s signal said guilty. Then $\Pr\{G \mid \theta_I, \theta_G\} = \frac{q(1-p)p}{q(1-p)p+(1-q)p(1-p)} = q > \tfrac12$: the two opposite signals cancel and leave the prior, which favours conviction. So voting one's signal is not a best response to itself: the swing voter's curse. The first option ignores the information in being pivotal.
> Ref: Tadelis (2013), §12.4 (pp. 261–264)
> Similar: Tadelis (2013), Exercise 12.8, pp. 268–269

Q: A single juror decides alone. The defendant is guilty with prior $q>\tfrac12$, the juror's private signal is correct with probability $p>\tfrac12$, and he earns $1$ for the right verdict and $0$ for the wrong one. When does he follow his signal, convicting after a guilty signal and acquitting after an innocent one?
- If and only if $p>\tfrac12$, since any informative signal moves the posterior in the direction the signal points
- If and only if $p>q$, since only then does the innocent signal bring the posterior of guilt below $\tfrac12$
- If and only if $p>1-q$, since only then does the innocent signal bring the posterior of guilt below $\tfrac12$
- If and only if $p^2>q$, since only then does the innocent signal bring the posterior of guilt below $\tfrac12$
<!-- YW5zOjE= -->
> After an innocent signal, $\Pr\{G\mid\theta_I\} = \frac{q(1-p)}{q(1-p)+(1-q)p}$, which is below $\tfrac12$ iff $q(1-p) < (1-q)p$, i.e. iff $q<p$. After a guilty signal the posterior rises above $q>\tfrac12$, so convicting is right anyway. An informative signal always moves the posterior, but it must move it past $\tfrac12$ to change the verdict; with $p \le q$ the juror convicts whatever he sees.
> Ref: Tadelis (2013), §12.4 (p. 262)
> Similar: Tadelis (2013), Exercise 12.8, pp. 268–269

Q: A buyer offering a price for a used asset, a juror voting under unanimity, and a bidder in a common-value auction all face one common trap. What is it?
- Each faces a rival with more bargaining power, so the price, the verdict or the bid is set by the other side's private interest
- Each has private values, so the information held by the others changes what they do but never what the outcome is worth
- Each is risk averse, so the variance of the outcome, and not its expected value, is what decides the best action in each case
- Each matters only in an event that is news about value: acceptance, a convicting partner, winning; the choice must condition on it
<!-- YW5zOjM= -->
> The seller accepts only when quality is below the price; the other juror convicts only when his signal said guilty; a bidder wins only when the rival's signal was lower. In each case the naive choice (pay the average, vote the signal, bid the expected value) is optimal for a decision taken alone and fails in the game, because it ignores Bayes' rule applied to the decisive event. All three are common-value settings; with private values there is no curse.
> Ref: Tadelis (2013), §12.3 (pp. 258–261), §12.4 (pp. 261–264), §13.2 (pp. 282–284)
> Similar: Tadelis (2013), Exercises 12.8 (pp. 268–269) and 13.10 (p. 287)
