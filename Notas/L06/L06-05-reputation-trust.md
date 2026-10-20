---
tags: [notes, lecture-06, repeated-games, reputation, trust-game, relational-contracts]
date: 2026-10-16
status: estimated
source: "Tadelis (2013) §10.5 'Sequential Interaction and Reputation' and §10.5.1 'Cooperation as Reputation', pp. 204–205 (Fig. 10.1, footnotes 8–9); Milgrom & Roberts (1992) Ch. 8 'Reputations as Contract Enforcers', pp. 259–266: the elementary theory and the trust box (pp. 261–263, footnote 11), 'live and let live' (p. 264), 'Ambiguity, Complexity, and Limits of Reputations' (pp. 264–266)"
---

# 10.5.1, M&R pp. 259–266 · Reputation: trust that pays for itself

> **Claim.** In the one-shot trust game trust is never offered, because it would never be
> honoured. Repeat it and the trusted party honours trust **to keep being trusted**: honesty
> becomes an asset whose value is the stream of future business, and it is worth protecting
> iff $\delta\ge G/(V+G)$ — the temptation over the temptation plus the per-period value of
> the relationship. A *reputation* is that asset when the future partners are **different
> people who observe the past**. Its limits are the limits of the assumption that everyone can
> tell, cheaply and after the fact, whether the right thing was done.
> Prev: [[L06-04-punishments-price-wars]] · Next: [[L06-06-institutions-reputation]] · Map: [[L06-00-map]]

---

## 1 · C — Tadelis's trust game (pp. 204–205)

**One shot** (Fig. 10.1). Player 1 trusts ($T$) or not ($N$); if trusted, player 2 cooperates
($C$) or defects ($D$). Payoffs (player 1, player 2): $N\to(0,0)$, $(T,C)\to(1,1)$,
$(T,D)\to(-1,2)$. Backward induction: player 2 defects ($2>1$); anticipating it, player 1
does not trust ($0>-1$). The SPE outcome $(0,0)$ is Pareto-dominated by $(1,1)$.

**Infinitely repeated** (footnote 8: the stage game is sequential, but every extensive form
has a normal form, so the repeated-game machinery applies). Grim trigger:

- **Player 1:** trust in period 1, and keep trusting while no deviation from $(T,C)$ has
  occurred; after one, never trust again.
- **Player 2:** cooperate in period 1, and keep cooperating while no deviation from $(T,C)$
  has occurred; after one, defect forever.

**Off the path** each prescription is a best response to the other's (never trust; defect if
ever trusted). **On the path** player 1's stream of 1s beats 0s. Player 2 conforms iff the
stream of 1s beats 2 today and 0 after:

$$\frac{1}{1-\delta}\ \ge\ 2\iff 1\ge2-2\delta\iff\boxed{\delta\ge\tfrac12}\qquad(\text{p. 205})$$

Template: $v^c=1$, $v^d=2$, $v^p=0$, so $\delta^*=(2-1)/(2-0)=\tfrac12$.

> **Footnote 9, the trap.** Writing player 2's strategy as "cooperate as long as player 1
> trusts me" gives a Nash equilibrium that is **not** subgame-perfect — some off-path
> prescriptions are not best responses. Tadelis leaves the proof as Exercise 10.4 (p. 216).
> The lesson: a repeated-game strategy must say what to do **after every history**, including
> the ones the equilibrium never reaches.

