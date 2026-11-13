# Plan: re-align the practice lists to the real lectures, with solutions (all T1–T19)

User request (2026-11-12): "re-create the lists for the topics". Choices confirmed by the user:
**re-align the per-lecture lists** to the real lecture boundaries, **all topics T1–T19**, **with a
solutions PDF** per lecture.

Source of the old lists: git commit `fe47ead` (`git show fe47ead:Listas/pratica-lecture-0N.md`).
Their statements were transcribed verbatim from the book pages and verified (2026-10-20/25); new
lists copy those statement blocks unchanged and keep their source lines.

## 1. Real lecture boundaries (slides `Aula/Lecture01–05.pdf`; L6–L8 still estimated)

| Real L | Content (slides) | Topics |
|---|---|---|
| 1 | dominance, IESDS, Cournot by IESDS, spatial competition | T1, T2 |
| 2 | best responses, rationalizability, NE, Cournot, Bertrand, mixed strategies intro, BoS mixed, Nash's theorem | T3, T4, T5, T6 (basics) |
| 3 | Edgeworth/capacity, mixed strategies finished, price dispersion; game trees, information sets, strategies, backward induction, subgames, SPE, Stackelberg | T6 (rest), T7, T8 |
| 4 | Brexit case, non-credible threats, subgames and SPE, commitment; repeated games defined, finitely repeated | T8, T9, T12 (definition) |
| 5 | finitely repeated (unraveling, carrot and stick), one-stage deviation, infinite repetition, grim trigger, tit-for-tat; homework tacit collusion | T10, T12 |
| 6 (est.) | bargaining (announced for L5, not in its slides), tacit collusion, reputation, relational contracts | T11, T13, T14 |
| 7 (est.) | Bayesian games, adverse selection, auctions | T15–T17 |
| 8 (est.) | PBE, signaling | T18, T19 |

## 2. Item assignment (old list → new list). "Lk #n" = old `pratica-lecture-0k.md` item n.

- **New L1** = old L1, all 24 items, order unchanged. Solutions exist (`pratica-lecture-01-solutions/`); no new work beyond a header note "aligned with the slides".
- **New L2** (22) = old L2 minus Tadelis 6.5 (L2 #16), Gibbons 1.14 (L2 #20), Tadelis 6.3 (L2 #24).
- **New L3** (18) = those 3 T6 items + old L3 #1 Tadelis 7.1, #2 7.2, #3 MG Ch.4 Ex.3, #4 MG Ch.4 Ex.4, #5 7.6, #7 MG Ch.4 Ex.9, #9 7.4, #10 7.9, #11 7.10, #12 8.5, #13 8.10, #14 8.11, #19 MWG 9.B.4, #20 MWG 9.B.5, #24 Gibbons 2.1.
- **New L4** (12, + up to 3 optional new Tadelis Ch. 8 exercises on subgames/credibility not used in any list) = old L3 #6 Tadelis 8.8, #8 MG Ch.4 Ex.11, #15 8.13, #16 8.6, #17 MG Ch.4 Ex.12, #18 8.15, #21 8.7, #22 8.12, #23 8.4, #25 8.16; old L4 #4 Gibbons 2.6; old L5 #1 Gibbons 2.12.
- **New L5** (25) = old L5 #2–#17 (16 items) + old L4 #1 Tadelis 9.1, #2 9.3, #3 Gibbons 2.22, #5 MG Ch.4 Ex.18, #10 9.2, #11 9.4, #12 9.6, #19 9.5, #20 Gibbons 2.8.
- **New L6** (≈28) = bargaining block from old L4: #6 Tadelis 11.1, #7 MG Ch.4 Ex.1, #13 11.2, #14 11.3, #16 11.5, #17 Gibbons 2.19, #21 Gibbons 2.20, #25 11.7 (8 items) + old L6 items, dropping at most 5 with a stated reason. Old L4 #8–9 MG Ch.4 Ex.16–17, #15 11.4, #18 11.6, #22–24 MWG 9.B.12, 9.B.13, MG Ch.6 Ex.8 go to a "Further practice (not in the tiers)" note with source lines only.
- **New L7** = old L7 (24), **new L8** = old L8 (25): same items, re-checked tiers.

Each new list keeps the old format: frontmatter (`status: aligned` for L1–L5, `estimated` for L6–L8),
header with the real lecture title, weighting table, three tiers (tables + verbatim statement
blocks, each opening with the source line), suggested study order, consolidated reading,
consolidated exercises. A "Moved here from" line records each item's old list and number.

## 3. Solutions

Per lecture: `Listas/pratica-lecture-NN-solutions/` (`main.tex`, `sol-items.tex`, one
`sol-<slug>.tex` per item, `check_*.py`) compiled to `main.pdf` and copied to
`Listas/pratica-lecture-NN-solutions.pdf`. Style = `lista-reais-lectures-01-05-solutions/`
(`\input{../lista-reais-lectures-01-05-solutions/sol-preamble}`, `exsol` environment). Items already
solved there are reused by `\input{../lista-reais-lectures-01-05-solutions/sol-<slug>}`, never
copied or rewritten. Every number is asserted by a check script; pdflatex with lmodern + cmap,
`pdffonts` all Type 1 / uni yes.

Already solved (reuse): L2 — Tadelis 5.6, 5.8, 6.8, Gibbons 1.6, 1.7, 1.12, MWG 8.D.2, 8.D.6, MG
Ch.2 Ex.2, MG Ch.3 Ex.1; L3 — Tadelis 7.1, 7.2, 7.4, 7.6, 7.9, 7.10, 8.5, 8.10, 8.11, MWG 9.B.4,
9.B.5, Gibbons 2.1, MG Ch.4 Ex.3; L4 — 8.4, 8.6, 8.7, 8.8, 8.11?, 8.13, MG Ch.4 Ex.11, Gibbons
2.12; L5 — Cabral 7.13, Tadelis 9.1, 10.2, 10.3, 10.7, Gibbons 2.11, MG Ch.6 Ex.1, 6.9; L6 —
Tadelis 11.5, Gibbons 2.20.

## 4. Work split (parallel agents, one owner per lecture folder)

A: L2 · B: L3 + L4 · C: L5 · D: L6 · E: L7 · F: L8. L1: header note only (me).

## 5. After the agents

- Rewrite the 445 `Listas/pratica-lecture-0N#k. Label` anchors in `Map/*.md` (and the notes that
  link items) with an old→new map built from the new lists, by script; verify zero dangling.
- Study guide rows: point each lecture to its new list and solutions PDF.
- Spot-check rendered pages of each solutions PDF.
