"""Figures for Lecture 1 (static games I: dominance and iterated elimination).

Run from anywhere:  python Notas/L01/figures/make_figures.py
Writes L01-*.png beside this file and ends with assert checks on the plotted numbers.
Sources: Aula/Lecture01.pdf (slides 10-12, 24, 27, 32-33); Tadelis (2013), printed pages
(PDF 1-based = printed + 19): PD p. 48/52, matrix (4.1) p. 64, Cournot p. 65-67, Pareto p. 57.
The IESDS, Cournot-interval and location routines are the ones already checked in
Listas/lista-lecture-01-check.py, loaded here without running that file's checks.
"""
import ast
import itertools
import pathlib
import random
import sys
from fractions import Fraction
from functools import lru_cache

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from _figstyle import C, apply, save  # noqa: E402

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import Rectangle  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[3]


def lista_functions():
    """Return the function definitions of Listas/lista-lecture-01-check.py as a namespace.

    Only the ``def`` statements are executed, so the file's module-level checks (and its
    sympy import) do not run. Used for iesds2, iesds_rounds_detail, cournot_iesds, line_game.
    """
    path = ROOT / "Listas" / "lista-lecture-01-check.py"
    tree = ast.parse(path.read_text(encoding="utf-8"))
    defs = [n for n in tree.body if isinstance(n, ast.FunctionDef)]
    ns = {"Fr": Fraction, "itertools": itertools, "lru_cache": lru_cache, "random": random}
    exec(compile(ast.Module(body=defs, type_ignores=[]), str(path), "exec"), ns)
    return ns


L = lista_functions()


def draw_matrix(ax, rows, cols, cells, title=None, face=None, dead_rows=(), dead_cols=(),
                ring=None, rowlab="Player 1", collab="Player 2"):
    """Draw a bimatrix as a table: cells[r][c] is the text; face[r][c] an optional fill.

    dead_rows/dead_cols are greyed and struck through (eliminated); ring=(r, c) outlines a cell.
    """
    nr, nc = len(rows), len(cols)
    ax.set_xlim(-1.1, nc)
    ax.set_ylim(-0.35, nr + 0.9)
    ax.axis("off")
    for r in range(nr):
        for c in range(nc):
            y = nr - 1 - r
            dead = r in dead_rows or c in dead_cols
            fc = (face[r][c] if face and face[r][c] else "white")
            ax.add_patch(Rectangle((c, y), 1, 1, fc=fc, ec=C["ref"], lw=1))
            ax.text(c + 0.5, y + 0.5, cells[r][c], ha="center", va="center", fontsize=11,
                    color=C["ref"] if dead else C["ink"], alpha=0.55 if dead else 1)
    for r in range(nr):
        y = nr - 1 - r + 0.5
        ax.text(-0.12, y, rows[r], ha="right", va="center", fontsize=11, fontweight="semibold",
                color=C["warn"] if r in dead_rows else C["ink"])
        if r in dead_rows:
            ax.plot([0.03, nc - 0.03], [y, y], color=C["warn"], lw=1.6)
    for c in range(nc):
        ax.text(c + 0.5, nr + 0.12, cols[c], ha="center", va="bottom", fontsize=11, fontweight="semibold",
                color=C["warn"] if c in dead_cols else C["ink"])
        if c in dead_cols:
            ax.plot([c + 0.5, c + 0.5], [0.03, nr - 0.03], color=C["warn"], lw=1.6)
    ax.text(nc / 2, nr + 0.62, collab, ha="center", va="bottom", fontsize=9.5, color=C["ref"])
    ax.text(-1.05, nr / 2, rowlab, ha="left", va="center", rotation=90, fontsize=9.5, color=C["ref"])
    if ring:
        r, c = ring
        ax.add_patch(Rectangle((c, nr - 1 - r), 1, 1, fill=False, ec=C["good"], lw=3))
    if title:
        ax.set_title(title, pad=4)


