# Errata and caveats found while solving Lecture 1 exercises (2026-10-13)

Source: worked solutions in `Listas/pratica-lecture-01-solutions/` (checks `check_A/B/C.py` pass).

| Book / item | Issue |
|---|---|
| Muñoz-Garcia & Toro-Gonzalez Ch. 1 Ex. 2, Fig. 1.4 | Cell (L, aar) printed as (10,0); plan aar rejects after L, so it is (0,0). |
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
| MWG Fig. 8.B.3 (3×2) | Iterated weak elimination has three end states, (D,R), (D,L), D×{L,R}, not two. | `Notas/L01` IESDS |
| Tadelis p. 81 | (M, C) is the unique *pure* NE, but the game has four more mixed NE (e.g. $(1/6, 5/6, 0)$ for both). | `Notas/L02` Nash equilibrium |
| Tadelis p. 87, fn. 5 | Commons gain 0.051 is the base-10 value; with natural logs $\ln(9/8) \approx 0.118$. | `Notas/L02` commons |
| Tadelis p. 93 (Remark) | Monopoly price called "45"; it is 55. | `Notas/L02` |
