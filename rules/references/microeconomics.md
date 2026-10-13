# microeconomics — reference

Loaded on demand from `rules/microeconomics.md`. Rules live there; this is the detail
needed to implement them.

Notation: `x` consumption bundle, `p` prices, `w` wealth, `u` utility, `e` expenditure,
`v` indirect utility, `h` Hicksian demand, `S` states of the world.

## 1. Preferences and representation

| Axiom | Statement | Consequence of dropping it |
|---|---|---|
| Completeness | Any two bundles are comparable | No preference relation |
| Transitivity | `x ≽ y`, `y ≽ z` ⟹ `x ≽ z` | Money pump; no maximum |
| Continuity | Upper/lower contour sets closed | No utility representation |
| Local non-satiation | Any neighbourhood contains a better point | Budget may not bind; welfare theorems fail |
| Convexity | Averages weakly preferred to extremes | Demand may not be convex-valued; existence problems |
| Monotonicity | More is better | Implies local non-satiation |
| Homotheticity | MRS constant along rays | Income expansion paths are rays; unit-elastic income |
| Quasi-linearity | `u = v(x₁,…,xₙ₋₁) + xₙ` | No income effects; CS = CV = EV |

**Debreu's representation theorem**: a complete, transitive, continuous preference
relation on a suitable space admits a continuous utility representation. Continuity is
the one that fails for lexicographic preferences — which is exactly why lexicographic
preferences have no utility function.

Utility is **ordinal**: any strictly increasing transform represents the same
preferences. Anything your result depends on that is *not* invariant to such a transform
is an artefact of the parameterization, not a property of preferences. (Under
uncertainty, expected utility is cardinal only up to positive affine transforms.)

`MRS_ij = (∂u/∂x_i)/(∂u/∂x_j)` — the slope of the indifference curve, and the only
directly meaningful derivative object in ordinal theory.

## 2. UMP, EMP, and duality

```
UMP:  max u(x)  s.t.  p·x ≤ w      →  Marshallian x(p,w),  indirect utility v(p,w)
EMP:  min p·x   s.t.  u(x) ≥ ū     →  Hicksian     h(p,ū),  expenditure   e(p,ū)
```

Identities linking them (valid where the solutions are unique and interior):

```
x(p, w)      = h(p, v(p,w))          e(p, v(p,w)) = w
h(p, ū)      = x(p, e(p,ū))          v(p, e(p,ū)) = ū
```

| Function | Properties |
|---|---|
| `v(p,w)` | Homogeneous of degree 0; strictly increasing in `w`, non-increasing in `p`; **quasi-convex** in `p`; continuous |
| `e(p,ū)` | Homogeneous of degree 1 in `p`; increasing in `ū`, non-decreasing in `p`; **concave** in `p`; continuous |
| `x(p,w)` | Homogeneous of degree 0; Walras' law `p·x = w`; Slutsky matrix symmetric NSD |
| `h(p,ū)` | Homogeneous of degree 0 in `p`; no excess utility; law of compensated demand |

Two derivative results that remove most of the calculus:

```
Roy's identity      x_i(p,w) = -(∂v/∂p_i)/(∂v/∂w)
Shephard's lemma    h_i(p,ū) =  ∂e/∂p_i
```

**Envelope theorem** — at an optimum, the derivative of the value function with respect
to a parameter equals the partial derivative of the Lagrangian holding choices fixed.
This is why you never differentiate the optimal policy.

## 3. Slutsky

```
∂x_i/∂p_j  =  ∂h_i/∂p_j  -  x_j · ∂x_i/∂w
                └ substitution ┘  └ income ┘
```

Slutsky matrix `S_ij = ∂h_i/∂p_j = ∂²e/∂p_i∂p_j`:

- **Symmetric** — `S_ij = S_ji`, from Young's theorem on `e`.
- **Negative semi-definite** — `vᵀSv ≤ 0` for all `v`.
- **Diagonal ≤ 0** — the compensated law of demand; Hicksian demand always slopes down.
- **`Sp = 0`** — homogeneity of degree zero.

Symmetry and NSD are the **entire testable content** of utility maximization. A demand
system estimated without imposing them is not a demand system.

| Good | Condition |
|---|---|
| Normal / inferior | `∂x_i/∂w > 0` / `< 0` |
| Giffen | `∂x_i/∂p_i > 0` — requires inferior *and* income effect dominating |
| Hicksian substitutes / complements | `∂h_i/∂p_j > 0` / `< 0` (symmetric, unlike gross) |

