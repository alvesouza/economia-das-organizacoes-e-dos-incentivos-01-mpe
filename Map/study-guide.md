---
tags: [map, cross-reference]
date: 2026-10-13
---

# Class plan and study guide

**Real schedule**, from the first lecture's slides (`Aula/Lecture01.pdf`, 2026-10-13):
instructor Isabela Brandão Furtado, MPE 4th term 2026, **10 lectures** (8 content lectures,
paper presentations, final exam), Tuesdays except Lecture 5 (Friday). The course is **game
theory** applied to organizations and incentives, and its slides follow **Tadelis (2013)**.
This replaces the 16-session draft built from the 2024/34 syllabus record (kept at the end).
Estimate vs. reality: `.agent/notes/roadmap-reality.md`.

**Assessment.** In-class exercises 10% (in pairs, handed in the same day) · short paper in
groups 35% (content 15%, presentation and Q&A in Lecture 9 15%, comments on another group's
paper 5%; motivation, brief literature review, research question and an economic model;
partial-submission dates to be agreed in class) · final exam, individual, Lecture 10: 55%.

**How to read.** Tadelis before class (the slides use its definitions, notation and
examples); Gibbons for a second, more applied pass; MWG after class for the formal side;
Muñoz-Garcia & Toro-Gonzalez for drill with worked answers; Milgrom & Roberts and Cabral for
the organizational and IO applications. Pages are printed pages, verified on 2026-10-13
([[Map/books-index|books-index]]; offsets in `Livros/book-registry.json`).

| L | Date | Session | Tadelis (2013) | Gibbons (1992) | Project material |
|---|---|---|---|---|---|
| 1 | Tue Oct 13 | Static games I: dominance, iterated elimination | Ch. 3 (43–58); §4.1–4.2 (59–69) | §1.1.A–B (2–7) | `Listas/pratica-lecture-01.md`, `Listas/lista-lecture-01.tex`, 3 quizzes |
| 2 | Tue Oct 20 | Static games II: Nash equilibrium, mixed strategies | §4.3 (69–76); Ch. 5 (79–100); Ch. 6 (101–126) | §1.1.C, §1.2, §1.3 (8–48) | — |
| 3 | Tue Oct 27 | Dynamic games: backward induction, subgame perfection | Ch. 7 (129–150); Ch. 8 (151–174) | §2.1.A, §2.2.A, §2.4 | — |
| 4 | Tue Nov 3 | Multistage games and bargaining | Ch. 9 (175–189); Ch. 11 (220–237) | §2.1.D (68); §2.2 (71–82) | Aula 2 notes §5; `lista-aulas-01-02` block 3 ([[rules/02_barganha\|Topic 2]]) |
| 5 | **Fri Nov 6** | Repeated games I: cooperation | §10.1–10.3 (190–201); §10.6 (209) | §2.3.A–B (82–102) | — |
| 6 | Tue Nov 10 | Repeated games II: collusion, relational contracts | §10.4–10.5 (201–209) | §2.3.C–D (102–) | — |
| 7 | Tue Nov 17 | Bayesian games, adverse selection and auctions | Ch. 12 (241–269); Ch. 13 (270–287) | Ch. 3 (143–172) | [[rules/07_selecao_adversa\|Topic 7]] |
| 8 | Tue Nov 24 | Signaling and perfect Bayesian equilibrium | Ch. 15 (303–317); Ch. 16 (318–338) | Ch. 4 (§4.1–4.2, 175–210) | [[rules/07_selecao_adversa\|Topic 7]] |
| 9 | Tue Dec 1 | Short-paper presentations | — | — | — |
| 10 | Tue Dec 8 | Final exam (55%) | — | — | — |

**Tight stretch.** Lectures 4, 5 and 6 fall within eight days (Nov 3, 6, 10): read Tadelis
Ch. 10 before Nov 3.

---

## Static games of complete information

