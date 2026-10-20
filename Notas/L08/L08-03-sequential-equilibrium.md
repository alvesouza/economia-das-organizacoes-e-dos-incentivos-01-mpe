---
tags: [notes, lecture-08, pbe, sequential-equilibrium, consistency, refinements]
date: 2026-10-16
status: estimated
source: "Tadelis (2013) §15.3 'Sequential Equilibrium', pp. 312–313 (Fig. 15.4, Def. 15.4–15.5) and §15.4 Summary, p. 314; Gibbons (1992) §4.1 footnote 1, p. 179; MWG §9.C, pp. 290–291 (Def. 9.C.4, Prop. 9.C.2)"
---

# 15.3 · Sequential equilibrium: discipline the beliefs nobody should be able to choose

> **Claim.** Requirement 15.3 lets off-path beliefs be anything, and some games then have PBE that
> rest on beliefs **no sequence of slightly-mistaken plays could ever generate**. Kreps and
> Wilson's **consistency** asks that beliefs be the **limit of Bayes' rule applied to totally
> mixed strategies converging to the equilibrium**. Sequential equilibrium = consistent PBE. It is
> the first *refinement*; the intuitive criterion (note 08) is the one signaling games need.
>
> Prev: [[L08-02-beliefs-and-pbe]] · Next: [[L08-04-signaling-games]] · Map: [[L08-00-map]]

---

## 1 · C — a game with an unreasonable PBE (Fig. 15.4, pp. 312–313)

Nature picks one of two nodes with probability $\tfrac12$ each; **player 1 does not observe the
draw** and chooses $U$ (ending the game at $(1,0)$) or $D$. After $D$ player 2 moves at an
information set $\{x_1,x_2\}$ (one node per draw) and chooses $L$ or $R$. Payoffs after $D$
(player 1, player 2):

| Node | $L$ | $R$ |
|---|---|---|
| $x_1$ | $2,\ 2$ | $0,\ 3$ |
| $x_2$ | $2,\ 2$ | $0,\ 0$ |

Player 2 with belief $\mu=\mu_2(x_1)$:

$$E[v_2(L)]=2\mu+2(1-\mu)=2,\qquad E[v_2(R)]=3\mu+0(1-\mu)=3\mu .$$

$R$ is a best reply iff $3\mu\ge2$, i.e. $\mu\ge\tfrac23$.

**PBE 1 — $(D,L)$ with $\mu=\tfrac12$.** $D$ is played, so the information set is on the path and
Bayes' rule gives

$$\mu_2(x_1)=\frac{\tfrac12\Pr\{D\}}{\tfrac12\Pr\{D\}+\tfrac12\Pr\{D\}}=\tfrac12$$

(player 1 cannot condition on Nature, so $\Pr\{D\}$ is the same at both nodes). Then
$3\cdot\tfrac12=\tfrac32<2$: $L$ is the best reply; given $L$, player 1 compares $D\to2$ with
$U\to1$ and plays $D$. ✔

**PBE 2 — $(U,R)$ with $\mu>\tfrac23$.** $U$ is played, the information set is off the path,
Requirement 15.3 allows any belief; pick $\mu_2(x_1)>\tfrac23$, so $3\mu>2$ and $R$ is a best
reply; given $R$, player 1 compares $U\to1$ with $D\to0$ and plays $U$. ✔

> **PBE 2 is absurd:** whatever made player 1 play $D$ by mistake, he could not have made it
> depend on a draw he never saw, so the two nodes must stay equally likely. Yet nothing in
> Requirements 15.1–15.4 says so.

---

## 2 · C — consistency and sequential equilibrium (Def. 15.4–15.5, p. 313)

> **Definition 15.4.** A profile $\sigma^*$ together with a belief system $\mu^*$ is **consistent**
> if there is a sequence of **non-degenerate** (totally mixed) strategy profiles
> $\{\sigma^k\}_{k=1}^\infty$ and the sequence of beliefs $\{\mu^k\}$ derived from each $\sigma^k$
> by Bayes' rule, such that $\lim_{k\to\infty}(\sigma^k,\mu^k)=(\sigma^*,\mu^*)$.
>
> **Definition 15.5.** A profile $\sigma^*$ with beliefs $\mu^*$ is a **sequential equilibrium** if
> it is a consistent perfect Bayesian equilibrium.

