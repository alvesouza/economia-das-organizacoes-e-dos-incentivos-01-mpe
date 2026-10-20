---
tags: [notes, lecture-06, repeated-games, reputation, institutions, law-merchant, brand-names]
date: 2026-10-16
status: estimated
source: "Tadelis (2013) §10.5.2 'Third-Party Institutions as Reputation Mechanisms', pp. 205–207 (Fig. 10.2, footnote 10) and §10.5.3 'Reputation Transfers without Third Parties', pp. 207–209; Milgrom & Roberts (1992) Ch. 8, pp. 252, 258–259 (Maghribi traders, brand names) and 'The Advanced Theory: Reputations Aided by Institutions', pp. 266–268"
---

# 10.5.2–10.5.3, M&R pp. 266–268 · When the traders are strangers: borrowed reputations

> **Claim.** One-shot traders cannot discipline each other, but a **long-lived third party**
> can: a guarantor holding a bond, a judge, a brand name passed from owner to owner. The
> repeated game moves from the traders to the institution, and the institution's own
> no-cheating condition is the same inequality — with a thin per-period rent it needs a very
> high $\delta$ (0.95 in Tadelis's example). Reputation is then not a trait of a person but an
> **asset that can be held, sold and lost**.
> Prev: [[L06-05-reputation-trust]] · Next: [[L06-07-efficiency-wages]] · Map: [[L06-00-map]]

---

## 1 · C — the guarantor (Tadelis pp. 205–207)

**A bond fixes the one-shot game** (Fig. 10.2). Player 2 deposits 2 with a guarantor (player
3) under the contract "if player 1 trusts me and I defect, you keep the 2; otherwise return
it". If the guarantor **must** follow the contract, defecting nets player 2
$2-2=0<1$: he cooperates, player 1 trusts, and the unique SPE is cooperative trade.

**Two objections** (p. 206): why would such a committed guarantor exist; and if player 3 is a
real player, his dominant strategy is to **keep** the deposit.

**The repeated-game answer.** Player 3 is a long-lived local official — a judge, an arbitrator
— with discount factor $\delta$. In each period $t$ a **new** pair $P_1^t,P_2^t$ arrives and
plays the trust game once. $P_2^t$ may post a bond of 2 with player 3 for a fee $w=0.1$.

| Player | Strategy (Tadelis pp. 206–207) |
|---|---|
| $P_1^t$ | trust iff $P_2^t$ posted a bond |
| $P_2^t$ | post a bond iff player 3 has honoured the bond contract in every earlier period; if a bond was posted, cooperate, otherwise defect |
| player 3 | return the bond to a $P_2^t$ who cooperated; keep it otherwise |

**Traders.** Given player 3's strategy, each pair plays Fig. 10.2: with the bond, $P_2^t$
gets $1-0.1=0.9$ by cooperating against $2-2-0.1=-0.1$ by defecting — he cooperates and
posts the bond ($0.9>0$).

**The guarantor.** Honour: $0.1$ every period. Cheat: keep the bond, 2 once, then no trader
ever posts again:

$$\frac{0.1}{1-\delta}\ \ge\ 2\iff0.1\ge2-2\delta\iff\boxed{\delta\ge0.95}\qquad(\text{p. 207})$$

Template: $v^c=0.1$, $v^d=2$, $v^p=0$: $(2-0.1)/2=0.95$.

> **Footnote 10, the design margin.** The bond need only exceed **1**, player 2's one-period
> gain from defecting; and a trader would pay any fee up to **1** for the service. Fee and bond
> are the institution's two dials: a higher fee raises the guarantor's stake in his reputation,
> a smaller bond lowers his temptation. Exercise 10.10 (p. 219) pushes this to its limit.

**History** (p. 207): Milgrom, North and Weingast (1990) — the **law merchants** of medieval
Europe as such third parties; future traders "somehow learned about the law merchant, and
about his past adherence" to the norms. Greif (2006) surveys institutions and trade.

---

## 2 · C — brand names: a reputation you can sell (Tadelis pp. 207–209)

**Kreps (1990b).** Drop the third party. Before period 1, $P_2^1$ can create a unique **brand
name** ("Trusted Associates") and sell it to the next period's player 2 at a price $p^*>1$.
Strategies (p. 208), in outline: player 1 trusts a brand that was **bought** and under which
**no abuse of trust ever occurred**; each player 2 buys the clean brand, cooperates, and sells
it on at $p^*$.

**Why it works** (Tadelis: "The investment made in the name … acts like a bond"). The brand
is worth $p^*$ to its holder only while it is clean. Cheating earns one extra unit today
(2 instead of 1) and destroys a resale value of $p^*>1$. Short-lived owners become, through
the name, an **infinitely lived** player — "the concept of a terminal period is removed
altogether". Proving the profile is an SPE is Exercise 10.11 (p. 219).

**Roots:** Klein and Leffler (1981), a firm's brand value as a bond for its performance;
Crémer (1986), a firm sustaining cooperation among employees who come and go (p. 208).

> **The open question** (pp. 208–209): bootstrap equilibria say nothing about **how**
> reputations arise or why their value rises and falls. Tadelis's remark: *The Princess Bride*'s
> Dread Pirate Roberts is a name handed from captain to captain — "no one would surrender to the
> Dread Pirate Westley."

**M&R's product-market version** (p. 259): Klein and Leffler — "thin profit margins are the
enemy of quality"; with recognizable products and high margins, the value of staying in
business outweighs the short-run gain from degrading quality. A brand covering a whole product
line extends the reputation to products replaced too fast for their own track record to
matter (the Black & Decker drill).

---

## 3 · C — institutions that make reputations work (M&R pp. 266–268)

M&R's **advanced theory**: when people specialize, transactions with any one partner are
infrequent and the elementary theory's repeated relationship is missing. Two responses:
replace reputation with the **legal system** (general rules, slow, costly, sometimes without
authority across borders), or **buttress** reputation with private institutions:

| Institution | What it does in the model | M&R |
|---|---|---|
| **Law merchant** — private judges, *lex mercatoria* | **judges** disputes and **broadcasts** offenders: the outsider's two hard tasks (§6 of [[L06-05-reputation-trust]]) | p. 267 |
| Whalers' "gam" | captains exchange information on disputes at sea; US whalers in a few towns needed none — no recorded court case over whale ownership until rents fell in the late 19th century | pp. 267–268 |
| Better Business Bureau, credit bureaus, consumer agencies | collect and **disseminate** past behaviour, raising the cost of cheating | p. 268 |
| Merchant guilds, the Hansa | coordinate **sanctions** — an embargo of a city that reneged — against the free-rider problem of individual sanctioners | p. 268 |

**The Hansa, worked as an incentive problem** (p. 268). In 1280 the guild trading in Bruges
moved its trade to Aardenburg; Bruges broke the embargo by offering special terms to merchants
from various towns. Each merchant's gain from breaking the embargo was private, the cost
(a weaker threat) shared — a free-rider problem. The Hansa added a **second-order sanction**:
traders who broke a declared embargo could have their **home city** embargoed, which made
complying individually rational again.

**The Maghribi traders** (M&R pp. 252, 258; Greif 1989). Eleventh-century merchants in Fustat
ostracized an agent who cheated **any** of them. In the efficiency-wage formula of
[[L06-07-efficiency-wages]] §6 this **lowers the cheater's outside option** $\bar w$ and
**raises the multiplier** $N$ (all merchants' business is lost, not one), and the web of
correspondence **raises detection** $p$. Overseas agency became cheaper to motivate as the
network grew.

---

## Links

- Previous: [[L06-05-reputation-trust]]. Next: [[L06-07-efficiency-wages]].
- Institutions and incomplete contracts: [[../../rules/06_racionalidade_limitada_contratos|rules/06]].
- Code: [[L06-11-python]] §6 (the 0.95 check). Formulas: [[L06-09-formulas]] §2.4.
- Exercises: Tadelis 10.10, 10.11 (p. 219).