### Lecture 1 — Static games I: dominance and iterated elimination
#lecture/1
- **Content:** what a game is (rationality, interdependence, strategic reasoning); normal-form games $G = (I, \{S_i\}, \{u_i\})$, profiles and $s_{-i}$; static vs. dynamic; complete information and common knowledge; strategies as complete contingent plans; payoffs over outcomes (the grade game); solution concepts judged by existence, uniqueness, invariance; strict and weak dominance; strict dominant-strategy equilibrium and its uniqueness; Pareto optimality and social dilemmas (prisoner's dilemma); IESDS and common knowledge of rationality; application: spatial competition (two pharmacy chains on a 7-block avenue, in-class exercise).
- **Before class:** Tadelis Ch. 3 (pp. 43–58: common knowledge Def. 3.1 p. 45, normal form Def. 3.3 p. 47, the M/F prisoner's dilemma pp. 48, 51–52, existence/uniqueness/invariance pp. 55–56, Pareto Def. 3.5 p. 57) and §4.1–4.2 (pp. 59–69: dominance Defs. 4.1–4.3 and Prop. 4.1 pp. 60–61, IESDS pp. 63–65 with the slides' 3×3 game on p. 64, Cournot by IESDS p. 65, Prop. 4.2 p. 68) · Gibbons §1.1.A–B (pp. 2–7)
- **After class:** `Listas/pratica-lecture-01.md` (24 items: Tadelis 3.2–3.7, 4.1–4.7, 4.10; Gibbons 1.2; MWG 8.B.1, 8.B.3–8.B.5, 8.B.7; Muñoz-Garcia Ch. 1) · worked solutions `Listas/pratica-lecture-01-solutions.pdf` · exam-style list `Listas/lista-lecture-01.tex` · quizzes `Simulados/quiz-lecture01-{1,2,3}-*.md`
- **Formal side:** MWG §7.D (p. 228), §8.A–8.B (pp. 235–241)
- **Applications:** Cabral §7.1 (pp. 161–163); Hotelling's linear city, Cabral §14.2 (pp. 354, 358–360); M&R's "grabbing" game as a prisoner's dilemma, Table 5.1 (pp. 138–139)

### Lecture 2 — Static games II: Nash equilibrium and mixed strategies
#lecture/2
- **Content (from the slides' preview and the course outline):** best responses and rationalizability; Nash equilibrium; mixed strategies and existence.
- **Before class:** Tadelis §4.3 (pp. 69–76), Ch. 5 (pp. 79–100; Hotelling voting §5.2.5 p. 93), Ch. 6 (pp. 101–126; IESDS revisited §6.3 p. 114, existence §6.4 p. 117) · Gibbons §1.1.C (p. 8), §1.2 (pp. 14–29), §1.3 (pp. 29–48)
- **After class:** Tadelis 5.2, 5.3, 5.15 (pp. 95, 99), 6.2, 6.3 (p. 123) · Gibbons 1.3, 1.5, 1.8 (pp. 49–50) · MWG 8.C.1, 8.D.3–8.D.5 (p. 263) · Muñoz-Garcia Ch. 2 (pp. 37–84), Ch. 3 (pp. 85–151)
- **Formal side:** MWG §8.C (p. 242), §8.D (p. 246), App. A (p. 260)
- **Applications:** Cabral §7.1 (from p. 161)

## Dynamic games of complete information

### Lecture 3 — Dynamic games: backward induction and subgame perfection
#lecture/3
- **Before class:** Tadelis Ch. 7 (pp. 129–150), Ch. 8 (pp. 151–174) · Gibbons §2.1.A (p. 57), §2.2.A (p. 71), §2.4 (pp. 115–129)
- **After class:** Muñoz-Garcia Ch. 4 (pp. 153–214) · Tadelis Ch. 7–8 exercises
- **Formal side:** MWG §7.C (p. 221), §9.A–9.B (pp. 267–281)
- **Applications:** Cabral §7.2 (p. 167)

### Lecture 4 — Multistage games and bargaining
#lecture/4
- **Before class:** Tadelis Ch. 9 (pp. 175–189), Ch. 11 (pp. 220–237) · Gibbons §2.1.D sequential bargaining (p. 68), §2.2 (pp. 71–82)
- **After class:** Muñoz-Garcia Ch. 4 Ex. 1 (p. 154), Ex. 16–18 (pp. 198–200); Ch. 6 Ex. 8 (p. 303) · MWG 9.B.12, 9.B.13 (pp. 302–303)
- **Formal side:** MWG 9.AA (p. 296)
- **Applications and project material:** M&R bargaining over a sale (p. 140) · `Aula/aula-02-notes.md` §5 (Nash bargaining, Rubinstein) · `Listas/lista-aulas-01-02.tex` block 3 · [[rules/02_barganha|Topic 2]]

### Lecture 5 — Repeated games I: cooperation
#lecture/5
- **Before class:** Tadelis §10.1–10.3 (pp. 190–201), folk theorem §10.6 (p. 209) · Gibbons §2.3.A–B (pp. 82–102)
- **After class:** Muñoz-Garcia Ch. 6 Ex. 1 (p. 274) · Tadelis Ch. 10 exercises
- **Formal side:** MWG §12.D (p. 400), App. 12.A "Infinitely Repeated Games and the Folk Theorem" (p. 417)
- **Applications:** Cabral §7.3 (p. 172)

### Lecture 6 — Repeated games II: collusion and relational contracts
#lecture/6
- **Before class:** Tadelis §10.4 tacit collusion (p. 201), §10.5 reputation (pp. 204–209) · Gibbons §2.3.C Cournot collusion (p. 102), §2.3.D efficiency wages (p. 107) · M&R Ch. 8 "Reputations as contract enforcers" (p. 259), the repeated trust game (pp. 261–263), "live and let live" (p. 264), limits of reputation (p. 265)
- **After class:** Muñoz-Garcia Ch. 6 Ex. 2–5 (pp. 278–290), Ex. 10 (p. 310); Ch. 5 Ex. 4–5, 8 (pp. 228–239) · M&R Quantitative Exercise 4 (p. 286)
- **Formal side:** MWG §12.D (p. 400)
- **Applications:** Cabral Ch. 9 (from p. 217: stability of collusive agreements p. 218, price wars p. 222) · M&R efficiency wages (p. 250)

## Games of incomplete information

### Lecture 7 — Bayesian games, adverse selection and auctions
#lecture/7
- **Before class:** Tadelis Ch. 12 (pp. 241–269; adverse selection §12.3 p. 258), Ch. 13 (pp. 270–287) · Gibbons Ch. 3 (pp. 143–172; auctions §3.2.B p. 155, double auction §3.2.C p. 158)
- **After class:** Muñoz-Garcia Ch. 7 (pp. 317–347), Ch. 8 (pp. 349–373) · MWG 13.B.1, 13.B.2
- **Formal side:** MWG §8.E (p. 253), §13.B (pp. 437–449)
- **Applications:** M&R adverse selection (p. 149) · Cabral §7.4 (p. 174), §6.4 auctions and negotiations (p. 140) · [[rules/07_selecao_adversa|Topic 7]]

### Lecture 8 — Signaling and perfect Bayesian equilibrium
#lecture/8
- **Before class:** Tadelis Ch. 15 (pp. 303–317), Ch. 16 (pp. 318–338) · Gibbons §4.1 (p. 175), §4.2 (pp. 183–210; job-market signaling p. 190)
- **After class:** Muñoz-Garcia Ch. 9 (pp. 375–451), Ch. 11 (pp. 481–520) · MWG 13.C.1, 13.C.5, then 13.C.2, 13.C.4
- **Formal side:** MWG §9.C (p. 282), §9.D (p. 292), §13.C (pp. 450–459), 13.AA (p. 467)
- **Applications:** M&R signaling and screening (p. 154) · [[rules/07_selecao_adversa|Topic 7]]

## Paper and exam

### Lecture 9 — Short-paper presentations (Tue Dec 1)
- Group paper: motivation, brief literature review, research question, an economic model (35% in all). Comments on another group's paper count 5%. Partial-submission dates: to be agreed in class (not yet known).

### Lecture 10 — Final exam (Tue Dec 8)
- Individual, 55%. Covers Lectures 1–8. Exam-style practice: `Listas/lista-lecture-01.tex` (more to follow lecture by lecture).

---

## Superseded draft (2026-10-09)

The 16-session plan built from the 2024/34 syllabus record, anchored in Milgrom & Roberts
(1992). Not taught as such; kept because Aulas 1–2 material was produced against it
(`Aula/aula-01-notes.md`, `Aula/aula-02-notes.md`, the six `quiz-aula01-*`/`quiz-aula02-*`
quizzes, `Listas/lista-aulas-01-02.*`, `Listas/pratica-aula-01*.md`). Use it as M&R
background for the applications above.

| Aula | Session | M&R (printed pp.) | Real lecture that now covers it |
|---|---|---|---|
| 1 | Does organization matter? Ford × GM × Toyota | Ch. 1 (2–18); Ch. 4 (106–113) | — (background) |
| 2 | Bargaining I: value maximization and the Coase theorem | Ch. 2 (35–39) | — (background; §5 feeds L4) |
| 3 | Bargaining II: private information, bargaining costs | Ch. 5 (140–149) | L4, L7 |
| 4–5 | Efficiency and economic organization; NEPKE | Ch. 2 (19–48) | — |
| 6–8 | Coordination: market, management, Sears | Ch. 3–4 | — |
| 9 | Bounded rationality, information and contracts | Ch. 5 (126–140) | L6 (relational contracts) |
| 10–12 | Adverse selection, screening, signaling | Ch. 5 (149–162) | L7, L8 |
| 13–14 | Moral hazard; the S&L crisis | Ch. 6 | — |
| 15–16 | Managing moral hazard | Ch. 7 | — |
