# Plan: two paper cases (Lectures 3 and 5), Lecture 5 homework, NotebookLM prompts

User request (2026-11-08): "run a analysis based on game theory and write notebooklm based on that
discussion" + "solve the cases of lecture 3 and 5 in detail and the short version". Scope confirmed
by the user: both papers as cases (Görges = Lecture 3, bank robberies = Lecture 5), each detailed +
short; the Lecture 5 tacit-collusion homework (slide 34 of `Aula/Lecture05.pdf`) detailed + short;
NotebookLM prompts on the papers. Lecture 3's "Work or shirk?" mini case is already solved
(`Resolucao/mini-case-lecture-03*.pdf`) and is not redone.

Every number below was computed in a scratch script (Fractions) on 2026-11-08; each case's own
check script must re-assert them.

## A. Görges (2021), "Of housewives and feminists", Labour Economics 72, 102044 — Lecture 3 case

Folder `Cases/Housewive and feminists/`: `housewives-game.tex/.pdf` (detailed),
`housewives-game-short.tex/.pdf` (≤ 3 pp.), `housewives-check.py`.

Game (Table 1, p. 3): players woman/man; actions Career/Family (Norm) or A/B (Neutral); payoffs
(C,F) → 200 to the Career player, 100 to the Family player; (C,C) and (F,F) → 0,0. ECU, 1:1 cents.
Simultaneous, one shot, no communication, choices revealed ex post to the partner.

Results: pure NE (C,F), (F,C); mixed NE Pr(C) = α/(α+β) = 2/3 each; EU = αβ/(α+β) = 200/3 ≈ 66.7;
coordination 4/9 ≈ 44.4% (paper: "just below 45%"); traditional 2/9, progressive 2/9, (C,C) 4/9,
(F,F) 1/9. Total payoff 300 in each pure NE vs 133.3 in the mixed NE.
Indifference: opponent's Pr(C) = q → C pays (1−q)·200, F pays q·100; BR is F iff q > 2/3.
Observed Career rates (Table 4 col. 1, linear prob.): men Neutral 0.536, women Neutral 0.563,
men Norm 0.625, women Norm 0.250. Under independence: Neutral coordination 0.495 (trad 0.234,
prog 0.261); Norm 0.5625 (trad 0.469, prog 0.094); expected Norm earnings men 103.1, women 65.6.
Observed Table C1 means: Norm men 112.50, women 75.00 (ratio 0.667: "women earn 67% of men");
Neutral men 80.36, women 83.04. AMEs (Table 3 col. 2): progressive −0.171, traditional +0.255,
not coordinated −0.085.
Best responses against actual rates in Norm: woman C 75 vs F 62.5 → Career was her BR against the
men's real 62.5%; men's beliefs/women's beliefs overshoot (fn. 27: women's predicted male Career
rates "substantially higher than the true rates"). Man C 150 vs F 25.
Signalling (§5.2): non-committed men with partner in Norm choose C 33% (vs 54% Neutral), with
strangers 78% (vs 48%). With belief Pr(partner C) = 0.33 (men in Norm about partner), C pays 134,
F pays 33 → the signal must be worth > 101 ECU (≈ €1) to justify Family.
Own-payoff puzzle (our analysis, label as such): give women identity utility n for Family; in the
mixed NE the woman's indifference pins the MAN's mix: Pr_m(C) = (200−n)/300, women stay at 2/3.
Data move the opposite way (women 0.563→0.250, men ≈ flat) → evidence for equilibrium selection
(focal point, Schelling) over a payoff change inside the mixed equilibrium.
Fehr–Schmidt (fn. 13): coordination survives iff β_FS < 2 (advantaged) and α_FS < 1
(disadvantaged).
Lecture 3 extensions: sequential BoS (first mover — whoever commits first, e.g. first job offer
or first child — gets 200: SPE); fn. 12 path dependence; repeated alternation gives 150 each per
period (Lecture 5 link) but specialization feedback makes it costly.

## B. Maheshri & Mastrobuoni (2021), "The race between deterrence and displacement", REStat 103(3) 547–562 — Lecture 5 case

Folder `Cases/the race between deterrence and displacement/`: `deterrence-game.tex/.pdf`,
`deterrence-game-short.tex/.pdf`, `deterrence-check.py`.

