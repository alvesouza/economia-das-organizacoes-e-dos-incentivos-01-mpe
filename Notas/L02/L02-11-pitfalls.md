---
tags: [notes, lecture-02, pitfalls, true-false, self-test]
date: 2026-10-16
status: estimated
source: "Tadelis (2013) §4.3, Ch. 5–6 (pp. 69–123); Gibbons (1992) §1.1.C–1.3; rules/00_estilo_avaliacao.md (macro-1 True/False style)"
---

# Lecture 2 · Pitfalls and a True/False self-test

> Prev: [[L02-10-formulas]] · Next: [[L02-12-python]] · Map: [[L02-00-map]]

---

## Part I — the confusions this material produces

### 1 · "One player best-responds, so it is an equilibrium"

Bertrand with $p_2=10$: every $p_1\ge10$ is a best reply for firm 1. But $(12,10)$ is **not** a NE: firm 2's price of 10
is not a best reply to 12 (it would rather price at 11.99). Equilibrium is **mutual** best response (Tadelis p. 90).
→ [[L02-04-bertrand]] §2.

### 2 · "Rationalizable (or IESDS-surviving) means Nash"

Battle of the Sexes: (O, F) survives both and is not a NE; each player best-responds to a **wrong** belief. The
inclusion runs one way only: NE ⊆ rationalizable ⊆ IESDS survivors. → [[L02-02-nash-equilibrium]] §2.

### 3 · "A Nash equilibrium is efficient" / "the Pareto-best equilibrium will be played"

Prisoner's dilemma, Cournot (1800 total vs 2025), the commons ($K/3$ vs $K/4$): NE need not be Pareto optimal. Stag Hunt:
(H, H) is a NE although (S, S) Pareto dominates it; nothing in the definition selects (S, S). → [[L02-05-commons]],
[[L02-02-nash-equilibrium]] §4.

### 4 · "In a mixed equilibrium my mix makes *me* indifferent"

It makes the **other** player indifferent. In the §6.2.3 game player 1's mix $p=\tfrac16$ comes from **player 2's**
payoffs ($4(1-p)=3+2p$); change player 1's payoffs (keeping the best-response pattern) and $p$ does not move, $q$ does.
→ [[L02-07-mixed-strategies]] §3.

### 5 · "Indifferent between two strategies, so any mix of all strategies is fine"

Prop. 6.1 covers strategies **in the support**; MWG Prop. 8.D.1(ii) adds that strategies **outside** it must not pay
more. A mix that puts weight only on equal-payoff strategies is a best reply only if no other strategy pays strictly
more. → [[L02-07-mixed-strategies]] §8.

### 6 · "Not dominated by any pure strategy, so it survives IESDS"

Tadelis p. 115: L is beaten by $(0,\tfrac12,\tfrac12)$ though by neither C nor R alone; Gibbons's B (1, 1) is beaten by
$\tfrac12T+\tfrac12M$. → [[L02-08-iesds-rationalizability-revisited]].

### 7 · "Never a best response to a pure belief means never a best response"

Gibbons Fig. 1.3.2: B = (2, 2) is a best reply to neither L nor R but is the unique best reply for $q\in(\tfrac13,\tfrac23)$.
Beliefs must be allowed to be mixed. → [[L02-08-iesds-rationalizability-revisited]] §2.

### 8 · "A best-response function always exists"

Asymmetric Bertrand with continuous prices: against $p_2=2$ firm 1's profit approaches 98 but never reaches it, so
$BR_1(2)=\emptyset$. Correspondences can be multi-valued (ties, p. 72) **or empty** (discontinuities). → [[L02-04-bertrand]] §4.

### 9 · "Nash's theorem guarantees a pure equilibrium" / "no equilibrium without finiteness"

Nash's theorem: finite games, **mixed** equilibrium (Matching Pennies has no pure one). It is sufficient, not
necessary: Cournot and the commons have infinite strategy sets and pure equilibria. → [[L02-09-existence]].

### 10 · "Cournot equilibrium" and "Bertrand equilibrium" are different solution concepts

They are the **same** concept, Nash, applied to two different games (quantities vs prices) (Gibbons p. 21).

### 11 · Substitutes vs complements, read off the wrong axis

Strategic substitutes/complements describe the slope of the **best response** (Cournot down, Bertrand up, p. 93), not
whether the **products** are substitutes (they are substitutes in both models).

### 12 · Two printed slips worth knowing

Tadelis p. 87 footnote 5 gives the commons gain as 0.051, which is the **base-10** value; with the natural log of
eq. (5.1) it is $\ln(9/8)\approx0.118$. Tadelis p. 93 (Remark) calls the monopoly price "45": it is **55** (45 is the
quantity). Neither changes a conclusion.

---

## Part II — True/False self-test

*Original items in the `macro-1` style: one claim per item. Score $=\max\{0,\text{right}-\text{wrong}/2\}$.*

1. **If a game has a unique profile surviving IESDS, that profile is the game's unique Nash equilibrium.**
   **True.** Prop. 5.1: the survivor is a mutual best reply (Prop. 4.4), and every NE survives IESDS, so no other NE can
   exist.

2. **In the 3×3 game of Tadelis p. 81, (M, C) is the only Nash equilibrium.**
   **False.** It is the only **pure** one (which is all Tadelis claims). Support enumeration finds four more, all mixed:
   e.g. both players put $\tfrac16$ on their first strategy and $\tfrac56$ on their second; then U and M each pay player 1
   $\tfrac{27}6=4.5$ and D pays $\tfrac{23}6$, and symmetrically for player 2. Five equilibria in all, an odd number as
   footnote 6 (p. 113) leads one to expect ([[L02-12-python]] §7).

