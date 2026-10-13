---
quiz: "Aula 1 · Quiz 3 of 3 — Coherent systems, the valley and NUMMI"
tags:
  systems: "Coherent systems (Figure 4.3)"
  valley: "The valley between systems"
  evidence: "NUMMI and the evidence"
---

## systems

P: Marketing chooses the number of models $n \ge 1$ and manufacturing the batch size $b > 0$, with profit $\pi = mQ + A\ln n - SQ/b - hnb/2 - \Delta c\,Q$, where $A$ is the taste for variety, $Q$ total volume, $S$ the cost of one changeover, $h$ the holding cost per unit of inventory, $m$ a unit margin and $\Delta c$ a unit-cost premium; $S$ and $\Delta c$ depend on the equipment.

Q: What is manufacturing's best batch size given $n$?
- $b^*(n) = \sqrt{2SQ/h}$, which does not depend on $n$, since each model's inventory is held separately from the others
- $b^*(n) = \sqrt{2SQ/(hn)}$, which falls as $n$ rises, since more models raise the inventory cost of a larger batch
- $b^*(n) = \sqrt{hn/(2SQ)}$, which rises with $n$, since more models make each changeover relatively cheaper to schedule
- $b^*(n) = SQ/(hn)$, which falls as $n$ rises, since changeover cost and inventory cost are equated at the margin
<!-- YW5zOjE= -->
> Setting $\partial\pi/\partial b = SQ/b^2 - hn/2 = 0$ gives the economic order quantity $b^* = \sqrt{2SQ/(hn)}$. The cross effect $\partial^2\pi/\partial n\,\partial b = -h/2 < 0$ makes variety and batch size substitutes, so variety and small batches are complements, as M&R argue for Figure 4.3. The $SQ/(hn)$ answer equates total rather than marginal costs.
> Ref: Milgrom & Roberts (1992), Ch. 4 "Complementarities, Innovation Attributes, and Coordination Failure", p. 111; Aula 1 notes §7.1
> Similar: Companion "Two Coherent Systems", plate 1

Q: For one type of equipment, which pair gives the joint optimum, and when does the solution sit at Ford's single-model corner?
- $n^* = A^2/(2hSQ)$ and $b^* = A/(SQ)$, with the corner $n^* = 1$ when $A^2 \le 2hSQ$
- $n^* = 2A^2/(hSQ)$ and $b^* = SQ/A$, with the corner $n^* = 1$ when $2A^2 \ge hSQ$
- $n^* = 2A/(hSQ)$ and $b^* = \sqrt{SQ/A}$, with the corner $n^* = 1$ when $2A \le hSQ$
- $n^* = 2A^2/(hSQ)$ and $b^* = SQ/A$, with the corner $n^* = 1$ when $2A^2 \le hSQ$
<!-- YW5zOjM= -->
> Marketing's condition $A/n = hb/2$ gives $n = 2A/(hb)$. Substituting into $b^2 = 2SQ/(hn)$: $b^2 = SQb/A$, so $b^* = SQ/A$ and $n^* = 2A^2/(hSQ)$. Since $n \ge 1$, the corner applies when that value is at most one: weak taste for variety, high changeover cost or high volume push the firm to one model. The reversed inequality would put Ford at the corner exactly when variety is most valued.
> Ref: Aula 1 notes §7.1; Milgrom & Roberts (1992), Ch. 4, pp. 111–112
> Similar: Practice plan Aula 1, companion task C4

Q: When the two smooth, downward-sloping best replies cross three times, what is true at the middle crossing?
- They cross so that $\pi_{nb}^2 > \pi_{nn}\pi_{bb}$, the Hessian is indefinite, and the point is a saddle rather than a third peak
- They cross so that $\pi_{nb}^2 < \pi_{nn}\pi_{bb}$, the Hessian is negative definite, and the point is a third local peak of profit
- They cross so that $\pi_{nn}\pi_{bb} < 0$, one own effect is positive there, and the point is the lowest profit between the two peaks
- They cross so that $\pi_{nb} = 0$, the two choices are locally independent, and the point lies on a flat ridge of the profit surface
<!-- YW5zOjA= -->
> Each crossing satisfies both first-order conditions. At the outer crossings the replies cross the stable way and $\pi_{nn}\pi_{bb} > \pi_{nb}^2$: local maxima. At the middle one they cross the other way, so $\pi_{nb}^2 > \pi_{nn}\pi_{bb}$ and the Hessian is indefinite: a saddle. M&R's footnote 9 speaks of "a mountain with three peaks"; the careful reading is two peaks and a saddle, which leaves the book's point intact.
> Ref: Milgrom & Roberts (1992), Ch. 4, p. 112 footnote 9; Aula 1 notes §7.2
> Similar: Companion "Two Coherent Systems", plate 2

