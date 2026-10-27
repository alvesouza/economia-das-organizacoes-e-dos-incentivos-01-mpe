---
quiz: "Lecture 7 · Quiz 3 of 3 — Auctions: formats, bidding, revenue and the winner's curse"
tags:
  spa: "Second-price and English auctions"
  fpa: "First-price and Dutch auctions"
  rev: "Revenue equivalence"
  wc: "Common values and the winner's curse"
---

## spa

Q: In a second-price sealed-bid auction with private values, a bidder of value $\theta_i$ considers bidding $b_i<\theta_i$ instead of $\theta_i$. Let $b^*$ be the highest rival bid. For which $b^*$ do the two bids give different payoffs, and how?
- Only for $b^*<b_i$, where both bids win but the underbid pays $\theta_i-b_i$ instead of the larger $\theta_i-b^*$
- Only for $b^*>\theta_i$, where the underbid loses while the truthful bid wins and pays $b^*$, more than $\theta_i$
- For every $b^*<\theta_i$, where the truthful bid pays $\theta_i-b^*$ and the underbid pays $\theta_i-b_i$ when it wins
- Only for $b_i<b^*<\theta_i$, where the truthful bid wins $\theta_i-b^*>0$ and the underbid loses, earning zero
<!-- YW5zOjM= -->
> The price is set by $b^*$, not by $b_i$, so the bid decides only whether $i$ wins. If $b^*<b_i$ both bids win at $b^*$; if $b^*>\theta_i$ both lose. Only in between does truthful bidding win, at a positive margin $\theta_i-b^*$, where the underbid forfeits it. Never worse, sometimes strictly better: weak dominance. Overbidding is the mirror image, winning at a loss when $\theta_i<b^*<b_i$.
> Ref: Tadelis (2013), §13.1.1, Prop. 13.1, Fig. 13.1 (pp. 272–274)
> Similar: Tadelis (2013), Exercise 13.1, p. 285; Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 8 Ex. 4, p. 362

Q: Bidding one's value is weakly dominant in the second-price sealed-bid auction with independent private values. What does that dominance buy that an ordinary Bayesian Nash equilibrium would not?
- It makes truthful bidding the unique Bayesian Nash equilibrium, so no other profile of bid functions can be an equilibrium of the auction
- It needs no beliefs about the rivals' distributions or strategies, so it survives dropping the common prior and correlated private values
- It extends to common values, so bidding one's own estimate of the object stays optimal however the bidders' signals are correlated
- It raises the seller's expected revenue above the first-price auction, since no bidder shades and every bid equals the bidder's value
<!-- YW5zOjE= -->
> A weakly dominant strategy is a best response to every rival behaviour, so the bidder need not know $F_j$ or the others' strategies: the common prior can be dropped, and correlation of private values does no harm. It also gives efficiency, since the highest value wins. It does not give uniqueness (other equilibria built on dominated bids can exist), it fails with common values (the winner's curse), and revenue equals the first-price revenue under revenue equivalence.
> Ref: Tadelis (2013), §13.1.1 (p. 274), §13.1.4 (pp. 279–282), §13.2 (pp. 282–284)
> Similar: Tadelis (2013), Exercise 13.2, p. 285

## fpa

Q: In a first-price sealed-bid auction, $n$ symmetric risk-neutral bidders have private values drawn independently from a c.d.f. $F$ on $[\underline\theta,\overline\theta]$, with $F(\underline\theta)=0$. What is the symmetric increasing Bayesian Nash equilibrium bid?
- $s(\theta)=\theta-\int_{\underline\theta}^{\theta}[F(x)]^{n}dx\,/\,[F(\theta)]^{n}$, the expected highest of all $n$ values below $\theta$
- $s(\theta)=\theta-\int_{\underline\theta}^{\theta}[F(x)]^{n-1}dx$, the value minus the area under the rivals' c.d.f. up to $\theta$
- $s(\theta)=\theta-\int_{\underline\theta}^{\theta}[F(x)]^{n-1}dx\,/\,[F(\theta)]^{n-1}$, the expected highest rival value below $\theta$
- $s(\theta)=\int_{\underline\theta}^{\theta}[F(x)]^{n-1}dx\,/\,[F(\theta)]^{n-1}$, the shading itself, which grows with the value $\theta$
<!-- YW5zOjI= -->
> Type $\theta$ maximizes $[F(s^{-1}(b))]^{n-1}(\theta-b)$. Imposing $b=s(\theta)$ in the first-order condition gives $\frac{d}{d\theta}\big([F(\theta)]^{n-1}s(\theta)\big) = (n-1)[F(\theta)]^{n-2}f(\theta)\theta$; integrating from $\underline\theta$ and by parts yields (13.7). The subtracted term divided by $[F(\theta)]^{n-1}$ makes the bid $E[Y\mid Y<\theta]$, where $Y$ is the highest of the $n-1$ rival values; without the division the bid is not even below $\theta$ by the right amount.
> Ref: Tadelis (2013), §13.1.3, eqs. (13.2)–(13.7) (pp. 277–278)
> Similar: Tadelis (2013), Exercise 13.6, pp. 286–287; Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 8 Ex. 3, p. 355