# ---------------------------------------------------------------- 1. grade game
GRADE_OUT = [["B-, B-", "A, C"], ["C, A", "B+, B+"]]          # slide 11
GRADE_PAY = [[(0, 0), (3, -1)], [(-1, 3), (1, 1)]]             # slide 12


def grade_game():
    """Slides 11-12: the outcome matrix, then one payoff matrix; alpha strictly dominant."""
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(9.6, 3.4))
    draw_matrix(a1, ["α", "β"], ["α", "β"], GRADE_OUT, "Outcome matrix (grades)", rowlab="You", collab="Pair")
    lt = {"good": "#dcebe2", "hi": "#ece3f5"}
    face = [[lt["good"], None], [None, lt["hi"]]]
    cells = [[f"{a}, {b}" for a, b in row] for row in GRADE_PAY]
    draw_matrix(a2, ["α", "β"], ["α", "β"], cells, "One payoff matrix: α strictly dominant",
                face=face, ring=(0, 0), rowlab="You", collab="Pair")
    a2.text(1.0, -0.28, "green: (α, α), the dominant-strategy equilibrium   purple: (β, β), better for both",
            ha="center", va="center", fontsize=8.5, color=C["ref"])
    save(fig, "L01-grade-game")
    # alpha beats beta against each pair choice: 0 > -1 and 3 > 1
    return [GRADE_PAY[0][c][0] - GRADE_PAY[1][c][0] for c in range(2)]


# ---------------------------------------------------------------- 2. PD in payoff space
PD = {("M", "M"): (-2, -2), ("M", "F"): (-5, -1), ("F", "M"): (-1, -5), ("F", "F"): (-4, -4)}  # Tadelis p. 48


def pareto_optimal(pay):
    """Profiles not Pareto dominated by any other (Tadelis Def. 3.5, p. 57)."""
    def dom(u, v):
        return all(a >= b for a, b in zip(u, v)) and any(a > b for a, b in zip(u, v))
    return {s for s, u in pay.items() if not any(dom(v, u) for t, v in pay.items() if t != s)}


def pd_pareto():
    fig, ax = plt.subplots(figsize=(6.0, 4.6))
    po = pareto_optimal(PD)
    ax.add_patch(Rectangle((-4, -4), 3.6, 3.6, fc=C["good"], alpha=0.07, ec="none"))
    ax.text(-0.5, -0.55, "profiles that Pareto\ndominate (F, F)", ha="right", va="top",
            fontsize=8.5, color=C["good"])
    for s, (u1, u2) in PD.items():
        col = C["warn"] if s == ("F", "F") else (C["main"] if s in po else C["ref"])
        ax.plot(u1, u2, "o", ms=10, color=col)
        lab = f"({s[0]}, {s[1]})  ({u1}, {u2})"
        off = {("M", "M"): (8, 6), ("M", "F"): (8, -4), ("F", "M"): (-2, 10), ("F", "F"): (8, -14)}[s]
        ax.annotate(lab, (u1, u2), xytext=off, textcoords="offset points", color=col, fontsize=10)
    ax.annotate("", (-2, -2), (-4, -4), arrowprops=dict(arrowstyle="->", color=C["good"], lw=1.8))
    ax.plot([-5, -2, -1], [-1, -2, -5], color=C["main"], lw=1, ls="--")
    ax.text(-5.3, -0.45, "Pareto-optimal set (blue, dashed)", color=C["main"], fontsize=9)
    ax.set(xlim=(-5.6, 0), ylim=(-5.6, 0), xlabel="$v_1$ (player 1)", ylabel="$v_2$ (player 2)",
           title="Prisoner's dilemma: the equilibrium (F, F) is Pareto dominated")
    ax.set_aspect("equal")
    save(fig, "L01-pd-pareto")
    return po


# ---------------------------------------------------------------- 3. partnership bands
Y_DEF, C_DEF = 6.0, 4.0   # with n = 2 this is Tadelis's PD (p. 48) plus 4 on every payoff


