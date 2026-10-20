---
tags: [notes, lecture-03, strategies, behavioral-strategies, perfect-recall, kuhn]
date: 2026-10-16
status: estimated
source: "Tadelis (2013) §7.2.1–7.2.2 (pp. 137–142): Definitions 7.4–7.7, Figs. 7.7, 7.9, 7.10 (absent-minded driver); Gibbons (1992) §2.4.A (pp. 117–118)"
---

# 7.2.1–7.2.2 · A strategy is a complete plan: pure, mixed and behavioral

> **Claim.** Once a player can condition on what she has seen, a strategy stops being an action and
> becomes **a complete contingent plan: one action at every information set, including the ones the
> plan itself makes unreachable.** Counting them is a product rule. Randomizing can happen over whole
> plans (mixed) or node by node (behavioral), and with perfect recall the two are equivalent (Kuhn).
> Prev: [[L03-01-extensive-form]] · Next: [[L03-03-normal-form-and-paths]] · Map: [[L03-00-map]]

---

## 1 · C — pure strategies (Definition 7.4, p. 139)

> **Pure strategy in extensive-form games** (p. 138). A complete plan of play that describes which
> pure action player $i$ will choose at each of his information sets.
>
> **Definition 7.4.** Let $H_i$ be the information sets of player $i$, $A_i(h_i)$ the actions at
> $h_i$, and $A_i=\bigcup_{h_i\in H_i}A_i(h_i)$. A pure strategy is a mapping $s_i:H_i\to A_i$ with
> $s_i(h_i)\in A_i(h_i)$ for every $h_i\in H_i$. $S_i$ is the set of all such maps.

**Worked — the sequential Battle of the Sexes (Fig. 7.7, p. 138).** Player 1 has one information set,
so $S_1=\{O,F\}$. Player 2 has two, $h_2^O=\{x_1\}$ (after $O$) and $h_2^F=\{x_2\}$ (after $F$), each
with $\{o,f\}$. A strategy "$ab$" reads "play $a$ after $O$, play $b$ after $F$":

| $s_2$ | after $O$ | after $F$ | in words |
|---|---|---|---|
| $oo$ | $o$ | $o$ | always opera |
| $of$ | $o$ | $f$ | **follow player 1** |
| $fo$ | $f$ | $o$ | do the opposite |
| $ff$ | $f$ | $f$ | always football |

$$S_2=\{oo,\,of,\,fo,\,ff\}\qquad(p.~139)$$

Two actions became four strategies because there are two information sets. In the simultaneous
version (one information set) $S_2=\{o,f\}$: the same two actions, two strategies.

### 1.1 · Counting (p. 139)

If player $i$ has $k$ information sets with $m_1,\dots,m_k$ actions:

$$\boxed{\;|S_i|=m_1\times m_2\times\cdots\times m_k\;}$$

because a strategy picks one action independently at each information set, and the choices multiply.

| Player | Information sets and actions | $\lvert S_i\rvert$ |
|---|---|---|
| Player 2, sequential BoS | $2$ sets × 2 actions | $2\times2=4$ |
| Player 2, simultaneous BoS | $1$ set × 2 actions | $2$ |
| Tadelis's example (p. 139) | 3 sets with 2, 3, 4 actions | $2\times3\times4=\mathbf{24}$ |
| Player 1, voluntary BoS (Fig. 8.4) | $x_0$: $\{Y,N\}$, $x_1$: $\{O,F\}$ | $2\times2=4$: $YO,YF,NO,NF$ |
| Each player, MAD game (Fig. 8.11) | 2 sets × 2 actions | $4$ |

> **A strategy specifies actions at information sets the strategy itself never reaches.** In the
> voluntary BoS, $NO$ and $NF$ are different strategies even though $N$ ends the game before $O$ or
> $F$ could be played (Tadelis p. 158; MWG p. 274, footnote 4). This is not pedantry: it is exactly
> what lets [[L03-05-subgame-perfection]] test whether a plan is still rational at nodes that are
> not reached.

**Why the plan must be complete** (Gibbons p. 117–118). For player $j$ to compute a best response to
$i$'s strategy, $j$ may need to know how $i$ would act in *every* contingency, not only the ones
expected to arise. A strategy that left some contingency blank could not be tested against
deviations that lead there.

---

## 2 · C — mixed strategies (Definition 7.5, p. 139)

> **Definition 7.5.** A mixed strategy for player $i$ is a probability distribution over his pure
> strategies $s_i\in S_i$.

The player draws one complete plan **before the game** and then follows it. For player 2 in the
sequential BoS a mixed strategy is $(p_{oo},p_{of},p_{fo},p_{ff})$ with each $p\ge0$ and the four
summing to 1.

The interpretation has a drawback: the randomization is once-and-for-all, so the player cannot
"cross the bridge when he gets there" (p. 140).

---

## 3 · C — behavioral strategies (Definition 7.6, p. 140)

> **Definition 7.6.** A behavioral strategy specifies for each information set $h_i\in H_i$ an
> independent probability distribution over $A_i(h_i)$, written $\sigma_i:H_i\to\Delta A_i(h_i)$,
> where $\sigma_i(a_i(h_i))$ is the probability that $i$ plays $a_i(h_i)$ at $h_i$.

