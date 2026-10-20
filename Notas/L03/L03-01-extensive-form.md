---
tags: [notes, lecture-03, extensive-form, game-tree, information-sets, perfect-information]
date: 2026-10-16
status: estimated
source: "Tadelis (2013) Ch. 7 intro and §7.1 (pp. 129–137): Definitions 7.1–7.3, Figs. 7.1–7.6 (trust game, sequential and simultaneous Battle of the Sexes, card game); Gibbons (1992) §2.4.A (pp. 115–122); MWG §7.C (pp. 221–225)"
---

# 7.1 · The extensive form: who moves when, and who knows what

> **Claim.** A normal form lists strategies and payoffs; it cannot say *when* a player moves or *what
> she has seen*. The extensive form adds both, and the second is the one that matters: **a game is
> sequential because a later mover observes an earlier move, not because the moves happen at
> different clock times.** Information sets are the device that records what a player knows.
> Prev: — · Next: [[L03-02-strategies]] · Map: [[L03-00-map]]

---

## 1 · U — why the normal form is not enough

Tadelis opens Ch. 7 (p. 129) with the Battle of the Sexes from Lecture 2, changed in one detail:

| | Chris: $O$ | Chris: $F$ |
|---|---|---|
| **Alex: $O$** | $2,1$ | $0,0$ |
| **Alex: $F$** | $0,0$ | $1,2$ |

Alex finishes work at 3 p.m., goes to a venue and phones Chris at 4:45: "I am here." Chris now
**knows** where Alex is.

1. Chris's payoff from joining Alex is 1 (if Alex is at the opera) or 2 (at the football); from
   going elsewhere, 0. So a rational Chris goes where Alex is, whatever that is.
2. Alex knows this (common knowledge of rationality). Going to the opera gives Alex 2; going to the
   football gives Alex 1. Alex goes to the opera.

The simultaneous game had two pure equilibria and a mixed one, with no way to choose among them.
The sequential version has **one prediction, $(O,o)$, the one Alex likes**: a *first-mover
advantage*.

> **Moving first is not always an advantage.** In Matching Pennies the player who shows the coin
> first loses for sure (p. 130). What decides is the structure of payoffs, and the extensive form is
> what lets us compute it.

---

## 2 · C — the seven elements of an extensive-form game (§7.1, pp. 130–131)

| # | Element | Already in the normal form? |
|---|---|---|
| 1 | Set of players $N$ | yes |
| 2 | Payoffs over outcomes $\{v_i(\cdot)\}_{i\in N}$ | yes |
| 3 | **Order of moves** | no |
| 4 | **Actions available when a player moves** | partly (the action sets) |
| 5 | **What a player knows when she moves** | no |
| 6 | Probability distributions over exogenous events (**moves of Nature**) | no |
| 7 | The structure 1–6 is **common knowledge** | yes (complete information) |

Gibbons states the same list in four items: players; when each moves, what each can do, what each
knows; payoffs (Definition, pp. 115–116).

> **Element 5 is the one that separates "Chris moves after Alex and knows what Alex did" from "Chris
> moves after Alex but does not know what Alex did" (p. 131).** The second is the simultaneous game,
> whatever the clock says.

---

## 3 · C — game trees (Definition 7.1, p. 133)

> **Definition 7.1.** A game tree is a set of nodes $x\in X$ with a precedence relation $x>x'$
> ("$x$ precedes $x'$"). Every node has only one predecessor. The relation is transitive,
> asymmetric and incomplete. The **root** $x_0$ precedes every other node. Nodes that precede no
> other node are **terminal nodes**, the set $Z\subset X$; payoffs $v_i:Z\to\mathbb R$ are attached
> to them. Every non-terminal node is assigned either to a player, $i(x)$, with action set
> $A_i(x)$, or to Nature.

What each clause buys:

| Clause | Consequence |
|---|---|
| one predecessor per node | **a unique path from the root to every terminal node**, so an outcome *is* a path (used in §7.3, [[L03-03-normal-form-and-paths]]) |
| transitive, asymmetric | the tree has no cycles: play only moves forward |
| incomplete | two nodes on different branches are not ordered: neither comes "before" the other |
| payoffs on $Z$ only | payoffs depend on the whole path, not on single moves |

**Worked: the trust game (Fig. 7.1, p. 132).** Player 1 trusts ($T$) or not ($N$). $N$ ends the game
at $(0,0)$. After $T$, player 2 cooperates ($C$): $(1,1)$, or defects ($D$): $(-1,2)$.

| Terminal node | Path | $v_1$ | $v_2$ |
|---|---|---|---|
| $z_1$ | $N$ | 0 | 0 |
| $z_2$ | $T,C$ | 1 | 1 |
| $z_3$ | $T,D$ | $-1$ | 2 |

Solve it forward from what player 2 would do: after $T$, $D$ pays player 2 a 2 against 1 from $C$, so
player 2 defects; anticipating $-1$, player 1 picks $N$ and gets 0. **Both would prefer
$(T,C)$ with $(1,1)$; it is not reached.** This is the logic of [[L03-04-sequential-rationality-backward-induction]] already at work.

Tadelis's drawing convention, followed in every figure here: play flows top to bottom, and payoffs
are a vertical list, player 1 on top.

---

## 4 · C — information sets (Definition 7.2, p. 135)

