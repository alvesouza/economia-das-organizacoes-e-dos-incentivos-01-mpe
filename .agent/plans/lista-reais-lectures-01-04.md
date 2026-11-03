# Plan: list of real book exercises, Lectures 1–4

User request (2026-10-31): "prepare a list with real exercises for up to lecture 04". No question
round (memory `feedback-skip-question-rounds`); defaults below, stated in the report.

## Output

`Listas/lista-reais-lectures-01-04.tex` → `.pdf` (pdflatex, lmodern + cmap, `pdffonts` all
Type 1). Real exercises only, no original questions, no answer key (the §9 question at the end
offers a solutions PDF and a roadmap PDF).

## Selection (default)

24 exercises, 4 blocks (one per lecture, 6 each), within each block rising difficulty:
2 foundations, 3 exam, 1 advanced. Drawn from `Listas/pratica-lecture-0{1,2,3,4}.md`, whose
statements are already transcribed and page-checked. Mix of sources per block (Tadelis
first, the book the slides follow; then Gibbons, Muñoz-Garcia, MWG). Excluded: graded in-class
cases and anything a list flags as protecting them (Tadelis 6.4, 6.12); items flagged "not
covered in class" in L02 unless no alternative.

## Block format (global rule + `rules/00_estilo_avaliacao.md` §5)

1. Source line: author (year), title, chapter, exercise number and name, printed page
   `[PDF n]` (viewer page = `(printed + offset) // scale + 1`, `Livros/book-registry.json`),
   answer availability, "reproduced verbatim".
2. Full statement: all parts, numbers, tables, figure values (figure embedded from
   `Listas/figures/` or rebuilt), and any referenced exercise/example/table copied in the
   same block under its own source line.
3. Source wording kept; only LaTeX re-typesetting, rebuilt tables, undone hyphenation.

## Steps

1. Select the 24 items; record the selection table at the top of the PDF (block, #, source,
   page, level, what it trains).
2. For each: re-check the statement against the rendered PDF page; resolve every internal
   reference ("Exercise X", "Figure Y", "the game above") and copy it in; settle answer
   availability (Muñoz-Garcia: worked answer; MWG: solutions manual; Tadelis/Gibbons: none
   in the book).
3. Write the `.tex`, compile twice, check `pdffonts`, page count, every figure present.
4. Report; end with the §9 question (roadmap PDF / solutions PDF).

## Follow-up (user chose both PDFs, 2026-10-31)

**Solutions** — mirror `Listas/pratica-lecture-01-solutions/`: folder
`Listas/lista-reais-lectures-01-04-solutions/` with `main.tex` (same preamble, `exsol`
environment, `\input{item01}`…`\input{item24}` in list order), one `itemNN.tex` per exercise,
check scripts, `main.pdf` copied to `Listas/lista-reais-lectures-01-04-solutions.pdf`.
Per item: number + page + one-line "what is asked" (never the statement), method (book section,
slide), derivation, interpretation, verification against the book's answer where one exists.
Agent A: `main.tex`, items 1–12 (items 1–6 reuse `pratica-lecture-01-solutions/itemNN.tex`
for the same exercises), `check_A*.py`. Agent B: items 13–24, `check_B*.py`. Main loop compiles.

**Study pack** — write `Listas/roteiro-lectures-01-04.md` with the `/exercise-plan` reading and
roadmap tables (pages of each exercise and its reading section), then `/study-pack` on it.