3. **A strictly dominant strategy is a best response to every belief, pure or mixed.**
   **True.** It beats each alternative against every pure profile, hence against every average of them.

4. **A pure strategy that is not a best response to any pure strategy of the opponent can be a best response to some
   mixed strategy.**
   **True.** Gibbons Fig. 1.3.2: B = (2, 2) is optimal for $q\in(\tfrac13,\tfrac23)$.

5. **In a two-player game, a strategy is never a best response if and only if it is strictly dominated, possibly by a
   mixed strategy.**
   **True.** Prop. 6.2; the "possibly mixed" is essential.

6. **In a mixed-strategy Nash equilibrium, each player's equilibrium mixing probabilities are determined by that
   player's own payoffs.**
   **False.** They are pinned by the **opponent's** indifference condition (Pitfall 4).

7. **If a player mixes between two pure strategies in a Nash equilibrium, both earn him the same expected payoff,
   equal to his equilibrium payoff.**
   **True.** Prop. 6.1.

8. **Matching Pennies has a Nash equilibrium.**
   **True.** $(\tfrac12,\tfrac12)$ for both; it has no **pure** one.

9. **In the Cournot duopoly with $P=a-bQ$ and equal costs $c$, each firm's equilibrium output is half the monopoly
   output.**
   **False.** $q_i^*=(a-c)/(3b)$, while half the monopoly output is $(a-c)/(4b)$: the duopoly overproduces relative to
   collusion because $BR(q_m/2)>q_m/2$.

10. **In the linear Cournot duopoly, a one-unit increase in firm 1's marginal cost raises the equilibrium price by
    one-third.**
    **True.** $P^*=(a+c_1+c_2)/3$, so $\partial P^*/\partial c_1=\tfrac13$ (interior case).

11. **In the homogeneous-good Bertrand duopoly with equal constant marginal costs and continuous prices, both firms earn
    zero profit in equilibrium.**
    **True.** Prop. 5.2: $p_1=p_2=c$.

12. **In the homogeneous Bertrand duopoly with continuous prices, if firm 1's marginal cost is 1 and firm 2's is 2,
    then $p_1=p_2=2$ is a Nash equilibrium.**
    **False.** Firm 1 would rather price just below 2; and there is no best such price, so no pure NE exists
    (pp. 91–93).

13. **Cournot competition is a game of strategic substitutes and Bertrand competition with differentiated products is a
    game of strategic complements.**
    **True.** Best responses slope $-1/2$ and $+b/2$ respectively.

14. **In the two-player tragedy of the commons of Tadelis §5.2.2, both players would be strictly better off if each
    consumed less than in the Nash equilibrium.**
    **True.** At $K/4$ each gains $\ln(9/8)>0$ relative to $K/3$.

15. **In the Hotelling voting game with 101 citizens, the best response to a rival at platform $a_j=+10$ is unique.**
    **False.** It is every platform in $[-9,9]$; only against $a_j\in\{-1,0,1\}$ is it unique (0).

16. **A Nash equilibrium always exists in pure strategies when each player has finitely many strategies.**
    **False.** Matching Pennies and rock-paper-scissors; Nash's theorem guarantees a **mixed** one.

17. **If a game has two pure-strategy Nash equilibria, it must also have a mixed-strategy Nash equilibrium.**
    **False.** "Almost always", not always (Tadelis footnote 6, p. 113; Gibbons footnote 15, p. 45). Counterexample: both
    players get 1 if both play their first strategy and 0 otherwise. (first, first) and (second, second) are NE, but a
    player is indifferent only if the other plays the second strategy for sure, so no profile with a mixing player is
    an equilibrium. The ties (weak dominance) are what break the generic rule.

18. **A Nash equilibrium is a fixed point of the players' joint best-response correspondence.**
    **True.** Tadelis's Fact, p. 120.

19. **Kakutani's theorem needs the best-response correspondence to be convex-valued; in finite games this is
    guaranteed by allowing mixed strategies.**
    **True.** Indifference between pure strategies makes every mix between them a best reply (Prop. 6.1); pure
    best-reply sets are not convex.

20. **If Chris believes Alex will go to the opera, Chris's unique best response in the Battle of the Sexes is to go to
    the opera, so (O, O) is the unique Nash equilibrium.**
    **False.** The first half is true ($v_2(O,O)=1>0$); the conclusion is not: (F, F) and the mixed profile are also NE.

21. **In the all-pay auction for a dollar, if the rival bids uniformly on $[0,1]$, every bid in $[0,1]$ gives the same
    expected payoff.**
    **True.** Each gives 0 (p. 107).

22. **The p-beauty contest prediction that nobody chooses a number above 1 relies only on each player being rational.**
    **False.** It needs **common knowledge** of rationality, 19 rounds deep; rationality alone removes only 20.

23. **Rationalizability always selects a unique outcome in the Battle of the Sexes.**
    **False.** "Anything can happen" (p. 76).

24. **In the mixed equilibrium of Tadelis's §6.2.3 game, player 1 plays M with probability $\tfrac37$.**
    **False.** $\tfrac37$ is player 2's probability of C; player 1 plays M with probability $\tfrac16$ (Pitfall 4 again).
