# Plan: add the game-theory books (2026-10-13)

Lecture 1 showed the course is a game-theory sequence that follows Tadelis's notation.

1. Copy into `Livros/` under `Author - Title (year, publisher).pdf`:
   Tadelis (2013), Gibbons (1992), Muñoz-Garcia & Toro-Gonzalez 2nd ed. (2019).
2. Convert each to `.md` with the markitdown Python API (`/convert` method, UTF-8).
3. Calibrate `pdf_index = (printed + offset) // scale` (0-based) from running heads/folios at
   3+ points (front, middle, end); per-chapter entries if the offset drifts.
4. `Livros/BOOKS.md`: new section for the three books + the Gibbons solutions manual (mention
   only); update summary counts.
5. `Map/books-index.md`: one section per book (Tadelis all chapters + sections; Gibbons Ch. 1–4
   with sections; Muñoz-Garcia chapter list with pages and exercise ranges).
6. Report: readings per lecture L1–L8, Lecture-1 exercise inventory, slide-example matches,
   unverified items.

Verification: PyMuPDF text of the computed PDF page must show the printed folio.
