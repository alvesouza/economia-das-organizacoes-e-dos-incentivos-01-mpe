---
quiz: "Lecture 1 · Quiz 2 of 3 — Dominance, dominant-strategy equilibrium and Pareto optimality"
tags:
  dom: "Strict and weak dominance"
  partnership: "The partnership game"
  pareto: "Pareto optimality and social dilemmas"
  auction: "Second-price auction"
---

## dom

Q: A strict dominant-strategy equilibrium is the game's unique dominant-strategy equilibrium. Which argument proves it?
- If two profiles were both strict dominant-strategy equilibria, each would be a Nash equilibrium, and a finite game has only one of those
- If two profiles differed for player $i$, both $s_i$ and $t_i$ would be best replies to one $s_{-i}$, which strict best replies allow
- If two profiles were both equilibria, their average $\tfrac12(s + t)$ would be one too, so the set is convex and must be a point
- If $s_i \ne t_i$ were both strictly dominant, then $u_i(s_i, s_{-i}) > u_i(t_i, s_{-i}) > u_i(s_i, s_{-i})$ for any $s_{-i}$
<!-- YW5zOjM= -->
> Each strictly dominant strategy strictly beats every other strategy of the same player, so two distinct ones would each beat the other against the same $s_{-i}$: a contradiction. Hence each player has at most one, and the profile is unique. Finite games can have many Nash equilibria, and pure profiles cannot be averaged, so the other arguments fail.
> Ref: Lecture 1 slide 25; Tadelis (2013), Prop. 4.1 (p. 61)
> Similar: Tadelis (2013), Exercise 4.1, p. 76

Q: Which statement about weak dominance is correct?
- A player has at most one weakly dominant strategy, but a weakly dominated strategy may tie for best against some profile, so rationality alone cannot exclude it
- A player can have several weakly dominant strategies, and any of them can be chosen, since a weakly dominant strategy is never strictly better than another
- A weakly dominated strategy is never a best response to any profile of the others, so rationality alone excludes it, exactly as with strict dominance
- Weak and strict dominance coincide in finite games, since a tie against one profile can always be broken by perturbing that payoff slightly in either direction
<!-- YW5zOjA= -->
> Two weakly dominant strategies would each need a strict advantage over the other somewhere while never being worse: impossible, so there is at most one. But a weakly dominated strategy ties with its dominator against some profiles, and if the player believes such a profile will be played it is a best response. Excluding it needs a caution assumption beyond rationality, which is why IESDS uses strict dominance.
> Ref: Lecture 1 slides 23, 28; Tadelis (2013), §4.1 (p. 63, on weak dominance)
> Similar: Tadelis (2013), Exercise 4.2, p. 76; Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 1 Ex. 16, p. 31

## partnership

P: Two partners simultaneously choose effort $E$, at private cost $c > 0$, or shirking $S$. Output equals $y > 0$ times the number of partners who exert effort and is split equally, so a partner's payoff is half the output minus the own effort cost.

Q: When is $E$ strictly dominant?
- When $c < y$, since effort then creates more output than it costs, whatever the other partner decides to do
- When $c < y/2$ against a shirking partner but $c < y$ against a working one, so it depends on the other's choice
- When $c < y/2$, since effort raises the own share by $y/2$ whatever the other does, and that gain must beat the cost
- When $c < y/4$, since the gain from effort is split twice, once in the output and once in the other partner's share of it
<!-- YW5zOjI= -->
> Against $S$: $E$ gives $y/2 - c$, $S$ gives 0. Against $E$: $E$ gives $y - c$, $S$ gives $y/2$. Both comparisons reduce to $y/2 > c$: one's own effort adds $y$ to output but only $y/2$ to one's own share, whatever the other does. The condition $c < y$ is the social one, comparing total output with cost.
> Ref: Lecture 1 slides 4, 23; Tadelis (2013), §4.1 (pp. 59–63)
> Similar: MWG 8.B.1, p. 262; Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 1 Ex. 15, p. 29

