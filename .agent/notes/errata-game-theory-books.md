# Errata and caveats found while solving Lecture 1 exercises (2026-10-13)

Source: worked solutions in `Listas/pratica-lecture-01-solutions/` (checks `check_A/B/C.py` pass).

| Book / item | Issue |
|---|---|
| Muñoz-Garcia & Toro-Gonzalez Ch. 1 Ex. 2, Fig. 1.4 | Cell (L, aar) printed as (10,0); plan aar rejects after L, so it is (0,0). |
| Muñoz-Garcia & Toro-Gonzalez Ch. 6 Ex. 1(c) | Threshold printed $\delta \ge 0.76$ (rounded down: at 0.76 the sum is ≈2.963 < 3, cooperation fails); exact 0.7627. Part (a) says the punisher plays "NC" (means C) and calls (NC,NC) "competitive"; the punishment phase is never checked and the strategies are called "tit-for-tat" (they are not). |
| Muñoz-Garcia & Toro-Gonzalez Ch. 6 Ex. 9, pp. 306–307 | $u_2(L;p)$ printed $7+3p$, is $1+8p$; the convex hull is called "not convex"; cites "Fig. 6.7" for Fig. 6.11. Final $\delta \ge 1/3$ correct. |
| Muñoz-Garcia & Toro-Gonzalez Ch. 6 Ex. 7 (= Gibbons 2.11) | Punishes with the mixed equilibrium, so it is not the pure-strategy SPE asked for (pure (M,C) works); states $BR_1(R)=B$, is $T$. |
| Muñoz-Garcia & Toro-Gonzalez Ch. 3 Ex. 1, p. 89 | Indifference condition printed $3+3q=q+2-2q$; it is $3-3q$ (as printed, $q=-1/4$). The final $q=1/2$ is right. |
| Tadelis 5.8 | "$Q=q_i+\cdots+q_n$" should be $q_1+\cdots+q_n$. |
| MWG solutions manual 8.D.6 (pp. 8-15–8-16) | Cases 3–4 say "Player 2" where player 1 is meant; the "all other cases" formula is 0/0 when a player is indifferent across all profiles. |
| MWG solutions manual 8.B.1 | Ignores $h_i \ge 0$: with $\alpha \le 0$, $\beta < 0$, $h_i = 0$ is strictly dominant though $\beta \ne 0$; "iff $\beta = 0$" holds only for $\alpha > 0$. |
| MWG solutions manual 8.B.3 | Does not prove uniqueness of the weakly dominant bid nor treat ties. |
| MWG solutions manual 8.B.4 | Assumes an undominated dominator exists without proof. |
| Tadelis 4.2(b) | Works only under Tadelis's weak-dominance definition ($\ge$ everywhere); under the lecture's (strict somewhere) a player cannot have two weakly dominant strategies. |
| Tadelis 4.4(b) | Fails with a positive bid increment: with one-cent steps, capped price and random ties, bidding $v - 1$ cent weakly dominates $v$. Holds in the zero-increment limit. |
| Gibbons Problem 1.2 | Top-left cell scans as "2.0"; read as (2,0), as the unofficial manual does. |
| Tadelis 4.10 | No tie rule stated; solutions assume even splits. |

# Errata found while writing the lecture notes `Notas/L01`–`L08` (2026-10-16)

Each is flagged in the note named and asserted in that unit's Python note. Unverified by a
second reader; check against a later printing before citing in an answer.

| Book / place | Issue | Note |
|---|---|---|
| Tadelis p. 163 | Flooding remark prints $q_2 = 40$; eq. (8.1) gives 35. | `Notas/L03` Stackelberg |
| Tadelis p. 169 | The FOC multiplies each derivative by the constant inside the log; the optimum is $x_1 = K/2$, not $2K/3$, so "player 1 overconsumes" does not follow with log utility. | `Notas/L03` time inconsistency |
| Cabral p. 168, Fig. 7.7 | Price-war payoff printed $(-10, 10)$; the text gives the incumbent $-10$. Conclusion unchanged. | `Notas/L03` entry/commitment |
| Tadelis p. 202 | Firm 2's deviation uses its own $q=23$ where the rival's 22 belongs: $v_2^d = 1156$, $\delta_2^* = 121/256 \approx 0.473$ (printed 1122, 0.392). Firm 1's 0.595 still binds. | `Notas/L06` Cournot collusion |
| Tadelis p. 203 | "$p = 45$" is total output; the collusive price is 55. | `Notas/L06` |
| M&R p. 263 | Honour condition printed $NV > G$; their trust box gives the cheater $V+G$, so $\delta \ge G/(V+G)$. | `Notas/L06` reputation |
| Tadelis p. 214 (Remark) | The adjustments 0.151, 0.076, … equal $\Delta\delta^{t-1}/(1+\delta)$ (a change every second period), not a one-off change (0.029 at $t=26$). | `Notas/L05` folk theorem |
| Tadelis p. 264 | "Both jurors always convict" is not an equilibrium when $p>q$ (pivotal juror with an innocence signal acquits; e.g. $q=0.6$, $p=0.7$). Check before Exercise 12.8(a). | `Notas/L07` common values |
| Tadelis p. 305 | $Ev_2$ for $(OE, A)$ printed $1-p$; should be $1+p$. | `Notas/L08` |
| Tadelis p. 322 | Matrix cell $(DU, BB)$ printed 4.5; should be 5.5. | `Notas/L08` MBA game |
| Tadelis p. 331 | Entrant's pooled-entry profit printed $7/18$; arithmetic gives $7/36$. | `Notas/L08` limit pricing |
| Tadelis Def. 16.1 | Condition 2 reads $v_2$ where it must be $v_1$. | `Notas/L08` |
| Tadelis Ex. 16.2 | Prints $q_1^{1L}=1.5$ where $q_1^{1H}$ belongs. | `Listas/pratica-lecture-08.md` (optional extra) |
| MWG Fig. 8.B.3 (3×2) | Iterated weak elimination has three end states, (D,R), (D,L), D×{L,R}, not two. | `Notas/L01` IESDS |
| Tadelis p. 81 | (M, C) is the unique *pure* NE, but the game has four more mixed NE (e.g. $(1/6, 5/6, 0)$ for both). | `Notas/L02` Nash equilibrium |
| Tadelis p. 87, fn. 5 | Commons gain 0.051 is the base-10 value; with natural logs $\ln(9/8) \approx 0.118$. | `Notas/L02` commons |
| Tadelis p. 93 (Remark) | Monopoly price called "45"; it is 55. | `Notas/L02` |

