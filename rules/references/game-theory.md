# game-theory — reference

Loaded on demand from `rules/game-theory.md`. Rules live there; this is the detail
needed to implement them.

## Solution concepts, from weakest to strongest

| Concept | Requires | Rules out |
|---|---|---|
| Strict dominance | Rationality | Never-best responses |
| Iterated strict dominance | Common knowledge of rationality | More, order-independently |
| Rationalizability | Common knowledge of rationality | Non-best-responses to any belief |
| **Nash** | Correct beliefs about others' play | Profitable unilateral deviation |
| Subgame perfect (SPNE) | Nash in every subgame | Incredible threats |
| Bayesian Nash | Nash with types and priors | — |
| Perfect Bayesian (PBE) | Beliefs + sequential rationality | Incredible threats off-path |
| Sequential equilibrium | PBE + consistent beliefs | More off-path beliefs |
| Trembling-hand perfect | Robust to small mistakes | Weakly dominated strategies |

Each refinement adds assumptions and shrinks the prediction set. Stronger is not
automatically better: trembling-hand perfection is unfalsifiable in most applied
settings, and using it to select an equilibrium is usually a way of asserting the answer.

Iterated elimination of *strictly* dominated strategies is order-independent. Elimination
of *weakly* dominated strategies is **not** — different orders give different survivors,
so the order must be justified.

## Canonical games and what each isolates

| Game | Structure | Isolates |
|---|---|---|
| Prisoner's dilemma | Dominant defect, Pareto-inferior | Individual vs collective rationality |
| Stag hunt | Two equilibria, one payoff- one risk-dominant | Coordination under risk; trust |
| Battle of the sexes | Two asymmetric equilibria | Coordination with conflicting preference |
| Matching pennies | No pure equilibrium | Necessity of mixing |
| Chicken / hawk-dove | Two asymmetric pure equilibria | Commitment value; brinkmanship |
| Coordination | Multiple Pareto-ranked equilibria | Focal points, path dependence |
| Bertrand | Price competition | Competition without many firms |
| Cournot | Quantity competition | Strategic substitutes |
| Centipede | Backward induction unravels cooperation | Limits of backward induction empirically |
| Beauty contest (`p`-guessing) | Iterated reasoning | Depth of strategic thinking |

**Strategic complements vs substitutes** is the most transferable classification: if
your rival's aggression makes your aggression more profitable (prices, usually),
reactions amplify; if less (quantities, usually), they dampen. It determines the sign of
every comparative static in the game.

## Repeated games

Cooperation is sustainable when the discounted value of continued cooperation exceeds
the one-period deviation gain:

```
cooperate  ⟺  π_c / (1 - δ)  ≥  π_d + δ · π_punish / (1 - δ)
```

Equivalently `δ ≥ (π_d - π_c) / (π_d - π_punish)` — the critical discount factor.

Conditions the folk theorem actually needs, and which are the ones that fail in practice:

1. Infinite horizon, or a finite horizon with unknown end.
2. Sufficiently patient players (`δ` above the threshold).
3. **Observable deviations** — usually the binding one. With noisy monitoring you need
   imperfect-monitoring equilibria, where punishment must occasionally occur on the
   equilibrium path.
4. Credible punishment (Nash reversion, or the harsher optimal penal codes).

A *known* finite horizon unravels by backward induction. Reputation effects (a small
chance the opponent is a committed type) restore cooperation for most of a long finite
game — which is why finite-horizon experiments cooperate until near the end.

## Information

| Structure | Feature | Canonical result |
|---|---|---|
| Adverse selection | Hidden type before contracting | Lemons; unravelling |
| Signalling | Informed party moves first | Spence: costly signal separates; multiple equilibria need intuitive-criterion refinement |
| Screening | Uninformed party offers a menu | Rothschild-Stiglitz; may fail to exist |
| Moral hazard | Hidden action after contracting | Insurance vs incentives trade-off |
| Cheap talk | Costless messages | Crawford-Sobel: informative only when preferences are close enough |

Separating vs pooling equilibria: separating requires the single-crossing (Spence-
Mirrlees) condition — the signal must be *differentially* costly by type. Without it,
separation is impossible regardless of signal cost.

## Auctions

Revenue equivalence holds under independent private values, risk neutrality, symmetry,
and no budget constraints. Everything interesting comes from breaking one:

| Break | Consequence |
|---|---|
| Affiliated/correlated values | Linkage principle: English ≥ second-price ≥ first-price |
| Risk aversion | First-price raises more revenue |
| Budget constraints | All-pay and sequential formats diverge |
| Asymmetry | Revenue ranking becomes format- and distribution-specific |
| Common values | **Winner's curse** — bid below your estimate by more as bidders increase |
| Collusion | Second-price and English are easier to collude in; first-price is harder |

**Optimal auction (Myerson).** Sell to the bidder with the highest *virtual value*
`ψ(v) = v - (1 - F(v))/f(v)`, provided it is non-negative. The reserve price solves
`ψ(r) = 0` and does not depend on the number of bidders — the single most useful
practical result in auction design.

## Matching

- **Deferred acceptance (Gale-Shapley)** — always produces a stable matching; strategy-
  proof for the proposing side, optimal for the proposing side, worst stable outcome for
  the receiving side. Which side proposes is a distributional decision.
- No stable matching mechanism is strategy-proof for both sides.
- **Top trading cycles** — for allocation without money and with existing endowments;
  strategy-proof and Pareto efficient, but not stable.
- Roommates (non-bipartite) may have no stable matching at all.

## Algorithmic game theory

- **Price of anarchy** = worst equilibrium welfare ÷ optimal welfare. Selfish routing on
  networks with linear latency: 4/3. Simple, and bounds how much decentralization can
  cost.
- **Price of stability** = best equilibrium ÷ optimum — relevant when a designer can
  suggest an equilibrium.
- **Complexity**: computing a Nash equilibrium is PPAD-complete; correlated equilibria
  are computable in polynomial time by linear programming, which is a reason to prefer
  them as a design target.
- **No-regret dynamics** converge to the set of coarse correlated equilibria. Regret
  matching and CFR solve very large extensive games (poker-scale) in practice.
- **Mechanisms for computational settings**: prefer strategy-proof and approximately
  efficient over exactly optimal and manipulable.

## Verification checklist

- [ ] Players, actions, timing, information, payoffs written down explicitly
- [ ] Solution concept named and justified
- [ ] Existence checked; multiplicity acknowledged and selection argued
- [ ] Off-path beliefs specified for any perfect-Bayesian claim
- [ ] Discount factor / horizon stated for repeated results
- [ ] Numerically verified: no player has a profitable deviation
- [ ] Comparative statics signed, with the strategic channel named
