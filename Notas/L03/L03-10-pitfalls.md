---
tags: [notes, lecture-03, pitfalls, true-false, review]
date: 2026-10-16
status: estimated
source: "Tadelis (2013) Ch. 7–8 (pp. 129–174); Gibbons (1992) §2.1, §2.4; Cabral (2017) §7.2; True/False items original, in the macro-1 style of rules/00_estilo_avaliacao.md"
---

# Lecture 3 · Pitfalls and an original True/False self-test

> Prev: [[L03-09-formulas]] · Next: [[L03-11-python]] · Map: [[L03-00-map]]

---

## Part I — the confusions this material produces

### 1 · An outcome is not an equilibrium

**Error:** answering "the SPE is $(45,22.5)$" or "the SPE is $(O,o)$".
**Minimal counterexample:** in Stackelberg, $q_1=45$ is not a best response to a constant $q_2=22.5$
(the best response is 33.75), so the pair is not even a Nash equilibrium of anything. The SPE is
$(45,\ q_2(q_1)=\tfrac{90-q_1}{2})$; in the BoS it is $(O,of)$.
→ [[L03-07-stackelberg]] §3, [[L03-05-subgame-perfection]] §5.

### 2 · A strategy is not an action

**Error:** giving player 2 in the sequential BoS the strategy set $\{o,f\}$.
**Counterexample:** she has two information sets, so $S_2=\{oo,of,fo,ff\}$. The plan must name an
action at **every** information set, including ones the plan makes unreachable ($NO$ vs $NF$).
→ [[L03-02-strategies]] §1.

### 3 · "Sequential" is about information, not time

**Error:** treating a later mover as a follower even when she cannot see the earlier move.
**Counterexample:** Gibbons's unobserved Stackelberg game: firm 1 moves first, firm 2 does not see $q_1$,
and the unique equilibrium is Cournot. → [[L03-07-stackelberg]] §5, [[L03-01-extensive-form]] §2.

### 4 · Complete ≠ perfect information

**Error:** "complete information, so backward induction applies."
**Counterexample:** the voluntary BoS has complete information and a non-singleton information set;
backward induction cannot start, subgame perfection can. → [[L03-05-subgame-perfection]] §1.

### 5 · Every Nash equilibrium of a tree is "reasonable"

**Error:** reporting $(F,ff)$ or $(\bar e,r)$ as predictions.
**Counterexample:** they rest on actions that are not optimal at the node where they would be taken.
Nash equilibrium never tests those nodes; subgame perfection does. → [[L03-03-normal-form-and-paths]] §3.

### 6 · Subgame perfection always gives a unique answer

**Error:** "SPE eliminates multiplicity."
**Counterexample:** MAD has two pure SPE, because the war-stage subgame has two Nash equilibria; the
voluntary BoS also has two. Uniqueness needs perfect information **and** no payoff ties
(Prop. 8.1). → [[L03-05-subgame-perfection]] §4.

### 7 · Any node with a singleton information set starts a subgame

**Error:** listing the card game's $x_1$ as a subgame root.
**Counterexample:** the subgame at $x_1$ would contain $x_3$ and hence $x_4$, which $x_1$ does not
precede: it cuts an information set. → [[L03-05-subgame-perfection]] §2.

### 8 · Committing is free / moving first always helps

**Error:** "the first mover always wins" or "a bond can only cost the incumbent."
**Counterexamples:** in Matching Pennies the first mover loses (p. 130); a bond below
$B^*=D_I-F_I$ lowers the incumbent's payoff and changes nothing; a bond above it raises the incumbent's
equilibrium payoff by lowering one of its own terminal payoffs. → [[L03-06-credibility-entry-commitment]] §3.

### 9 · Backward induction always finds the efficient outcome

**Error:** expecting rational players to reach the high-payoff end of a game.
**Counterexample:** Centipede: $(1,1)$ instead of $(3,3)$; trust game: $(0,0)$ instead of $(1,1)$.
→ [[L03-04-sequential-rationality-backward-induction]] §4.