# Found while solving `Listas/lista-reais-lectures-01-04.tex` items 13-24 (2026-10-31)

Source: `Listas/lista-reais-lectures-01-04-solutions/item13`-`item24.tex`; checks `check_B_L03.py`, `check_B_L04.py` pass.

| Book / item | Issue |
|---|---|
| Muñoz-Garcia Ch. 4 Ex. 3 (p. 162) | SPNE text calls the third component the reply "to player 1 selecting Confess (in Subgame 3)"; Subgame 3 follows Not Confess. |
| Muñoz-Garcia Ch. 4 Ex. 12 (pp. 186-188) | Follower FOCs carry "if $q_1 > 0$" where $q_2 > 0$ is meant. Quantities (4,2) and (4,2,1) correct. |
| Muñoz-Garcia Ch. 6 Ex. 8 (pp. 303-304) | With simultaneous unanimity votes, "everyone always rejects" is also a stationary SPE (payoff 0); uniqueness needs pivotal (undominated) votes or sequential responses. Its $x_{two} \ge \delta^2 x_{prop}$ skips the step $\delta x_{next}$; same result. |
| Tadelis 9.4(d) (p. 188) | With $\delta = 0.4 > \delta^* = 1/16$ the monopoly split is supported, so the "if not" branch is empty. General bound: $q \ge \frac{100}{3}(1-\sqrt\delta)$. |
| Tadelis 9.4(a) | With $\delta = 0$ literally, stage-2 actions affect no payoff, so every stage-2 profile is an equilibrium of those subgames; read as stage-2 NE. |

## Found while solving the re-aligned practice lists, Lectures 2–8 (2026-11-12)

Source: `Listas/pratica-lecture-0{2..8}-solutions/` (all check scripts pass). Each item is also
flagged inside its solution and, where the statement itself is at fault, in a note under the
verbatim statement in the list.

| Book / item | Issue |
|---|---|
| Tadelis 5.3(a) | "Unique NE ⇒ IESDS leaves it alone" fails with payoff ties (e.g. (1,1),(1,0)/(1,0),(0,1): unique NE (U,L), IESDS deletes nothing; 6,912 of 65,536 ordinal 2×2 games). Holds without ties. |
| Gibbons 1.5 (second part) | No $q'$ makes $(q_c,q_c)$ the unique NE with no strictly dominated strategy; $q'=5(a-c)/12$ is the closest (two extra weak NE). |
| Tadelis 9.3 | As printed has no answer for $\delta\le1$: stage-1 gain 3 vs. stage-2 swing at most $2\delta$ (verified on PDF p. 206–207). |
| Cabral 7.12 | As printed $H$ is dominant and $(H,H)$ efficient (5 > 4, 8 > 4): no cooperation problem (verified on PDF p. 193). |
| MWG 12.AA.1 | False as printed; the MWG solutions manual (p. 12-46) lists it as a first-printing erratum. |
| Muñoz-Garcia Ch. 6 Ex. 3(c) | Prints $\delta \ge 0.901$; its own numbers (1012.5, 1139.06, 900) give $9/17 \approx 0.529$. |
| Muñoz-Garcia Ch. 6 Ex. 10 | Text layer shows collusive profit $a^2/(8(b+d))$; derivation gives $a^2/(4(b+d))$ (scan-dependent, stated "as extracted"). |
| Cabral 9.1 | Ambiguous discount: eq. (9.5) as written gives $\delta_A=0.80$, $\delta_B=0.694$; a monthly reading of −30% flips the ranking. |
| Tadelis 8.12 | No SPE unless player 2 accepts at the tie $x=2$. |
| Tadelis 8.16 | Sophisticated plan is $(K/2, K/3, K/6)$; the book's printed $2K/3$ plan is wrong. |
| Muñoz-Garcia Ch. 4 Ex. 9 | Statement text and figure disagree on who moves at stage 100 (solution follows the figure). |
| Tadelis 12.8(a) (and p. 264) | $CC,CC$ is a BNE only if $p\le q$; for $p>q$ the pure BNE are $AA,AA$, $CA,CC$, $CC,CA$. |
| Tadelis 13.5(c) | "High type uniform on [4,6]" is not an equilibrium; the indifference cdf is $G(b)=(b-4)/(8-b)$, revenue 5 (= English). |
| MWG solutions manual 13.C.4 | Drops $w(0)=\underline\theta$: correct $w(e)=\sqrt{2e^2+\underline\theta^2}$; the manual's $\sqrt2\,e$ is the case $\underline\theta=0$. |
| Tadelis Def. 16.1 | Prints $v_2$ where the sender's $v_1$ belongs (intuitive criterion). |
| Muñoz-Garcia Ch. 9 Ex. 1 | Extracted text garbles the pooling-belief condition; best reply gives $q\le1/3$. |
