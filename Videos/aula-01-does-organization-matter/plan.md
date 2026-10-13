---
tags: [video, aula-01, explainer, plan]
date: 2026-10-09
slug: aula-01-does-organization-matter
---

# Plan — Aula 1: Does Organization Matter? Ford × GM × Toyota

**Scoping answers (2026-10-09).** Purpose *first exposure*; length **~50 min** (a whole
class); math **textbook derivation**, every line on screen; examples *Ford × GM × Toyota
history + NUMMI + a stylized payoff table + the course's exercises (number and page only)*.
Narration **English** per the global rule.

**Allocation, stated rather than asked.** 50 minutes is past the skill's 15–25 min ceiling, so
the beat count scales with it: **25 beats, 7,853 words, 3,140 s budgeted at 150 wpm**. `george`
speaks at ~197 wpm (measured in the Macro videos), so the projection is **~43 min** (40 min of
speech + 71 scripted pauses at 2.5 s). Closing the rest of the gap to 50 is a voice choice, decided
on measured audio (see Build order). Eleven of the 25 beats are textbook derivations.

**Sources.** *Update 2026-10-09 evening:* Milgrom & Roberts (1992) arrived and is now cited in
eight beats (ch. 1, pp. 2–5, 17; ch. 4, nn. 8–9); see `provenance.md` rows 19–22. Originally it was **not in `Livros/`**: the course framing comes from the
syllabus and `rules/01`, and the mathematics from Milgrom & Roberts' own research on this exact
case — *"The Economics of Modern Manufacturing: Technology, Strategy, and Organization"*,
AER 80(3), 1990, pp. 511–528. Local anchor: Cabral (2017) §3.5 (pp. 56–59; Toyota procurement,
p. 57). Every historical number is listed with its source in `provenance.md`; two are marked
*to confirm* (the 1987 plant table is from a secondary reproduction of Womack, Jones & Roos 1990).

---

## Thesis

> **A firm's performance comes from a coherent system of complementary choices, not from any
> single practice. That is why the same workers in the same plant could be GM's worst and
> Toyota's best — and why GM could watch the better system every day and still not copy it.**

Two pieces of mathematics carry it: **increasing differences** (why the choices move together)
and **the valley** (why the road from one coherent system to another runs downhill first).

## The cold open, with its clock (0:00–1:30)

Fremont, California. One building, one workforce, one union, two outcomes.

| | |
|---|---|
| 1982 | GM closes Fremont Assembly, one of its worst plants |
| 1984 | It reopens as NUMMI, a GM–Toyota joint venture; **over 85%** of the first workforce are the laid-off GM workers |
| 1987 | Assembly hours per car: **19** at NUMMI against **31** at a comparable GM plant; defects per 100 cars: **45** against **135** |

*"Same building. Same people. Same union. Within three years, these workers were building cars
as fast and as well as Toyota's best plant in Japan. Nothing about them had changed. Something
else had. And General Motors owned half of this plant — its managers could walk the floor every
day — and still could not make it happen anywhere else. By the end of this class you will be
able to write down, in two lines of mathematics, why."*

No definition in the first ninety seconds. The hook is a puzzle the viewer cannot yet resolve:
**if you can see it, why can't you copy it?**

## Colour mapping (fixed for the whole video)

| Colour | Role |
|---|---|
| `BLUE` | the object being studied: cost curves, the profit function, payoffs |
| `YELLOW` | the live derivation line; the object of attention |
| `GREY` | muted: lines already past; background |
| `RED` | what breaks: the wrong first attempt, the valley, piecemeal adoption |
| `GREEN` | the result that survives; the coherent jump |

Firms are told apart by **labels, never colours**: a colour that means "Ford" and also "breaks"
would mean nothing.

## Beat sheet — 25 beats

`D` marks a textbook derivation (one line per step, live line yellow, earlier lines grey).

### Act 0 — the puzzle

| Beat | On screen | Narration's job | s |
|---|---|---|---|
| `BeatOpen` | the three-row Fremont table, one row at a time; then the hours and defects cells lit | pose "if you can see it, why can't you copy it?"; promise the two-line answer | 95 |

### Act I — Ford: the system that made the car cheap

| Beat | On screen | Narration's job | s | Anchor |
|---|---|---|---|---|
| `BeatFordFacts` | a real table: Model T price 1908 → mid-1920s; chassis assembly time before/after the moving line | the line cut labour per chassis ~8×; price fell to under a third. Concrete before abstract | 120 | provenance 1–2 |
| `BeatScale` **D** | two average-cost curves, then the threshold derivation | stationary vs. line: $AC = F/q + c$; the line wins iff $q > \bar q = \Delta F/\Delta c$. Mass production pays only at enormous volume — which needs one cheap, standard car, which needs mass production: a loop | 150 | illustrative $F$ |
| `BeatFiveDollar` **D** | 1913 turnover 370% → the $5 day → cost per unit of *effective* labour $w/e(w)$, minimised | the Solow condition $e'(w)\,w/e(w)=1$, line by line. The line made the work monotonous, which made the high wage pay: the first sighting of complementarity. Incentive pay is developed in Aulas 13–16 | 150 | Raff & Summers 1987 |
| `BeatFordSystem` | a table of Ford's choices, one row per reveal: one model, dedicated machines, moving line, narrow tasks, high wage, making its own parts | each choice raises the value of the others. Then the question: what if buyers wanted something else? | 135 | |