**The library analogy** (Luce and Raiffa, p. 140): a pure strategy is an instruction manual with one
page per information set; $S_i$ is the library of manuals. **Mixed:** pick a manual at random, then
obey it. **Behavioral:** one manual whose pages say "toss a coin here".

### 3.1 · Worked — mixed to behavioral (p. 141)

Given $(p_{oo},p_{of},p_{fo},p_{ff})$, the probability of each action *conditional on reaching* each
information set is the total weight of the plans that prescribe it there:

$$\Pr\{o\mid O\}=p_{oo}+p_{of},\qquad \Pr\{f\mid O\}=p_{fo}+p_{ff},$$
$$\Pr\{o\mid F\}=p_{oo}+p_{fo},\qquad \Pr\{f\mid F\}=p_{of}+p_{ff}.$$

Each pair sums to 1 because the four $p$'s do. Setting $\sigma_2(a\mid h)=\Pr\{a\mid h\}$ gives a
behavioral strategy with the same distribution over outcomes. **Every mixed strategy has a behavioral
equivalent.**

### 3.2 · Worked — behavioral to mixed, and why it is not unique (pp. 141–142)

Fig. 7.9's behavioral strategy: $\sigma_2(o\mid O)=\tfrac13$, $\sigma_2(o\mid F)=\tfrac12$. A mixed
strategy reproduces it iff

$$p_{oo}+p_{of}=\tfrac13,\quad p_{fo}+p_{ff}=\tfrac23,\quad p_{oo}+p_{fo}=\tfrac12,\quad p_{of}+p_{ff}=\tfrac12 .$$

With $p_{oo}+p_{of}+p_{fo}+p_{ff}=1$, the second equation follows from the first and the fourth from
the third (footnote 4, p. 142), so there are **three independent equations in four unknowns**: a
one-parameter family of solutions. Check the book's two:

| $(p_{oo},p_{of},p_{fo},p_{ff})$ | sum | $p_{oo}+p_{of}$ | $p_{oo}+p_{fo}$ |
|---|---|---|---|
| $(\tfrac13,0,\tfrac16,\tfrac12)$ | $\tfrac{2+0+1+3}{6}=1$ | $\tfrac13$ ✓ | $\tfrac13+\tfrac16=\tfrac12$ ✓ |
| $(\tfrac16,\tfrac16,\tfrac13,\tfrac13)$ | $\tfrac{1+1+2+2}{6}=1$ | $\tfrac16+\tfrac16=\tfrac13$ ✓ | $\tfrac16+\tfrac13=\tfrac12$ ✓ |

A general solution: pick $p_{oo}=t\in[0,\tfrac13]$, then $p_{of}=\tfrac13-t$, $p_{fo}=\tfrac12-t$,
$p_{ff}=1-t-(\tfrac13-t)-(\tfrac12-t)=\tfrac16+t$. The book's two are $t=\tfrac13$ and $t=\tfrac16$.

---

## 4 · C — perfect recall and Kuhn's equivalence (Definition 7.7, p. 142)

> **Definition 7.7.** A game of **perfect recall** is one in which no player ever forgets information
> that he previously knew (including his own earlier moves).

> **Kuhn (1953), as stated on p. 142.** In games of perfect recall, mixed and behavioral strategies are
> equivalent: given the opponents' strategies, the same distribution over outcomes can be generated by
> either.

Everything in this course assumes perfect recall, so from here on "a mixed strategy" in an extensive
form can be read as a behavioral one, which is how [[L03-05-subgame-perfection]] states Definition 8.3.

### 4.1 · U — what breaks without perfect recall: the absent-minded driver (Remark, pp. 142–143)

A driver passes two identical exits and cannot tell which one he is at. Exit 1 pays 0, exit 2 pays 4,
missing both pays 1. He has **one** information set containing both intersections, so any plan is "exit
with probability $p$ whenever at an intersection":

$$V(p)=0\cdot p+4\,p(1-p)+1\cdot(1-p)^2=4p-4p^2+1-2p+p^2=-3p^2+2p+1 .$$

$$V'(p)=-6p+2=0\ \Rightarrow\ p^*=\tfrac13,\qquad V(\tfrac13)=-\tfrac13+\tfrac23+1=\tfrac43 .$$

No pure plan does as well: $p=0$ gives 1 and $p=1$ gives 0. With imperfect recall **randomizing at
the node can beat every pure plan**, which never happens to a single decision maker with perfect recall.
At the intersection the driver's payoff from $p$ is
$q[4p(1-p)+(1-p)^2]+(1-q)[4p+(1-p)]$, where $q$ is his belief that he is at exit 1; this coincides
with the planning problem only at $q=1$, so the plan and the in-the-moment choice disagree. **Named
only; not examinable.**

---

## Links

- Next: put these strategy sets in a matrix and find the Nash equilibria, [[L03-03-normal-form-and-paths]].
- Mixed strategies in normal-form games: [[../L02/L02-00-map|Lecture 2]].
- Strategies in repeated games are history-contingent plans of the same kind:
  [[../L05/L05-00-map|Lecture 5]].
- Python: `pure_strategies`, `n_pure_strategies`, `behavioral_from_mixed`, the driver in
  [[L03-11-python]] §1–2.
- Exercises: Tadelis 7.1 (p. 147), 7.2(c) (p. 147), 7.4(c) (p. 148), 7.5(b) (p. 148), 7.10 (p. 150).