![Left: the one-shot trust game tree, player 1 choosing N (0,0) or T, then player 2 choosing C (1,1) or D (-1,2), with the cooperative path in green; right: average payoff of honouring (flat at 1) and of cheating ((1-delta) 2) crossing at delta 1/2, and the guarantor's fee 0.1 crossing the same cheating line at 0.95](figures/L06-trust-game.png)
*Figure — the stage game and its two repeated-game thresholds: $\delta\ge1/2$ for the trusted
player (p. 205) and $\delta\ge0.95$ for a guarantor paid 0.1 a period who could pocket a bond
of 2 (p. 207, [[L06-06-institutions-reputation]] §1). Source: Tadelis Fig. 10.1, §10.5.1–10.5.2.*

The same dashed "cheat" line serves both players because both grab 2 once and get 0 after;
what differs is the flat line they give up — the trusted player's 1 against the guarantor's
0.1. A thinner stream of rents needs a far more patient keeper.

---

## 2 · C — Milgrom & Roberts's elementary theory (pp. 259–263)

**Setting.** Relational contracts — an authority relation, an employee who accepts direction
"within somewhat nebulous customary limits", a contractor who must handle rain delays and
discontinued fixtures (pp. 259–261) — leave one party relying on the other's good faith.
The **elementary theory** assumes contracts cannot specify what to do, **but the parties can
tell afterwards whether the right thing was done** (p. 261).

**The box** (p. 261): the offeror offers trust or not; the decision maker honours it or not.

| Offeror \ Decision maker | Honour trust | Don't |
|---|---|---|
| **Offer trust** | $V,\ V$ | $-L,\ V+G$ |
| **Don't offer** | $0,\ 0$ | $0,\ 0$ |

with $V,G,L>0$: honoured trust beats no trade ($V>0$), dishonouring pays $G$ extra, and the
offeror risks $L$. One shot: no trust (p. 262), the same unravelling as Tadelis's tree.

**The decision maker's speech** (p. 262): "trust me once … if I should ever fail to honor your
trust, you would never trust me again. For that very reason, it will actually be in my interest
… to honor your trust." Is it believable? Value a stream of $X$ per meeting as $NX$ today:

$$\text{honour forever: }NV,\qquad\text{cheat now: }V+G\text{ today, nothing after.}$$

**M&R's multiplier** (footnote 11, p. 263): meetings every $t$ periods at interest $r$,

$$N=\frac{1}{(1+r)^t-1}+1=\frac{(1+r)^t}{(1+r)^t-1}=\frac{1}{1-(1+r)^{-t}}=\frac{1}{1-\delta},\qquad\delta\equiv(1+r)^{-t}.$$

So the exact condition is

$$NV\ge V+G\iff(N-1)V\ge G\iff\frac{\delta}{1-\delta}V\ge G\iff\boxed{\delta\ge\frac{G}{V+G}}$$

— Tadelis's $\tfrac12$ when $V=G=1$.

> **M&R write the comparison as $NV>G$** (p. 263) — honouring is worth $NV$ against "only
> $G$" from cheating. Their box gives the cheater $V+G$ in the round he cheats; the exact
> one-shot-deviation comparison is $NV\ge V+G$. The two differ by one round's $V$ and agree
> in spirit (and almost in value when $N$ is large). In an exam, derive from the box.

### 2.1 · Worked — how often must you meet? ($r=10\%$ a year)

| Meetings | $\delta=(1.1)^{-t}$ | $N=1/(1-\delta)$ | honours iff $G\le(N-1)V$ |
|---|---|---|---|
| every year ($t=1$) | 0.909 | 11.0 | $G\le10V$ |
| every 5 years ($t=5$) | $1/1.6105=0.621$ | 2.64 | $G\le1.64V$ |
| every 20 years ($t=20$) | $1/6.727=0.149$ | 1.17 | $G\le0.17V$ |

**Frequency is patience**: a relationship renewed every year carries a temptation ten times
its per-meeting value; one renewed every twenty years almost none (compare Cabral's $f$ in
[[L06-03-bertrand-market-structure]] §3).

---

## 3 · C — many equilibria (M&R p. 263)

The trusting equilibrium is not the only one. **Never offer, never honour** is also an
equilibrium (it repeats the stage SPE). So is a third: the decision maker **cheats every
second time** trust is offered and the offeror keeps offering as long as there are never two
cheats in a row — an equilibrium if $L<V$ and rounds are frequent (the offeror's average over
a pair of rounds is $(V-L)/2>0$). "The hypothesis of Nash equilibrium rules out some
patterns of behavior but does not always lead to a unique prediction" (p. 263) — the folk
theorem of [[../L05/L05-00-map|Lecture 5]] in M&R's words.

---

## 4 · C — from relationship to reputation (M&R p. 263)

Nothing in §2 needs the offeror to be the **same** person each round. If the decision maker
faces a **series of different offerors**, each of whom trusts iff trust was honoured the last
time it was offered, his calculation is unchanged: he honours trust "to encourage future
trading partners to offer trust or, in other words, to maintain his or her **reputation for
honesty**." Two preconditions follow, and both are where reputations fail:

1. **Future partners observe the past** (the history must travel).
2. **They can judge it** — tell honoured from dishonoured trust.

A good reputation then attracts partners **and saves the cost of detailed contracts and of
legal enforcement**.

---

## 5 · U — "live and let live", 1914–1918 (M&R p. 264)

The same opposing battalions faced each other for long stretches on the Western Front: the
repeated game. Each side could reciprocate deadly fire, so "fire in earnest only if fired
upon" became an equilibrium — and to keep it one, each side **showed it could retaliate**
(German snipers cutting a hole in a cottage wall; artillery placing a few accurate shots)
while showing it would not fire unprovoked (Axelrod 1984). Commanders ended the truces with
commando raids that set off cycles of retaliation. **The punishment must be visibly feasible**,
and an outsider who can inject deviations can destroy the equilibrium.

---

## 6 · C — the limits of reputation (M&R pp. 264–266)

| Limit | Why it bites | What helps |
|---|---|---|
| **Ambiguity** — was it honourable? | if right behaviour were easy to judge, courts could enforce it cheaply; parties disagree about circumstances and about what would have worked | shared principles |
| **Outsiders must judge** | a reputation system asks a *series* of third parties to evaluate disputes they did not see — costly and error-prone | institutions that judge and broadcast ([[L06-06-institutions-reputation]]) |
| **The end game** | the relationship must be expected to last long enough that its value exceeds the gain from cheating; near a known end, reputation is worth little | explicit incentives, sale of the business |

**Corporate culture** as a fix for ambiguity (p. 265): simple, communicable rules that make
"the right thing" unambiguous — the 49ers' rule that an injured starter always gets his place
back (so injuries are not concealed); Nordstrom's story of cheerfully accepting returned tyres
it never sold. **Reputations and the law** (pp. 265–266): in Shasta County, neighbours settle
stray-cattle damage by community norms, not the law (Ellickson); "most contractual disputes
never reach a court of law."

**The end game, three cases** (p. 266):

- **CEOs near retirement**: career concerns weaken, so pay should become more sensitive to
  performance — Gibbons and Murphy found exactly that.
- **Selling the business**: a founder near retirement keeps the firm's reputation intact to
  get a higher price — the firm acts with a longer horizon than its owner (the brand-name
  logic of [[L06-06-institutions-reputation]] §2).
- **Bankruptcy**: customers of a failing firm claim the last deliveries were defective and
  refuse to pay in full — with the relationship ending, attitudes harden.

> **The end game is the finite-horizon unravelling of Lecture 5 in business form**: the
> final period cannot be rewarded, so it cannot be disciplined, and the problem creeps
> backwards. M&R Quantitative Exercise 4 (p. 286) asks it for a trust game played exactly
> twice.

---

## Links

- Previous: [[L06-04-punishments-price-wars]]. Next: [[L06-06-institutions-reputation]].
- Finite vs infinite repetition and the folk theorem: [[../L05/L05-00-map|Lecture 5]].
  Backward induction in the centipede game, the same unravelling:
  [`Listas/pratica-aula-01-02-solutions/item19.tex`](../../Listas/pratica-aula-01-02-solutions/item19.tex).
- Reputation as a substitute for commitment (M&R pp. 139–140), already in the Aula 2 notes:
  [`Aula/notes-aulas-01-02/part2.tex`](../../Aula/notes-aulas-01-02/part2.tex), section
  "Commitment, reputation and the ultimatum game".
- Rules: [[../../rules/06_racionalidade_limitada_contratos|rules/06]] ("Relational and
  implicit contracts"), [[../../rules/game-theory|rules/game-theory]] items 4 and 15.
- Code: [[L06-11-python]] §6. Synthesis: [[L06-08-relational-contracts]].
- Exercises: Tadelis 10.4 (p. 216), 10.12 (p. 219); M&R Quantitative Exercises 4–5 (p. 286).