def partnership_bands():
    """u(E) - u(S) = y/n - c against c, for y = 6; the dilemma band y/n < c < y."""
    fig, ax = plt.subplots(figsize=(7.4, 4.2))
    c = np.linspace(0, 8, 400)
    for n, col in [(2, C["main"]), (3, C["hi"]), (6, C["ref"])]:
        ax.plot(c, Y_DEF / n - c, color=col, label=f"$n={n}$: $y/n-c$")
        ax.plot(Y_DEF / n, 0, "o", color=col, ms=6)
    ax.plot(c, Y_DEF - c, color=C["good"], ls="--", label="all-E minus all-S per partner: $y-c$")
    ax.axhline(0, color=C["ink"], lw=0.8)
    ax.axvspan(Y_DEF / 2, Y_DEF, color=C["warn"], alpha=0.10)
    ax.text((Y_DEF / 2 + Y_DEF) / 2, -5.3, "social dilemma\n($n=2$): $y/2<c<y$", ha="center", color=C["warn"], fontsize=9.5)
    ax.text(1.3, -5.2, "E strictly dominant\n($c<y/n$)", ha="center", color=C["main"], fontsize=9)
    ax.text(7.25, 0.9, "S dominant and\nall-S efficient ($c>y$)", ha="center", color=C["ref"], fontsize=9)
    ax.plot(C_DEF, Y_DEF / 2 - C_DEF, "s", color=C["warn"], ms=8)
    ax.annotate("default $y=6,\\ c=4,\\ n=2$:\nthe slides' PD + 4", (C_DEF, Y_DEF / 2 - C_DEF),
                xytext=(14, -26), textcoords="offset points", color=C["warn"], fontsize=9)
    ax.set(xlim=(0, 8), ylim=(-6, 6), xlabel="effort cost $c$", ylabel="payoff difference",
           title="Partnership ($y=6$): when effort is dominant, and when shirking is a dilemma")
    ax.legend(loc="upper right", fontsize=8.5)
    save(fig, "L01-partnership-bands")
    return Y_DEF / 2 - C_DEF, Y_DEF - C_DEF


# ---------------------------------------------------------------- 4. second-price auction
def spa_payoff(b, v, m):
    """Payoff of a bidder with value v bidding b when the highest rival bid is m (ties: m = b split)."""
    return np.where(b > m, v - m, np.where(b == m, (v - m) / 2, 0.0))


def spa_weak():
    """Slide 4's second-price auction: bidding v weakly (not strictly) dominates any other bid."""
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(10.2, 3.8), sharey=True)
    v = 1.0
    m = np.linspace(0, 2, 801)
    truth = spa_payoff(v, v, m)
    for ax, b, name in [(a1, 0.6, "underbid $b=0.6v$"), (a2, 1.4, "overbid $b=1.4v$")]:
        alt = spa_payoff(b, v, m)
        ax.plot(m, truth, color=C["good"], lw=2.6, label="bid $v$ (truthful)")
        ax.plot(m, alt, color=C["warn"], lw=1.8, ls="--", label=name)
        lo, hi = sorted([b, v])
        ax.axvspan(lo, hi, color=C["warn"], alpha=0.10)
        ax.text((lo + hi) / 2, 0.72, "strictly\nworse here", ha="center", color=C["warn"], fontsize=9)
        ax.text(0.05 if b > v else 1.55, -0.55, "equal\nelsewhere", color=C["ref"], fontsize=9)
        ax.axhline(0, color=C["ink"], lw=0.8)
        ax.set(xlabel="highest rival bid $m$ (in units of $v$)", xlim=(0, 2), ylim=(-1.1, 1.1),
               title=name)
        ax.legend(loc="lower left" if b < v else "lower left", fontsize=8.5)
    a1.set_ylabel("payoff (in units of $v$)")
    save(fig, "L01-spa-weak-dominance")
    gap_under = (spa_payoff(v, v, 0.8) - spa_payoff(0.6, v, 0.8)).item()
    gap_over = (spa_payoff(v, v, 1.2) - spa_payoff(1.4, v, 1.2)).item()
    return gap_under, gap_over


