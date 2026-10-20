---
tags: [notes, lecture-07, pitfalls, true-false, self-test]
date: 2026-10-16
status: estimated
source: "Built from notes L07-01 to L07-09 (Tadelis Ch. 12–13, Gibbons Ch. 3, M&R pp. 149–153, Cabral pp. 140–142, 174–176). True/False items are original, in the macro-1 style of rules/00_estilo_avaliacao.md (one claim per item; scoring max{0, correct − wrong/2})."
---

# Lecture 7 · Pitfalls and an original True/False self-test

> Prev: [[L07-10-formulas]] · Next: [[L07-12-python]] · Map: [[L07-00-map]]

---

## Part I — the confusions this material produces

### 1 · A type is not an action, and a strategy is not an action

A strategy in a Bayesian game is a **function** $s_i:\Theta_i\to A_i$. "Firm 2 produces $q_2$" is not a
strategy; "$q_2(c_H)=13/6$, $q_2(c_L)=19/6$" is. Minimal counterexample: in the entry game the
incumbent has 2 actions but **4** strategies ($AA,AF,FA,FF$), and the equilibrium $(E,AF)$ cannot even be
written with actions alone. → [[L07-02-bayesian-nash-equilibrium]] §1.

### 2 · Why specify what types that were not drawn would do?

Because **the other players' expected payoffs depend on it**. Firm 1 in Gibbons's Cournot game cannot
evaluate $q_1$ against "firm 2 produces 13/6" — it needs both quantities and $\theta$. Same reason a
strategy covers unreached nodes in Lecture 3. → [[L07-03-cournot-private-costs]] §1.

### 3 · Incomplete vs imperfect information

Incomplete: someone does not know another's **payoffs**. Imperfect: someone does not know the
**history** of moves. Harsanyi converts the first into the second by adding Nature's move. A
simultaneous-move game with known payoffs has imperfect, not incomplete, information.
→ [[L07-01-bayesian-games-harsanyi]] §2.

### 4 · Private values vs common values

Private: $u_i$ depends on $\theta_i$ only. Common: on others' types too. Adverse selection, the
swing voter's curse and the winner's curse **all need common values**; in an IPV auction learning the
rival's value never changes what the object is worth to you. → [[L07-09-common-values-curses]] §2.4.

### 5 · "The buyer's average value exceeds the seller's, so trade happens at some average price"

False with private quality information. Orange grove: average values 24 vs 20, yet at $p=20$ only $L,M$
sell and that pool is worth 19 to the buyer. **The relevant average is over the sellers who accept,
and it depends on the price.** → [[L07-05-adverse-selection-lemons]] §3.

### 6 · "Adverse selection needs a small gain from trade"

It needs a gain that is small **relative to the spread of the privately known quality**: the $k$-th
quality joins iff $\Delta\ge(k-1)s/2$. Raising every value by the same amount ($v_1$) changes nothing.
→ [[L07-05-adverse-selection-lemons]] §4.

### 7 · Weakly dominant ≠ unique equilibrium, and ≠ strictly dominant

Bidding $\theta_i$ in a second-price auction is **weakly** dominant (ties in regions L and H). That
selects an equilibrium; it does not prove there is no other. → [[L07-06-second-price-english]] §2.

### 8 · "In a first-price auction, bid your value"

Bidding your value guarantees zero (Claim 13.1). The equilibrium bid is $\tfrac{n-1}{n}\theta$ under
uniform values — **shading falls with $n$**, it does not rise. → [[L07-07-first-price-dutch]] §3.

### 9 · Strategic equivalence vs outcome equivalence

Dutch and first-price have the **same normal form** (strategically equivalent). English and
second-price give the **same outcome under private values** (Prop. 13.2) but are different games: in
the English auction bidders observe exits, which matters with common values.
→ [[L07-07-first-price-dutch]] §5.

### 10 · Revenue equivalence ≠ "the auctions are the same"

Same **expected** revenue and same expected payoff per type; different bids, different realized prices,
different price variance ($\tfrac1{72}$ vs $\tfrac1{18}$ at $n=2$). And only under its four conditions.
→ [[L07-08-revenue-equivalence]] §4, §6.

### 11 · "Voting your informative signal is an equilibrium"

Under unanimity a juror is decisive only when the other votes $C$; conditional on that, an innocence
signal leaves the posterior at $q>\tfrac12$. Decision-theoretic optimality alone is not equilibrium
optimality. → [[L07-09-common-values-curses]] §1.3.

### 12 · Adverse selection vs moral hazard