### 10 · Copying the book's slips

Two printed numbers in Ch. 8 do not follow from the book's own equations: the on-path reply in the
flooding remark is $\tfrac{90-20}{2}=35$, not 40 (p. 163); and the sophisticated first-period choice in
§8.3.4 is $x_1=\tfrac K2$, not $\tfrac23K$ (p. 169). → [[L03-07-stackelberg]] §4,
[[L03-08-time-inconsistency]] §2.2.

---

## Part II — True/False self-test (original items)

Scoring as in the exam: $\max\{0,\ \text{correct}-\text{wrong}/2\}$ × item value; blanks do not count as
wrong ([rules/00_estilo_avaliacao.md](../../rules/00_estilo_avaliacao.md)).

**1.** A game in which player 2 moves one hour after player 1 but without observing player 1's choice
is strategically equivalent to the simultaneous-move game with the same payoffs.
**True.** What defines a sequential game is what the later mover knows (element 5, p. 131); with one
information set containing all of player 1's choices, the tree is the simultaneous game's tree.

**2.** A game of complete information is necessarily a game of perfect information.
**False.** Complete information means payoffs are common knowledge; perfect information also requires
singleton information sets and no Nature (Def. 7.3). Any simultaneous game is a counterexample.

**3.** A player with three information sets, having 2, 2 and 3 actions respectively, has 7 pure
strategies.
**False.** Strategies multiply, they do not add: $2\times2\times3=12$.

**4.** In the sequential Battle of the Sexes, the strategies $oo$ and $of$ of player 2 always produce the
same outcome.
**False.** They coincide only when player 1 plays $O$; after $F$, $oo$ leads to $(0,0)$ and $of$ to
$(1,2)$.

**5.** Every mixed strategy in an extensive-form game can be replicated by a behavioral strategy, and
in a game of perfect recall the converse also holds.
**True.** Mixed → behavioral by conditioning (p. 141); behavioral → mixed under perfect recall is Kuhn's
theorem (p. 142).

**6.** The behavioral strategy that replicates a given mixed strategy may correspond to several mixed
strategies, but the mixed strategy that replicates a given behavioral strategy is unique.
**False.** It is the other way round: many mixed strategies map to the same behavioral one (Fig. 7.9's
example has a one-parameter family); conditioning a mixed strategy gives exactly one behavioral strategy.

**7.** In a Nash equilibrium of an extensive-form game, a player's action at an information set that is
off the equilibrium path does not affect her own equilibrium payoff.
**True.** Off-path sets are reached with probability 0 given the profile, so her payoff is the same
whatever she plans there; that is why Nash cannot discipline those plans.

**8.** In a Nash equilibrium, a player's action at an off-path information set cannot affect the other
players' choices.
**False.** It can, and that is the whole problem: player 2's $f$ at $x_1$ is what keeps player 1 at $F$
in $(F,ff)$.

**9.** Every subgame-perfect equilibrium is a Nash equilibrium.
**True.** The whole game is a proper subgame, so the restriction to it, the profile itself, is a Nash
equilibrium.

**10.** Every finite game of perfect information has a subgame-perfect equilibrium in pure strategies.
**True.** Backward induction constructs one (Prop. 8.1, Cor. 8.1, and the Fact on p. 158).

**11.** If a finite game of perfect information has two terminal nodes giving player 1 the same payoff, it
has more than one subgame-perfect equilibrium.
**False.** Uniqueness may fail but need not: if the tie is never the deciding comparison at any node, the
solution is still unique. The proposition gives a sufficient condition for uniqueness, not a necessary one.

**12.** In a game whose only proper subgame is the whole game, every Nash equilibrium is subgame perfect.
**True.** Definition 8.3 then only requires a Nash equilibrium of the whole game (MWG Exercise 9.B.2(a)).

