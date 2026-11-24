# Plan — "How to write strategies" guide + NotebookLM prompt (2026-11-24)

User has trouble writing strategies. Deliver a PDF guide and a NotebookLM audio prompt, then push.

1. `Notas/strategies-guide/how-to-write-strategies.tex` → PDF (pdflatex, lmodern+cmap, pdffonts check).
   Reuse definitions/pages already in Notas: L03-02 (Def 7.4 p.139, counting, BoS p.138, behavioral
   p.140), L05-03/04 (Def 10.4 p.196, grim trigger p.198, δ*=1/4), L07-01/02 (Def 12.3 p.249, entry
   with crazy type p.243–244), L08-04 (Gibbons signaling pp.183–188).
   Sections: the one rule; 4-step recipe; entry game; follower with many nodes; player moving twice
   (NE vs SPE, off-path part); imperfect info / multistage; mixed vs behavioral; repeated; Bayesian
   + auctions; signaling/PBE; mistakes; templates; original self-check with answers.
   Toy games marked as original illustrations. No book exercise numbers (global rule) — point to
   the existing real list (Lecture 3 block) instead.
2. `NotebookLM/audio/strategies-guide-audio.md` (<5,000 chars, no language line); copy PDF to
   `NotebookLM/sources/`; add README row.
3. Index line in `Notas/00-index.md`. Commit + push to origin master.
