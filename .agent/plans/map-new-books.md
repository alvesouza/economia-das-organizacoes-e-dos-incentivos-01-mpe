# Plan: map the new books (2026-10-09)

New in `Livros/`: Cabral (2017, 2nd ed.), Giambiagi & Garcia (2010), Varian *Intermediate
Microeconomics with Calculus* (2014, 1st ed.; the syllabus cites *Intermediate Microeconomics*
8th ed., so chapter numbers differ). M&R is still missing.

1. Dump each PDF with `pdftotext -layout` (form feeds = page breaks) to the scratchpad. Read
   TOCs, find the printed-page offset per book, and locate the in-scope chapters and their
   end-of-chapter exercises.
2. Convert the three to `.md` with markitdown (background), same naming as MWG.
3. Update `book-registry.json` (offsets), `BOOKS.md` (status + edition divergence).
4. Update `Map/books-index.md`, `exercises-index.md`, `topics-index.md`, `study-guide.md`.
5. Update the `Other refs` lines in `rules/01`–`09`, the bibliography table in
   `rules/11_curso_programa.md`, the README warning, and `rules/00_estilo_avaliacao.md` §5.
6. Copy the PDFs into `NotebookLM/sources/` with the `Livro_` prefix.

Scope: only chapters that serve the 9 topics; everything else gets one line.
