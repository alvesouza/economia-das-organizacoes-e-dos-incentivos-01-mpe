---
quiz: "Lecture 2 · Quiz 2 of 3 — Oligopoly: Cournot, the cartel and Bertrand"
tags:
  cournot: "Cournot duopoly"
  cartel: "Cartel and Cournot with n firms"
  bertrand: "Bertrand duopoly"
  compare: "Cournot versus Bertrand"
---

## cournot

Q: Two firms choose outputs $q_1,q_2\ge0$; inverse demand is $P(Q)=a-bQ$ with $Q=q_1+q_2$, and both have constant marginal cost $c<a$. Let $q^m=(a-c)/(2b)$ be the monopoly output and $q^{cp}=(a-c)/b$ the competitive output. What is firm $i$'s best-response function?
- $q_i^*(q_j)=q^m-q_j$ for $0\le q_j<q^m$ and $0$ otherwise, from maximizing the joint profit $(a-c-bQ)\,Q$ over $q_i$
- $q_i^*(q_j)=q^m-\tfrac12q_j$ for $0\le q_j<q^{cp}$ and $0$ otherwise, from the first-order condition $a-c-2bq_i-bq_j=0$
- $q_i^*(q_j)=q^{cp}-q_j$ for $0\le q_j<q^{cp}$ and $0$ otherwise, from the first-order condition $a-c-bq_i-bq_j=0$
- $q_i^*(q_j)=\tfrac12(q^{cp}-q_j)$ for every $q_j\ge0$, negative values included, from the condition $a-c-2bq_i-bq_j=0$
<!-- YW5zOjE= -->
> Firm $i$'s profit is $\Pi_i=(a-c-b(q_i+q_j))\,q_i$. The first-order condition $a-c-2bq_i-bq_j=0$ (second derivative $-2b<0$) gives $q_i=(a-c-bq_j)/(2b)=q^m-\tfrac12q_j$, which reaches zero at $q_j=2q^m=q^{cp}$; output cannot be negative, so the best response is $0$ beyond that point. The fourth option has the right interior formula but drops the corner. The first maximizes joint profit (the cartel's problem); the third sets price equal to cost, ignoring the firm's own effect on the price.
> Ref: Lecture 2 slides 21–23; Tadelis (2013), §5.2.3, eq. (5.2) (p. 87); Gibbons (1992), §1.2.A (pp. 14–16)
> Similar: Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 2 Ex. 7, p. 48; Gibbons (1992), Problem 1.6, p. 49

Q: Two firms choose outputs $q_1,q_2\ge0$ facing $P(Q)=a-bQ$, with common marginal cost $c<a$ and monopoly output $q^m=(a-c)/(2b)$. What are the Nash equilibrium outputs $q_i^*$, total output $Q^*$ and price $P^*$?
- $q_i^*=\tfrac12q^m$, $Q^*=q^m$ and $P^*=\tfrac{a+c}{2}$, since the two best-response lines cross on the line where the joint profit is maximal
- $q_i^*=q^m$, $Q^*=2q^m$ and $P^*=c$, since each firm's best response to the rival's monopoly output is again the monopoly output
- $q_i^*=\tfrac34q^m$, $Q^*=\tfrac32q^m$ and $P^*=\tfrac{a+3c}{4}$, since each firm best-responds to half the monopoly output of its rival
- $q_i^*=\tfrac23q^m$, $Q^*=\tfrac43q^m$ and $P^*=\tfrac{a+2c}{3}$, since the lines $q_i=q^m-\tfrac12q_j$ cross at one symmetric point
<!-- YW5zOjM= -->
> Substituting $q_2=q^m-\tfrac12q_1$ into $q_1=q^m-\tfrac12q_2$ gives $q_1=\tfrac12q^m+\tfrac14q_1$, so $q_1^*=\tfrac23q^m$, and symmetrically for firm 2. Then $Q^*=\tfrac43q^m=\tfrac{2(a-c)}{3b}$ and $P^*=a-bQ^*=\tfrac{a+2c}{3}$. The duopoly lands between monopoly ($q^m$) and competition ($2q^m$). The third option is the best response to the cartel output, not a fixed point; the first is the cartel itself.
> Ref: Lecture 2 slides 22, 24; Tadelis (2013), §5.2.3 (pp. 87–88); Gibbons (1992), §1.2.A (pp. 16–17)
> Similar: Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 2 Ex. 7, p. 48; Gibbons (1992), Problem 1.6, p. 49

