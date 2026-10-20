---
tags: [notes, lecture-08, pbe, beliefs, bayes-rule, sequential-rationality]
date: 2026-10-16
status: estimated
source: "Tadelis (2013) §15.2 'Perfect Bayesian Equilibrium', pp. 307–312 (Def. 15.1–15.3, Requirements 15.1–15.4, Prop. 15.1, Remark and Fig. 15.3); Gibbons (1992) §4.1, pp. 177–182 (Requirements 1–4, Figs. 4.1.3–4.1.5); MWG §9.C, pp. 282–285 (Def. 9.C.1–9.C.3)"
---

# 15.2 · Beliefs at every information set, Bayes' rule where it applies, best replies everywhere

> **Claim.** A perfect Bayesian equilibrium is a strategy profile **plus a belief system**. Beliefs
> are **pinned by Bayes' rule wherever the equilibrium reaches an information set** and are
> **free where it does not**; given the beliefs, every player best-responds **at every
> information set**, reached or not. The freedom off the path is the concept's power (it kills
> threats no belief can justify) and its weakness (it can support almost anything — notes 03 and
> 08).
>
> Prev: [[L08-01-subgame-perfection-fails]] · Next: [[L08-03-sequential-equilibrium]] · Map: [[L08-00-map]]

---

## 1 · C — on and off the equilibrium path (Definition 15.1, p. 307)

> **Definition 15.1.** Let $\sigma^*$ be a Bayesian Nash equilibrium profile. An information set is
> **on the equilibrium path** if, given $\sigma^*$ and the type distribution, it is reached with
> positive probability, and **off the equilibrium path** if it is reached with probability zero.

The definition needs a **candidate profile** first. In the entry game of
[[L08-01-subgame-perfection-fails]]:

| Entrant plays | Incumbent's information set after $E$ | Reached with prob. |
|---|---|---|
| $EO$ | on the path | $p\cdot1+(1-p)\cdot0=p>0$ |
| $OO$ | **off** the path | $p\cdot0+(1-p)\cdot0=0$ |

> **The informed player's strategy decides which of the uninformed player's information sets are
> reached** (p. 308).

---

## 2 · C — a system of beliefs (Definition 15.2, Requirement 15.1, p. 308)

> **Definition 15.2.** A system of beliefs $\mu$ assigns to every information set $h$ a probability
> distribution over its decision nodes: $\mu(x)\in[0,1]$ for $x\in h$, and
> $\sum_{x\in h}\mu(x)=1$ for every $h\in H$.
>
> **Requirement 15.1.** Every player has a well-defined belief over where he is in each of his
> information sets.

In the entry game the entrant's information sets are singletons (trivial beliefs); the incumbent
holds $\mu(x_3)=\Pr\{C\mid E\}$ and $1-\mu(x_3)=\Pr\{W\mid E\}$.

---

## 3 · C — Bayes' rule on the path (Requirement 15.2, p. 309)

Let type $C$ enter with probability $\sigma_C$ and type $W$ with $\sigma_W$ (pure strategies are
the cases $\sigma\in\{0,1\}$). Write the event "competitive and entered" and apply the definition
of conditional probability:

$$\mu(x_3)=\Pr\{C\mid E\}=\frac{\Pr\{C\text{ and }E\}}{\Pr\{E\}}
=\frac{\Pr\{C\}\Pr\{E\mid C\}}{\Pr\{C\}\Pr\{E\mid C\}+\Pr\{W\}\Pr\{E\mid W\}}
=\frac{p\,\sigma_C}{p\,\sigma_C+(1-p)\,\sigma_W}.$$

| Entrant's strategy | $\sigma_C$ | $\sigma_W$ | $\mu(x_3)$ |
|---|---|---|---|
| $EO$ | 1 | 0 | $\dfrac{p}{p}=1$ |
| $OE$ | 0 | 1 | $0$ |
| $EE$ | 1 | 1 | $p$ — **pooling teaches nothing** |
| $OO$ | 0 | 0 | $\tfrac00$: **undefined** |
| $\sigma_C=\tfrac12,\ \sigma_W=\tfrac14,\ p=\tfrac13$ | | | $\dfrac{1/6}{1/6+1/6}=\tfrac12$ |