Model (§II): banks i choose g_i ∈ {0,1}; cost c_i, loss L_i; robbery probability p(g_i, g_−i);
hire iff guard premium Δ(g_−i) = p(0,·) − p(1,·) > θ_i = c_i/L_i (eq. 5). Δ increasing in g_−i
(displacement falls on unguarded banks) → strategic complements → coordination, Props 1–3.
Estimates, baseline 500 m (Table 3 col. 7 = Table 4 col. 1): β1 = −0.0318, β2 = 0.0169,
β3 = −0.0336; base risk 0.07 (Table 1). Linear p(g,x) = 0.07 + β1 g + β2 x + β3 g x, x = share of
neighbours guarded. Δ(0) = 0.0318, Δ(1) = 0.0654; displaced share β2/|β1| = 0.531 ("over half").
Paper's Prop. 3 numbers (p. 557): €1.37M and €662k reproduce with c = 44,000 and Table 4 col. 2
(β1 = −0.0321, β3 = −0.0343): 44,000/0.0321 = 1,370,717; 44,000/0.0664 = 662,651. With the
stated 40,000 and the baseline they would be 1,257,862 and 611,621. Flag the discrepancy.
Table 4 col. 4 (quadratic trends): −0.0342, 0.0190, −0.0245.

Two-bank game, c = 40,000: unique NN if L < 611,621; unique GG if L > 1,257,862; both in between.
Social (banks' losses + guard cost): GG beats NN iff c < 0.0485 L ⇔ L > 824,742. Risk dominance:
GG iff θ < (Δ0+Δ1)/2 = 0.0486 (almost the same cut — because β2 ≈ −β3/2).
L = 1,000,000 (θ = 0.04), costs €k (row, col): NN 70.0/70.0; GN 78.2/86.9; GG 61.5/61.5; mixed
Pr(G) = 0.244. Stag hunt: GG Pareto-better; "too few guards" possible.
L = 700,000 (θ = 0.0571): NN 49.0; GN 66.74/60.83; GG 55.05; mixed Pr(G) = 0.754; GG is the
Pareto-dominated equilibrium: "too many guards" possible. (Prop. 2.)
Four banks, c = 40,000, θ = (0.020, 0.044, 0.050, 0.068), L = (2,000,000; 909,091; 800,000;
588,235); Δ(k/3) = 0.0318, 0.0430, 0.0542, 0.0654. Pure NE: {1} (total 290,154) and {1,2,3}
(271,510); social optimum all four (252,393), not an NE: bank 4 gains 1,529 by firing. Ban → all
zero 300,813; requirement → 252,393. Subsidy: s = 1,529.4 makes bank 4 indifferent; s = 1,600
makes all-four the unique NE (price instrument selects here because θ's sit near thresholds).
Lecture 5: T = 10 (2000–2009) finitely repeated game. Any sequence of stage NE is an SPE.
Carrot and stick, two periods: play all four in t = 1; in t = 2 play {1} if bank 4 complied (its
cost 44,490) and {1,2,3} if it fired (51,118): sustains t = 1 iff δ ≥ 1,529/6,628 = 0.2307.
The carrot for an unguarded bank is FEWER guards around it. Infinite horizon: both stage NE give
bank 4 less cost (44,490; 51,118) than all-four (52,647), so Nash reversion cannot sustain
all-four forever. Policy reading: quantity regulation (requirement) instead of reliance on
repetition. Also Figure 1 example θ = (0.025, 0.035, 0.058, 0.060): NE {1,2} and all four.

## C. Lecture 5 homework: tacit collusion (slide 34)

`Resolucao/homework-lecture-05.tex/.pdf`, `-short.tex/.pdf`, `homework-lecture-05-check.py`.
P = 100 − q1 − q2, C = 10q. (1) Cournot q = 30, π = 900; cartel q = 22.5, π = 1012.5.
(2) Best deviation q = 33.75, π = 1139.0625. (3) Grim trigger, one-stage deviation: on path
π_C/(1−δ) ≥ π_D + δπ_N/(1−δ) ⇔ δ ≥ (π_D−π_C)/(π_D−π_N) = 9/17 ≈ 0.529; off path Nash reversion
is a stage NE. (4) General: π_N = (a−c)²/9b, π_C = (a−c)²/8b, π_D = 9(a−c)²/64b → 9/17.
(5) n firms: δ*(n) = (n+1)²/(n²+6n+1): 9/17, 4/7, 25/41, 9/14 (n = 2..5), 121/161 at n = 10;
plus frequency, observability, demand growth, symmetry, multimarket contact (Tadelis §10.4,
Cabral Ch. 9).

## D. NotebookLM

`NotebookLM/audio/case-lecture-03-housewives-audio.md`, `case-lecture-05-deterrence-audio.md`
(< 5,000 chars, no language line). Sources: copy both papers and `Aula/Lecture05.pdf` into
`NotebookLM/sources/` (`Caso_…`, `Aula_Lecture05 - Repeated Games.pdf`) and the two detailed
case PDFs. README rows. Study-guide rows for Lectures 3 and 5 get one pointer each.

## Checks

pdflatex twice per file, lmodern + cmap, `pdffonts` all Type 1 with uni = yes; short versions
≤ 3 pages; each check script exits 0; prompts measured with `wc -c`.
