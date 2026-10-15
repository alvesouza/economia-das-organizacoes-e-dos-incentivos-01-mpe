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
