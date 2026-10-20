# Plan — `/notes` skill and study notes for Lectures 1–8

Decided with the user (2026-10-16): copy the design of
`../Finanças 01 - MPE/Notas/` into a reusable `/notes` command; **companions for every
lecture** (1–2 each, built and linked). Lecture 1 is taught (slides `Aula/Lecture01.pdf`);
Lectures 2–8 are **estimated** from `Map/study-guide.md` and reconciled when slides arrive.

## 1. The skill — `.claude/commands/notes.md`

Codifies the Finanças design:

- one folder per unit `Notas/LNN/`; `LNN-00-map.md` first; one note per section
  (`LNN-NN-<slug>.md`); support notes `-formulas`, `-pitfalls`, `-python`;
  `figures/make_figures.py` + PNGs through the shared `Notas/_figstyle.py`;
  `companions/companion-<model>.html`.
- per note: YAML front matter (`tags`, `date`, `status`, `source` with printed pages),
  **Claim** block, Prev/Next/Map links, numbered sections tagged **U/C/G**, every
  derivation step, worked examples with arithmetic, figures with one italic caption
  line, `Interactive companion` callouts, a Links section.
- layers for this course: **U** intuition (Gibbons, Tadelis prose), **C** examinable
  (slides + Tadelis definitions/propositions), **G** formal (MWG), named or proved,
  not examinable unless the lecture brings it.
- `status: taught | estimated`; estimated units carry a banner and a reconcile step.
- companions follow `.claude/commands/companion.md` Steps 2–6. The control contract
  is fixed in this plan (§3) instead of the Step 0 question round, because the user
  approved companions for all lectures in one answer.
- exercises by number + page only; English; LaTeX; Python only.

## 2. Shared files

- `Notas/_figstyle.py` — copied from Finanças (same colour roles as the companions).
- `Notas/00-index.md` — the units, their status, and their companions.
- `Map/study-guide.md` — one `Notes:` line per lecture pointing to its map.
- `README.md` — a `/notes` row in the command table.

## 3. Units and companion contracts

| Unit | Sources (printed pp.) | Companions (`companions/companion-<model>.html`) |
|---|---|---|
| L01 taught | slides; Tadelis Ch. 3 (43–58), §4.1–4.2 (59–69); Gibbons §1.1.A–B | **partnership-dominance**: $y$, $c$, $n$ → payoff to E vs S, which strategy is dominant, social-dilemma band $y/n<c<y$ (landmarks $c=y/n$, $c=y$). **cournot-iesds**: $a,b,c_1,c_2$, rounds $k$ → shrinking IESDS interval converging to the Cournot point (Tadelis p. 65) |
| L02 est. | Tadelis §4.3, Ch. 5–6 (69–126); Gibbons §1.1.C–1.3 | **mixed-2x2**: four payoff parameters of a 2×2 game → best-response correspondences in $(p,q)$, every NE (pure and mixed), indifference read-outs. **cournot-best-responses**: $a,b,c_1,c_2$ → BR lines, NE, monopoly and competitive benchmarks |
| L03 est. | Tadelis Ch. 7–8 (129–174); Gibbons §2.1.A, 2.2.A, 2.4 | **stackelberg-vs-cournot**: $a,b,c_1,c_2$ → leader/follower vs simultaneous quantities, prices, profits, first-mover advantage |
| L04 est. | Tadelis Ch. 9, 11 (175–189, 220–237); Gibbons §2.1.D, 2.2 | **rubinstein-bargaining**: $\delta_1,\delta_2$, horizon $T$ (finite/∞), pie → proposer share by backward induction, convergence to $(1-\delta_2)/(1-\delta_1\delta_2)$ (reuse `Aula/notes-aulas-01-02/check_part2.py::proposer_share`) |
| L05 est. | Tadelis §10.1–10.3, 10.6 (190–201, 209); Gibbons §2.3.A–B | **grim-trigger**: PD payoffs $T>R>P>S$, $\delta$ → critical $\delta^*=(T-R)/(T-P)$, discounted payoffs on/off path, feasible-IR payoff set with the folk-theorem region |
| L06 est. | Tadelis §10.4–10.5 (201–209); Gibbons §2.3.C–D; M&R Ch. 8 | **collusion-threshold**: Bertrand/Cournot, $n$, $\delta$ → critical $\delta^*$ ($1-1/n$; Cournot grim-trigger expression), sustainable or not. **efficiency-wage**: Gibbons §2.3.D parameters → minimum wage that deters shirking against $\delta$ |
| L07 est. | Tadelis Ch. 12–13 (241–287); Gibbons Ch. 3 | **auction-bidding**: $n$, value $v$, reserve 0, uniform values → FPA bid $(n-1)v/n$, SPA bid $v$, expected revenue $(n-1)/(n+1)$ for both. **lemons**: quality support, buyer premium → unravelling and the traded set |
| L08 est. | Tadelis Ch. 15–16 (303–338); Gibbons §4.1–4.2 | **spence-signaling**: $\theta_L,\theta_H$, prior, cost $e/\theta$ → separating education interval, least-cost separating $e^*$, pooling wage, which equilibria exist |

Defaults come from the book example each model is taken from, cited on the page.

## 4. Execution

One subagent per unit, in parallel, each following `/notes` with this plan's row. I
write the skill, `_figstyle.py`, the index, the study-guide links and the README row,
then verify.

## Acceptance

- Every `make_figures.py` runs clean with an `assert` self-check; every embedded PNG exists.
- Every companion: Step 6 checks of `companion.md`, the three control vectors reported.
- Every `[[wiki-link]]` and `](path)` under `Notas/` resolves.
- No exercise statement reproduced; L02–L08 front matter says `status: estimated`.
