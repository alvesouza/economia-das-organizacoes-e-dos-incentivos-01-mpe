---
tags: [notes, lecture-02, existence, nash-theorem, fixed-point, brouwer, kakutani]
date: 2026-10-16
status: estimated
source: "Tadelis (2013) §6.4, printed pp. 117–123 (Nash's Existence Theorem p. 117; Brouwer p. 117, Fig. 6.5; Def. 6.9 and Fig. 6.6 pp. 118–119; Fact p. 120; Kakutani Theorem 6.1 p. 120; the 2×2 proof pp. 121–122); Gibbons (1992) §1.3.B pp. 41–48; MWG §8.D pp. 252–253 and Appendix A pp. 260–261 (G)"
---

# 6.4 · Nash's existence theorem: an equilibrium is a fixed point, and fixed points exist

> **Claim.** A profile is a Nash equilibrium **iff it is a fixed point of the joint best-response correspondence**
> $BR(\sigma)=BR_1(\sigma_{-1})\times\dots\times BR_n(\sigma_{-n})$. In a finite game, mixed strategies make the
> strategy space a **compact convex simplex** and expected payoffs **linear**, which delivers Kakutani's four
> conditions; so **every finite game has at least one Nash equilibrium, possibly mixed**. When the conditions fail
> (asymmetric Bertrand with continuous prices), existence can fail too.
>
> Prev: [[L02-08-iesds-rationalizability-revisited]] · Next: [[L02-10-formulas]] · Map: [[L02-00-map]]

---

## 1 · C — the theorem

