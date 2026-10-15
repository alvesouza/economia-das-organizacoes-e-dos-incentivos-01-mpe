# Book list — Economia das Organizações e dos Incentivos (MPE Insper, 2024/34)

Bibliography taken from the course syllabus (`Captura de tela 2026-10-07 225909.png`).
First search: `D:\Livros` (≈49,500 files, by file name and folder path) and the sibling MPE
projects, 2026-10-09. Three more books were added to `Livros/` by hand later that day, and the
main textbook (Milgrom & Roberts) that evening.

## Summary

| # | Role | Book | Status |
|---|---|---|---|
| 1 | **Basic (main)** | Milgrom & Roberts — *Economics, Organization, and Management* (Prentice-Hall, 1992) | ✅ **In `Livros/`** (PDF + `.md`), syllabus edition |
| 2 | Complementary | Cabral — *Introduction to Industrial Organization*, 2nd ed. (MIT Press, 2017) | ✅ **In `Livros/`** (PDF + `.md`), syllabus edition |
| 3 | Complementary | Giambiagi & Garcia — *Risco e Regulação: Por que o Brasil enfrentou bem a crise financeira e como ela afetou a economia mundial* (Elsevier, 2010) | ✅ **In `Livros/`** (PDF + `.md`; Campus imprint, 2010) |
| 4 | Complementary | Mas-Colell, Whinston & Green — *Microeconomic Theory* (Oxford UP, 1995) | ✅ **In `Livros/`** (PDF + `.md` + solutions manual) |
| 5 | Complementary | Varian — *Intermediate Microeconomics*, 8th ed. (W.W. Norton, 2010) | ⚠️ **Different edition**: *Intermediate Microeconomics **with Calculus***, 1st ed. (2014) |

| 6 | **Game theory (main for the lectures)** | Tadelis — *Game Theory: An Introduction* (Princeton UP, 2013) | ✅ **In `Livros/`** (PDF + `.md`), added 2026-10-13 |
| 7 | Game theory | Gibbons — *Game Theory for Applied Economists* (Princeton UP, 1992) | ✅ **In `Livros/`** (PDF + `.md`), added 2026-10-13 |
| 8 | Game theory (exercises) | Muñoz-Garcia & Toro-Gonzalez — *Strategy and Game Theory: Practice Exercises with Answers*, 2nd ed. (Springer, 2019) | ✅ **In `Livros/`** (PDF + `.md`), added 2026-10-13 |

**5 of 5 syllabus books in hand** (Varian in a different edition), plus **3 game-theory books**
(rows 6–8) added on 2026-10-13: 8 books in `Livros/`.

## In `Livros/`

| File | Notes |
|---|---|
| `Paul Milgrom, John Roberts - Economics, Organization, and Management (1992, Prentice-Hall, Inc.) - libgen.li.pdf` + `.md` | **Main textbook**, syllabus edition. 635 PDF pages, OCR text layer (noisy: split digits like "1 92 1", broken small caps in headings; the body reads well). The scan drops part-divider versos, so `pdf_page = printed + 17` (Ch. 1–2), `+16` (Ch. 3–6), `+15` (Ch. 7–15), `+14` (Ch. 16–17): see `book-registry.json`. |
| `Luis M. B. Cabral - Introduction to Industrial Organization, second edition (2017, MIT Press) - libgen.li.pdf` + `.md` | Syllabus edition. Text layer (ClearScan OCR: spaced-out headings, otherwise clean). `pdf_page = printed + 12`. |
| `Fabio Giambiagi, Marcio Garcia - Risco E Regulação (2010, Campus) - libgen.li.pdf` + `.md` | Edited volume, 18 chapters by different authors, in Portuguese. The scan drops blank pages, so the offset changes by chapter (25 → 13): see `book-registry.json`. |
| `[First edition] Hal R. VArian - Intermediate Microeconomics with Calculus Hal (2014, W. W. Norton & Company) - libgen.li.pdf` + `.md` | **Edition divergence**: the syllabus cites the 8th edition of *Intermediate Microeconomics* (2010). This is the calculus version (math moved from appendices into the text). Chapter titles match the standard book, but chapter numbers and pages may not. Always cite it as "Varian (2014, with Calculus)". `pdf_page = printed + 25`. |
| `Andreu Mas-Colell, … - Microeconomic Theory (1995 …).pdf` + `.md` | From `D:\Livros\Mercado\Economia\Microeconomia\avançado\MasCollel\`; `.md` reused from `Microeconomia 01-MPE` (md5-identical PDF). 2-up scan: `pdf_page = (printed + 20) // 2`. |
| `Andreu Mas-Colell, … - Solutions Manual … (1997 …).pdf` + `.md` | Companion solutions manual, not in the syllabus. |
| `Risco_Incerteza_Varian.pdf` | 48-page scanned excerpt (Ch. 11–13), no text layer. **Superseded** by the full Varian above; its page numbers differ from the calculus edition, so it may be from the 8th edition the syllabus cites (not confirmed). Can be deleted. |

