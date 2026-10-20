"""Figures for Lecture 4 (multistage games and bargaining). Estimated unit: no slides yet.

Run from anywhere:  python Notas/L04/figures/make_figures.py
Writes L04-*.png beside this file. Book numbers are printed pages:
Tadelis (2013) Ch. 9 pp. 175-189, Ch. 11 pp. 220-237; Gibbons (1992) Sec. 2.1.D pp. 68-71,
Sec. 2.2.C pp. 75-79. Where a book gives no number (the discount factor), the value is the
project's own calibration (Aula/notes-aulas-01-02/check_part2.py uses delta = 0.6) and says so.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from _figstyle import C, apply, save

import numpy as np
import matplotlib.pyplot as plt

# Prisoner-Revenge Game, Tadelis pp. 176-177.
PD = {("M", "m"): (4, 4), ("M", "f"): (-1, 5), ("F", "m"): (5, -1), ("F", "f"): (1, 1)}
REV = {("L", "l"): (0, 0), ("L", "g"): (-4, -1), ("G", "l"): (-1, -4), ("G", "g"): (-3, -3)}
CARROT, STICK = 0, -3                                   # (L,l) and (G,g), Tadelis p. 182


def table(ax, rows, cols, cells, title, colors=None):
    """Draw a bimatrix as a table: cells[r][c] is a string, colors[r][c] an optional facecolor."""
    ax.axis("off")
    t = ax.table(cellText=cells, rowLabels=rows, colLabels=cols, loc="center", cellLoc="center")
    t.scale(1, 2.1)
    t.set_fontsize(11)
    for (r, c), cell in t.get_celld().items():
        cell.set_edgecolor(C["ref"])
        if r >= 1 and c >= 0 and colors and colors[r - 1][c]:
            cell.set_facecolor(colors[r - 1][c])
    ax.set_title(title, fontsize=11)


def prisoner_revenge_reduced(delta=0.5):
    """Stage games and the stage-1 game reduced by the carrot-and-stick continuation (p. 182)."""
    fig, axs = plt.subplots(1, 3, figsize=(11.5, 2.9))
    pd_cells = [[f"{PD[(a, b)][0]}, {PD[(a, b)][1]}" for b in "mf"] for a in "MF"]
    table(axs[0], ["M", "F"], ["m", "f"], pd_cells, "Stage 1: Prisoner's Dilemma",
          [[None, None], [None, "#e3efe8"]])
    rv_cells = [[f"{REV[(a, b)][0]}, {REV[(a, b)][1]}" for b in "lg"] for a in "LG"]
    table(axs[1], ["L", "G"], ["l", "g"], rv_cells, "Stage 2: Revenge Game (two pure NE)",
          [["#e3efe8", None], [None, "#f6e3d6"]])
    red, cells, cols = {}, [], []
    for a in "MF":
        row, crow = [], []
        for b in "mf":
            cont = CARROT if (a, b) == ("M", "m") else STICK
            v = (PD[(a, b)][0] + delta * cont, PD[(a, b)][1] + delta * cont)
            red[(a, b)] = v
            row.append(f"{v[0]:g}, {v[1]:g}")
            crow.append("#e3efe8" if (a, b) == ("M", "m") else None)
        cells.append(row)
        cols.append(crow)
    table(axs[2], ["M", "F"], ["m", "f"], cells,
          f"Stage 1 with continuation, $\\delta={delta}$", cols)
    save(fig, "L04-prisoner-revenge-reduced")
    return red


def carrot_stick_threshold():
    """Stay vs deviate along delta for the two paths of Tadelis pp. 182-184."""
    fig, ax = plt.subplots(figsize=(7.2, 4.0))
    d = np.linspace(0, 1, 301)
    # path (M,m): player 1 compares 4 + 0*delta with 5 - 3*delta
    ax.plot(d, 4 + CARROT * d, color=C["good"], label="(M,m) path: stay, $4+0\\cdot\\delta$")
    ax.plot(d, 5 + STICK * d, color=C["warn"], label="(M,m) path: fink, $5-3\\delta$")
    # path (F,m): player 2 compares -1 + 0*delta with 1 - 3*delta
    ax.plot(d, -1 + CARROT * d, color=C["good"], ls="--", label="(F,m) path: player 2 stays, $-1$")
    ax.plot(d, 1 + STICK * d, color=C["warn"], ls="--", label="(F,m) path: player 2 finks, $1-3\\delta$")
    for ds, y, lab in [(1 / 3, 4, "$\\delta^*=1/3$"), (2 / 3, -1, "$\\delta^*=2/3$")]:
        ax.plot(ds, y, "o", color=C["hi"], ms=8)
        ax.annotate(lab, (ds, y), xytext=(8, 10), textcoords="offset points", color=C["hi"])
    ax.set(xlabel="discount factor $\\delta$", ylabel="discounted payoff $v_i$",
           title="Carrot and stick: deviation gain vs discounted punishment", xlim=(0, 1))
    ax.legend(fontsize=8.5, loc="center right", bbox_to_anchor=(1.0, 0.52))
    save(fig, "L04-carrot-stick-threshold")
    return (5 - 4) / (CARROT - STICK), (1 - (-1)) / (CARROT - STICK)


def tariff_welfare(ti, tj, A=1.0):
    """Gibbons p. 78: W_i*(t_i,t_j) with a - c = A, firms at the stage-2 equilibrium (2.2.3)."""
    return ((2 * A - ti) ** 2 / 18 + (A + ti) ** 2 / 9 + (A - 2 * tj) ** 2 / 9
            + ti * (A - 2 * ti) / 3)


def tariff_dilemma():
    """W_i against t_i for two values of t_j: the peak never moves (dominant t = A/3)."""
    fig, ax = plt.subplots()
    t = np.linspace(0, 0.5, 300)
    for tj, col, lab in [(0, C["main"], "$t_j=0$ (free trade abroad)"),
                         (1 / 3, C["ref"], "$t_j=(a-c)/3$")]:
        ax.plot(t, tariff_welfare(t, tj), color=col, label=lab)
        ax.plot(1 / 3, tariff_welfare(1 / 3, tj), "o", color=C["warn"], ms=7)
    ax.axvline(1 / 3, color=C["warn"], lw=1, ls=":")
    ax.text(0.338, 0.37, "$t_i^*=(a-c)/3$\nwhatever $t_j$", color=C["warn"], fontsize=9.5)
    ax.plot(0, tariff_welfare(0, 0), "s", color=C["good"], ms=7)
    ax.annotate("both free trade: 72/162", (0, tariff_welfare(0, 0)), xytext=(8, 6),
                textcoords="offset points", color=C["good"])
    ax.annotate("both at $t^*$: 65/162", (1 / 3, tariff_welfare(1 / 3, 1 / 3)), xytext=(-130, -18),
                textcoords="offset points", color=C["warn"])
    ax.set(xlabel="own tariff $t_i$ (units of $a-c$)", ylabel="$W_i^*$ (units of $(a-c)^2$)",
           title="Tariffs: a dominant strategy and a Prisoners' Dilemma", xlim=(0, 0.5))
    ax.legend(loc="lower center")
    save(fig, "L04-tariff-dilemma")
    return [round(162 * tariff_welfare(a, b)) for a, b in [(0, 0), (1/3, 0), (0, 1/3), (1/3, 1/3)]]


def finite_share(T, d1, d2):
    """Player 1's period-1 share x_1 in the T-period game, player 1 proposing in odd periods."""
    x = 1.0 if T % 2 else 0.0                         # last proposer takes the pie
    for t in range(T - 1, 0, -1):                     # walk back from period T-1 to 1
        x = 1 - d2 * (1 - x) if t % 2 else d1 * x     # odd t: 1 proposes; even t: 2 proposes
    return x