> **Requirement 15.2.** Given a BNE profile $\sigma^*$, beliefs at every information set **on the
> equilibrium path** are consistent with Bayes' rule.

Two constraints enter the formula (pp. 308–309): an **exogenous** one (Nature's prior $p$) and an
**endogenous** one (the conjectured strategy $\sigma$). Beliefs are "correct" in the same sense in
which Nash equilibrium makes beliefs about strategies correct.

---

## 4 · C — off the path anything goes; then best-respond (Requirements 15.3–15.4, p. 310)

> **Requirement 15.3.** At information sets **off** the equilibrium path, any belief can be
> assigned, since Bayes' rule does not apply.
>
> **Requirement 15.4.** Given their beliefs, players' strategies are sequentially rational: at
> every information set $h$ of player $i$,
> $$E[v_i(\sigma_i^*,\sigma_{-i}^*,\theta_i)\mid h,\mu]\ \ge\ E[v_i(s_i,\sigma_{-i}^*,\theta_i)\mid h,\mu]\quad\text{for all }s_i\in S_i .$$

> **Definition 15.3.** A BNE profile $\sigma^*$ together with a system of beliefs $\mu$ is a
> **perfect Bayesian equilibrium** if they satisfy Requirements 15.1–15.4.

---

## 5 · Worked — the entry game, settled (pp. 310–311)

**Candidate $(OO,F)$.** The information set after $E$ is off the path, so by Requirement 15.3 any
$\mu(x_3)\in[0,1]$ is allowed. Requirement 15.4 asks whether $F$ is a best reply to *some* belief:

$$E[v_2(A)\mid\mu]=\mu\cdot1+(1-\mu)\cdot1=1,\qquad E[v_2(F)\mid\mu]=\mu(-1)+(1-\mu)\cdot0=-\mu .$$

$1>-\mu$ for every $\mu\in[0,1]$ (the gap is at least 1: right panel of the figure in
[[L08-01-subgame-perfection-fails]] §2). **No belief supports $F$**, so $(OO,F)$ is **not** a PBE.

**Candidate $(EO,A)$.** Every information set is reached; Bayes gives $\mu(x_3)=1$ (only $C$
enters). Check each information set:

| Who, where | Belief | Prescribed | Payoff | Alternative | Payoff |
|---|---|---|---|---|---|
| Incumbent after $E$ | $\mu=1$ | $A$ | $1$ | $F$ | $-1$ |
| Entrant, type $C$ | — | $E$ | $1$ (then $A$) | $O$ | $0$ |
| Entrant, type $W$ | — | $O$ | $0$ | $E$ | $-1$ (then $A$) |

All strict: $\boxed{(EO,A),\ \mu(x_3)=1}$ **is the unique pure PBE.**

> **What did the work was not Bayes' rule — the belief was unrestricted — but the requirement
> to *have* a belief and to best-respond to it at an unreached information set.**

---

## 6 · C — Proposition 15.1: when every information set is reached (p. 311)

> **Proposition 15.1.** If a (possibly mixed) profile $\sigma^*$ is a BNE of a Bayesian game
> $\Gamma$ and induces **every** information set to be reached with positive probability, then
> $\sigma^*$ together with the belief system derived from $\sigma^*$ and the type distribution
> by Bayes' rule is a PBE of $\Gamma$.

**Proof, every step.** Suppose not: $\sigma^*$ is a BNE, all information sets are reached, but
$(\sigma^*,\mu)$ is not a PBE.

1. Requirements 15.1–15.3 hold by construction: every information set has a belief, and each is
   given by Bayes' rule because each is on the path ($\Pr\{h\}>0$, so the denominator is
   positive).
2. So Requirement 15.4 must fail: some player $i$ at some information set $h$ is not best
   responding to $\mu(h)$.
3. Because $h$ is reached with positive probability, player $i$ could switch to the better
   action at $h$ and **raise his ex-ante expected payoff** by $\Pr\{h\}\times(\text{gain at }h)>0$.
4. That is a profitable deviation from $\sigma^*$ in the Bayesian game — contradicting that
   $\sigma^*$ is a BNE. $\blacksquare$

> **Off-path information sets are the *only* place where BNE and PBE can differ.** A BNE's only
> licence to play badly is at information sets it never reaches, because there a bad action
> costs nothing ex ante. PBE withdraws that licence.