Q: In the Cournot duopoly with $P=a-bQ$, common marginal cost $c$ and monopoly output $q^m=(a-c)/(2b)$, IESDS first leaves each firm the outputs $[0,q^m]$ and then $[\tfrac12q^m,q^m]$. Which statement describes the following rounds and the limit?
- The bounds move to $\tfrac34q^m$, then $\tfrac58q^m$, $\tfrac{11}{16}q^m$, …, since each new bound is $q^m-\tfrac12x$ for the last bound $x$; they converge to $\tfrac23q^m$
- The bounds move to $\tfrac34q^m$, then $\tfrac78q^m$, $\tfrac{15}{16}q^m$, …, since each new bound halves the gap left to $q^m$; they converge to the monopoly output $q^m$
- The bounds move to $\tfrac14q^m$, then $\tfrac38q^m$, $\tfrac{5}{16}q^m$, …, since each new bound is half the last one plus a constant; they converge to $\tfrac13q^m$
- The process stops after two rounds, since every output in $[\tfrac12q^m,q^m]$ is a best response to some output the rival still has; that interval remains
<!-- YW5zOjA= -->
> A belief $q_j$ in $[L,U]$ yields best replies $q^m-\tfrac12q_j$ in $[q^m-\tfrac12U,\,q^m-\tfrac12L]$, so each round maps the previous bound $x$ to $q^m-\tfrac12x$: $\tfrac12q^m\mapsto\tfrac34q^m\mapsto\tfrac58q^m\mapsto\tfrac{11}{16}q^m$. The map has slope $-\tfrac12$, so the interval halves each round and closes on the fixed point $x=q^m-\tfrac12x$, i.e. $x=\tfrac23q^m$, the Nash output. Replies to $[\tfrac12q^m,q^m]$ lie only in $[\tfrac12q^m,\tfrac34q^m]$, so the process does not stop.
> Ref: Lecture 2 slide 24; Tadelis (2013), §4.3.4 (pp. 73–74); Gibbons (1992), §1.2.A (pp. 18–20)
> Similar: Tadelis (2013), Exercise 5.3, p. 95; Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 2 Ex. 7, p. 48

## cartel

Q: In a Cournot duopoly with $P=a-bQ$ and common marginal cost $c$, the monopoly output is $q^m=(a-c)/(2b)$. In a cartel each firm produces $\tfrac12q^m$. What is a firm's best response to the rival's cartel output, and what does it imply?
- Exactly $\tfrac12q^m$, since the cartel maximizes joint profit and therefore also each firm's own profit given the rival's cartel output
- The Cournot output $\tfrac23q^m$, since any deviation from the cartel moves both firms straight to the Nash equilibrium of the game
- The output $\tfrac34q^m=\tfrac{3(a-c)}{8b}$, above $\tfrac12q^m$: expanding raises own profit, so the cartel is not a Nash equilibrium
- The output $q^m$ itself, since a firm facing a rival that restricts output acts as a monopolist on the residual demand left over
<!-- YW5zOjI= -->
> From the best response $q_i^*(q_j)=q^m-\tfrac12q_j$: $q_i^*(\tfrac12q^m)=q^m-\tfrac14q^m=\tfrac34q^m$. The joint optimum ignores that one extra unit lowers the price for the rival's output too; a single firm bears only the loss on its own output, so it expands. The residual-demand monopolist of the last option solves exactly the best-response problem, which gives $\tfrac34q^m$, not $q^m$. With the slides' numbers: $q_i^*(22.5)=33.75>22.5$.
> Ref: Lecture 2 slide 25; Gibbons (1992), §1.2.A (p. 17); Tadelis (2013), §5.2.3 (pp. 87–88)
> Similar: Gibbons (1992), Problem 1.5, p. 49