Q: Why, in M&R's account, must the choice among coherent strategy patterns be made centrally?
- Managers adjusting in turn always converge to the most profitable crossing, so the centre only speeds up an adjustment that happens anyway
- A coherent crossing is by definition the most profitable one, so the centre only keeps managers there while demand and costs move smoothly
- Managers track local shifts of their own crossing, but seeing that another crossing has become best needs information neither of them holds
- Every crossing is unstable to small shocks, so the centre picks one at random and forbids managers to adjust their own choices afterwards
<!-- YW5zOjI= -->
> M&R pp. 112–113: a small change in the curves "may hide the fact that the relative profitability of the different coherent patterns has changed"; "recognizing that a radical strategic shift is desirable is likely to require information that neither manager has". Choosing among coherent patterns has innovation attributes, so it is centralised (p. 115), the argument of Aula 7. Coherence is local; only one pattern is profit maximizing (p. 112).
> Ref: Milgrom & Roberts (1992), Ch. 4, pp. 112–115
> Similar: M&R FFT 4.2, p. 119

## valley

P: Three yes-or-no practices, just-in-time $J$, multi-skilled teams $T$ and long-term suppliers $S$, give profit $\pi = \pi_0 + v_J J + v_T T + v_S S + i_{JT} JT + i_{JS} JS + i_{TS} TS + i_{JTS} JTS$, where the $v$ are stand-alone values, the $i$ interaction terms, and Ford's corner $(0,0,0)$ earns $\pi_0$.

Q: When is $\pi$ supermodular on the cube $\{0,1\}^3$?
- When each stand-alone value is nonnegative, $v_J, v_T, v_S \ge 0$, since a practice that loses alone cannot raise the return to another practice
- When the three pairwise terms sum to a nonnegative number, $i_{JT} + i_{JS} + i_{TS} \ge 0$, whatever the sign of the three-way term may be
- When the three-way term is nonnegative, $i_{JTS} \ge 0$, since only the full system tests whether all three practices fit together at once
- When each pairwise term, alone and plus the triple term, is nonnegative: $i_{JT} \ge 0$, $i_{JT} + i_{JTS} \ge 0$, and so on for each pair
<!-- YW5zOjM= -->
> Supermodularity on the cube is equivalent to increasing differences in every pair at every value of the third practice. The gain from $J$ given $T$ rises by $i_{JT} + i_{JTS}S$ when $T$ switches on, so both $i_{JT}$ (at $S = 0$) and $i_{JT} + i_{JTS}$ (at $S = 1$) must be nonnegative; similarly for the other pairs. Stand-alone values play no role: complements can each lose alone.
> Ref: Aula 1 notes §6.1, §8.1; Milgrom & Roberts (1992), Ch. 4, p. 108
> Similar: Companion "The Valley Between Systems" (supermodularity read-out)

Q: Suppose $v_J$, $v_T$ and $v_S$ are all negative. What can the interaction terms do about the dip on the way from $(0,0,0)$ to $(1,1,1)$?
- Large pairwise terms remove the dip, since the second practice then repays the first step's loss before the third one is added
- Nothing: every order's first step adds one practice to an empty system and earns only its stand-alone value, so every order dips
- A large three-way term removes the dip, since the full system's gain is then spread over all three steps of the best order
- Supermodularity removes the dip, since with complements every order raises profit at each step once the first one is taken
<!-- YW5zOjE= -->
> The first step of any order moves from $(0,0,0)$ to a corner with one practice, changing profit by $v_J$, $v_T$ or $v_S$; no interaction term is active yet. So with all three negative, every order falls below $\pi_0$ at step one, however large the interactions. The remedy has to lower a stand-alone loss to zero or above (or move several practices at once). Complementarity locates the optimum but creates the valley.
> Ref: Aula 1 notes §8.1
> Similar: Practice plan Aula 1, companion task C5

Q: Suppose $\pi(1,1,1) > \pi_0$, yet every single change from $(0,0,0)$ and every single change from $(1,1,1)$ lowers profit. What does marginal analysis conclude?
- Only the full system passes the one-step test, so marginal analysis run from Ford's corner leads the firm uphill to the full system
- Only Ford's corner passes the one-step test, so the full system's higher profit must reflect an error in measuring the interactions
- Both corners pass every one-step test, so it cannot rank them, and comparing the packages requires evaluating each whole system at once
- Neither corner passes the one-step test, so marginal analysis tells the firm to stop at whichever intermediate corner it reaches first
<!-- YW5zOjI= -->
> Both corners are local peaks: no single change improves either. Marginal tests therefore return "stay" at both and cannot tell which peak is higher; in the class cube the package gain is positive while the best single step from Ford's corner is negative. That is why the switch is a design decision taken as a whole, not a sequence of local improvements.
> Ref: Aula 1 notes §8.1; Milgrom & Roberts (1992), Ch. 4, pp. 112–113
> Similar: Companion "The Valley Between Systems"

