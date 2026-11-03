# Plan: short (<= 3 pages) class version of the Brexit case write-up

Request (2026-11-03): `Cases/Brexit/brexit-game-short.tex/.pdf`, a class handout derived from
`Cases/Brexit/brexit-game.tex` (the full, checked document). The case PDFs are not opened.

1. Same preamble style (lmodern + cmap after fontenc), 10pt, tighter margins.
2. Order (i)-(vii): players; timing/actions; information (baseline + one-line variant);
   18-leaf payoff table + one-line ordering; tree (the full file's `\branch` TikZ, y-scale
   reduced) with SPE edges; 3-step backward induction, SPE profile, expected payoffs;
   one box with comparative statics (r regimes, k <= 5, sigma = 8/13, tau = 11/36,
   UK ~ -26.64); (vii) four bullets + pointer to the full file's template (Sec. 11).
3. No new numbers: every number copied from the full file.
4. Verify: a scratch script extracts numeric tokens of the short file's body and checks each
   occurs in the full file; pdflatex twice, no errors, no overfull > 10pt; pdffonts all Type 1;
   delete aux/log/out. The full document is not edited.
