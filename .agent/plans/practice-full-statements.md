# Plan: full exercise statements in the practice plans

User request (2026-10-20): rewrite the practice plans with the full text of every book
exercise, per the global style rule (`~/.claude/commands/templates/estilo-avaliacao.md` §5,
"Book questions used in a list or mock exam"). This overrides the repo's "number + page only"
rule for these files; `CLAUDE.md` and `rules/00_estilo_avaliacao.md` §5 are updated to match.

## Scope

- `Listas/pratica-lecture-01.md` — 24 items (Tadelis, Muñoz-Garcia, Gibbons, MWG).
- `Listas/pratica-aula-01-02.md` — 30 items (M&R, Cabral, Varian Calc, MWG).
- `Listas/pratica-aula-01.md` — 14 book items; 12 shared with the Aula 1+2 plan, plus M&R FFT 2.2, 2.4.
- Not in scope: the `*-solutions.pdf` builds (they cite by number; offer separately).

## Steps

1. Extract statements per book in parallel (5 agents), from the PDF (text layer + rendered
   page image to check math, tables, OCR). Fragments go to the session scratchpad, one file
   per book, one block per exercise:
   source line (author (year), *title*, exercise number and name, page, "reproduced
   verbatim"), then the statement as a blockquote; math in `$...$`; tables as Markdown
   tables; figures cropped to `Listas/figures/<book>-<ex>.png` and embedded.
2. Insert a "Statements" subsection after each tier table, in plan order (# matches the
   tier table). Edit the plan headers: "cited by number and page only" → "reproduced
   verbatim below".
3. Update `CLAUDE.md` line "Never reproduce an exercise statement" and
   `rules/00_estilo_avaliacao.md` §5 to the global rule.
4. Verify: every tier-table row has a statement block; each block's page matches the table.

## Then

Solve mini case 01 (`Listas/prep-mini-case-lecture-01.md`, slides 31–33).