Adverse selection: **pre-contractual** hidden information (who you are). Moral hazard: **post-contractual**
hidden action (what you do). M&R p. 150: a family buying maternity cover because it plans children is
adverse selection; having more children *because* it is covered is moral hazard — which is outside
this course. → [[L07-05-adverse-selection-lemons]] §5.

---

## Part II — True/False self-test (original)

**[E]** easy · **[M]** medium · **[H]** hard. Each answer is settled by one paragraph.

### Block A — Bayesian games and BNE

**1. [E]** In a static Bayesian game, a player's pure strategy specifies one action for each of his own
types. — **T.** Def. 12.3: $s_i:\Theta_i\to A_i$. With 2 actions and 3 types there are $2^3=8$ pure
strategies, not 2.

**2. [M]** If types are independent, a player's posterior about the others' types depends on his own
type. — **F.** Independence makes $\pi(\theta_i,\theta_{-i})=\pi_i(\theta_i)\pi_{-i}(\theta_{-i})$, so Bayes'
rule returns $\phi_i(\theta_{-i}\mid\theta_i)=\pi_{-i}(\theta_{-i})$ for every $\theta_i$. Dependence on one's own
type requires correlation, as in the 1/6–1/3 prior (p. 249).

**3. [E]** Harsanyi's transformation turns a game of incomplete information into a game of imperfect
information in which Nature moves first. — **T.** Nature draws types; each player observes only his own,
so later movers do not know the full history (Gibbons p. 148).

**4. [M]** In the entry game with $p=2/3$, $(O,FF)$ is a Nash equilibrium of the induced normal form but not
an equilibrium in which each type of incumbent acts optimally at his node. — **T.** Against $FF$ the
entrant prefers $O$ ($0>-1$); against $O$ every incumbent strategy pays 2. But a rational incumbent
reaching his node would accommodate ($1>-1$), so $FF$ asks him to carry out a non-credible fight.

**5. [M]** To verify a pure BNE in a finite game it suffices to check, type by type, that no single
alternative action raises that type's expected payoff. — **T.** Tadelis p. 251 / MWG Prop. 8.E.1: if no
type gains by changing his own action, no type-contingent rearrangement gains either.

**6. [H]** In the chicken game with $R=8$, $H=16$, $L=0$, the harsh-parent type drives in the unique BNE.
— **F.** The unique BNE is $(DC,dc)$: lenient types drive, harsh types swerve. A harsh type facing $dc$
gets $\tfrac12(4-16)+\tfrac12\cdot8=-2$ from driving, $0$ from swerving.

### Block B — continuous types and purification

**7. [E]** In the study-group game a student's best response to any strategy of his partner is a cutoff
in his own type. — **T.** Claim 12.1: work iff $\theta_i\ge\sqrt{c/(1-\Pr\{s_j=1\})}$, a constant cutoff.

**8. [M]** The more likely the partner is to work, the lower a student's own effort cutoff. — **F.** The
cutoff $\sqrt{c/(1-\Pr\{s_j=1\})}$ **rises** with $\Pr\{s_j=1\}$: free-riding. $BR_i$ is decreasing in
$\hat\theta_j$ precisely because a lower $\hat\theta_j$ means $j$ works more.

**9. [M]** With $c=1/8$ each student works with probability one half in equilibrium. — **T.**
$\hat\theta^*=c^{1/3}=\tfrac12$ and $\Pr\{\theta_i\ge\tfrac12\}=\tfrac12$.

**10. [H]** Harsanyi's purification says players in a mixed equilibrium literally randomize because they
are indifferent. — **F.** It says the opposite: each type plays a **pure** strict best response; the mix is
the opponent's uncertainty about which type he faces (Gibbons p. 152). In Gibbons's example the
probability of Opera, $1-c/x$, tends to $2/3$ as $x\to0$.

### Block C — Cournot with private costs

**11. [M]** In Gibbons's asymmetric-cost Cournot game, the high-cost type of firm 2 produces more than it
would if its cost were common knowledge. — **T.** $q_2^*(c_H)$ exceeds $(a-2c_H+c)/3$ by
$\frac{1-\theta}{6}(c_H-c_L)>0$: firm 1, not knowing the cost is high, produces less than it would against
a known high-cost rival.

**12. [H]** In that game firm 1's equilibrium quantity always equals the average of its complete-
information quantities. — **F.** It does with linear demand and linear costs (p. 146), but Gibbons flags
it as misleading: with total cost $c_iq_i^2$ the equality fails in general.

### Block D — adverse selection and bilateral trade

