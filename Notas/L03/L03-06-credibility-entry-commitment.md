---
tags: [notes, lecture-03, credibility, entry-deterrence, commitment, non-credible-threats]
date: 2026-10-16
status: estimated
source: "Cabral (2017) §7.2 (pp. 167–171): the sequential-entry game, Fig. 7.7; the value of credible commitment, Figs. 7.8–7.9; short run and long run, Fig. 7.10; MWG Example 9.B.1 (pp. 268–269) and Example 9.B.3 (§9.B); Gibbons (1992) pp. 127–128"
---

# Applications · Credible threats, entry deterrence and the value of commitment

> **Claim.** An incumbent's threat to fight an entrant can hold up a Nash equilibrium and still be
> empty, because once entry has happened fighting pays the incumbent less than sharing. Subgame
> perfection deletes that equilibrium. **The incumbent's remedy is to change its own payoffs before
> the entrant moves**, so that fighting becomes its best reply: a credible commitment. Cabral's numbers
> put the value of that commitment at 30, and it is earned by making one of the incumbent's own
> payoffs *worse*.
> Prev: [[L03-05-subgame-perfection]] · Next: [[L03-07-stackelberg]] · Map: [[L03-00-map]]

---

## 1 · C — the sequential-entry game (Cabral Fig. 7.7, p. 168)

A monopolized industry. Player 1 (the **entrant**) chooses $e$ (enter) or $\bar e$ (stay out). If it
enters, player 2 (the **incumbent**) chooses $r$ (retaliate: a price war) or $\bar r$ (accommodate).
Payoffs (entrant, incumbent):

| Path | Entrant | Incumbent |
|---|---|---|
| $\bar e$ (stay out) | 0 | 50 |
| $e$, $\bar r$ (accommodate) | 10 | 20 |
| $e$, $r$ (retaliate) | $-10$ | 10 |

*Source detail.* Fig. 7.7 prints $(-10,10)$ after a price war; the text on p. 168 says the incumbent
"would get $-10$" there. Every conclusion below holds for either value, since both are below 20 (the
incumbent prefers to accommodate) and above $-20$ (the bonded case of §3). The companion lets you check
both.

### 1.1 · Nash equilibria (p. 168)

| | $\bar r$ | $r$ |
|---|---|---|
| $e$ | $10,20$ | $-10,10$ |
| $\bar e$ | $0,50$ | $0,50$ |

- $(e,\bar r)$: given $e$, the incumbent gets 20 from $\bar r$ against 10 from $r$; given $\bar r$, the
  entrant gets 10 from $e$ against 0. **Nash.**
- $(\bar e,r)$: given $r$, the entrant gets 0 from $\bar e$ against $-10$ from $e$; given $\bar e$, the
  incumbent gets 50 whatever it plans, so $r$ is a best reply ("though not the only one"). **Nash.**

### 1.2 · Only one survives (p. 169)

The second equilibrium rests on the incumbent's plan to retaliate at a node that $\bar e$ never reaches.
**Is the threat credible?** If the entrant did enter, the incumbent would compare 10 (retaliate) with
20 (accommodate) and accommodate. Backward induction:

| Step | Node | Comparison | Choice |
|---|---|---|---|
| 1 | incumbent after $e$ | $\bar r$: 20 vs $r$: 10 | $\bar r$ |
| 2 | entrant | $e$ then $\bar r$: 10 vs $\bar e$: 0 | $e$ |

$$\text{SPE}=(e,\bar r),\quad\text{payoffs }(10,20).$$

For a tree this simple, subgame perfection and backward induction coincide (p. 169), as the Fact of
[[L03-05-subgame-perfection]] §3 says.

### 1.3 · The same game in MWG (Example 9.B.1, pp. 268–269)

MWG's predation game has out $(0,2)$, in–fight $(-3,-1)$, in–accommodate $(2,1)$, and the same two Nash
equilibria, (out, fight if in) and (in, accommodate if in). Their diagnosis is the clearest statement of
the problem:

> "When the entrant plays 'out,' actions at decision nodes that are unreached by play of the
> equilibrium strategies … do not affect firm I's payoff. As a result, firm I can plan to do absolutely
> anything at this decision node … But … what firm I's strategy says it will do at the unreached node
> can actually insure that firm E, taking firm I's strategy as given, wants to play 'out.'" (p. 269)

Their Example 9.B.3 (§9.B) replaces the post-entry move by a *simultaneous* fight/accommodate game
between both firms; it has three pure Nash equilibria, and solving the post-entry subgame first
(accommodate, accommodate) leaves a unique SPE in which E enters. (G layer.)

---

## 2 · U — why "threat" is the right word, and why it fails

Gibbons (pp. 127–128), on the equilibrium $(L,(R',R'))$ of his Fig. 2.4.1 ([[L03-03-normal-form-and-paths]] §4):
"one might say that player 2 is threatening to play $R'$ if player 1 plays $R$ … If this threat works
… then 2 is not given the opportunity to carry out the threat. The threat should not work, however,
because it is not credible."

| | What it is | What the entrant does with it |
|---|---|---|
| **Threat** | a plan to act against your own interest if the other side does X | believes it in a Nash equilibrium |
| **Credible threat** | a plan that is your best reply *when the moment comes* | believes it in a subgame-perfect equilibrium |
| **Non-credible threat** | a plan you would abandon when the moment comes | ignores it |

> **A threat is credible only if carrying it out is optimal at the node where it would be carried
> out.** Saying it louder, or saying it first, changes nothing; only changing the payoffs at that node
> does.

---

## 3 · C — the value of credible commitment (Cabral pp. 169–170, Fig. 7.8)

Suppose the incumbent can first sign an **enforceable, non-renegotiable** contract (a bond): if the
entrant enters and the incumbent does *not* retaliate, the incumbent pays a penalty of 40. Its
accommodation payoff drops from 20 to $20-40=-20$. Everything else is unchanged. The game now starts
with the incumbent choosing bond ($b$) or no bond ($\bar b$).

| Subgame | Incumbent after entry | Entrant | Incumbent's payoff |
|---|---|---|---|
| **no bond** (Fig. 7.7) | $\bar r$: 20 vs $r$: 10 → $\bar r$ | $e$: 10 vs $\bar e$: 0 → **enter** | 20 |
| **bond** | $\bar r$: $-20$ vs $r$: 10 → $r$ | $e$: $-10$ vs $\bar e$: 0 → **stay out** | 50 |

At the root the incumbent compares 50 with 20 and **posts the bond**.

$$\text{value of commitment}=50-20=\mathbf{30}\qquad(p.~170)$$