**Theorem (Nash's Existence Theorem, p. 117).** Any $n$-player normal-form game with finite strategy sets $S_i$ for
all players has a Nash equilibrium in mixed strategies. (A pure equilibrium counts: pure strategies are degenerate
mixtures, footnote 8.)

Gibbons's statement (p. 45): in $G=\{S_1,\dots,S_n;u_1,\dots,u_n\}$, if $n$ is finite and each $S_i$ is finite, there
exists at least one NE, possibly in mixed strategies.

> **Sufficient, not necessary.** Cournot and the commons have infinite strategy sets and still have equilibria
> (constructed by hand, "following Cournot's lead", Gibbons p. 11). The theorem guarantees existence where we cannot
> construct.

---

## 2 · U — Brouwer in one dimension (p. 117, Fig. 6.5)

**Brouwer's Fixed-Point Theorem.** If $f:[0,1]\to[0,1]$ is continuous, some $x^*$ has $f(x^*)=x^*$.

*Why.* If $f(0)=0$ or $f(1)=1$ we are done. Otherwise $f(0)>0$ and $f(1)<1$: $f$ starts **above** the 45° line and
ends **below** it, so the continuous function $g(x)=f(x)-x$ goes from positive to negative and has a zero (the
intermediate value theorem). A function that **jumps** across the diagonal ($f_3$ in Fig. 6.5) need not cross it.

Each hypothesis matters (footnote 10, p. 121): on $(0,1)$ (not closed) $f(x)=\sqrt x$ stays above the diagonal with no
fixed point; on $[0,\tfrac13]\cup[\tfrac23,1]$ (not convex) $f=\tfrac34$ on the first piece and $\tfrac14$ on the second
jumps over the gap.

---

## 3 · C — equilibrium as a fixed point (pp. 118–120)

**Definition 6.9 (p. 119).** The collection of best-response correspondences $BR\equiv BR_1\times\dots\times BR_n$
maps the set of mixed profiles $\Delta S=\Delta S_1\times\dots\times\Delta S_n$ into its subsets: $BR:\Delta S\rightrightarrows\Delta S$.

**Fact (p. 120).** $\sigma^*$ is a Nash equilibrium **iff** $\sigma^*\in BR(\sigma^*)$.

*Why.* $\sigma^*\in BR(\sigma^*)$ says $\sigma_i^*\in BR_i(\sigma_{-i}^*)$ for every $i$, which is Def. 6.6 word for word.

**Worked — the §6.2.3 game (Fig. 6.6).** With $BR(q,p)=(BR_2(p),BR_1(q))$ and the correspondences of
[[L02-07-mixed-strategies]] §5:

| Point $(q,p)$ | $BR_1(q)$ | $BR_2(p)$ | $BR(q,p)$ | Fixed point? |
|---|---|---|---|---|
| $(0,1)$ | $q<\tfrac37\Rightarrow p=1$ | $p>\tfrac16\Rightarrow q=0$ | $(0,1)$ | **yes**: (M, R) |
| $(1,0)$ | $q>\tfrac37\Rightarrow p=0$ | $p<\tfrac16\Rightarrow q=1$ | $(1,0)$ | **yes**: (D, C) |
| $(\tfrac37,\tfrac16)$ | $[0,1]$ | $[0,1]$ | $[0,1]^2$ | **yes**: it contains itself |
| $(0.8,0.5)$ | $p=0$ | $q=0$ | $(0,0)$ | no |
| $(0.2,0.1)$ | $p=1$ | $q=1$ | $(1,1)$ | no |

---

## 4 · C — Kakutani, and why mixed strategies satisfy it (pp. 120–122)

**Theorem 6.1 (Kakutani's Fixed-Point Theorem, p. 120).** A correspondence $C:X\rightrightarrows X$ has a fixed point
$x\in C(x)$ if (1) $X$ is a non-empty, compact and convex subset of $\mathbb R^n$; (2) $C(x)$ is non-empty for all $x$;
(3) $C(x)$ is convex for all $x$; (4) $C$ has a closed graph.

Definitions (p. 120): **convex**: $\lambda x+(1-\lambda)y\in X$ for $x,y\in X$, $\lambda\in[0,1]$; **closed**: limits of
sequences in $X$ stay in $X$ ($(0,1]$ is not closed: $1/n\to0$); **compact**: closed and bounded; **closed graph**:
if $x_n\to x$, $y_n\in C(x_n)$ and $y_n\to y$, then $y\in C(x)$.

**The four conditions for any 2×2 game (pp. 121–122).**

| Condition | Why it holds |
|---|---|
| (1) $X=[0,1]^2$ | non-empty, convex, compact |
| (2) $BR$ non-empty | expected payoff is continuous (linear) in own mix on the compact $[0,1]$: a maximum exists (extreme value theorem) |
| (3) $BR$ convex-valued | by Prop. 6.1, if two mixes are best replies the player is indifferent between the pure strategies they use, so **every** mix between them is a best reply; $BR_i$ is $\{0\}$, $\{1\}$ or $[0,1]$ |
| (4) closed graph | if $q_n\in BR_2(p_n)$, i.e. $v_2(q_n,p_n)\ge v_2(q,p_n)$ for all $q$, and $(q_n,p_n)\to(\hat q,\hat p)$, continuity lets the inequality pass to the limit: $v_2(\hat q,\hat p)\ge v_2(q,\hat p)$, so $\hat q\in BR_2(\hat p)$ |

So $BR$ has a fixed point and **every 2×2 game has a NE**. With $m$ pure strategies the simplex
$\Delta_i=\{\sigma_i:\sigma_i(s_{ik})\in[0,1],\sum_k\sigma_i(s_{ik})=1\}$ is non-empty, compact and convex in $\mathbb R^m$,
and the same four arguments go through (pp. 122–123).

> **Mixed strategies are what make existence work.** A finite set of pure strategies is not convex, so condition (3)
> fails for pure best replies (Matching Pennies has no pure fixed point). Allowing mixtures convexifies the strategy
> space and turns indifference into a convex set of best replies (MWG footnote 5, p. 253).

---

## 5 · C — when existence fails: back to Bertrand

Asymmetric Bertrand with continuous prices ([[L02-04-bertrand]] §4) has infinite strategy sets **and** a payoff that
jumps at $p_1=p_2$, so firm 1's best-response set to $p_2=2$ is **empty**: condition (2) fails. Tadelis's choice
(p. 93) is to avoid such discontinuities, or restore discreteness, rather than to abandon NE.

---

## 6 · G — MWG's general statements

- **Prop. 8.D.2 (p. 252):** every game whose strategy sets $S_1,\dots,S_I$ are finite has a mixed-strategy NE.
- **Prop. 8.D.3 (p. 253):** a (pure) NE exists if each $S_i$ is a non-empty, convex, compact subset of some $\mathbb R^M$
  and $u_i$ is **continuous** in all strategies and **quasiconcave** in $s_i$. Cournot and the commons satisfy it;
  homogeneous Bertrand violates continuity.
- **Appendix A (pp. 260–261):** Lemma 8.AA.1 shows $b(\cdot)$ is non-empty, convex-valued and upper hemicontinuous; Kakutani
  then gives Prop. 8.D.3, and Prop. 8.D.2 follows by applying 8.D.3 to the mixed extension.

Not examinable unless the lecture states it.

---

## Links

- Neighbours: [[L02-07-mixed-strategies]] (Prop. 6.1, used for convexity), [[L02-04-bertrand]] (non-existence).
- Lecture 7 (existence in Bayesian games reuses the same fixed-point idea): [[../L07/L07-00-map|Lecture 7]].
- Code: [[L02-12-python]] §9 (fixed points of $BR$ on a grid).
- Practice: Gibbons 1.10 (pp. 50–51); Tadelis 6.10 (p. 125, the all-pay auction with no finite-support equilibrium).