Q: With $n$ bidders whose private values are independent $U[0,1]$, what is the symmetric equilibrium bid of the first-price auction, and what is the expected surplus of a bidder with value $\theta$?
- $s(\theta)=\frac{n-1}{n}\theta$, and the expected surplus is $\theta^{n}/n$, the win probability $\theta^{n-1}$ times the margin $\theta/n$
- $s(\theta)=\frac{n-1}{n}\theta$, and the expected surplus is $\theta^{n-1}/n$, the margin $\theta/n$ times the probability $\theta^{n-2}$
- $s(\theta)=\frac{n}{n+1}\theta$, and the expected surplus is $\theta^{n+1}/(n+1)$, the win probability $\theta^{n}$ times its margin
- $s(\theta)=\theta/n$, and the expected surplus is $\frac{n-1}{n}\theta^{n}$, the win probability $\theta^{n-1}$ times the margin
<!-- YW5zOjA= -->
> With $F(x)=x$, $\int_0^\theta x^{n-1}dx/\theta^{n-1} = \theta/n$, so $s(\theta)=\theta-\theta/n=\frac{n-1}{n}\theta$. The bidder wins iff all $n-1$ rival values are below $\theta$, with probability $\theta^{n-1}$, and keeps $\theta-s(\theta)=\theta/n$. The last option inverts bid and shading. Gibbons's two-bidder case is $b=v/2$.
> Ref: Tadelis (2013), §13.1.3, eq. (13.8) (p. 279); Gibbons (1992), §3.2.B (pp. 155–158)
> Similar: Gibbons (1992), Problem 3.6, p. 170; Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 8 Ex. 1, p. 350

Q: How are the Dutch and English auctions related to the two sealed-bid formats?
- Dutch and second-price are strategically equivalent in any setting; English and first-price have the same outcome only with private values
- Dutch and first-price are strategically equivalent in any setting; English and second-price have the same outcome only with private values
- Dutch and first-price have the same outcome only with private values; English and second-price are strategically equivalent in any setting
- Dutch and first-price are strategically equivalent only with common values; English and second-price have the same outcome in any setting
<!-- YW5zOjE= -->
> In a falling-price auction the only news, that someone shouted, ends the auction, so a strategy is just a stopping price and the highest one wins and pays it: the first-price normal form. In the English auction bidders do see others quit; with private values that changes nothing, so the outcome matches the second-price auction, but with common values the quitting prices reveal signals and the two formats come apart.
> Ref: Tadelis (2013), §13.1.2, Prop. 13.2 (pp. 275–276), §13.1.3 (p. 279), §13.2 (p. 284)
> Similar: Tadelis (2013), Exercise 13.3, pp. 285–286

## rev

Q: With $n$ risk-neutral bidders whose private values are independent $U[0,1]$, what is the seller's expected revenue in the first-price and in the second-price sealed-bid auctions?
- $\frac{n}{n+1}$ in both formats, the expected highest value, since the highest-value bidder always wins the object
- $\frac{n-1}{n+1}$ in the second-price and $\frac{(n-1)^2}{n(n+1)}$ in the first-price, since first-price bids are shaded
- $\frac{n-1}{n}$ in both formats, the shading factor, since the price is the highest bid scaled down by that factor
- $\frac{n-1}{n+1}$ in both formats, as the expected second-highest value equals the expected highest shaded bid
<!-- YW5zOjM= -->
> The second-highest of $n$ uniform values has c.d.f. $nx^{n-1}-(n-1)x^n$ and mean $\frac{n-1}{n+1}$. Bids $\frac{n-1}{n}\theta$ make the highest bid $\frac{n-1}{n}$ times the highest value, whose mean is $\frac{n}{n+1}$, giving again $\frac{n-1}{n+1}$. The second option applies the shading factor to the second-highest value instead of the highest. Revenue rises with $n$ toward $1$.
> Ref: Tadelis (2013), §13.1.4, eqs. (13.9)–(13.10) (pp. 280–282)
> Similar: Tadelis (2013), Exercise 13.5, p. 286; Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 8 Ex. 3, p. 355