### Act II — GM: the same industry, a different answer

| Beat | On screen | Narration's job | s | Anchor |
|---|---|---|---|---|
| `BeatGMFacts` | timeline: 1919 GMAC credit; the price ladder "a car for every purse and purpose"; annual models; 1927 Ford shut May–Nov to retool | by the 1920s the buyer is replacing a car, not buying a first one, and wants it to be different | 110 | provenance 4–6 |
| `BeatVariety` **D** | $\Pi(n)=q\,(\bar p + a\ln n - c) - nF$, then FOC, SOC, $n^*=aq/F$; the corner $n^*=1$ | one formula for how many models to make; Ford sits at the corner | 160 | stylized |
| `BeatVarietyStatics` **D** | three partial derivatives of $n^*$; the signed table; the three firms placed on it | taste for variety up → GM's ladder; changeover cost down → Toyota. And $\partial^2\Pi/\partial n\,\partial a = q/n>0$: our second complementarity, named later | 140 | |
| `BeatMForm` | Ford's single office vs. GM's divisions with central financial control | many product lines cannot be run from one desk: variety and decentralisation are chosen together. Detail belongs to Aula 7 | 115 | Chandler / Sloan |

### Act III — Toyota: a small market, many models, little capital

| Beat | On screen | Narration's job | s | Anchor |
|---|---|---|---|---|
| `BeatToyota` | the practices, one row each: just-in-time with kanban; quick die changes; any worker can stop the line (andon); multi-skilled teams; few long-term suppliers | each looks irrational to Ford's eyes taken alone: stopping the line? no inventory? | 120 | Cabral §3.5, p. 57 |
| `BeatTwoProblems` | coordination (information) and motivation (interests), each firm's answer to both, one row per reveal | the two words arrive as the end point of three cases, and they organise the course: Aulas 6–8 coordination, 9–16 motivation | 125 | syllabus *ementa* |
| `BeatThreeSystems` | a 3-column table: Ford / GM / Toyota, one row per design dimension | three coherent answers to three environments. If Toyota's is better, why not adopt it one practice at a time? | 100 | |

### Act IV — the mathematics of fit

| Beat | On screen | Narration's job | s |
|---|---|---|---|
| `BeatWrongAttempt` | **wrong first attempt**: $\pi(x)=\pi_0+\sum_i v_i x_i$; adopt practices one by one; then just-in-time alone with unreliable suppliers: the line stops | additivity is the hidden assumption of "best practices", and it is false | 115 |
| `BeatIncreasingDiff` **D** | the 2×2 payoff table $(0,-2,-1,5)$; gain from $x$ when $y=0$ vs. when $y=1$; rearranged three ways | increasing differences ⇔ symmetric ⇔ supermodularity. Each practice alone loses money; together they win. **The definition arrives as the answer** | 150 |
| `BeatCrossPartial` **D** | the double difference quotient, its limit, $\partial^2 f/\partial x\,\partial y \ge 0$; checked on $xy$, $x+y$ and $\Pi(n)$ | the smooth version; the variety model was already supermodular | 140 |
| `BeatSubstitutes` **D** | buffers vs. problem solving; $f_{xy}\le0$; $z=-y$, $g(x,z)=f(x,-z)$, $g_{xz}=-f_{xy}\ge0$ | substitutes are complements with one variable turned upside down: Ford's (buffers, narrow jobs) and Toyota's (no buffers, problem solvers) are both coherent; the mixtures are not | 130 |
| `BeatTopkis` **D** | maximise $f(x,t)$: FOC, total derivative in $t$, $x^{*\prime}=-f_{xt}/f_{xx}\ge0$; then Topkis' theorem stated | when the environment favours one choice, every complement follows. Named result, stated, not proved | 150 |
| `BeatTwoChoices` **D** | $\pi = tx+sy+bxy-\tfrac c2x^2-\tfrac c2y^2$: two FOCs, solved by substitution, the concavity condition $c>b$ | the closed forms $x^*=(ct+bs)/(c^2-b^2)$, $y^*=(cs+bt)/(c^2-b^2)$ | 170 |
| `BeatMultiplier` **D** | $dx^*/dt$, $dy^*/dt$; the ratio $1/(1-(b/c)^2)$ as a geometric series; best-response lines in $(x,y)$ with the staircase | $t$ never enters the $y$ condition, yet $y$ moves; with $c=2,b=1$ the response is 4/3 of the stand-alone one. The ping-pong between two lines **is** the systems effect | 160 |

### Act V — the valley, and NUMMI