Aggregation restrictions worth checking as a sanity test, with budget shares `s_i`:

```
Engel      Σ s_i η_i = 1                (income elasticities, share-weighted)
Cournot    Σ s_i ε_ij = -s_j            (own+cross price elasticities)
Homogeneity Σ_j ε_ij + η_i = 0
```

**Welfare.** `CV = e(p¹, u⁰) - w` (income change at *new* prices restoring old utility);
`EV = w - e(p⁰, u¹)` (at *old* prices). Consumer surplus lies between them and equals
both only under quasi-linearity. Use CV/EV whenever the budget share is non-trivial.

## 4. Aggregation

Exact aggregation to a representative consumer requires **Gorman form** indirect
utility:

```
v_i(p, w_i) = a_i(p) + b(p)·w_i          b(p) common across consumers
```

which makes wealth-expansion paths parallel straight lines, so aggregate demand depends
on aggregate wealth alone. Special cases: homothetic (identical, `a_i = 0`) and
quasi-linear preferences.

Without it, aggregate demand depends on the wealth *distribution*, and the
**Sonnenschein-Mantel-Debreu** result applies: aggregate excess demand inherits only
continuity, homogeneity of degree zero, and Walras' law. Anything else — uniqueness,
stability, well-behaved comparative statics — must come from assumptions on the
distribution, not from individual rationality.

## 5. Production

Cost minimization gives `c(w,q)`; profit maximization gives `π(p)`. Both are concave in
prices; `c` is homogeneous of degree 1 in input prices. Hotelling's lemma gives supply
and factor demands as derivatives of `π`.

Returns to scale determine long-run structure: constant ⟹ flat supply and zero profit;
decreasing ⟹ upward-sloping supply; increasing ⟹ no competitive equilibrium (natural
monopoly).

## 6. General equilibrium

**Walras' law**: `p · z(p) = 0` for all `p`, where `z` is aggregate excess demand — a
consequence of every consumer's budget constraint binding. Consequence: if `L-1` markets
clear, the `L`-th clears too. Only relative prices are determined; normalize one.

**Existence** requires continuity, homogeneity of degree zero, Walras' law, and a
boundary condition; proved by fixed point (Brouwer/Kakutani). Convexity of preferences
and production sets is what makes the excess-demand correspondence convex-valued.

**First welfare theorem** — any Walrasian equilibrium allocation is Pareto efficient.
Needs: local non-satiation, complete markets, no externalities, price-taking. Notably
does *not* need convexity.

**Second welfare theorem** — any Pareto-efficient allocation is a Walrasian equilibrium
with transfers. Needs convexity of preferences and production sets, plus lump-sum
transfers. Convexity and the availability of lump-sum transfers are the two assumptions
that fail in practice.

**Core and Edgeworth.** The core (allocations no coalition can improve upon) contains
the equilibrium allocations, and as the economy is replicated the core shrinks to the
set of Walrasian equilibria — the core-convergence result that gives competitive
equilibrium a cooperative-game foundation.

## 7. Uncertainty, Arrow-Debreu, and Radner

**von Neumann-Morgenstern.** Preferences over lotteries satisfying completeness,
transitivity, continuity, and **independence** are represented by `U(L) = Σ p_s u(x_s)`.
Independence is the substantive axiom and the one violated by the Allais paradox.
`u` is unique up to positive affine transformation.

Risk aversion: `u` concave. Arrow-Pratt absolute `A(x) = -u''/u'`, relative
`R(x) = -x·u''/u'`. CARA (`u = -e^{-ax}`) implies wealth-independent absolute risk
aversion; CRRA (`u = x^{1-γ}/(1-γ)`) implies wealth-independent *relative* risk aversion.
The choice determines how demand scales with wealth and is substantive, not cosmetic.

**Arrow-Debreu equilibrium** — trade in state-contingent commodities, all at date 0.
With one contingent claim per state, markets are complete, and both welfare theorems
apply exactly as in the certainty case.

**Radner equilibrium** — sequential trade in assets, with spot markets reopening.
Equivalent to Arrow-Debreu **if and only if** the asset structure spans the state space
and agents have correct price expectations:

```
A  =  S × J payoff matrix (J assets, S states)
rank(A) = S   ⟺  complete   ⟺  Radner allocation = Arrow-Debreu allocation
rank(A) < S   ⟹  incomplete markets
```

With `rank(A) = S`, `S` Arrow securities can be synthesized and the date-0 economy is
recovered. This is the formal content of "dynamic completeness".