def finite_horizon_shares():
    """Tadelis (11.1)-(11.2): x_1(T) zig-zags around 1/(1+delta) and converges to it."""
    fig, ax = plt.subplots()
    Ts = np.arange(1, 21)
    for d, col in [(0.6, C["main"]), (0.9, C["hi"])]:
        xs = [finite_share(T, d, d) for T in Ts]
        ax.plot(Ts, xs, "o-", color=col, lw=1.2, ms=5, label=f"$\\delta={d}$")
        ax.axhline(1 / (1 + d), color=col, lw=1, ls="--")
        ax.text(20.3, 1 / (1 + d), f"$1/(1+\\delta)$\n$={1/(1+d):.3f}$", color=col, va="center",
                fontsize=9)
    ax.set(xlabel="horizon $T$ (rounds)", ylabel="player 1's share $v_1$",
           title="Finite horizon: last-mover advantage fades as $T$ grows",
           xlim=(0.5, 23), ylim=(0, 1.05), xticks=[1, 3, 5, 7, 9, 11, 13, 15, 17, 19])
    ax.legend(loc="lower right")
    save(fig, "L04-finite-horizon-shares")
    return [finite_share(T, 0.6, 0.6) for T in (1, 2, 3, 4)]


def shaked_sutton_fixed_point(d=0.6):
    """Gibbons p. 71: f(s) = 1 - delta + delta^2 s; its fixed point is s* = 1/(1+delta)."""
    fig, ax = plt.subplots(figsize=(5.6, 5.0))
    s = np.linspace(0, 1, 100)
    ax.plot(s, s, color=C["ref"], lw=1, label="45-degree line")
    ax.plot(s, 1 - d + d ** 2 * s, color=C["main"], label="$f(s)=1-\\delta+\\delta^2 s$")
    star = 1 / (1 + d)
    ax.plot(star, star, "o", color=C["good"], ms=9)
    ax.annotate(f"$s^*=1/(1+\\delta)={star:.3f}$", (star, star), xytext=(10, -22),
                textcoords="offset points", color=C["good"])
    x = 0.05                                           # iterate f from a low guess (cobweb)
    for _ in range(4):
        y = 1 - d + d ** 2 * x
        ax.plot([x, x, y], [x, y, y], color=C["hi"], lw=1)
        x = y
    ax.set(xlabel="player 1's payoff if period 3 is reached, $s$",
           ylabel="player 1's period-1 payoff, $f(s)$", xlim=(0, 1), ylim=(0, 1),
           title=f"The Shaked-Sutton fixed point ($\\delta={d}$)")
    ax.legend(loc="upper left")
    save(fig, "L04-shaked-sutton-fixed-point")
    return star, 1 - d + d ** 2 * star