| Beat | On screen | Narration's job | s |
|---|---|---|---|
| `BeatEvidence` **D** | $y=\beta_0+\beta_1x+\beta_2z+\beta_3xz+\varepsilon$; effect of $x$ at $z=0,1$; Ichniowski–Shaw–Prennushi | $\beta_3$ is the cross effect. 36 steel lines: the bundle raises productivity, single practices in isolation do not. Correlated adoption alone is not proof | 125 |
| `BeatCube` **D** | the cube $\{0,1\}^3$ (J, T, S) built vertex by vertex with payoffs; one pair checked line by line | supermodular, and still every first step from Ford's corner loses: 6, 8, 9 < 10. Full system: 16 | 170 |
| `BeatValley` **D** | every edge path from 000 to 111 traced; the best one still dips to 9; the stand-alone gain is the minimum gain | complementarity says *where* the optimum is, not that the road is uphill — it *creates* the valley, because a practice is worth least where its complements are missing | 140 |
| `BeatTwoPeaks` **D** | local vs. global optimum; neighbours of 000 (6, 8, 9) and of 111 (9, 10, 8) | two peaks; marginal analysis cannot tell them apart; the package gain (+6) vs. the best step (−1) | 110 |
| `BeatNUMMI` | back to Fremont: the 1987 table (GM plant / NUMMI / Takaoka); the cube with the green jump and GM's red piecemeal paths | Toyota moved the whole system at once; GM's attempts to spread it piece by piece "proved largely unsuccessful" — except in Brazil, through managers trained at NUMMI | 130 |
| `BeatClose` | the closing image | the answer to the opening question; exercises Cabral 1.1 (p. 11) and 3.14 (p. 63); Aula 2 next | 115 |

**Budget: 3,140 s at 150 wpm (7,853 words).**

## The wrong first attempt

| Where | The plausible move | How it fails |
|---|---|---|
| Act IV | "Adopt best practices one at a time": profit is additive, $\pi=\pi_0+\sum v_ix_i$ | additivity has zero cross-effects; the 2×2 table has a cross-effect of +8 |
| Act V | "Climb gradually": adopt the practice with the best stand-alone gain first | from Ford's corner every single step loses money; gradual climbing never starts |

## Stylized numbers (declared illustrative on screen)

| Object | Values | Checks |
|---|---|---|
| 2×2 payoffs $f(x,y)$ | $f(0,0)=0,\ f(1,0)=-2,\ f(0,1)=-1,\ f(1,1)=5$ | $5-(-1)=6 \ge -2-0=-2$; sum test $5+0 \ge -3$ |
| Two-choice model | $c=2,\ b=1,\ s=1$; $t:1\to3$ | $x^*: 1\to7/3$, $y^*: 1\to5/3$; with $b=0$: $x^*: 0.5\to1.5$, $y^*$ fixed at 0.5; multiplier $4/3=1/(1-1/4)$ |
| Cube $\pi(J,T,S)$ | $10-4J-2T-S+4JT+5JS+2TS+2JTS$ → 000:10 · 100:6 · 010:8 · 001:9 · 110:8 · 101:10 · 011:9 · 111:16 | pairwise interactions $4+2S$, $5+2T$, $2+2J$ all $>0$ ⇒ supermodular; best edge path dips to 9 |

`check_numbers.py` recomputes every entry (and the two-peaks, substitutes and elasticity claims)
and aborts on a mismatch: **passes**.

## Scope line

- **Aula 2–3** own bargaining; **Aula 4** owns efficiency and transaction costs; **Aula 7** owns
  hierarchy, decision rights and the design-attributes argument for management over markets —
  the M-form appears here only as GM's fact; **Aulas 13–16** own incentive pay — the $5 day's
  efficiency-wage condition is derived as Ford's history, and handed forward.
- The variety model is a **stylised organisational device**, not Cabral ch. 14's product
  differentiation; no oligopoly, no Hotelling.
- **No exercise statement is animated.** Cited by number and page only: Cabral 1.1 (p. 11),
  3.14 (p. 63), 3.20 (p. 64).
- Topkis' theorem is **stated**, not proved; the lattice-theoretic proof is beyond the course.

## Closing image

**The cube.** Ford's corner at the bottom (10), Toyota's at the top (16), every vertex labelled
with its payoff. GM's piecemeal paths drawn in red along the edges, each one dipping below 10;
NUMMI's single green arrow straight through the middle. One line underneath:
*complements move together — and the road between two good systems runs through a valley.*

Why it is the memorable frame: it answers the opening question in one picture. A student who
can redraw the cube with its numbers can explain NUMMI, the failure of "best practices", and
why organizational change is lumpy.

## The novelty line

Every telling of Ford, GM and Toyota is a story. This one turns the story into two theorems —
increasing differences and the valley — and then checks them against the one natural
experiment the industry ever ran: the same workers, in the same plant, under two systems.

## Build order

1. `script.md` → `check_script.py` (word budget) → `build_beats.py` → `beats.json`.
2. **Stop: show this plan; synthesise only on approval** (TTS is billable; the Macro run ran out
   of credits mid-way).
3. `speechify-tts --check`, then synthesis → `fill_durations.py`.
4. `scenes.py` with the fixed-grid `Stack` carried from the Macro videos; `check_numbers.py`.
5. `layoutcheck`, `beatcheck`, render `-ql`, pull one frame per derivation beat and look at it,
   compile the 480p draft, hand it over, ask before 1080p.
