---
quiz: "Aula 2 · Quiz 1 of 3 — Wealth effects and the value index"
tags:
  conditions: "No wealth effects: the three conditions"
  index: "The value index x + v(y)"
  wtpwta: "WTP, WTA and the river"
---

## conditions

Q: A plant proposes to make each nuclear-plant operator personally liable for the losses that the operator's own errors cause, in exchange for a higher wage. Which no-wealth-effects condition fails, and what does that do to the value maximization argument?
- Compensability fails, since no sum of money can make up for the risk of injury, so a value comparison between the two contracts is undefined
- Independence fails, since a richer operator would ask a smaller wage premium, so the efficient contract varies with the operator's savings
- Ability to pay fails, since the losses can dwarf the operator's wealth, so the transfers the argument relies on cannot be made
- No condition fails, since the higher wage compensates exactly, so liability is efficient whenever the operator controls the error rate
<!-- YW5zOjI= -->
> The liability is financial, so the issue is not whether money can compensate (condition 1) but whether the operator can pay: a large accident costs far more than any worker owns (condition 3). Without ability to pay, the transfers that let the parties pick the value-maximizing contract and settle the split separately cannot happen. M&R use exactly this example for condition 3; risk to life is their example for condition 1, and it is not what the liability changes.
> Ref: Milgrom & Roberts (1992), Ch. 2, pp. 35–36; Aula 2 notes §1
> Similar: M&R FFT 2.3, p. 52

Q: A worker needs a payment $c(M)$ to switch from the day shift to the night shift, where $M$ is the worker's wealth and $c'(M) > 0$. Which no-wealth-effects condition fails, and what follows for the Coase prediction about who works nights?
- Independence fails, since $c(M)$ moves with wealth, so who works nights can depend on who held the right and on prior wealth
- Compensability fails, since $c(M)$ varies with wealth, so no definite payment exists for the switch and nights cannot be allocated by bargaining
- Ability to pay fails, since $c'(M) > 0$ means poorer workers cannot afford the switch, so nights always go to whoever holds the least wealth
- Independence holds as long as $c(M)$ is finite, since a definite payment exists, so efficiency alone decides who works nights, as Coase predicts
<!-- YW5zOjA= -->
> A definite compensating payment exists at each wealth level, so condition 1 holds; it changes with $M$, so condition 2 (independence from wealth) fails. Then each worker's valuation of the night shift depends on wealth, and wealth depends on who held the right and who paid whom. The efficient assignment is no longer pinned down by values alone, which is exactly the hypothesis the Coase theorem needs.
> Ref: Milgrom & Roberts (1992), Ch. 2, pp. 35–36, 38; Aula 2 notes §1, §4.2
> Similar: M&R Mathematical Exercise 2.4, p. 53

Q: Consider two bargains: (i) General Motors and Toyota negotiate who bears the cost of a parts-quality upgrade; (ii) a tenant farmer must buy a landlord's consent to switch to a higher-value crop. Where is the Coase theorem a safe guide, and why?
- In both, since in each case the parties bargain face to face and the gains from the efficient choice are large enough to cover any payment
- In neither, since both involve parties of unequal size, and unequal bargaining power is enough to make the agreed activity differ from the efficient one
- In (ii) only, since a farmer's crop is a small decision with no wealth effects, while corporate bargains involve transfers too large to absorb
- In (i) only, since corporate transfers are small relative to the firms' resources, while the farmer may be unable to pay for the efficient switch
<!-- YW5zOjM= -->
> M&R: the assumption is most dangerous "when the decision makers are individuals and when large cash transfers … are involved" (p. 36), and the theorem relies "on the ability to make unlimited transfer payments" (p. 39). A contract between GM and Toyota is their example of a reasonable application; land tenure in a developing country is their example of a mistaken one. Unequal bargaining power, by itself, moves only the split.
> Ref: Milgrom & Roberts (1992), Ch. 2, pp. 36, 39; Aula 2 notes §1, §4.4
> Similar: M&R FFT 2.3, p. 52

## index