![Left: the entry game tree with the entrant choosing out or in; out ends at (0, 50); after in, the incumbent's accommodate edge is highlighted leading to (10, 20) and the retaliate edge to (-10, 10) is dashed as a non-credible threat. Right: the incumbent first chooses bond or no bond; in the no-bond branch the entrant enters and the incumbent accommodates; in the bond branch, where accommodation pays -20, the incumbent would retaliate and the entrant stays out, giving (0, 50); the bond edge is highlighted](figures/L03-entry-commitment.png)
*Figure — the entry game without and with a bond. Green: subgame-perfect choices at every node; dashed orange: the non-credible threat. Source: Cabral Figs. 7.7–7.8, pp. 168–170; bond 40, p. 169.*

In the right-hand tree the two subgames differ in a single number, $20$ versus $-20$ in the
incumbent's accommodation payoff, and that one number flips the incumbent's post-entry choice, which
flips the entrant's choice, which moves the incumbent from 20 to 50.

> **"A credible commitment may have significant strategic value"** (Cabral p. 170). The bond makes the
> incumbent worse off in one terminal node and better off in equilibrium, because the node it worsens
> is the one the threat needed it to avoid.

### 3.1 · How big must the bond be?

Retaliation becomes the incumbent's strict best reply after a bond $B$ when

$$\underbrace{10}_{r}\;>\;\underbrace{20-B}_{\bar r}\quad\Longleftrightarrow\quad B>B^*=20-10=10 .$$

| $B$ | Accommodation pays | Incumbent after entry | Entrant | Incumbent's payoff |
|---|---|---|---|---|
| 0 | 20 | accommodate | enter | 20 |
| 5 | 15 | accommodate | enter | 15 (worse than no bond: not posted) |
| 10 | 10 | **indifferent**: two SPE | enter or stay out | 10 or 50 |
| 11 | 9 | retaliate | stay out | 50 |
| 40 (Cabral) | $-20$ | retaliate | stay out | 50 |

A bond below $B^*$ is worse than none: it lowers the accommodation payoff without changing behaviour.
With the text's value of $-10$ for retaliation, $B^*=20-(-10)=30$ and Cabral's 40 still clears it.

> **Interactive companion.** [The Credible Threat Desk](companions/companion-entry-commitment.html) —
> move the bond through $B^*$ and watch the incumbent's subgame-perfect payoff jump from 20 to 50; move
> the incumbent's war payoff above its accommodation payoff and the bond becomes worthless because the
> threat is credible on its own; push the entrant's war payoff above 0 and no threat deters it.

### 3.2 · Two ways to model commitment (pp. 170–171)

Cabral's methodological point: if a player is credibly committed to an action, model it either by
**changing its payoffs** (the bond, Fig. 7.8) or by **changing the order of moves**, letting it choose
$r$ or $\bar r$ *before* the entrant moves (Fig. 7.9). Solving Fig. 7.9 backward gives the same answer as
Fig. 7.8. What a commitment does, in game-theoretic terms, is **turn a later move into an earlier one**.
The Stackelberg leader of [[L03-07-stackelberg]] is exactly this: a firm whose quantity is fixed before
its rival moves.

### 3.3 · Short-run and long-run variables (p. 171, Fig. 7.10)

When firms choose both a long-run variable (capacity, plant, product position) and a short-run one
(price), model the long-run choice in the **first stage** and the short-run choice in the second:
short-run variables are chosen *given* the long-run ones. The two-stage game is then solved by subgame
perfection, the second stage first. Cabral uses this timing for capacity and price, entry and output, and
product positioning and price in his Chs. 8, 10 and 14.

---

## 4 · Organizational reading

| Setting | The non-credible threat | The commitment that fixes it |
|---|---|---|
| Incumbent vs entrant | "we will start a price war" | sunk capacity, a bond, a reputation at stake in other markets |
| Seller vs shopper | "the price will be fair once you are here" (after the trip is sunk, the seller takes everything) | a price posted in advance (Tadelis exercise 8.13, p. 173–174) |
| Lender vs debtor | "we will sue if you default" when suing costs more than it recovers | a cheap, enforceable legal system (Tadelis exercise 8.7, p. 171) |

The broader theme, **commitment as a source of value and renegotiation as its enemy**, returns with
relational contracts in [[../L06/L06-00-map|Lecture 6]]; Cabral's footnote $n$ (p. 169) already flags
that most real contracts are renegotiable, which is what makes the bond assumption strong.

---

## Links

- Previous: the refinement itself, [[L03-05-subgame-perfection]]. Next: commitment through a quantity,
  [[L03-07-stackelberg]].
- Rules pack: [[../../rules/game-theory|rules/game-theory]] item 2; commitment and hold-up in contracts:
  [[../../rules/06_racionalidade_limitada_contratos|rules/06]].
- Python: `cabral` and `mwg` games, [[L03-11-python]] §1.
- Practice: [Listas/pratica-aula-01-02.md](../../Listas/pratica-aula-01-02.md) (Cabral §7.2,
  pp. 167–174, marked "Exam").
- Exercises: Tadelis 7.6 (p. 148–149), 8.7 (p. 171), 8.8 (p. 171–172), 8.9 (p. 172), 8.13 (p. 173–174);
  Muñoz-Garcia & Toro-González Ch. 4, Exercise 2 (p. 156).
