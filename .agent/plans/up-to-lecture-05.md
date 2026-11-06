# Plan: remap to the real schedule, audio prompts L03–L05, real-exercise list L01–L05, push (2026-11-06)

User request: "map the lectures, write notebooklm audio prompts for up to what lecture 05 would be,
create exercises lists for up to lecture 05 with real exercises, then push to origin".

## Real schedule (from the slides)

| L | Date | Content (slides) | Old estimated unit(s) it draws on |
|---|---|---|---|
| 3 | Oct 27 | `Aula/Lecture03.pdf` "Mixed strategies and dynamic games": mixed strategies, indifference, existence (end of L2); extensive form, information sets, perfect/imperfect info; pure, mixed, behavioral strategies, perfect recall; sequential rationality, backward induction, SPE; mini case "Work or shirk?" | `Notas/L02` §07–09, `Notas/L03` |
| 4 | Nov 3 | `Aula/Lecture04.pdf` "Credible threats and subgame perfection": Brexit case (extensive and strategic form, too many NE, backward induction, lessons: sunk investment, observability, cheap talk); subgames and SPE (examples); repeated games: definition and payoffs | `Notas/L03` §05–06, `Notas/L05` §01, §03 |
| 5 | Fri Nov 6 | (no slides yet; L04 wrap-up) finitely repeated games: unraveling, carrots and sticks; infinitely repeated games, one-stage deviation principle, folk theorem; bargaining | `Notas/L05`, `Notas/L04` §03 (OSDP), §05–07 (bargaining) |
| 6–8 | Nov 10–24 | not yet known; the estimated units L06–L08 stand, possibly shifted | `Notas/L06`–`L08` |

## Work

1. **Map (main loop):** `Map/study-guide.md` rows and sections L3–L5 to the table above, L6–L8
   flagged; `Map/topics-index.md` schedule note (T-topic → real lecture); `Notas/00-index.md`
   note mapping estimated units to real lectures.
2. **Audio (agent):** overwrite `NotebookLM/audio/lecture-0{3,4,5}-audio-part{1,2}.md` with prompts
   built on the real content (L3, L4 from their slides; L5 from the L04 wrap-up + notes). Sources
   `Aula_Lecture03 - Mixed Strategies and Dynamic Games.pdf`, `Aula_Lecture04 - Credible Threats
   and Subgame Perfection.pdf`. < 5,000 chars, no language line. README rows updated.
3. **List (agent):** `Listas/lista-reais-lectures-01-05.tex/.pdf`, 5 blocks × 6 real exercises,
   blocks follow the real schedule; reuse statements from `lista-reais-lectures-01-04.tex` and
   `pratica-lecture-0{1..5}.md`; global rule + `rules/00_estilo_avaliacao.md` §5.
3b. **Difficulty and solutions (user, 2026-11-06):** within each block, strictly increasing
   difficulty rated 1–5, the last item genuinely graduate-level. Then detailed solutions for all
   30 in `Listas/lista-reais-lectures-01-05-solutions/` (mirror `lista-reais-lectures-01-04-solutions/`:
   `main.tex`, `itemNN.tex`, check scripts; reuse 01-04 items for the same exercises and deepen
   them where thin). Detail per item: what is asked (one line), method with book section and slide,
   every derivation step, the economic interpretation, a check against the book's answer where
   one exists, and the common mistakes. Compiled to `Listas/lista-reais-lectures-01-05-solutions.pdf`.
   This replaces the §9 solutions question (the user asked).
3c. **One PDF per lecture (user, 2026-11-06):** list in `Listas/lista-reais-lectures-01-05/block{1..5}.tex`
   + `preamble.tex`; full driver `Listas/lista-reais-lectures-01-05.tex` and per-lecture drivers
   `Listas/lista-reais-lecture-0{1..5}.tex`. Solutions likewise: per-lecture drivers in the
   solutions folder inputting that lecture's items, PDFs `Listas/lista-reais-lecture-0N-solutions.pdf`
   next to the combined `lista-reais-lectures-01-05-solutions.pdf`.
3d. **10 per lecture (user, 2026-11-06):** 50 exercises, 10 per block, same difficulty rule.
   Single source of order: `Listas/lista-reais-lectures-01-05/order.md` (per-lecture no., combined
   no., ID, slug, difficulty). Solution files are `sol-<slug>.tex` with no hard-coded numbers;
   drivers call `\solitem{n}{slug}` (defined in `sol-preamble.tex`) in `order.md` order.
4. **Commit and push (main loop):** check nothing copyrighted is staged (books, NotebookLM sources,
   case PDFs are ignored); commit; `git push origin master`. Then the §9 question (solutions / study pack).