## evidence

P:

Q: What does the NUMMI plant at Fremont show, read together with the valley?
- Mostly the same laid-off GM workers reached Toyota-level productivity under Toyota's whole system, while GM's piecemeal transfer largely failed
- Toyota's workers, brought over from Japan, outperformed GM's in the same plant, showing that the workforce rather than the system explained the gap
- GM's own plants matched NUMMI within a few years by copying its most visible practices one at a time, so imitating the system was straightforward
- The plant's gains came from new automation that Toyota installed in 1984, so the case shows the value of technology rather than of organization
<!-- YW5zOjA= -->
> Over 85% of NUMMI's first workforce were the laid-off Fremont workers; in 1987 NUMMI needed about 19 assembly hours per car against 31 at a comparable GM plant (figures from a secondary reproduction of Womack, Jones and Roos 1990, still to confirm). GM's efforts to spread the system piece by piece "proved largely unsuccessful". Toyota moved the whole system at once, a jump across the valley; GM, adopting practice by practice, kept landing on low corners.
> Ref: Aula 1 notes §8.2; class video provenance file (`Videos/aula-01-does-organization-matter/provenance.md`)
> Similar: Cabral 3.14 Intel, p. 63

Q: A researcher estimates $y = \beta_0 + \beta_1 x + \beta_2 z + \beta_3 xz + \varepsilon$, where $y$ is productivity and $x, z \in \{0,1\}$ indicate two practices. What do the coefficients say about complementarity?
- The effect of $x$ is $\beta_1 + \beta_2$ when $z = 1$; $\beta_3$ measures the effect of $z$ alone, so a positive $\beta_2$ is what shows complementarity
- The effect of $x$ is $\beta_3$ whatever $z$ is; $\beta_1$ measures the cross effect, so a positive $\beta_1$ shows complementarity if adoption is common
- The effect of $x$ is $\beta_1$ when $z = 0$ and $\beta_1 + \beta_3$ when $z = 1$; a positive $\beta_3$ proves complementarity whatever drove adoption
- The effect of $x$ is $\beta_1$ when $z = 0$ and $\beta_1 + \beta_3$ when $z = 1$; $\beta_3 > 0$ fits complementarity, but firms adopting both may differ
<!-- YW5zOjM= -->
> $\partial y/\partial x$ switches from $\beta_1$ to $\beta_1 + \beta_3$ as $z$ goes from 0 to 1, so $\beta_3$ is the cross effect, the regression version of increasing differences. Ichniowski, Shaw and Prennushi (1997) find, on 36 steel finishing lines, that the bundle of HR practices raises productivity and isolated practices do not. But adoption is not random: firms that adopt practices together may differ in unobserved ways, so correlated adoption alone does not prove complementarity.
> Ref: Aula 1 notes §8.3; Ichniowski, Shaw & Prennushi (1997), AER 87(3), 291–313
> Similar: Cabral 3.20 Productivity, p. 64

Q: Why did Toyota end up with the full lean system while GM, able to watch it, did not?
- Toyota adopted the practices one at a time in the most profitable order, an order GM could not see because Toyota kept it secret for decades
- Toyota built it as a whole from a different starting point, while GM sat at a coherent peak where each single change lowered profit
- GM's managers lacked the information to rank the systems, while Toyota's had it because its suppliers were integrated into the firm itself
- Toyota's practices were each profitable alone in Japan, so it climbed steadily, while GM faced different stand-alone values in America
<!-- YW5zOjE= -->
> Toyota's constraints in the 1950s (small scale, little capital) made the lean system the natural answer, after a failed attempt to copy mass production (M&R p. 4); it built the whole package. GM started at mass production, a coherent local peak, where piecemeal steps lose money (the valley), and choosing between systems needs information local managers lack. Toyota relied on outside suppliers rather than integrating them (pp. 5–6).
> Ref: Milgrom & Roberts (1992), Ch. 1, pp. 4–6, 16–17; Ch. 4, pp. 111–113; Aula 1 notes §7–§8
> Similar: Practice plan Aula 1, items 15 and 18
