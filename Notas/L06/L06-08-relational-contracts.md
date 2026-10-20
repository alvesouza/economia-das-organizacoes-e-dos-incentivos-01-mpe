---
tags: [notes, lecture-06, repeated-games, relational-contracts, synthesis]
date: 2026-10-16
status: estimated
source: "Synthesis of Tadelis (2013) §10.4–10.5, pp. 201–209; Gibbons (1992) §2.3.C–D, pp. 102–112; Cabral (2017) §9.1–9.3, pp. 218–231; Milgrom & Roberts (1992) Ch. 8, pp. 250–268 (relational contract defined p. 259)"
---

# Synthesis · A relational contract is a self-enforcing promise

> **Claim.** A *relational contract* — M&R's term for an agreement that leaves decisions to
> discretion and relies on good faith (p. 259) — is enforced not by a court but by **the value
> of the relationship itself**. Every case in this lecture is one inequality with four
> numbers: the per-period value of cooperating, the best one-period gain from cheating, what is
> left after the breakdown, and $\delta$. Organizational design is the art of moving those
> four numbers.
> Prev: [[L06-07-efficiency-wages]] · Next: [[L06-09-formulas]] · Map: [[L06-00-map]]

---

## 1 · C — the four cases side by side

$$\text{cooperation is self-enforcing}\iff
\underbrace{v^d-v^c}_{\text{gain from cheating today}}\ \le\ \frac{\delta}{1-\delta}\,\pi_{\text{det}}\,\underbrace{(v^c-v^p)}_{\text{per-period stake}}$$

with $\pi_{\text{det}}=1$ under perfect monitoring.

| Relationship | $v^c$ | $v^d$ | $v^p$ | $\delta^*$ (book's numbers) | Note |
|---|---|---|---|---|---|
| Cournot cartel, symmetric | $(a-c)^2/8$ | $9(a-c)^2/64$ | $(a-c)^2/9$ | $9/17=0.529$ | [[L06-02-cournot-collusion]] |
| Cournot cartel, 22/23 split | 990 / 1035 | 1122.25 / 1156 | 900 | $0.595$ / $0.473$ | [[L06-02-cournot-collusion]] §2 |
| Bertrand cartel, $n$ firms | $\pi_M/n$ | $\pi_M$ | 0 | $1-1/n$ | [[L06-03-bertrand-market-structure]] |
| Trust game (trusted party) | $V=1$ | $V+G=2$ | 0 | $G/(V+G)=1/2$ | [[L06-05-reputation-trust]] |
| Guarantor / law merchant | fee $0.1$ | bond $2$ | 0 | $0.95$ | [[L06-06-institutions-reputation]] |
| Efficiency wage (worker) | $w^*-e$ | $w^*$ (no effort), caught w.p. $1-p$ | $w_0$ | $w^*\ge w_0+e+\frac{(1-\delta)e}{\delta(1-p)}$ | [[L06-07-efficiency-wages]] |

---

## 2 · C — the design levers

| Lever | Moves | Example in this lecture |
|---|---|---|
| **Raise the stake** $v^c-v^p$ | denominator up | efficiency-wage rent; a brand's resale value; a harsher (Abreu) punishment |
| **Cut the temptation** $v^d-v^c$ | numerator down | most-favoured-customer clauses; a bond that is lost on cheating; sharing a cartel so no member is "worse treated" |
| **Raise $\delta$** | patience up | frequent interaction ($f$), stable market (low $h$), growth ($g$) — Cabral (9.5); lifetime employment |
| **Raise detection** | $\pi_{\text{det}}$ up | monitoring $M(p)$; credit bureaus; the Maghribi correspondence; transparent prices |
| **Make judging easy** | removes ambiguity | corporate culture's simple rules; private judges |
| **Remove the end** | no terminal period | sale of the business, brand names that outlive owners |

> **Every lever has a social sign.** The same levers that let a firm buy honesty from its
> workers let competitors keep prices high — which is why antitrust attacks transparency
> devices (GE's price book, Cabral Box 9.5) that a personnel manager would welcome.

---

## 3 · C — when relational contracts fail

1. **A known last period** — the end game (M&R p. 266) and finite-horizon unravelling
   ([[../L05/L05-00-map|Lecture 5]]).
2. **Too little patience** — $\delta<\delta^*$; a financially weak firm whose $\delta$ falls
   starts the war (Cabral p. 226).
3. **Nothing to lose** — a party with zero stake (the high-cost firm in an efficient cartel;
   a worker whose next job is as good) cannot be disciplined at any $\delta$.
4. **Noisy monitoring** — punishments must fire on bad luck too: price wars on the path
   (Green–Porter).
5. **Renegotiation** — a punishment both parties would rather skip is not credible.
6. **Ambiguity** — when nobody can tell whether the right thing was done, there is nothing to
   condition the punishment on.

---

## 4 · U — where this sits in the course

Relational contracts are the bridge between the **complete-information repeated games** of
Lectures 5–6 and the **incomplete contracts** of M&R Ch. 5: a contract can be incomplete
(courts cannot verify effort, quality or honour) and still be enforced, because the parties
themselves can see enough to punish. Lectures 7–8 drop complete information: then reputation
becomes a **belief about a type** (Tadelis Ch. 17, background only) rather than a strategy
profile.

## Links

- Map [[L06-00-map]] · formulas [[L06-09-formulas]] · pitfalls [[L06-10-pitfalls]].
- Rules: [[../../rules/06_racionalidade_limitada_contratos|rules/06]] ("Relational and
  implicit contracts"), [[../../rules/game-theory|rules/game-theory]].
- Next lectures: [[../L07/L07-00-map|Lecture 7]], [[../L08/L08-00-map|Lecture 8]].
