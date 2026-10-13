# Plan: map Milgrom & Roberts (1992), replan the classes, write Aula 1 notes + companions (2026-10-09)

The main textbook arrived: `Livros/Paul Milgrom, John Roberts - Economics, Organization, and
Management (1992, Prentice-Hall, Inc.) - libgen.li.pdf` (635 PDF pages, text layer, OCR noise).

## 1. Map the book
- Offsets, from chapter-opening and running-head page numbers (pdftotext dump):
  Ch. 1–2 `+17`, Ch. 3–6 `+16`, Ch. 7–15 `+15`, Ch. 16–17 `+14`. One registry entry per band.
- `.md` via markitdown (same naming as the other books).
- Section-level TOC for Ch. 1–9 with printed pages; end-of-chapter exercises (location + count) for Ch. 1–7.
- Update `book-registry.json`, `BOOKS.md` (missing → in hand; the catalogue TOC was wrong for
  Part IV: Ch. 6 is moral hazard incl. the S&L case, Ch. 7 risk sharing/incentive contracts).
- Update `Map/books-index.md` (replace the catalogue section), `Map/exercises-index.md`
  (M&R exercises by number + page), `Map/topics-index.md`.

## 2. Replan the classes
- Re-anchor each of the 16 sessions in M&R sections (printed pages). Keep the syllabus order
  and the 16-session count unless the book argues otherwise; record any change and why.
- Notable facts from the TOC: Ch. 1 cases are GM/Toyota, Hudson's Bay vs. Northwest Co.,
  Salomon Brothers, Eastern Europe (Ford appears inside the GM story, to verify);
  bargaining = Ch. 2 Coase/value maximization (pp. 35–39) + Ch. 5 "Bargaining over a sale"
  (p. 140); NEPKE ↔ Ch. 2 medical-intern matching case (p. 43); Sears ↔ Ch. 3 transfer
  pricing in multidivisional firms (p. 79); S&L = Ch. 6 case (p. 170); managing moral hazard =
  Ch. 7 (pp. 206–247) + Ch. 8 efficiency wages if a lecture brings it (out by default).
- Files: `Map/study-guide.md`, `rules/11_curso_programa.md` (topic table, bibliography),
  `rules/01`–`09` header lines, README topic table if it cites pages.

## 3. Aula 1 notes
- `Aula/aula-01-notes.md`: M&R Ch. 1 as the spine (read in full, pp. 2–18), the syllabus case
  Ford × GM × Toyota, complementarities (M&R Ch. 4 pp. 106–113 "Complementarities and Design
  Decisions" — read), Cabral §3.5. Reuse the video's sourced facts (`provenance.md`) and
  checked stylized numbers (`check_numbers.py`). Exercises by number + page only.
- Fill the `rules/01` placeholders with short summaries pointing at the notes.

## 4. Companions (companion skill; question round first)
- Candidates: the two-choice complementarity model, the valley cube, the variety model.
- Ask the mandatory round (models, controls, read-outs, publish). Build in `Aula/`
  next to the notes, verify numbers in Python, publish if asked.

## Verification
- Every printed page cited is checked against the PDF text (page = pdf − offset).
- `check_numbers.py` style independent recomputation for each companion.
