---
tags: [notes, lecture-04, bargaining, private-information, organizations]
date: 2026-10-16
status: estimated
source: "Milgrom & Roberts (1992) Ch. 5 'Bargaining over a Sale', printed pp. 140–142, Tables 5.2–5.3; Gibbons (1992) §2.1.D opening paragraph, p. 68; Tadelis (2013) Remark, p. 229"
---

# M&R · Bargaining over a sale: where the complete-information prediction stops

> **Claim.** Notes 05–08 predict **immediate, efficient agreement** whenever values are common
> knowledge (Proposition 11.3). M&R's two-type example shows the prediction depends on that
> assumption: once each side privately knows its own value, **no price rule** can make both report
> truthfully *and* trade whenever trade is efficient. The seller needs $p\ge\$1.75$, the buyer
> $p\le\$1.25$. Bargaining power then decides more than the split; it decides whether value is created.

Prev: [[L04-08-legislative-bargaining]] · Next: [[L04-10-formulas]] · Map: [[L04-00-map]]

> **Layer.** U (application), from the study guide's "Applications" line. The general theory behind
> it, mechanism design and the revelation principle, is **out of scope** (`CLAUDE.md`); it is named
> here only so the result can be placed. Incomplete information proper is
> [[../L07/L07-00-map|Lecture 7]].

---

## 1 · U — the organizational point (M&R p. 140)

With no wealth effects the **value-creating** part of an agreement is determinate (the value
maximization principle, `Aula/aula-02-notes.md` §3); bargaining strength, patience and guile decide
only the **transfers**. That is exactly what Rubinstein's model delivers: the pie is never wasted and
$\delta$ sets the split. M&R's caveat: efficiency is defined relative to what is **feasible**, and what is
feasible depends on information.

---

## 2 · Worked — the example (pp. 140–142)

**Values.** Seller's value $0$ (prob. $0.8$) or $\$2$ (prob. $0.2$); buyer's value $\$1$ (prob. $0.2$)
or $\$3$ (prob. $0.8$). Each knows only its own value.

**Efficient outcome (Table 5.2).** Trade unless buyer $\$1$ and seller $\$2$, which has probability
$0.2\times0.2=0.04$. **Trade is efficient 96% of the time.**

**A mediator's prices (Table 5.3).** Look for prices that make truthful reports optimal:

| Reports | Price | Why |
|---|---|---|
| seller 2, buyer 3 | $\$2$ | a seller claiming 2 must get at least 2; more would only reward the claim |
| seller 0, buyer 1 | $\$1$ | a buyer claiming 1 cannot be asked more than 1 |
| seller 2, buyer 1 | no trade | inefficient |
| seller 0, buyer 3 | $p$ | to be found |

**Seller with value 0 (incentive compatibility).**

- Honest: she trades at $\$1$ with a low buyer (prob. $0.2$) and at $p$ with a high one (prob. $0.8$):
  $0.2(1)+0.8p$.
- Claims 2: no trade with a low buyer; $\$2$ with a high one: $0.2(0)+0.8(2)=1.60$.

$$0.2+0.8p\ge1.60\iff p\ge\frac{1.40}{0.8}=\mathbf{\$1.75}.$$

**Buyer with value 3.**

- Honest: pays $\$2$ against a high-value seller (prob. $0.2$), $p$ against a low one (prob. $0.8$):
  $0.2(3-2)+0.8(3-p)=2.60-0.8p$.
- Claims 1: trades only with the low seller, at $\$1$: $0.8(3-1)=1.60$.

$$2.60-0.8p\ge1.60\iff p\le\frac{1.00}{0.8}=\mathbf{\$1.25}.$$

> **$p\ge1.75$ and $p\le1.25$ cannot both hold. There is no price schedule under which both report
> truthfully and trade happens exactly when it is efficient (p. 142).** Footnote 8 adds that
> allowing misreporting does not help; that is where the revelation principle enters, out of scope
> here.

The same numbers are verified in `Aula/notes-aulas-01-02/check_part2.py` (block "M&R Table
5.2/5.3"), together with the reversed-probability case where efficient trade *is* feasible.

---

## 3 · U — the bridge back to the game theory

| | Complete information (notes 05–08) | Private values (this note) |
|---|---|---|
| Delay | never on the equilibrium path (Prop. 11.3) | can be a costly way to signal strength |
| Efficiency | always reached | can be unattainable by any rule |
| What bargaining power decides | the split | the split **and** whether trade happens |

Gibbons anticipates the same contrast when he opens §2.1.D (p. 68): in Rubinstein's model
"settlement occurs immediately", whereas in sequential bargaining under asymmetric information
strikes occur with positive probability (Sobel and Takahashi, 1983; his §4.3.B), which belongs with
[[../L08/L08-00-map|Lecture 8]]'s perfect Bayesian equilibrium.

> **For the organization designer: the complete-information model tells you how surplus is split
> once the parties can see it; the private-information example tells you why so much effort goes
> into making it visible** (audits, standard costs, third-party appraisals).

---

## Links

- Previous / next: [[L04-08-legislative-bargaining]] · [[L04-10-formulas]].
- Earlier material: `Aula/notes-aulas-01-02/main.pdf` part 2; `Listas/pratica-aula-01-02.md`
  block B3 (items 21–23, 30).
- Rules packs: [[../../rules/02_barganha|rules/02_barganha]], [[../../rules/07_selecao_adversa|rules/07_selecao_adversa]].
- Python: [[L04-12-python]] §5.