Q: For which $c$ is the game a social dilemma, with shirking strictly dominant yet both working Pareto dominating both shirking?
- $0 < c < y/2$, where effort is dominant and both working gives each partner $y - c > 0$
- $y/2 < c < y$, where shirking is dominant yet both working gives each partner $y - c > 0$
- $c > y$, where shirking is dominant and both working gives each partner $y - c < 0$
- $y/2 < c < 2y$, where shirking is dominant yet both working gives each partner $2y - c > 0$
<!-- YW5zOjE= -->
> Shirking is strictly dominant when $c > y/2$. Both working gives each $\tfrac12(2y) - c = y - c$, which beats both shirking (0) iff $c < y$. So in $(y/2, y)$ the dominant-strategy equilibrium ($S$, $S$) is Pareto dominated by ($E$, $E$): the prisoner's dilemma structure. The $2y - c$ option forgets that output is split.
> Ref: Lecture 1 slides 4, 24–26; Tadelis (2013), §4.1 (pp. 59–63), Def. 3.5 (p. 57)
> Similar: Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 1 Ex. 15, p. 29

Q: Suppose $c = y/2$ exactly. Which statement is true?
- Effort is weakly dominant, since it ties against a shirker and wins against a worker, so both partners should work
- Shirking is strictly dominant, since a partner who works pays $c$ for sure and receives only half of what that effort adds
- Effort is strictly dominant, since the surplus from both working, $2(y - c) = y$, is then positive and as large as it can be
- Each partner is indifferent between $E$ and $S$ whatever the other does, so neither dominates and the prediction is not robust
<!-- YW5zOjM= -->
> At $c = y/2$, against $S$ both strategies give 0, and against $E$ both give $y/2$. Ties everywhere mean neither strategy weakly dominates the other (weak dominance needs one strict inequality). This knife edge separates the effort-dominant region from the shirk-dominant one, so an $\varepsilon$ change in $c$ flips the prediction: invariance fails exactly here.
> Ref: Lecture 1 slides 22–23; Tadelis (2013), §3.3.2 (pp. 55–56), §4.1.3 (p. 62)
> Similar: Tadelis (2013), Exercise 4.2, p. 76

P:

Q: $n \ge 2$ partners each choose effort, at private cost $c > 0$, or shirking; output equals $y > 0$ times the number who work and is split equally among the $n$ partners. For which $c$ is shirking strictly dominant while everyone working Pareto dominates everyone shirking?
- $y/n < c < y$, a range that widens with $n$, since each keeps only $1/n$ of what the own effort adds
- $y/2 < c < y$, a range that does not depend on $n$, since each effort decision still involves only pairs of partners
- $y/n < c < ny$, a range that widens with $n$, since the output from everyone working, $ny$, is shared among $n$ partners
- $y/n^2 < c < y/n$, a range that narrows with $n$, since each partner's share of output shrinks as the team grows
<!-- YW5zOjA= -->
> One's own effort raises one's share by $y/n$ whatever the others do, so shirking is strictly dominant iff $c > y/n$. Everyone working gives each $ny/n - c = y - c$, better than 0 iff $c < y$. The dilemma region $(y/n, y)$ grows with team size: free-riding worsens as each member keeps a smaller share of what their own effort produces, the team-production problem that moral-hazard models later address.
> Ref: Lecture 1 slides 4, 26; Tadelis (2013), §4.1 (pp. 59–63)
> Similar: MWG 8.B.1, p. 262

## pareto

Q: In a prisoner's dilemma each player cooperates ($C$) or defects ($D$); both cooperating gives $R$ each, both defecting gives $P$ each, and when choices differ the defector gets $T$ and the cooperator $S$, with $T > R > P > S$. Which profiles are Pareto optimal?
- Only ($C$, $C$), since it gives the highest total payoff, and Pareto optimality selects the profile with the largest sum
- ($C$, $C$) and ($D$, $D$), since symmetric profiles cannot be Pareto dominated by profiles that treat the two players unequally
- Every profile except ($D$, $D$), since each of the others gives some player a payoff that no alternative profile can match
- Every profile except ($D$, $D$) when $2R > T + S$, and only ($C$, $C$) otherwise, since optimality depends on the sum
<!-- YW5zOjI= -->
> ($D$, $D$) is Pareto dominated by ($C$, $C$) since $R > P$. ($C$, $C$) cannot be dominated: any other profile gives someone $S$ or $P$, both below $R$. ($C$, $D$) gives the defector $T$, the highest payoff in the game, so no other profile makes that player as well off: Pareto optimal, and symmetrically for ($D$, $C$). Pareto optimality is not sum maximization, so the sign of $2R - (T + S)$ is irrelevant.
> Ref: Lecture 1 slides 24, 26; Tadelis (2013), §3.2.1 (pp. 51–52), Def. 3.5 (p. 57)
> Similar: Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 1 Ex. 5, p. 8

