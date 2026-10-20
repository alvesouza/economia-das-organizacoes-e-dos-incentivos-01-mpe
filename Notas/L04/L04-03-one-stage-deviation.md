---
tags: [notes, lecture-04, one-stage-deviation, subgame-perfect-equilibrium]
date: 2026-10-16
status: estimated
source: "Tadelis (2013) §9.5, printed pp. 184–186: Definition 9.1, Theorem 9.1 and its proof (eqs. 9.1–9.3); closing remark of §9.4, p. 184"
---

# 9.5 · The one-stage deviation principle: check one information set at a time

> **Claim.** To verify that a profile is subgame perfect in a finite game you never need to test
> combinations of deviations: if no player gains by changing his action at **one** information set
> and following his strategy everywhere else, no multi-stage deviation gains either. This is what
> made note 02's check a two-line inequality, and it is the workhorse of
> [[../L05/L05-00-map|Lecture 5]].

Prev: [[L04-02-carrot-and-stick]] · Next: [[L04-04-two-stage-applications]] · Map: [[L04-00-map]]

---

## 1 · U — the worry it removes (p. 184)

In a five-stage game a player might hope to gain by *combining* deviations: fink at stage 2 **and**
switch at stage 4. Checking every combination looks daunting. The principle, due to Blackwell
(1965) in dynamic programming, says it is unnecessary. Fixing the others' strategies
$\sigma_{-i}$, player $i$ faces a one-person decision tree, and in a finite decision tree a plan
that cannot be improved one node at a time cannot be improved at all (pp. 184–185).

---

## 2 · C — definition and theorem (p. 185)

Fix $\sigma_{-i}$. For an information set $h_i$ let $v_i(\sigma_i,h_i)$ be $i$'s expected payoff
from $h_i$ onward. $\sigma_i$ is **optimal** if no $\sigma_i'$ and $h_i$ give
$v_i(\sigma_i',h_i)>v_i(\sigma_i,h_i)$. Let $\hat\sigma_i^{a,h_i}$ be $\sigma_i$ with the action at
$h_i$ replaced by $a\in A_i(h_i)$.

> **Definition 9.1.** A strategy $\sigma_i$ is **one-stage unimprovable** if there is no information
> set $h_i$, action $a\in A_i(h_i)$ and corresponding strategy $\hat\sigma_i^{a,h_i}$ such that
> $v_i(\hat\sigma_i^{a,h_i},h_i)>v_i(\sigma_i,h_i)$.

> **Theorem 9.1.** A one-stage unimprovable strategy must be optimal.

(The converse, optimal $\Rightarrow$ one-stage unimprovable, is immediate.)

### 2.1 · The proof, step by step (pp. 185–186)

1. Suppose $\sigma_i$ is one-stage unimprovable but not optimal: some $\sigma_i'$ and $h_i^1$ have
   $v_i(\sigma_i',h_i^1)>v_i(\sigma_i,h_i^1)$.
2. Randomization cannot raise the best attainable payoff, so there is a **path** through finitely
   many of $i$'s information sets $h_i^1,\dots,h_i^n$ (the last a terminal node) that beats
   $\sigma_i$. Hence finitely many one-stage changes, at $h_i^1,\dots,h_i^{n-1}$, beat $\sigma_i$.
3. Let $\hat\sigma_i^t$ make the improving changes at $h_i^1,\dots,h_i^t$ and follow $\sigma_i$
   elsewhere. Then
   $$v_i(\hat\sigma_i^{n-1},h_i^1)>v_i(\sigma_i,h_i^1).\tag{9.1}$$
4. Look at the **last** change. From $h_i^{n-1}$ on, $\hat\sigma_i^{n-2}$ coincides with
   $\sigma_i$, and $\hat\sigma_i^{n-1}$ is a one-stage deviation from $\sigma_i$ there. Unimprovability
   gives
   $v_i(\hat\sigma_i^{n-2},h_i^{n-1})=v_i(\sigma_i,h_i^{n-1})\ge v_i(\hat\sigma_i^{n-1},h_i^{n-1})$.
   The two strategies agree before $h_i^{n-1}$, so
   $$v_i(\hat\sigma_i^{n-2},h_i^1)\ge v_i(\hat\sigma_i^{n-1},h_i^1).\tag{9.2}$$
5. (9.1) and (9.2) give $v_i(\hat\sigma_i^{n-2},h_i^1)>v_i(\sigma_i,h_i^1)$: the improvement survives
   with one change fewer. Repeat down to one change:
   $$v_i(\hat\sigma_i^{1},h_i^1)>v_i(\sigma_i,h_i^1),\tag{9.3}$$
   but $\hat\sigma_i^1$ is a single one-stage deviation, contradicting unimprovability.
   $\blacksquare$

> **Intuition (p. 186): look for the *last* profitable deviation in the sequence. In the subgame
> where it happens, it is a one-stage deviation that makes the player better off.** Peeling
> deviations off from the end is backward induction in disguise.

---

## 3 · C — how to use it

**Recipe (closing remark of §9.4, p. 184).** To check that $(\sigma_i,\sigma_{-i})$ is an SPE of a
finite game: for every player $i$, given $\sigma_{-i}$, show that $i$ has **no single information set**
at which changing the action alone pays.

**Worked: note 02's carrot and stick.** Player 1's information sets are stage 1 and the four stage-2
sets $Mm,Mf,Fm,Ff$.

| Information set | Prescribed | One-stage deviation | Compare | Verdict |
|---|---|---|---|---|
| stage 2 after $Mm$ | $L$ (2 plays $l$) | $G$ | $0$ vs $-1$ | no gain |
| stage 2 after $Mf,Fm,Ff$ | $G$ (2 plays $g$) | $L$ | $-3$ vs $-4$ | no gain |
| stage 1 | $M$ | $F$, **then follow $s_1$** (play $G$) | $4$ vs $5-3\delta$ | no gain iff $\delta\ge\frac13$ |

Five checks, each one line, instead of comparing $s_1$ with 31 alternative strategies.

> **The deviation is evaluated with the player's *own* strategy continuing afterwards.** At stage 1
> the deviator finks and then still plays $G$ after $Fm$, because $s_{12}(Fm)=G$. A combined deviation
> (fink, then $L$) is covered automatically: by the stage-2 row it is no better.

---

## 4 · G — finiteness, and what comes next

Theorem 9.1 is stated for trees of **finite length**. Tadelis announces (p. 184) that it will be
"even more useful" in Chapter 10, where the horizon is infinite. There the principle still holds
when payoffs are discounted ($\delta<1$), because what happens far in the future matters little
(continuity at infinity); that extension is stated and used in [[../L05/L05-00-map|Lecture 5]].
Without discounting it can fail: a player may gain only by deviating at infinitely many dates.

---

## Links

- Previous / next: [[L04-02-carrot-and-stick]] · [[L04-04-two-stage-applications]].
- Used again in: [[L04-07-rubinstein-infinite-horizon]] §3 (checking the Rubinstein strategies)
  and [[../L05/L05-00-map|Lecture 5]] (grim trigger).
- Backward induction in finite perfect-information games: [[../L03/L03-00-map|Lecture 3]].
- Pitfalls: [[L04-11-pitfalls]] item 4.