# ---------------------------------------------------------------- 5. the 3x3 IESDS game
U1 = [[4, 5, 6], [2, 8, 3], [3, 9, 2]]   # Tadelis (4.1), p. 64 = slide 27
U2 = [[3, 1, 2], [1, 4, 6], [0, 6, 8]]


def iesds_3x3():
    R, Cc, rounds = L["iesds_rounds_detail"](U1, U2)
    cells = [[f"{U1[r][c]}, {U2[r][c]}" for c in range(3)] for r in range(3)]
    fig, axes = plt.subplots(1, 4, figsize=(13.2, 3.3))
    dr, dc = set(), set()
    titles = ["Round 0: the game", "Round 1: C ≺ R (player 2)",
              "Round 2: M, D ≺ U (player 1)", "Round 3: R ≺ L (player 2)"]
    for k, ax in enumerate(axes):
        if k:
            rr, cc = rounds[k - 1]
            dr |= set(rr)
            dc |= set(cc)
        ring = (R[0], Cc[0]) if k == 3 else None
        draw_matrix(ax, ["U", "M", "D"], ["L", "C", "R"], cells, titles[k],
                    dead_rows=dr, dead_cols=dc, ring=ring)
    save(fig, "L01-iesds-3x3")
    return R, Cc, rounds


# ---------------------------------------------------------------- 6. Cournot by IESDS
A, B, CC = 100, 1, 10    # Tadelis Sec. 4.2.2, p. 65: p = 100 - q, c_i(q_i) = 10 q_i


def cournot_iesds_fig():
    hist = L["cournot_iesds"](Fraction(A), Fraction(B), Fraction(CC), Fraction(CC), 8)
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(10.6, 4.4))
    q = np.linspace(0, 90, 200)
    br = np.maximum(0, (A - CC - B * q) / (2 * B))           # (4.2): q1 = (90 - q2)/2
    a1.plot(br, q, color=C["main"], label="$q_1=(90-q_2)/2$")
    a1.plot(q, br, color=C["hi"], label="$q_2=(90-q_1)/2$")
    for k, (lo, hi) in enumerate(hist[:6], start=1):
        l, h = float(lo[0]), float(hi[0])
        a1.add_patch(Rectangle((l, l), h - l, h - l, fill=False, ec=C["warn"], lw=1.2,
                               alpha=1 - 0.12 * k))
    a1.plot(30, 30, "o", color=C["good"], ms=8)
    a1.annotate("(30, 30)", (30, 30), xytext=(10, 8), textcoords="offset points", color=C["good"])
    a1.set(xlim=(0, 50), ylim=(0, 50), xlabel="$q_1$", ylabel="$q_2$", aspect="equal",
           title="Surviving sets $S_1^k\\times S_2^k$, rounds 1-6")
    a1.legend(loc="upper right", fontsize=8.5)
    ks = np.arange(1, 9)
    lows = [float(h[0][0]) for h in hist]
    highs = [float(h[1][0]) for h in hist]
    a2.vlines(ks, lows, highs, color=C["warn"], lw=6, alpha=0.65)
    a2.axhline(30, color=C["good"], ls="--", lw=1.2)
    for k, (l, h) in zip(ks[:4], zip(lows, highs)):
        a2.text(k + 0.15, h, f"{h:g}", va="center", fontsize=8.5, color=C["ink"])
        a2.text(k + 0.15, l, f"{l:g}", va="center", fontsize=8.5, color=C["ink"])
    a2.text(8.4, 30.6, "$q^*=30$", color=C["good"], ha="right")
    a2.set(xlabel="round $k$", ylabel="surviving interval for each firm", ylim=(-2, 48),
           xticks=ks, title="Each round halves the width and alternates the end that moves")
    save(fig, "L01-cournot-iesds")
    return hist


# ---------------------------------------------------------------- 7. pharmacy avenue
N_BLOCKS = 7   # slide 32