def rubinstein_patience():
    """Player 1's infinite-horizon share (1-d2)/(1-d1 d2) against d2, for several d1."""
    fig, ax = plt.subplots()
    d2 = np.linspace(0, 0.995, 300)
    for d1, col in [(0.3, C["ref"]), (0.6, C["main"]), (0.9, C["hi"])]:
        ax.plot(d2, (1 - d2) / (1 - d1 * d2), color=col, label=f"$\\delta_1={d1}$")
    ax.plot(d2, 1 / (1 + d2), color=C["good"], ls="--", lw=1.6,
            label="equal patience $1/(1+\\delta)$")
    ax.axhline(0.5, color=C["ref"], lw=1, ls=":")
    ax.text(0.02, 0.52, "equal split, the $\\delta\\to1$ limit", color=C["ref"], fontsize=9)
    ax.set(xlabel="responder's discount factor $\\delta_2$", ylabel="proposer's share $x^*$",
           title="Rubinstein: patience is bargaining power", xlim=(0, 1), ylim=(0, 1.02))
    ax.legend(loc="lower left")
    save(fig, "L04-rubinstein-patience")
    return (1 - 0.7) / (1 - 0.9 * 0.7)


def legislative_shares():
    """Tadelis (11.8) N=3, (11.9) and (11.13): what the proposer expects, against delta."""
    fig, ax = plt.subplots()
    d = np.linspace(0, 1, 300)
    ax.plot(d, 1 - d / 3, color=C["main"], label="closed rule, $N=3$: $k=1-\\delta/3$  (11.8)")
    ax.plot(d, 1 / (1 + 2 * d), color=C["warn"], label="open rule, guaranteed: $1/(1+2\\delta)$  (11.9)")
    ax.plot(d, 2 / (4 + 2 * d - d ** 2), color=C["hi"],
            label="open rule, risky: $2/(4+2\\delta-\\delta^2)$  (11.13)")
    ds = np.sqrt(3) - 1
    ax.plot(ds, 1 / (1 + 2 * ds), "o", color=C["good"], ms=8)
    ax.annotate(f"$\\delta=\\sqrt{{3}}-1\\approx{ds:.3f}$", (ds, 1 / (1 + 2 * ds)), xytext=(-40, -34),
                textcoords="offset points", color=C["good"])
    ax.set(xlabel="discount factor $\\delta$", ylabel="proposer's expected payoff",
           title="Legislative bargaining (Baron-Ferejohn), three legislators",
           xlim=(0, 1), ylim=(0, 1.02))
    ax.legend(fontsize=8.8, loc="lower left")
    save(fig, "L04-legislative-shares")
    return ds, 1 / (1 + 2 * ds), 2 / (4 + 2 * ds - ds ** 2)


if __name__ == "__main__":
    apply()
    red = prisoner_revenge_reduced()
    assert red[("M", "m")] == (4, 4) and red[("F", "m")] == (3.5, -2.5)   # 5 - 3(0.5), -1 - 1.5
    lo, hi = carrot_stick_threshold()
    assert abs(lo - 1 / 3) < 1e-12 and abs(hi - 2 / 3) < 1e-12               # Tadelis pp. 183-184
    assert tariff_dilemma() == [72, 81, 56, 65]                              # free trade 4/9 > 65/162
    assert np.allclose(finite_horizon_shares(), [1, 0.4, 0.76, 0.544])      # (11.1), delta = 0.6
    s_star, f_star = shaked_sutton_fixed_point()
    assert abs(s_star - 0.625) < 1e-12 and abs(f_star - s_star) < 1e-12
    assert abs(rubinstein_patience() - 0.3 / 0.37) < 1e-12
    ds, g, r = legislative_shares()
    assert abs(g - r) < 1e-12                                                # the two open-rule payoffs cross
    for T in range(1, 12):                                                   # (11.1) closed form
        assert abs(finite_share(T, 0.6, 0.6) - (1 - (-0.6) ** T) / 1.6) < 1e-12
    print("L04 figures written; all checks pass")