Q: In a prisoner's dilemma with money payoffs, $R$ each if both cooperate, $P$ each if both defect, and $T$ to a defector and $S$ to a cooperator when choices differ ($T > R > P > S$), suppose the players could first sign a binding contract with side payments, enforced by a court. What would they agree on?
- Both defect anyway, since defection is strictly dominant and a contract cannot change which strategy is dominant in the game
- The profile with the largest total, ($C$, $C$) when $2R > T + S$, since a binding contract changes the game the players face
- Both cooperate whatever the payoffs, since a contract always selects the symmetric Pareto optimal profile of the game
- Mutual cooperation only if $R > T$, since a court can enforce the agreement but cannot alter the temptation to defect
<!-- YW5zOjE= -->
> With enforceable contracts and transfers, the value maximization logic of Aula 2 (the Coase theorem) applies: the parties pick the profile with the largest total and split it by side payments, ($C$, $C$) if $2R > T + S$; otherwise one cooperates, one defects, and the defector compensates. The dilemma needs the absence of binding agreements: it is a noncooperative game, and a contract changes the payoffs, hence the dominance relations.
> Ref: Lecture 1 slides 24–26; Tadelis (2013), §4.1.3 (p. 62, the modified prisoner's dilemma); Aula 2 notes §3–§4; Milgrom & Roberts (1992), Ch. 2, pp. 36–38
> Similar: Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 1 Ex. 14, p. 28

## auction

P: In a second-price sealed-bid auction for one object, bidder $i$ values it at $v_i$; let $m$ be the highest bid among the other bidders. Bidder $i$ wins if $b_i > m$ and then pays $m$, earning $v_i - m$; if $b_i < m$ the bidder loses and earns 0 (ignore ties).

Q: Against which values of $m$ does a bid $b' < v_i$ do strictly worse than bidding $v_i$, and against which does a bid $b'' > v_i$?
- $b'$ is worse for $m \in (b', v_i)$, losing a profitable win, and $b''$ is worse for $m \in (v_i, b'')$, winning at a loss
- $b'$ is worse for $m < b'$, paying more than it needs to, and $b''$ is worse for $m > b''$, losing a win it would profit from
- $b'$ is worse for $m \in (b', v_i)$, paying more than needed, and $b''$ is worse for $m < v_i$, paying more than $v_i$
- $b'$ and $b''$ are worse for every value of $m$, since the bid $v_i$ strictly maximizes the payoff against each $m$
<!-- YW5zOjA= -->
> The price is $m$, not the own bid, so a bid matters only through whether it wins. Underbidding changes the outcome only when $b' < m < v_i$: it loses a win worth $v_i - m > 0$. Overbidding changes it only when $v_i < m < b''$: it wins and pays $m > v_i$. For every other $m$ the outcomes coincide.
> Ref: Lecture 1 slide 4; Tadelis (2013), Ch. 13 (pp. 270–287)
> Similar: Tadelis (2013), Exercise 4.4, pp. 76–77

Q: What kind of dominance does bidding $b_i = v_i$ have?
- Strict dominance, since against every $m$ the truthful bid earns strictly more than any other bid
- No dominance, since the best bid depends on $m$, which the bidder cannot observe when bidding
- Strict dominance once $n \ge 3$, since more bidders make every $m$ between the bids occur
- Weak dominance, since any other bid ties with it for every $m$ outside the bid–value interval
<!-- YW5zOjM= -->
> Truthful bidding is never worse and is strictly better against some $m$, which is weak dominance. It is not strict: for $m$ outside the interval between the bid and $v_i$, the alternative bid gives the same payoff. Dominance does not require observing $m$; that is the point of it. The number of bidders does not remove the ties.
> Ref: Lecture 1 slides 4, 23; Tadelis (2013), Ch. 13 (pp. 270–287); MWG §8.B (pp. 238–241)
> Similar: MWG 8.B.3, p. 262