**Pricing.** No-arbitrage is equivalent to the existence of a strictly positive state-
price vector `ψ ≫ 0` with `q = Aᵀψ` for asset prices `q`. Equivalently:

```
state prices     ψ_s
SDF / kernel     m_s = ψ_s / π_s                (π = physical probabilities)
risk-neutral     π̂_s = ψ_s / Σ ψ               (normalized state prices)
pricing equation q_j = E[m · x_j] = Σ_s π_s m_s x_js
```

In a complete market `ψ` — hence `m` and `π̂` — is **unique**. In an incomplete market
there is a *set* of consistent kernels, which is exactly why incomplete-market prices
are bounded rather than determined.

With an interior optimum, the kernel equals the marginal rate of substitution:
`m_s = β u'(c_s)/u'(c_0)`. That identity is the bridge between this pack and asset
pricing: consumption-based models are this equation with a functional form chosen for
`u`.

Two standard consequences:

```
E[R_j] - R_f = -R_f · Cov(m, R_j)          risk premium is covariance with the kernel
σ(m)/E[m] ≥ |E[R_j] - R_f| / σ(R_j)        Hansen-Jagannathan bound
```

The HJ bound says any candidate kernel must be volatile enough to explain observed
Sharpe ratios — the quantitative form of the equity premium puzzle.

**Incomplete markets.** Equilibrium exists under conditions but is generically only
**constrained Pareto efficient**: a planner restricted to the same asset structure can
often still improve welfare by changing portfolio choices, because agents do not
internalize the effect of their trades on spot prices. Complete-markets intuition does
not transfer.

## 8. Externalities and public goods

- **Pigouvian tax** = marginal external damage **evaluated at the optimum**, not at the
  status quo. Computing it at current output over- or under-corrects.
- **Coase** — with well-defined rights and zero transaction costs, bargaining reaches
  efficiency regardless of the initial assignment; the assignment determines
  distribution only. The zero-transaction-cost condition is the entire content.
- **Samuelson condition** for a public good: `Σ_i MRS_i = MRT`. Sum willingness to pay
  across agents rather than equating each individually — non-rivalry is why.
- **Lindahl equilibrium** — personalized prices equal to each agent's marginal benefit;
  efficient, but not incentive-compatible (agents understate to lower their price).
- **VCG / pivotal mechanism** — truthful and efficient with transfers; each agent pays
  the externality they impose. Not budget-balanced, and vulnerable to collusion.

## 9. Asymmetric information

| Structure | Timing | Canonical result |
|---|---|---|
| Adverse selection | Hidden **type** before contracting | Akerlof: quality unravels; market can collapse |
| Signalling | Informed party moves first, at a cost | Spence: separation needs single-crossing; multiple equilibria |
| Screening | Uninformed party offers a menu | Rothschild-Stiglitz: no pooling equilibrium; separating may not exist |
| Moral hazard | Hidden **action** after contracting | Insurance-vs-incentive trade-off; first-best unattainable |

**Screening/menu design**, the general recipe:

```
max  principal's objective
s.t. IC:  U_i(contract_i) ≥ U_i(contract_j)   for all i, j      (truth-telling)
     IR:  U_i(contract_i) ≥ Ū_i                                  (participation)
```

Standard results: the **efficient type's IC binds** and the **worst type's IR binds**;
there is **no distortion at the top** and downward distortion elsewhere; information
rents accrue to the better types. **Single-crossing** (Spence-Mirrlees) is what makes
sorting possible at all — without it, no menu separates.

**Moral hazard.** With a risk-averse agent and unobservable effort, the optimal contract
trades insurance against incentives; the wage must vary with output even though the
agent would prefer certainty. Informativeness principle: any signal that is informative
about effort *conditional on output* belongs in the contract.

## 10. Social choice

- **Arrow's impossibility** — with three or more alternatives, no social welfare
  function satisfies unrestricted domain, Pareto, independence of irrelevant
  alternatives, and non-dictatorship simultaneously.
- **Gibbard-Satterthwaite** — with three or more outcomes, any non-dictatorial,
  onto social choice *function* is manipulable. Strategy-proofness is essentially
  unattainable without restricting preferences.
- **Escape routes**: restrict the domain (single-peaked preferences ⟹ median voter is
  strategy-proof), or allow transfers (quasi-linearity ⟹ VCG). Both are used constantly,
  and both are the assumption doing the work.
- **Revelation principle** — anything implementable by any mechanism is implementable by
  a direct, truthful one, so the search can be restricted to truthful mechanisms without
  loss.