Q: A decision maker has utility $u = x + v(y)$, where $x$ is money, $y$ every non-monetary aspect of a decision, and $M$ the initial wealth. What payment $\Delta x$ leaves the person indifferent to a switch from $y_1$ to $y_2$, and when does ability to pay hold?
- $\Delta x = v(y_2) - v(y_1)$, the same at every $M$, with ability to pay holding when $M$ exceeds $|v(y_1) - v(y_2)|$ for the pair being switched
- $\Delta x = v(y_1) - v(y_2)$, the same at every $M$, with ability to pay holding when $M$ exceeds $\max |v(y) - v(y')|$ over all pairs
- $\Delta x = M[v(y_1) - v(y_2)]$, rising with $M$, with ability to pay holding when $M$ exceeds $\max |v(y) - v(y')|$ over all pairs
- $\Delta x = v(y_1) - v(y_2)$, the same at every $M$, with ability to pay holding whenever $v$ is bounded above, whatever $M$ is
<!-- YW5zOjE= -->
> Indifference requires $M + \Delta x + v(y_2) = M + v(y_1)$, so $\Delta x = v(y_1) - v(y_2)$: it exists (condition 1) and $M$ cancels (condition 2). Condition 3 is about every possible switch, so $M$ must exceed the largest difference in $v$ over all pairs, not only the pair at hand. The first option has the sign reversed: it is what the person would pay, not receive.
> Ref: Milgrom & Roberts (1992), Ch. 2, p. 36 and n. 7; Aula 2 notes §2
> Similar: M&R Mathematical Exercise 2.4, p. 53

Q: Let $x$ be money, $y$ a non-monetary decision, $v(y)$ a real-valued function and $w(y) > 0$ a positive one. Which utility displays no wealth effects over $y$?
- $u = \ln x + v(y)$, because money and the decision enter additively, so the marginal rate of substitution never involves $y$ at all
- $u = x\,w(y)$, because money and the decision enter as a product, so the compensation for a switch is a fixed ratio of two values
- $u = \sqrt{x} + v(y)$, because money still enters apart from the decision, so a switch is priced by the difference $v(y_1) - v(y_2)$
- $u = e^{\,x + v(y)}$, because it ranks bundles as $x + v(y)$ does, so the compensation for a switch is $v(y_1) - v(y_2)$ at every wealth
<!-- YW5zOjM= -->
> Preferences are ordinal, so any increasing transformation of $x + v(y)$ describes the same choices; with $e^{x + v(y)}$ the compensation solves $M + \Delta x + v(y_2) = M + v(y_1)$. The others fail independence: with $\ln x + v(y)$, $\Delta x = M(e^{v(y_1) - v(y_2)} - 1)$; with $x\,w(y)$, $\Delta x = M[w(y_1)/w(y_2) - 1]$; with $\sqrt{x} + v(y)$ the payment also depends on $M$. Additive separability is not enough: money must enter linearly, up to a monotone transformation.
> Ref: Milgrom & Roberts (1992), Ch. 2, p. 36 and n. 7; Aula 2 notes §2
> Similar: M&R Mathematical Exercise 2.4, p. 53

Q: A colleague says: "with $u = x + v(y)$, where $x$ is money and $y$ the rest of a decision, the person does not care about money, which is why wealth effects vanish." What is wrong with the claim?
- The person cares about money one for one; what wealth does not change is the amount of money needed to compensate any switch in $y$
- Nothing substantive; with $u = x + v(y)$ only the decision $y$ moves utility, and money serves as a neutral unit for bookkeeping
- The person cares about money only at low wealth; above the ability-to-pay threshold the marginal utility of money falls to zero
- The person cares about money, but less as wealth rises; what stays fixed is the ratio of the compensation for a switch to wealth
<!-- YW5zOjA= -->
> Money enters with marginal utility one, so more is always better. "No wealth effects" means that the cash equivalent of any change in $y$ does not depend on how much money the person already has. A fixed ratio of compensation to wealth is the log-utility case, which is exactly a wealth effect.
> Ref: Milgrom & Roberts (1992), Ch. 2, pp. 35–36; Aula 2 notes §2, §8
> Similar: Varian (2014), Ch. 35 Review Questions 1–2, p. 687

## wtpwta

P: A resident has utility $u(x, c) = \ln x + \theta c$, where $x$ is money, $c \in \{0, 1\}$ indicates clean water, $\theta > 0$ is the taste for clean water and $M$ is the resident's wealth. Let $p$ be the most the resident would pay to get clean water ($c$ from 0 to 1) and $a$ the least the resident would accept to give it up ($c$ from 1 to 0).

Q: What are $p$ and $a$?
- $p = M(e^{\theta} - 1)$ and $a = M(1 - e^{-\theta})$, both proportional to wealth, with $p > a$
- $p = M(1 - e^{-\theta})$ and $a = M(e^{\theta} - 1)$, both proportional to wealth, with $a > p$
- $p = M e^{-\theta}$ and $a = M e^{\theta}$, both proportional to wealth, with $a > p$
- $p = \theta M$ and $a = \theta M$, both proportional to wealth, with $p = a$ at every $M$
<!-- YW5zOjE= -->
> Paying: $\ln(M - p) + \theta = \ln M$ gives $M - p = Me^{-\theta}$, so $p = M(1 - e^{-\theta})$. Accepting: $\ln(M + a) = \ln M + \theta$ gives $a = M(e^{\theta} - 1)$. Both scale with $M$, so condition 2 fails. $Me^{\pm\theta}$ forgets to subtract the starting wealth; $\theta M$ is only a first-order approximation for small $\theta$.
> Ref: Aula 2 notes §2 (worked counterexample)
> Similar: M&R Mathematical Exercise 2.4, p. 53

Q: How does the gap $a - p$ behave?
- $a - p = M(e^{\theta} - e^{-\theta})$, positive for every $\theta > 0$ and proportional to $M$
- $a - p = e^{\theta} + e^{-\theta} - 2$, positive for every $\theta > 0$ and the same at every $M$
- $a - p = M(e^{\theta/2} - e^{-\theta/2})^2$, positive for every $\theta > 0$ and proportional to $M$
- $a - p = M(e^{\theta} + e^{-\theta} - 2)$, negative for small $\theta$ and positive for large $\theta$
<!-- YW5zOjI= -->
> $a - p = M(e^{\theta} - 1) - M(1 - e^{-\theta}) = M(e^{\theta} + e^{-\theta} - 2) = M(e^{\theta/2} - e^{-\theta/2})^2$, a square times $M$, hence strictly positive for $\theta > 0$ and proportional to wealth. The last option has the right expression but the wrong sign claim: $e^{\theta} + e^{-\theta} \ge 2$ always. Under quasi-linear utility the gap is zero.
> Ref: Aula 2 notes §2, §8
> Similar: M&R Mathematical Exercise 2.4, p. 53; Cabral 5.1 "Front yards", p. 117

Q: A factory upstream gains $G > 0$ from dumping waste into the resident's water; money moves freely and bargaining is costless. For which values of $G$ does the initial assignment of the right to clean water decide whether dumping happens?
- $M(1 - e^{-\theta}) < G < M(e^{\theta} - 1)$, where the resident holding the right blocks dumping and the factory holding it dumps
- $M(1 - e^{-\theta}) < G < M(e^{\theta} - 1)$, where the resident holding the right allows dumping and the factory holding it stops
- $\theta < G < M(e^{\theta} - 1)$, where the resident holding the right blocks dumping and the factory holding it dumps
- No value of $G$, since with costless bargaining the factory dumps if and only if $G > \theta$, whoever holds the right
<!-- YW5zOjA= -->
> If the resident holds the right, the factory must pay at least $a$ and gains only $G$: if $G < a$, no dumping. If the factory holds it, the resident pays at most $p$: if $G > p$, the factory dumps. For $p < G < a$ the assignment decides the outcome, and both outcomes are Pareto efficient. The "$G > \theta$" rule is the quasi-linear case and does not apply to $\ln x + \theta c$.
> Ref: Milgrom & Roberts (1992), Ch. 2, p. 37 n. 10, p. 39; Cabral (2017), §5.1, pp. 97–98; Aula 2 notes §4.2
> Similar: Cabral 5.1 "Front yards", p. 117

P:

Q: A survey finds that residents demand far more to give up a clean river than they would pay to obtain one. Within the course's framework, what does this imply for applying the Coase theorem to the river?
- Nothing, since the gap reflects only how the question is framed, and under costless bargaining the efficient outcome is independent of who holds the right
- It shows that residents hold more bargaining power than the factory, so they capture more of the surplus, while the outcome stays fixed by total value
- It shows that residents value the river more than the factory values dumping, so the efficient outcome is a clean river whatever the initial assignment
- It contradicts quasi-linear utility, which forces the two amounts to be equal; with wealth effects, who holds the right can decide the outcome
<!-- YW5zOjM= -->
> With $u = x + \theta c$, paying and accepting amounts are both $\theta$. A systematic gap is the signature of a wealth effect (for a normal good, the amount accepted exceeds the amount paid), and then whenever the polluter's gain lies between the two amounts the initial assignment decides whether the river is clean. Bargaining power moves the split, not the outcome; and the gap alone does not say whose value is larger.
> Ref: Milgrom & Roberts (1992), Ch. 2, pp. 36–39; Aula 2 notes §2, §4.2, §8
> Similar: Varian (2014), Ch. 35 Review Questions 1–2, p. 687
