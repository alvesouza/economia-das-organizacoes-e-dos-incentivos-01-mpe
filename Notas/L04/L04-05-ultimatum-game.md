---
tags: [notes, lecture-04, bargaining, ultimatum-game, subgame-perfect-equilibrium]
date: 2026-10-16
status: estimated
source: "Tadelis (2013) Ch. 11 intro and §11.1, printed pp. 220–224: the alternating-offer protocol (pp. 220–221), Figure 11.1 (p. 222), Propositions 11.1–11.2, footnote 1 and the experimental Remark (pp. 223–224)"
---

# 11 intro · 11.1 · The ultimatum game: Nash says anything, subgame perfection says everything

> **Claim.** With one round of bargaining, **every** split of the pie is a Nash equilibrium,
> because the responder can "threaten" to reject small offers. Sequential rationality kills those
> threats: a responder offered something positive accepts it, so the proposer takes the whole pie.
> **The gap between the two answers is the case for subgame perfection in bargaining.**

Prev: [[L04-04-two-stage-applications]] · Next: [[L04-06-finite-alternating-offers]] · Map: [[L04-00-map]]

---

## 1 · C — the bargaining protocol (Ståhl, Rubinstein; pp. 220–222)

Two players split a pie of size 1 (it stands for the gains from trade). Every rejection shrinks
the pie by the discount factor $0<\delta<1$: in period $t$ it is worth $\delta^{t-1}$ (p. 221).

| Round | Proposer | Offer $(x,1-x)$ | Responder | Accept: payoffs |
|---|---|---|---|---|
| 1 | player 1 | $x$ to 1, $1-x$ to 2 | player 2 | $(x,\ 1-x)$ |
| 2 | player 2 | $x$ to 1, $1-x$ to 2 | player 1 | $(\delta x,\ \delta(1-x))$ |
| $t$ | 1 if $t$ odd, 2 if even | same convention | the other | $(\delta^{t-1}x,\ \delta^{t-1}(1-x))$ |

**Convention:** $x$ is always *player 1's* share, whoever proposes (Gibbons uses the same
convention with $s_t$, p. 69). If round $T$ ends without agreement, both get 0, a **hard deadline**
(Tadelis's fisherman and restaurateur, p. 221).

**How it differs from a repeated game (p. 221):** the game can **end in any round**, and payoffs
arrive **only at agreement**, not as a flow.

---

## 2 · C — Proposition 11.1: any split is a Nash equilibrium (p. 223)

> **Proposition 11.1.** In the bargaining game, if $T=1$ then any division of surplus
> $x^*\in[0,1]$, $(v_1,v_2)=(x^*,1-x^*)$, can be supported as a Nash equilibrium.

**Proof.** Player 1: "propose $x^*$". Player 2: "accept any $x\le x^*$, reject any $x>x^*$".

- Given player 2's rule, any $x>x^*$ yields 0 and any $x<x^*$ yields less than $x^*$; so $x^*$ is a
  best response.
- Given $x^*$ is offered, accepting yields $1-x^*\ge0$ and rejecting 0; so the rule (which accepts)
  is a best response. **The rule's rejections are never tested on the path.** $\blacksquare$

> **Nash equilibrium "has no bite" here (p. 223): it rationalizes every division.**

---

## 3 · C — Proposition 11.2: the unique SPE gives the proposer everything (p. 223)

**The flaw in §2.** Player 2's rule says "there is a minimum I accept". If offered $1-x=\varepsilon>0$
below that minimum, rejecting yields 0 and accepting $\varepsilon>0$. **Rejecting a positive offer is
not sequentially rational.** So in any SPE player 2 accepts every $x<1$.

> **Proposition 11.2.** The bargaining game with $T=1$ admits a unique subgame-perfect
> equilibrium, in which player 1 offers $x=1$ and player 2 accepts any offer $x\le1$.

**Proof, both cases.**

1. Player 2 accepts every $x<1$ (above). At $x=1$ she is indifferent.
2. *If she accepts $x=1$:* player 1's unique best response is $x=1$. This is the SPE.
3. *If she rejects $x=1$* (accepts only $x<1$): player 1 has **no best response**. Any $x'<1$ is beaten
   by $x''=x'+\frac{1-x'}{2}$, which is still below 1 and still accepted (footnote 1, p. 223); the
   supremum 1 is not attained. So this strategy cannot be part of an SPE. $\blacksquare$

| Concept | Prediction for $T=1$ |
|---|---|
| Nash equilibrium | any $(x^*,1-x^*)$, $x^*\in[0,1]$ |
| **Subgame-perfect equilibrium** | **$(1,0)$**, unique |

> **The responder's indifference at $x=1$ is resolved in favour of accepting, not by assumption but
> because the alternative leaves the proposer without a best response.** MWG make the same point
> (footnote 16, p. 297): with offers on a penny grid the proposer keeps the pie minus one penny,
> and the outcome converges to $(1,0)$ as the penny shrinks.

**Worked: the same in money (illustrative numbers).** A buyer and a seller have gains from trade of $\$1{,}000$; the
seller makes a take-it-or-leave-it price offer. The SPE price extracts all $\$1{,}000$; any price
between the seller's cost and the buyer's value is a Nash outcome. The take-it-or-leave-it power
is worth the entire surplus.

---

## 4 · U — the experiments (Remark, pp. 223–224)

In laboratory ultimatum games proposers typically offer **25%–50%** of the pie, and responders
usually **reject** offers below about **20%–25%** (Camerer, 2003). Responders act with "spite": they
prefer nothing to a split that gives the proposer much more.

**How to read this.** The prediction assumed payoffs equal the money. If the responder's utility
also falls with the proposer's advantage, rejecting a small offer can be sequentially rational,
and the SPE of *that* game gives the responder a positive share. The game theory is fine; the
payoff specification changed. M&R's Food for Thought 5.1 (pp. 163–164) asks the organizational
version (fairness and vengeance in commitment), set as practice item 20 in
`Listas/pratica-aula-01-02.md`.

---

## 5 · C — the indifference convention, carried forward

Every backward-induction step in notes 06–07 repeats §3: **the responder accepts when
indifferent**, and the proposer offers *exactly* the responder's continuation value. Hold that
convention fixed; it is what makes the formulas closed-form.

---

## Links

- Next: [[L04-06-finite-alternating-offers]] (two rounds and more).
- Subgame perfection and non-credible threats: [[../L03/L03-00-map|Lecture 3]].
- Earlier treatment: `Aula/aula-02-notes.md` §5.2 ("Ultimatum (one round)").
- Python: [[L04-12-python]] §3. Pitfalls: [[L04-11-pitfalls]] items 6–7.
- **Exercises (number and page only):** Tadelis 11.1 (p. 236), 11.2 (p. 236); Muñoz-Garcia
  Ch. 4 Ex. 1 (p. 154).