def pharmacy():
    U1p, U2p = L["line_game"](N_BLOCKS, [1] * N_BLOCKS)
    R, Cc, rounds = L["iesds_rounds_detail"](U1p, U2p)
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11.2, 4.3), gridspec_kw={"width_ratios": [1.05, 1]})
    M = np.array([[float(x) for x in row] for row in U1p])
    a1.imshow(M, cmap="Blues", vmin=0, vmax=7, origin="upper")
    for i in range(N_BLOCKS):
        for j in range(N_BLOCKS):
            a1.text(j, i, f"{M[i, j]:g}", ha="center", va="center", fontsize=9,
                    color="white" if M[i, j] > 4.6 else C["ink"])
    a1.set(xticks=range(7), yticks=range(7), xticklabels=range(1, 8), yticklabels=range(1, 8),
           xlabel="$s_B$ (chain B's block)", ylabel="$s_A$ (chain A's block)",
           title="$u_A(s_A,s_B)$: customers of chain A")
    a1.grid(False)
    a1.add_patch(Rectangle((-0.5, -0.5), 7, 1, fill=False, ec=C["warn"], lw=2))
    a1.add_patch(Rectangle((-0.5, 0.5), 7, 1, fill=False, ec=C["good"], lw=2))
    a2.set(xlim=(0.4, 7.6), ylim=(-0.6, 3.6), xlabel="block", title="IESDS on the avenue (same for A and B)")
    a2.set_yticks(range(4))
    a2.set_yticklabels([f"$S^{k}$" for k in range(4)])
    a2.invert_yaxis()
    a2.grid(False)
    alive = set(range(7))
    for k in range(4):
        if k:
            alive -= set(rounds[k - 1][0])
        for b in range(7):
            col = C["good"] if (b in alive and k == 3) else (C["main"] if b in alive else "#e8ecef")
            a2.add_patch(Rectangle((b + 0.55, k - 0.35), 0.9, 0.7, fc=col, ec="white"))
            if k and b in rounds[k - 1][0]:
                a2.text(b + 1, k, "×", ha="center", va="center", color=C["warn"], fontsize=15)
    a2.text(4, 3.5, "only block 4 survives: (4, 4)", ha="center", color=C["good"], fontsize=9.5)
    save(fig, "L01-pharmacy-iesds")
    return M, R, Cc, rounds


if __name__ == "__main__":
    apply()
    assert grade_game() == [1, 2]                                   # 0 - (-1), 3 - 1
    assert pd_pareto() == {("M", "M"), ("M", "F"), ("F", "M")}      # Tadelis p. 57
    assert partnership_bands() == (-1.0, 2.0)                      # y/2 - c < 0 < y - c: dilemma
    gu, go = spa_weak()
    assert abs(gu - 0.2) < 1e-12 and abs(go - 0.2) < 1e-12        # v - m = 0.2 lost in the gap
    R, Cc, rounds = iesds_3x3()
    assert (R, Cc) == ([0], [0]) and rounds == [([], [1]), ([1, 2], []), ([], [2])]  # (U, L), p. 65
    hist = cournot_iesds_fig()
    assert [tuple(map(float, (h[0][0], h[1][0]))) for h in hist[:3]] == [(0, 45), (22.5, 45), (22.5, 33.75)]
    assert abs(float(hist[-1][0][0]) - 30) < 0.2 and abs(float(hist[-1][1][0]) - 30) < 0.25
    M, R, Cc, rounds = pharmacy()
    assert R == Cc == [3] and [r[0] for r in rounds] == [[0, 6], [1, 5], [2, 4]]
    assert M[0, 0] == 3.5 and M[1, 0] == 6 and all(M[1] > M[0])     # block 2 strictly beats block 1
    for p in ["grade-game", "pd-pareto", "partnership-bands", "spa-weak-dominance",
              "iesds-3x3", "cournot-iesds", "pharmacy-iesds"]:
        assert (pathlib.Path(__file__).parent / f"L01-{p}.png").exists(), p
    print("7 figures written; all figure checks pass")
