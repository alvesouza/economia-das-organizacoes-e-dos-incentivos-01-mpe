# Topic 1 - Does Organization Matter?

> **Lecture** - Aula 1 (planned, [[Map/study-guide|class plan]]; notes `Aula/aula-01-notes.md`) · syllabus item: *Aplicação: As organizações importam? Ford x GM x Toyota*
> **Main book** - Milgrom & Roberts (1992), Ch. 1 "Does Organization Matter?" (pp. 2–18; Patterns of Organizational Success and Failure, pp. 16–17) · Ch. 4 "Complementarities and Design Decisions" (p. 108) and "Complementarities, Innovation Attributes, and Coordination Failure" (pp. 111–113; Figure 4.3)
> **Other refs** - Cabral (2017), §3.5 "Why are firms different?" (pp. 56–59; Toyota's procurement system p. 57)

---

## Organizations as coordination and motivation problems
Every organization must **coordinate** (make plans fit: information) and **motivate** (get them carried out: interests). M&R: organization is "not about how berries are arranged on a tree of authority but about how people are coordinated and motivated to get things done" (p. 16). The four patterns (pp. 16–17): organization and strategy matter as much as technology, cost and demand; incentives; authority placed with information; **incentives and delegated authority are complements** (p. 17). Full notes: `Aula/aula-01-notes.md` §5.

## Organizational design choices
Choices: product strategy, equipment, inventories, supplier relations (make or buy, long-term vs. price competition), decision rights (centre vs. units), pay. GM's multidivisional form (pp. 3–4): divisions keep operating autonomy, the centre audits, plans strategy and checks internal prices against the market. Cases: HBC vs. NWC (decision rights + profit shares, pp. 6–9), Salomon (individual bonuses discourage cooperation, pp. 9–12), central planning and the ratchet effect (p. 14). Notes §2, §4.

## Complementarities among design choices
Definition (M&R p. 108): activities are complements if doing more of one raises the marginal profitability of the others; smooth form $\partial^2\pi/\partial x_i\partial x_j \ge 0$ (n. 8); discrete form: increasing differences ⇔ supermodularity. Consequences, with signs: complements move together ($x^{*\prime}(t) = -f_{xt}/f_{xx} \ge 0$; Topkis); two-choice multiplier $\partial x^*/\partial t = (1/c)\cdot 1/(1-(b/c)^2) \ge 1/c$ for either sign of $b$, while $\partial y^*/\partial t$ has the sign of $b$; several **coherent** systems can coexist and only one is best (Fig. 4.3, pp. 111–113); local adjustment cannot find the jump, so strategy is a central decision (p. 115). The valley: a supermodular payoff can make every one-at-a-time path lose money. Notes §6–§8; companions in `Aula/aula-01-companions/`.

**Armadilhas frequentes:** additive "best practices"; complements ≠ "each is good alone"; coherent ≠ optimal; using the cross-price definition for internal choices; footnote 9's "three peaks" (the middle crossing of smooth curves is a saddle). Notes §9.

## Application: Ford x GM x Toyota
Ford: one model, dedicated equipment, disciplined labour paid by job, >50% share — "equally coherent" for its time (p. 109); 55% share in 1921 (p. 2). GM: Sloan's segmented ladder needed variety *and* coordination → multidivisional form; 1927–37 Ford lost $\$200$m, GM earned $>\$2$bn; 1940 shares 45% vs. 16% (pp. 2–4). Toyota: just-in-time without buffers ⇒ reliability, operators repair machines, flexible equipment, frequent redesign, few long-term outside suppliers (pp. 4–6, 17). NUMMI (outside M&R, sourced in the video's `provenance.md`): same Fremont workers, Toyota's system, 19 vs. 31 hours per car (1987, *to confirm*). Notes §1–§3, §8.2.

## Code patterns
Reference implementations and checks: `Aula/aula-01-companions/model_two_systems.py`, `check_companions.py`; the video's `Videos/aula-01-does-organization-matter/check_numbers.py`.