> **Definition 7.2.** Every player $i$ has a collection of information sets $h_i\in H_i$ that
> partition the nodes at which $i$ moves, with:
> 1. if $h_i=\{x\}$ is a singleton, $i$ knows she is at $x$;
> 2. if $x\ne x'$ and both are in $h_i$, $i$ does not know whether she is at $x$ or $x'$;
> 3. if $x\ne x'$ and both are in $h_i$, then $A_i(x)=A_i(x')$.

**Property 3 is a consistency requirement, not an assumption about the world.** If two nodes offered
different actions, the player could tell them apart by looking at her menu, and they could not be in
one information set (p. 135; Gibbons p. 119 makes the same point).

Information sets are drawn either as an ellipse around the nodes or as a dashed line joining them
(Fig. 7.4, p. 135). The figures here use the dashed line.

![Two game trees with identical moves and payoffs. Left: player 1 chooses O or F, player 2 then chooses o or f at two separate nodes. Right: the same tree with a dashed line joining player 2's two nodes into one information set h2. Below each, the strategy set of player 2: four plans on the left, two on the right](figures/L03-bos-sequential-vs-simultaneous.png)
*Figure — the Battle of the Sexes with the same moves and payoffs, two information structures. Left: player 2 has two information sets ($\{x_1\},\{x_2\}$). Right: one, $h_2=\{x_1,x_2\}$. Source: Tadelis Figs. 7.7–7.8, p. 138; payoffs p. 129.*

The two trees are identical except for one dashed line, and the dashed line changes everything that
follows: on the left player 2 can condition on $O$ versus $F$, so she has $2\times2=4$ plans; on the
right she cannot, so she has 2, and the game *is* the simultaneous Battle of the Sexes of Lecture 2.

---

## 5 · C — perfect versus imperfect information (Definition 7.3, p. 136)

> **Definition 7.3.** A game of complete information in which **every information set is a
> singleton and there are no moves of Nature** is a game of **perfect information**. A game in which
> some information set contains several nodes, or in which Nature moves, is a game of **imperfect
> information**.

| Game | Information sets | Nature? | Type |
|---|---|---|---|
| Trust game, Fig. 7.1 | all singletons | no | perfect |
| Sequential BoS, Fig. 7.2 | all singletons | no | perfect |
| Simultaneous BoS, Fig. 7.4 | $h_2=\{x_1,x_2\}$ | no | imperfect |
| Rock–paper–scissors, Fig. 7.5 | player 2's three nodes in one set | no | imperfect |
| Card game, Fig. 7.6 | player 1's two nodes in one set | yes | imperfect |

> **Every simultaneous-move game is a game of imperfect information** (p. 136). "Complete" (everyone
> knows the payoffs) and "perfect" (everyone sees every earlier move) are different properties;
> Lecture 3 is complete information throughout, perfect or imperfect.

### 5.1 · Worked — the card game (Fig. 7.6, pp. 136–137)

Nature draws a king ($K$) or an ace ($A$), each with probability $\tfrac12$. Player 1 does not see it,
and calls ($C$) or folds ($F$). Fold: player 1 pays 1 to player 2. Call: player 1 pays 2 on a king,
receives 2 on an ace.

| Player 1's action | $K$ (prob. ½) | $A$ (prob. ½) | Expected $v_1$ |
|---|---|---|---|
| $C$ | $-2$ | $+2$ | $\tfrac12(-2)+\tfrac12(2)=0$ |
| $F$ | $-1$ | $-1$ | $-1$ |

Player 1 calls. The game can be drawn with Nature first (player 1's two nodes in one information set)
or with player 1 first and Nature after; **both trees carry the same information, so they are the same
game** (p. 137). Player 2 has no move, so this is a single-person decision problem in game clothing.

> **Two kinds of uncertainty, one device.** Not knowing Nature's draw (*exogenous* uncertainty) and
> not knowing another player's move (*endogenous* uncertainty) are both represented as not knowing
> where you are in the tree; in both cases the player needs a belief about which node she is at
> (p. 137). That belief is the object of Lecture 8 ([[../L08/L08-00-map|Lecture 8]]).

---

## 6 · G — the formal version (MWG §7.C, pp. 221–225)

MWG build the same object in their own notation: nodes, a predecessor function, a map from nodes to
information sets $H(x)$, and payoffs at terminal nodes. Their Matching Pennies **Version B** (player 2
sees player 1's coin, Example 7.C.1) and **Version C** (she does not, Example 7.C.3) are the pair of
trees in the figure above with different payoffs. MWG also define **perfect recall** formally (a
player never forgets a move she made or saw); Tadelis states it in words as Definition 7.7 (p. 142),
used in [[L03-02-strategies]] §4. Not examinable beyond the definitions above.

---

## Links

- Next: what a strategy is once players can condition on what they saw, [[L03-02-strategies]].
- The simultaneous Battle of the Sexes and its three equilibria: [[../L02/L02-00-map|Lecture 2]].
- Rules pack: [[../../rules/game-theory|rules/game-theory]] item 1 (*specify the game completely: players,
  actions, timing, information sets, payoffs*).
- Exercises (number and page only): Tadelis 7.2 (p. 147), 7.3 (p. 147–148), 7.9 (p. 149–150);
  Muñoz-Garcia & Toro-González Ch. 4, Exercise 3 (p. 160) and Exercise 4 (p. 163).