## Game-theory books (added 2026-10-13)

Lecture 1 (`Aula/Lecture01.pdf`, 2026-10-13) showed that the course is a game-theory sequence
(static games → Nash → dynamic games → bargaining → repeated games → Bayesian games, auctions →
signaling), not the Milgrom & Roberts plan the syllabus suggested. The slides follow **Tadelis**'s
notation and examples (the M/F Prisoner's Dilemma, the 3×3 IESDS game (4.1), the
existence/uniqueness/invariance criteria), so Tadelis is now the main reference. The three books
were copied from `D:\Livros` under clean names and converted with markitdown (`/convert` method).
Page offsets are 0-based PDF indices (`pdf_index = printed + offset`): see `book-registry.json`.

| File | Notes |
|---|---|
| `Steven Tadelis - Game Theory An Introduction (2013, Princeton University Press).pdf` + `.md` | **Main game-theory reference.** From `D:\Livros\Desenvolvimento de Jogos\livros de game design\game_theory_an_introduction.pdf`. Publisher e-book, 417 PDF pages, clean text layer (markitdown runs some headings together, e.g. "IteratedEliminationand…"; the body reads well). Offset **+18** everywhere. 19 chapters, end-of-chapter exercises; **no answers in the book** (the preface says about half have solutions online at the Princeton UP page, the rest are instructor-only). |
| `Robert Gibbons - Game Theory for Applied Economists (1992, Princeton University Press).pdf` + `.md` | From `D:\Livros\Mercado\Economia\`. 272 PDF pages, OCR text layer (some broken symbols in math, e.g. "Coumot"). The scan drops the blank page after each chapter, so the offset falls by chapter: **+7** (Ch. 1), **+6** (Ch. 2), **+5** (Ch. 3–4), +4 (index). |
| `Felix Munoz-Garcia, Daniel Toro-Gonzalez - Strategy and Game Theory Practice Exercises with Answers, 2nd ed. (2019, Springer).pdf` + `.md` | From `D:\Livros\downloads\`. 530 PDF pages, text layer. Worked answers follow every exercise; exercises are graded A/B/C by difficulty. 11 chapters, 134 numbered exercises in the body (the preface says 153). Blank versos are missing before some chapters, so the offset falls from **+12** (Ch. 1–3) to **+6** (Ch. 11): see the registry. |

**Not copied: Gibbons solutions.** `D:\Livros\Mercado\Economia\378467289-Gibbons-Game-Theory-for-Applied-Economists-Solutions-pdf.pdf`
(36 pages) is *The Unofficial Solution Manual to A Primer in Game Theory* by Navin Kumar (Delhi
School of Economics, unfinished draft, last updated 2013-01-20; it warns that it is a beta with
errors). It has answers to Problems 1.1–1.14, 2.1–2.23, 3.1–3.8 and 4.1–4.6. Use with care.

## Missing: still to obtain

| Priority | Book | What it is used for |
|---|---|---|
| optional | Varian, *Intermediate Microeconomics*, 8th ed. | Only to cite the syllabus edition's page numbers; the content is covered by the calculus edition. |

The catalogue TOC of Milgrom & Roberts that stood here before the book arrived is superseded
by the section-level map read from the book itself.

Chapter- and section-level mapping of every book: [`Map/books-index.md`](../Map/books-index.md).

## Related titles already in `D:\Livros` (not in the syllabus, not copied)

| Book | Path under `D:\Livros` | Useful for |
|---|---|---|
| Jean Tirole, *The Theory of Industrial Organization* (1988) | `Mercado\Economia\Regulation Theory\` | Graduate-level theory of the firm, vertical control |
| Choi, Dunaway & Muñoz-Garcia, *Industrial Organization: Practice Exercises with Answer Keys* (Springer, 2023) | `Mercado\Economia\` | Extra IO exercises with answers |
| Viscusi, Harrington & Sappington, *Economics of Regulation and Antitrust*, 5th ed. (MIT Press, 2018) | `Mercado\Economia\Regulation Theory\` | Regulation |
| Jehle & Reny, *Advanced Microeconomic Theory*, 3rd ed. (2011) | `Mercado\Economia\Microeconomia\avançado\` | Information economics at graduate level |
| Varian, *Microeconomic Analysis* (+ solutions) | `Mercado\Economia\Microeconomia\avançado\` | Graduate version of Varian |
| Muñoz-Garcia, *Practice Exercises for Advanced Microeconomic Theory* (MIT Press, 2017) | `Mercado\Economia\Microeconomia\` | MWG-level exercises |