Q: A bidder with value $\theta$ faces $n-1$ rivals with independent $U[0,1]$ private values, all bidding their equilibrium strategies. What is his expected payment in the first-price and in the second-price auction?
- $\frac{n-1}{n}\theta^{n}$ in both formats, his win probability $\theta^{n-1}$ times his expected payment when he wins
- $\frac{n-1}{n}\theta^{n}$ in the first-price and $\frac{n-1}{n+1}\theta^{n}$ in the second-price, which pays less
- $\theta^{n}/n$ in both formats, his win probability $\theta^{n-1}$ times his expected payment when he wins
- $\frac{n-1}{n}\theta$ in both formats, the first-price bid, which is also the second-price payment on winning
<!-- YW5zOjA= -->
> He wins iff the highest rival value $Y$ is below $\theta$, with probability $\theta^{n-1}$. In the first-price auction he then pays $\frac{n-1}{n}\theta$; in the second-price auction he pays $Y$, and $\int_0^\theta y(n-1)y^{n-2}dy = \frac{n-1}{n}\theta^n$. The payments agree type by type, so the surplus $\theta^n/n$ (the third option's expression) agrees too. Averaging over $\theta$ and multiplying by $n$ gives the revenue $\frac{n-1}{n+1}$.
> Ref: Tadelis (2013), §13.1.4 (pp. 279–282)
> Similar: Tadelis (2013), Exercise 13.5, p. 286; Exercise 13.6, pp. 286–287

Q: Bidders are risk neutral with independent $U[0,1]$ private values, but the seller is risk averse. Which sealed-bid format should the seller choose, and why?
- The second-price, since its price equals a bidder's value and so carries no strategic shading risk for the seller
- Neither, since revenue equivalence makes the two price distributions identical and the seller is therefore indifferent
- The first-price, since both prices have the same mean, and the highest shaded bid is less dispersed than the second value
- The second-price, since dominant-strategy bidding raises the expected price above the first-price auction's expected price
<!-- YW5zOjI= -->
> Revenue equivalence fixes the mean, not the distribution. The first-price price is $\frac{n-1}{n}$ times the highest value and never exceeds $\frac{n-1}{n}$; the second-price price ranges over the whole support. At $n=2$ their variances are $\tfrac1{72}$ and $\tfrac1{18}$. A risk-averse seller who cares about variance prefers the first-price format.
> Ref: Tadelis (2013), §13.1.4 (pp. 279–282)
> Similar: Tadelis (2013), Exercise 13.7, p. 287

## wc

Q: An oil field has a common value $v$ to two firms. Each firm sees a private signal, low or high, correlated through $v$. In a second-price auction firm 2 bids $E[v \mid \theta_2]$, its expected value given its own signal. Why is bidding $E[v \mid \theta_1 = L]$ not a best response for firm 1 with a low signal?
- Because firm 2 always outbids it, so firm 1 never wins and would gain by bidding above $E[v\mid\theta_1=L]$
- Because bidding one's value is weakly dominant, so firm 1 should bid the highest possible $v$, not $E[v\mid\theta_1=L]$
- Because ties at $E[v\mid\theta_1=L]$ are broken against firm 1, so it wins less often than its expected value warrants
- Because it wins only if $\theta_2 = L$ too, so its value given winning is $E[v\mid LL]$, below the price $E[v\mid\theta_1=L]$
<!-- YW5zOjM= -->
> Firm 1 with $L$ wins (or ties) only when firm 2 also saw $L$ and bid the same amount. In that event both signals were low and the value is $E[v\mid LL] < E[v\mid L]$. In Tadelis's example ($v = 10, 20, 30$ with probabilities $\tfrac14,\tfrac12,\tfrac14$) this gives $-1.25$ in expectation. The truthful-bidding argument of private values does not apply: winning is itself news that the rival's signal was low.
> Ref: Tadelis (2013), §13.2 (pp. 282–284)
> Similar: Tadelis (2013), Exercises 13.8 and 13.10, p. 287

Q: A domestic operator and a foreign one bid for a spectrum licence whose value is common to both; the domestic firm is better informed. How should the foreign firm bid, relative to its own estimate of the value?
- It should shade more, since when it wins it is likely that the informed rival bid low because the value is low
- It should bid its estimate, since the rival's better information affects how the rival bids but not the licence's value
- It should bid above its estimate, since the informed rival will bid high and the foreign firm must outbid it to win
- It should not bid at all, since a less informed bidder can never earn a positive expected payoff in any such auction
<!-- YW5zOjA= -->
> With common values, winning against a better-informed rival is bad news: it happens mostly when that rival's information said the licence is worth little. The uninformed bidder corrects by shading more and wins less often; experienced bidders learn this. Cabral notes that US offshore oil leases are most often won by the firm already drilling the adjacent tract, the better-informed bidder. Shading need not mean abstaining: a low enough bid still earns a non-negative expected payoff.
> Ref: Cabral (2017), §6.4 (p. 142); Tadelis (2013), §13.2 (p. 284)
> Similar: Tadelis (2013), Exercise 13.10, p. 287