Q: There are $n$ identical Cournot firms facing $P=a-bQ$ with marginal cost $c<a$; $q^m=(a-c)/(2b)$ and $q^{cp}=(a-c)/b$. In the symmetric Nash equilibrium, what are total output $Q^*$ and each firm's output $q_i^*$, and what happens as $n\to\infty$?
- $Q^*=\tfrac{2n}{n+1}q^m$ and $q_i^*=\tfrac{2q^m}{n+1}$; as $n\to\infty$ total output tends to $q^{cp}$ and the price to $c$
- $Q^*=\tfrac{n}{n+1}q^m$ and $q_i^*=\tfrac{q^m}{n+1}$; as $n\to\infty$ total output tends to $q^{m}$ and the price to $\tfrac{a+c}2$
- $Q^*=\tfrac{2n}{n+2}q^m$ and $q_i^*=\tfrac{2q^m}{n+2}$; as $n\to\infty$ total output tends to $q^{cp}$ and the price to $c$
- $Q^*=\tfrac{2n}{n+1}q^{cp}$ and $q_i^*=\tfrac{2q^{cp}}{n+1}$; as $n\to\infty$ total output tends to $2q^{cp}$ and the price to $2c-a$
<!-- YW5zOjA= -->
> Each best response is $q_i=q^m-\tfrac12\sum_{j\ne i}q_j$; doubling and moving the sum gives $q_i^*=2q^m-Q^*$. Summing over $n$ firms: $Q^*=2nq^m-nQ^*$, so $Q^*=\tfrac{2n}{n+1}q^m$ and $q_i^*=\tfrac{2q^m}{n+1}$. Checks: $n=1$ gives $q^m$, $n=2$ gives $\tfrac23q^m$ each. The third option fails the $n=2$ check (it gives total output $q^m$). As $n\to\infty$, $Q^*\to2q^m=q^{cp}$ and $P^*=\tfrac{a+nc}{n+1}\to c$.
> Ref: Lecture 2 slides 26–27; Tadelis (2013), §5.2.3 (pp. 87–88); Gibbons (1992), §1.2.A (pp. 14–17)
> Similar: Tadelis (2013), Exercise 5.8, pp. 96–97

Q: In a symmetric Cournot duopoly the cartel splits the monopoly output, and each firm's best response to the rival's cartel output is larger. Restricted to the two strategies Cartel and Deviate, the game has the structure of a well-known game. Which one, and why?
- A coordination game, since both (Cartel, Cartel) and (Deviate, Deviate) are equilibria and the firms only need a signal to pick the better one
- The Battle of the Sexes, since each firm prefers the outcome in which it deviates, but both prefer either asymmetric outcome to joint deviation
- Matching Pennies, since each firm wants to deviate when the rival colludes and to collude when the rival deviates, so no pure profile is stable
- The prisoner's dilemma, since Deviate is the better reply to either choice of the rival, yet both firms earn more when both stay in the Cartel
<!-- YW5zOjM= -->
> Against Cartel, Deviate pays more (it is the best response to the cartel output); against Deviate, Cartel pays less, since the deviator floods the market. So Deviate is dominant, the equilibrium is mutual deviation, and both would be better off in the cartel: the prisoner's dilemma. In the slides' example the cartel pays about 1,012 each, a deviator about 1,139 against a cartel firm's 759, and the Nash outputs pay 900 each. Lectures 5–6 ask whether repetition can sustain the cartel.
> Ref: Lecture 2 slide 25; Gibbons (1992), §1.2.A (p. 17); Tadelis (2013), §5.2.3 (pp. 87–88)
> Similar: Gibbons (1992), Problem 1.5, p. 49

## bertrand

Q: Homogeneous-good Bertrand duopoly: prices are chosen simultaneously, both firms have marginal cost $c$, the cheaper firm serves the whole demand $Q(p)=(a-p)/b$, ties split it, and $p^m=(a+c)/2$ is the monopoly price. What is firm $i$'s best response when $c<p_j\le p^m$?
- The single price $p_i=p_j$, since matching the rival secures half of the market at a positive margin without starting a price war
- There is none, since any price below $p_j$ takes the market and a slightly higher price that is still below $p_j$ earns more
- The monopoly price $p^m$, since a firm that takes the whole market should charge the price that maximizes $(p-c)Q(p)$
- Every price $p_i\ge p_j$, since at those prices firm $i$ earns zero or half of the market and no lower price can do better
<!-- YW5zOjE= -->
> For $p_i<p_j$ firm $i$ earns $(p_i-c)Q(p_i)$, which rises in $p_i$ up to $p^m\ge p_j$; its supremum, approached as $p_i\to p_j$ from below, is not attained, because at $p_i=p_j$ the firm gets only half. So the best-response set is empty, the existence problem of the continuous model. The monopoly price is the best response only when $p_j>p^m$; "every $p_i\ge p_j$" is the case $p_j=c$.
> Ref: Lecture 2 slides 30–34; Tadelis (2013), §5.2.4 (pp. 88–91)
> Similar: Gibbons (1992), Problem 1.7, pp. 49–50; Tadelis (2013), Exercise 5.12, p. 98