**13. [E]** In Tadelis's orange-grove game, the grove trades in every BNE at a price in $[10,14]$ when its
quality is $L$. — **F.** Prop. 12.1 says trade *can* occur only with the lowest type, and any $p^*\in[10,14]$
*can* be supported; it does not say trade occurs in every BNE (an offer of $p<10$ that everybody rejects is
also part of an equilibrium). Read "only if", not "if".

**14. [M]** In the orange grove, raising every seller and buyer value by 100 would let the $M$ type trade.
— **F.** The condition $\Delta\ge(k-1)s/2$ involves only the premium $\Delta=4$ and the spread $s=10$; the
level drops out. The pool $\{L,M\}$ would be worth 119 against a price of 120.

**15. [M]** In M&R's insurance model the private market collapses whenever mandatory coverage would be
inefficient. — **F.** The false converse. Collapse iff $c\bar x>v$; mandatory coverage is efficient iff
$v>c\bar x/2$. In the band $c\bar x>v>c\bar x/2$ the market collapses **although** coverage is efficient.

**16. [E]** In Cabral's insurer game, a premium between the average valuation and the average cost
makes money. — **F.** At $p=4.5$ only high-risk patients buy; expected profit $0.1(4.5-30)=-2.55$. The
averages are over the whole population; the buyers are not.

**17. [M]** In Gibbons's linear equilibrium of the double auction, every pair with $v_b>v_s$ trades. —
**F.** Trade iff $v_b\ge v_s+\tfrac14$; pairs with gains below $\tfrac14$ do not trade, and expected gains are
$\tfrac9{64}<\tfrac16$.

### Block E — auctions

**18. [E]** In a second-price auction with private values, bidding one's value is weakly dominant even if
the bidder knows nothing about the distribution of the others' values. — **T.** Prop. 13.1's proof never
uses $F_j$: in each case the comparison holds pointwise in the rivals' bids (p. 274).

**19. [M]** In a second-price auction, raising your bid above your value can change the price you pay. —
**F.** Your bid only decides whether you win; the price is the highest rival bid. Overbidding changes
the outcome only when that rival bid lies between your value and your bid — and then you win at a loss.

**20. [E]** With $n$ bidders and values uniform on $[0,1]$, the symmetric first-price equilibrium bid is
$\theta/n$. — **F.** It is $(n-1)\theta/n$; $\theta/n$ is the amount **shaded**. At $n=2$: bid $\theta/2$, shade
$\theta/2$ — the two coincide only there.

**21. [M]** The Dutch auction and the first-price sealed-bid auction have the same set of Bayesian Nash
equilibria. — **T.** They are strategically equivalent: in both a strategy maps a value to a price, the
highest price wins and pays it, and nothing useful is observed before one's own choice (p. 279).

**22. [M]** With uniform values on $[0,1]$, the seller's expected revenue is $1/3$ with two bidders in
both the first- and second-price auctions. — **T.** $(n-1)/(n+1)$ at $n=2$; first price: $E[\tfrac12\max]=
\tfrac12\cdot\tfrac23$; second price: $E[\min]=\tfrac13$.

**23. [H]** Revenue equivalence implies that, for each realization of values, the first- and second-price
auctions raise the same revenue. — **F.** It is a statement about expectations. With values $0.9$ and
$0.2$: first price raises $0.45$, second price $0.2$.

**24. [H]** In the type-by-type comparison, a bidder of value $\theta$ expects to pay $\tfrac{n-1}{n}\theta^n$ in
both the first- and second-price auctions. — **T.** First price: $\theta^{n-1}\cdot\tfrac{n-1}{n}\theta$; second
price: $\int_0^\theta y(n-1)y^{n-2}dy=\tfrac{n-1}{n}\theta^n$.

### Block F — common values

**25. [M]** In the oil-field auction, a firm with a low signal that bids its expected value, 15, earns zero
expected profit when the rival does the same. — **F.** It wins only on a tie with another low signal,
when $v=10$: $\tfrac12\cdot\tfrac12(10-15)=-1.25<0$ — the winner's curse.

**26. [H]** Under unanimity with informative signals, a juror who sees an innocence signal and believes
the other juror votes his signal should acquit. — **F.** He is pivotal only if the other saw a guilt
signal; then $\Pr\{G\mid\theta_I,\theta_G\}=q>\tfrac12$ and he should convict.

---

## Links

- Map: [[L07-00-map]] · formulas: [[L07-10-formulas]] · code: [[L07-12-python]].
- Exam style: `rules/00_estilo_avaliacao.md` (macro-1 True/False rules).