**Applying it to Fig. 15.4.** In any totally mixed $\sigma^k$, player 1 plays $D$ with some
$\varepsilon_k\in(0,1)$ — the same at both nodes. So for every $k$

$$\mu_2^k(x_1)=\frac{\tfrac12\varepsilon_k}{\tfrac12\varepsilon_k+\tfrac12\varepsilon_k}=\tfrac12,
\qquad\text{hence}\qquad \lim_k\mu_2^k(x_1)=\tfrac12 .$$

| $\varepsilon_k$ | $\mu_2^k(x_1)$ |
|---|---|
| $0.1$ | $0.05/0.10=\tfrac12$ |
| $0.001$ | $0.0005/0.001=\tfrac12$ |
| $10^{-6}$ | $\tfrac12$ |

The only consistent belief is $\tfrac12<\tfrac23$, under which $R$ is not a best reply. **$(U,R)$
is not a sequential equilibrium; $(D,L)$ with $\mu=\tfrac12$ is the unique one.**

> **Consistency turns "off-path beliefs are free" into "off-path beliefs are what trembles would
> teach you."** The trembles must be *the players' own* — here, one tremble by a player who cannot
> see Nature's draw, which therefore cannot shift the odds between the two nodes.

---

## 3 · C — where the concepts sit

$$\text{every sequential equilibrium is a PBE}\qquad\text{(Def. 15.5; the converse fails: Fig. 15.4's }(U,R)\text{)}$$

| Concept | Beliefs required | Off-path beliefs | Kills in Fig. 15.4 |
|---|---|---|---|
| Bayesian Nash | none | — | nothing |
| PBE (Tadelis, "weak") | Bayes on the path | anything | nothing ($(U,R)$ survives) |
| **Sequential** | limits of Bayes from trembles | **pinned** to $\tfrac12$ | $(U,R)$ |

Tadelis's practical verdict (p. 313): sequential equilibrium "is a bit harder to apply", so
applications use PBE; and **even sequential equilibrium can admit unreasonable outcomes**, which
motivates the signaling-specific refinement of [[L08-08-intuitive-criterion]].

---

## 4 · G — the formal side (MWG §9.C)

- **MWG Def. 9.C.4 (p. 290):** sequential equilibrium = sequentially rational (Def. 9.C.2) and
  consistent in the Kreps–Wilson sense — the same as Tadelis Def. 15.4–15.5.
- **MWG Prop. 9.C.2 (p. 291):** *"In every sequential equilibrium $(\sigma,\mu)$ of an extensive form
  game $\Gamma_E$, the equilibrium strategy profile $\sigma$ constitutes a subgame perfect Nash
  equilibrium of $\Gamma_E$."* (Weak PBE does **not** guarantee this — Gibbons Fig. 4.1.4,
  note 02 §7.)
- **Existence (Gibbons footnote 1, p. 179):** Kreps and Wilson show every **finite** game has a
  sequential equilibrium, hence a perfect Bayesian equilibrium.
- **MWG §9.D "Reasonable Beliefs and Forward Induction" (p. 292)** opens the programme of further
  restrictions on off-path beliefs that Chapter 13's Appendix A applies to signaling — the
  bridge to [[L08-08-intuitive-criterion]] §5. Named only.

---

## Links

- Prev: [[L08-02-beliefs-and-pbe]] · Next: [[L08-04-signaling-games]].
- The refinement that matters for signaling: [[L08-08-intuitive-criterion]].
- Subgame perfection, which sequential equilibrium implies: [[../L03/L03-00-map|Lecture 3]].
- Code: the tremble computation in [[L08-11-python]] §8.
- Exercises (number and page only): Tadelis 15.6 "Selten's Horse" (p. 317).
