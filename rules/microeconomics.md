---
id: microeconomics
title: Microeconomic modelling
tier: 2
applyTo: "**/{micro,theory,welfare,equilibrium,pricing,mechanism,auction}/**"
skills: [econ]
owner: quant-team
---

Rules for building and using microeconomic models in applied work — pricing, market
design, policy analysis, asset pricing under uncertainty, and the structural side of
empirical research. A model is a set of assumptions with implications; the discipline is
knowing which assumption is doing the work.

## Non-negotiable

1. **State the primitives before the result**: agents, action sets, information,
   preferences (or technology), endowments, and timing.
   *Why:* nearly every disagreement about a model's conclusion is actually a
   disagreement about an unstated primitive, and it stays invisible until named.

2. **State which assumptions are doing the work**, and which are for tractability. A
   result that hinges on quasi-linearity, single-crossing, homotheticity, or common
   knowledge must say so.
   *Why:* a conclusion is only as portable as its load-bearing assumption, and the
   tractability assumptions are the ones people wrongly defend.

3. **Comparative statics require the sign of the effect and its source** — income
   effect, substitution effect, wealth effect, or strategic effect. "Demand falls"
   without the channel cannot be transferred to another setting.

4. **Never claim a welfare conclusion from a positive model without naming the welfare
   criterion** — Pareto, compensating or equivalent variation, consumer surplus, or a
   social welfare function with stated weights.
   *Why:* consumer surplus is a valid welfare measure only when income effects are
   absent, which is usually assumed rather than checked, and distribution is invisible
   inside an efficiency statement.

5. **Equilibrium existence and uniqueness are checked, not assumed.** With multiple
   equilibria, say which is selected and why.
   *Why:* comparative statics across a multiplicity are meaningless — you may be
   comparing different equilibria rather than one equilibrium under different
   parameters. Aggregate excess demand inherits almost no structure from individual
   rationality, so uniqueness generically fails without extra assumptions.

6. **Under uncertainty, state the market structure explicitly**: complete contingent
   claims, sequential trade with enough assets to span, or genuinely incomplete.
   *Why:* the welfare theorems and the representative-agent pricing results hold under
   completeness and fail without it. Assuming completeness is assuming the conclusion.
   *Check:* the payoff matrix has rank equal to the number of states, or the model is
   labelled incomplete and the constrained-efficiency caveat is stated.

7. **No-arbitrage and the existence of a strictly positive pricing kernel are the same
   statement.** Say which you are assuming and do not derive one from the other twice.
   *Why:* every discount-factor, risk-neutral-measure, and state-price representation
   is the same object viewed differently; treating them as independent assumptions
   double-counts.

## Prefer

8. Duality as a working tool: expenditure and indirect utility, cost and profit
   functions. Shephard's and Roy's identities turn a hard optimization into a
   derivative, and the envelope theorem does most comparative-statics work.

9. Revealed preference when you need testable restrictions without assuming a
   functional form — WARP/GARP are checks you can run on data.

10. Explicit functional forms only when the qualitative result is already understood.
    Cobb-Douglas and CES are tractable *and* impose strong substitution restrictions
    that frequently drive the finding.

11. Partial equilibrium for a single market with small spillovers; general equilibrium
    when the market is large relative to the economy or when factor prices respond. Say
    which, and why it is adequate.

12. Mechanism design framing when the object is to *choose* rules rather than predict
    behaviour under given rules: state the objective, the incentive-compatibility
    constraints, and the participation constraints separately.

13. Second-best reasoning where a distortion cannot be removed. Optimizing one margin
    while another is distorted can reduce welfare, and the first-best intuition inverts.

14. Robustness across preference, information, and market-structure specifications,
    reported together.

## Avoid

15. Treating a representative agent as a population. Exact aggregation requires
    conditions (Gorman form) that rarely hold, and distributional questions disappear by
    construction.

16. Interpreting a correlation as a structural parameter. Elasticities estimated from
    equilibrium data are not the demand curve unless supply variation identifies it —
    see `microeconometrics.md`.

17. Assuming interior solutions. Corner solutions, participation margins, and binding
    constraints are usually where the interesting behaviour lives.

18. Comparative statics by differentiating a solved closed form when the model has
    constraints that may switch between binding and slack.

19. Extending a partial-equilibrium welfare result to an economy-wide claim.

20. Confusing efficiency with desirability. Pareto efficiency is silent about
    distribution, and every competitive-equilibrium efficiency result is conditional on
    complete markets, no externalities, and full information.

21. Applying complete-markets intuition to an incomplete-markets economy. With
    incomplete markets, equilibrium is generically only *constrained* efficient, and a
    planner respecting the same asset structure can still improve on it.

**Reference:** `rules/references/microeconomics.md` — preference axioms and
representation, UMP/EMP duality with the full property lists, Slutsky, aggregation,
general equilibrium and the welfare theorems, uncertainty and Arrow-Debreu/Radner
pricing, externalities and public goods, asymmetric information, social choice.
Load it when implementing; the rules above stand on their own.
