# Course programme — Economia das Organizações e dos Incentivos (tier 2, load on demand)

Moved out of `CLAUDE.md` to keep the always-on file under its 900-token budget.

## Identity

| Field | Value |
|---|---|
| Course | ECONOMIA DAS ORGANIZAÇÕES E DOS INCENTIVOS: TEORIA E APLICAÇÕES (abbr. **EOI**) |
| Programme | Mestrado Profissional em Economia (MPE), Insper |
| Syllabus record | Currículo 202431 · Período Letivo 2024/34 · 30 hours |
| Term taught | MPE 4th term 2026, 10 lectures, Oct 13 – Dec 8 |
| Professor | Isabela Brandão Furtado (from `Aula/Lecture01.pdf`) |
| Evaluation weights | In-class exercises 10% · short paper in groups 35% (content 15, presentation 15, comments on another group's paper 5) · final exam 55% (Lecture 10, Dec 8) |
| Sources | Syllabus record `Captura de tela 2026-10-07 225909.png`; real schedule and assessment `Aula/Lecture01.pdf` (slides 6–8) |

Ementa (verbatim): *"Importância do desenho organizacional. Estabelecimento de acordos
(barganha). Coordenação, motivação e eficiência. O papel dos preços de mercado. Coordenação de
atividades centralizada. Contratos, informação e incentivos."*

## Lectures × bibliography

The syllabus record lists M&R organization topics, but the course as taught (Lecture 1 slides)
is **game theory** in 10 lectures, following Tadelis (2013). Readings per lecture, with pages:
[`Map/study-guide.md`](../Map/study-guide.md). Estimate vs. reality: `.agent/notes/roadmap-reality.md`.

| L | Date | Lecture | Tadelis (2013) | Others | Project topic rules |
|---|---|---|---|---|---|
| 1 | Oct 13 | Static games: dominance, iterated elimination | Ch. 3; §4.1–4.2 | Gibbons §1.1; MWG §8.A–8.B; Muñoz-Garcia Ch. 1 | — |
| 2 | Oct 20 | Static games: Nash equilibrium, mixed strategies | §4.3; Ch. 5–6 | Gibbons §1.1.C–1.3; MWG §8.C–8.D | — |
| 3 | Oct 27 | Dynamic games: backward induction, subgame perfection | Ch. 7–8 | Gibbons §2.1–2.2, 2.4; MWG §9.A–9.B | — |
| 4 | Nov 3 | Multistage games and bargaining | Ch. 9, 11 | Gibbons §2.1.D, 2.2; MWG 9.AA; M&R p. 140 | [02](02_barganha.md) |
| 5 | Nov 6 | Repeated games I: cooperation | §10.1–10.3, 10.6 | Gibbons §2.3.A–B; MWG §12.D, App. 12.A | — |
| 6 | Nov 10 | Repeated games II: collusion, relational contracts | §10.4–10.5 | Gibbons §2.3.C–D; Cabral Ch. 9; M&R Ch. 8 pp. 259–265 | — |
| 7 | Nov 17 | Bayesian games, adverse selection and auctions | Ch. 12–13 | Gibbons Ch. 3; MWG §8.E, §13.B; M&R p. 149 | [07](07_selecao_adversa.md) |
| 8 | Nov 24 | Signaling and perfect Bayesian equilibrium | Ch. 15–16 | Gibbons Ch. 4; MWG §9.C–9.D, §13.C; M&R p. 154 | [07](07_selecao_adversa.md) |
| 9 | Dec 1 | Short-paper presentations | — | — | — |
| 10 | Dec 8 | Final exam | — | — | — |

The syllabus-record topic files `rules/01`–`09` and their M&R mapping (below) are kept as
**application background**; topics 01, 03–06, 08–09 have no lecture of their own.

| # | Topic (syllabus record) | M&R (1992) | Real lecture |
|---|---|---|---|
| 01 | Does organization matter? | Ch. 1; Ch. 4 (pp. 106–113) | — |
| 02 | Bargaining | Ch. 2 (pp. 35–39); Ch. 5 (pp. 140–149) | L4 |
| 03 | Efficiency and economic organization (+ NEPKE) | Ch. 2 (pp. 19–48) | — |
| 04 | Coordination through the market | Ch. 3 (pp. 56–78) | — |
| 05 | Coordination through management (+ Sears) | Ch. 4; Ch. 3 (pp. 78–85) | — |
| 06 | Bounded rationality, information and contracts | Ch. 5 (pp. 126–140) | L6 (relational contracts, partly) |
| 07 | Adverse selection (+ signaling) | Ch. 5 (pp. 149–162) | L7–L8 |
| 08 | Moral hazard (+ S&L crisis) | Ch. 6 | — |
| 09 | Managing moral hazard | Ch. 7 | — |

## Bibliography

| Role | Book | Edition on syllabus | Local copy |
|---|---|---|---|
| **Main as taught** | Tadelis, *Game Theory: An Introduction* | not on the syllabus record; the slides follow it | ✅ PDF + `.md` (Princeton UP, 2013) |
| Game theory | Gibbons, *Game Theory for Applied Economists* | not on the syllabus record | ✅ PDF + `.md` (Princeton UP, 1992) |
| Exercises | Muñoz-Garcia & Toro-Gonzalez, *Strategy and Game Theory: Practice Exercises with Answers* | not on the syllabus record | ✅ PDF + `.md` (2nd ed., Springer, 2019) |
| Basic (syllabus) | Milgrom & Roberts, *Economics, Organization, and Management* | Prentice-Hall, 1992 | ✅ PDF + `.md` (syllabus edition) |
| Complementary | Cabral, *Introduction to Industrial Organization* | 2nd ed., MIT Press, 2017 | ✅ PDF + `.md` (syllabus edition) |
| Complementary | Giambiagi & Garcia, *Risco e Regulação* | Elsevier, 2010 | ✅ PDF + `.md` (Campus imprint) |
| Complementary | Mas-Colell, Whinston & Green (MWG), *Microeconomic Theory* | OUP, 1995 | ✅ PDF + `.md` + solutions manual |
| Complementary | Varian, *Intermediate Microeconomics* | 8th ed., Norton, 2010 | ⚠️ *Intermediate Microeconomics with Calculus*, 1st ed. (2014): PDF + `.md`; cite as "Varian (2014, with Calculus)" |

Usage:
- **Tadelis is the floor** for game-theory content: definitions and notation follow it, and every question cites its chapter, section and printed page. **M&R** is the floor for organizational applications.
- **MWG** (Ch. 7–9, 12.D, 13) gives formal depth and graduate-mode questions; it does not set the scope. **Gibbons** is the applied second pass; **Muñoz-Garcia** gives drill with worked answers.
- **Varian** gives intermediate intuition; **Cabral** gives market structure and vertical relations; **Giambiagi & Garcia** give the Brazilian and 2008 regulatory context.
- Section and page detail for every book: [`Map/books-index.md`](../Map/books-index.md).

Full status, sources and stand-ins: [`Livros/BOOKS.md`](../Livros/BOOKS.md).

## Rules index

| File | Content |
|---|---|
| [00_estilo_avaliacao.md](00_estilo_avaliacao.md) | Exam style (macro-1 MPE style, rebound to this course) |
| [01_organizacoes_importam.md](01_organizacoes_importam.md) | Topic 1: Does organization matter? |
| [02_barganha.md](02_barganha.md) | Topic 2: Bargaining |
| [03_eficiencia_organizacao.md](03_eficiencia_organizacao.md) | Topic 3: Efficiency and economic organization (+ NEPKE) |
| [04_coordenacao_mercado.md](04_coordenacao_mercado.md) | Topic 4: Coordination through the market |
| [05_coordenacao_management.md](05_coordenacao_management.md) | Topic 5: Coordination through management (+ Sears) |
| [06_racionalidade_limitada_contratos.md](06_racionalidade_limitada_contratos.md) | Topic 6: Bounded rationality, information and contracts |
| [07_selecao_adversa.md](07_selecao_adversa.md) | Topic 7: Adverse selection (+ labour-market signaling) |
| [08_risco_moral.md](08_risco_moral.md) | Topic 8: Moral hazard (+ US S&L crisis) |
| [09_gestao_risco_moral.md](09_gestao_risco_moral.md) | Topic 9: Managing moral hazard in an organization |
| `core.md`, `context.md`, … | Efficient Token governance packs (machine-managed) |

## Directory structure

| Directory | Purpose |
|---|---|
| `Aula/` | Lecture slides and class scripts |
| `Listas/` | Exercise lists; `lista-exam.tex` template for `/exam-gen` |
| `Monitoria/` | Tutorial / office-hour material |
| `Prova/` | Exams and their solutions |
| `Simulados/` | Quiz MD files for `quiz.html` |
| `Livros/` | Textbooks (gitignored) + `BOOKS.md`, `book-registry.json` |
| `Resolucao/` | Generated exercise solutions |
| `Leituras/` | Chapter extracts and TTS narrations (`/speechify`) |
| `Map/` | Obsidian cross-reference maps (`/study-map`) |
| `NotebookLM/` | Prompts (`slides/`, `audio/`, `video/`) and `sources/` for upload (gitignored) |
| `Notebooks/` | Jupyter projects, created on first `/lab-init` |
| `Videos/` | `/explainer` videos, created on first use |
| `rules/` | Topic rules + governance packs |
| `.agent/` | `plans/` (plan before non-trivial change), `notes/` (persisted findings) |

## Sibling projects

- **Video explainer**: `D:\Documents\Git\Github\Video explainer`. Installed with `install.py --into` (editable link, no copy). Console scripts `beatcheck`, `speechify-tts`, `explainer-compile`.
- **Efficient Token**: `D:\Documents\Git\Github\Efficient Token`. Adopted with `tools/adopt.py`; packs in `rules/`, tooling in `tools/`.

## NotebookLM

Output language is set once in NotebookLM → Settings → Output language (English, all types,
audio included). Confirm it before generating a batch; prompts never carry a language line.