**How to use it (p. 311).** (i) Find the BNE (the matrix of
[[L08-01-subgame-perfection-fails]] §2.3); (ii) for each, compute beliefs on the path by Bayes;
(iii) if nothing is off the path, Prop. 15.1 finishes; otherwise (iv) look for an off-path
belief that makes the prescribed off-path action a best reply. In signaling games one usually
works directly: **guess a sender strategy, derive beliefs, derive the receiver's best replies,
pick supporting off-path beliefs, check the sender's incentive constraints** (note 04, §3).

---

## 7 · G — "weak" PBE, and Bayes' rule *where possible* off the path (Remark, Fig. 15.3, pp. 311–312)

Requirement 15.3 puts **no** restriction off the path, which is why some texts call Tadelis's
concept **weak perfect Bayesian equilibrium** (MWG Def. 9.C.3, p. 285). A stronger version asks for
Bayes' rule **"where possible"** even off the path.

Fig. 15.3: player 1 chooses $L$ (to player 2) or $R$ (to player 3); players 2 and 3 each choose
between two actions ($A/B$ and $C/D$); player 4 then moves at two information sets, one after
player 2's move and one after player 3's, not seeing which action was taken. Let the profile have
1 play $L$, 2 play $A$ with probability $\sigma_A$ and 3 play $C$ with probability $\sigma_C$.

- Player 4's information set after player 2 is on the path: $\mu_A=\sigma_A$ by Bayes.
- The one after player 3 is off the path (1 never plays $R$): Requirement 15.3 allows anything.
  But if player 4 finds himself there, **only player 1 has deviated**; there is no reason to
  think player 3 deviated too, so the natural belief is $\mu_C=\sigma_C$.

Gibbons builds this into his definition (Requirement 4, p. 180: *"At information sets off the
equilibrium path, beliefs are determined by Bayes' rule and the players' equilibrium strategies
where possible"*), and shows with Fig. 4.1.4 (pp. 180–181) why it matters: there the strategies
$(A,L,L')$ with belief $p=0$ satisfy his Requirements 1–3 and are a Nash equilibrium, **but not
subgame perfect** — player 3's belief contradicts player 2's strategy $L$, and Requirement 4
forces $p=1$, after which player 3 must play $R'$.

| Gibbons (pp. 177–180) | Tadelis (pp. 308–310) | Content |
|---|---|---|
| Requirement 1 | Requirement 15.1 (+ Def. 15.2) | a belief at every information set |
| Requirement 2 | Requirement 15.4 | sequential rationality given beliefs |
| Requirement 3 | Requirement 15.2 | Bayes' rule on the path |
| Requirement 4 | — (Tadelis's 15.3 is weaker) | Bayes' rule off the path **where possible** |

> **In a two-stage signaling game the distinction is moot**: the receiver's off-path information
> sets follow messages no type sends, so Bayes' rule is never "possible" there — Gibbons notes
> Requirement 4 is vacuous in signaling games (p. 186). Everything examinable in notes 04–08 is
> the same under both definitions.

**MWG (G).** Def. 9.C.1 (p. 283) is the belief system; Def. 9.C.2 (p. 284) sequential rationality
via $E[u_i\mid H,\mu,\sigma_i,\sigma_{-i}]$; Def. 9.C.3 (p. 285) the weak PBE. Not examinable
beyond what Tadelis states.

---

## Links

- Prev: [[L08-01-subgame-perfection-fails]] · Next: [[L08-03-sequential-equilibrium]].
- The signaling-game version of these requirements: [[L08-04-signaling-games]] §2.
- Bayesian games and BNE (the input to Prop. 15.1): [[../L07/L07-00-map|Lecture 7]].
- Rules: [[../../rules/game-theory|rules/game-theory]] item 9 ("beliefs consistent with Bayes' rule
  wherever possible").
- Code: `posterior` and the entry-game check in [[L08-11-python]] §1–2.
- Exercises (number and page only): Tadelis 15.1–15.2 (p. 314), 15.3 (p. 315), 15.4–15.5
  (p. 316); Gibbons Problems 4.1–4.2 (p. 245); Muñoz-Garcia Ch. 9 Exercise 1 (p. 376).