Q: In the homogeneous Bertrand duopoly with common marginal cost $c$, the proof that $(c,c)$ is the unique Nash equilibrium must rule out a profile with $p_1>p_2=c$. Which deviation does it?
- Firm 1 lowers its price to $c$, since matching the rival restores its share of the market and turns its zero profit into a positive one
- Firm 2 lowers its price below $c$, since the lowest price takes the whole market and the extra volume covers the loss on each unit
- Firm 2 raises its price to $p_1$ or just below, since it earns zero at $c$ and a positive margin on the market it then serves
- Firm 1 raises its price above $p_1$, since it sells nothing either way and a higher posted price improves its position later on
<!-- YW5zOjI= -->
> At $p_1>p_2=c$ firm 2 serves the market at a zero margin. Raising its price to $p_1$ (sharing the market) or just below it (keeping it all) earns a positive margin, so $p_2=c$ is not a best response to $p_1>c$. Firm 1 matching at $c$ still earns zero; pricing below cost earns a loss on every unit; and the game is static, so there is no "later" to prepare for.
> Ref: Lecture 2 slides 37–38; Tadelis (2013), Prop. 5.2 (p. 91)
> Similar: Gibbons (1992), Problem 1.7, pp. 49–50

## compare

Q: Two firms face $P=a-bQ$ with common marginal cost $c<a$. Compare the equilibrium price under Cournot competition, $P^C$, the equilibrium price under Bertrand competition, $P^B$, and the monopoly price $p^m$.
- $P^B=c<p^m=\tfrac{a+c}{2}<P^C=\tfrac{a+2c}{3}$, since quantity competition restrains output more than a single monopolist does
- $P^B=P^C=\tfrac{a+2c}{3}<p^m=\tfrac{a+c}{2}$, since the two models apply the same Nash concept and therefore yield one price
- $P^C=c<P^B=\tfrac{a+2c}{3}<p^m=\tfrac{a+c}{2}$, since quantity competition is the fiercer form and drives the price to cost
- $P^B=c<P^C=\tfrac{a+2c}{3}<p^m=\tfrac{a+c}{2}$, since Cournot firms keep some market power while Bertrand firms undercut
<!-- YW5zOjM= -->
> Cournot: $P^C=a-b\cdot\tfrac{2(a-c)}{3b}=\tfrac{a+2c}{3}$. Bertrand: $P^B=c$. Monopoly: $p^m=\tfrac{a+c}{2}$. And $\tfrac{a+2c}{3}<\tfrac{a+c}{2}\iff2a+4c<3a+3c\iff c<a$. The same solution concept, Nash equilibrium, applied to two different games gives two different prices: both predict more output than a cartel, Bertrand far more.
> Ref: Lecture 2 slides 22, 24, 30, 38, 40; Gibbons (1992), §1.2.A–B (pp. 14–22); Tadelis (2013), §5.2.3–5.2.4 (pp. 87–91)
> Similar: Gibbons (1992), Problems 1.6–1.7, pp. 49–50

Q: The Bertrand paradox says that two firms price at marginal cost and earn zero profit. Which list gives the assumptions the lecture names behind it, and when is Bertrand the better model?
- Homogeneous products, simultaneous choices and unlimited capacity; Bertrand fits when price is harder to adjust than quantity, as for software
- Homogeneous products, linear demand and equal market shares; Bertrand fits when capacity is harder to adjust than price, as for cement
- Differentiated products, sequential choices and unlimited capacity; Bertrand fits when price is harder to adjust than quantity, as for steel
- Homogeneous products, simultaneous choices and capacity limits; Bertrand fits when capacity is harder to adjust than price, as for cars
<!-- YW5zOjA= -->
> The paradox rests on (i) homogeneous products, (ii) simultaneous choices and (iii) unlimited capacity; relax any one and prices rise above cost. Which model to use depends on what is harder to adjust: when capacity is the slow variable (cars, cement, steel, commodities) firms compete in quantities, Cournot; when price is the commitment and quantity expands at almost no cost (software, digital goods), Bertrand.
> Ref: Lecture 2 slides 39–40; Tadelis (2013), §5.2.4 (pp. 90–93); Gibbons (1992), §1.2.B (pp. 21–22)
> Similar: Gibbons (1992), Problem 1.7, pp. 49–50