**13.** A node that is a singleton information set always starts a proper subgame.
**False.** It must also not cut any later information set; the card game's $x_1$ and $x_2$ are
singletons and start no subgame.

**14.** In the voluntary Battle of the Sexes, $(NO,f)$ is not a Nash equilibrium because $O$ is never
played.
**False.** It is a Nash equilibrium (player 1 gets 1.5 against $f$ whatever she plans after $Y$); it
fails subgame perfection because $(O,f)$ is not an equilibrium of the subgame at $x_1$.

**15.** In the mutually assured destruction game the war stage is off the path in every subgame-perfect
equilibrium, so the war-stage payoffs do not affect which equilibria are subgame perfect.
**False.** The war stage is off the path in both SPE, but which of its equilibria is expected decides
whether player 2 backs down and whether player 1 escalates.

**16.** In the entry game of Cabral Fig. 7.7, $(\bar e,r)$ is a Nash equilibrium.
**True.** Against $r$ the entrant prefers 0 to $-10$; against $\bar e$ the incumbent gets 50 whatever it
plans, so $r$ is a best reply. It is not subgame perfect.

**17.** A bond that lowers the incumbent's payoff from accommodating can never raise its equilibrium
payoff.
**False.** In Cabral's example it raises it from 20 to 50: the lower payoff sits at a node the bond makes
unreachable, and it makes retaliation credible.

**18.** In Cabral's entry game, any bond $B>0$ makes the incumbent better off.
**False.** Only $B>B^*=10$ changes the incumbent's post-entry choice; a smaller bond only lowers its
accommodation payoff, which is then its equilibrium payoff.

**19.** In the Stackelberg game with $p=100-q$ and unit cost 10, the leader's profit exceeds its Cournot
profit, the follower's is lower, and industry profit is lower than in Cournot.
**True.** $1012.5>900$, $506.25<900$, $1518.75<1800$.

**20.** The pair $(q_1,q_2)=(45,22.5)$ is a subgame-perfect equilibrium of the Stackelberg game.
**False.** It is the SPE outcome. The equilibrium specifies firm 2's quantity after every $q_1$:
$(45,\tfrac{90-q_1}{2})$.

**21.** The Cournot quantities $(30,30)$ can be the outcome of a Nash equilibrium of the Stackelberg
game.
**True.** $q_1=30$ with $q_2(q_1)\equiv30$ is a Nash equilibrium (p. 162); it is not subgame perfect
because 30 is not firm 2's best reply to other $q_1$.

**22.** If firm 1 still moves first but firm 2 cannot observe $q_1$, firm 2 earns more than in the
Stackelberg game.
**True.** Without observation the unique Nash equilibrium is Cournot (Gibbons pp. 63–64), where firm 2
earns 900 instead of 506.25: knowing $q_1$, and being known to know it, hurts firm 2.

**23.** In the Stackelberg game, total output is higher and price lower than in Cournot.
**True.** $\tfrac34(a-c)>\tfrac23(a-c)$; $32.5<40$.

**24.** A player with exponential discounting and log utility revises her consumption plan when the second
period arrives.
**False.** Exponential discounting is time consistent: the period-2 choice (8.8) equals the planned (8.5).

**25.** A sophisticated hyperbolic discounter solves her consumption problem by backward induction against
her future selves.
**True.** She treats period-2 self as a player who best-responds to the remaining budget, and chooses
period-1 consumption given that reply: an SPE (pp. 168–169).

**26.** Backward induction predicts that the Centipede game ends at the first node, and laboratory
subjects typically behave this way.
**False.** The first half is true; most lab subjects continue for some time (McKelvey and Palfrey, 1992),
though chess players mostly stop at once (Palacios-Huerta and Volij, 2009; p. 160).

---

## Links

- Map: [[L03-00-map]]. Formulas: [[L03-09-formulas]]. Python checks for the numerical items:
  [[L03-11-python]].
- Quizzes can be generated from this note and [[L03-09-formulas]] with `/quiz-gen`.
