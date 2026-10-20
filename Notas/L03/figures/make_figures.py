"""Figures for Lecture 3 (dynamic games: backward induction and subgame perfection).

Run from anywhere:  python Notas/L03/figures/make_figures.py
Writes L03-*.png beside this file. Every payoff is the book's own, cited by printed page:
Tadelis (2013) Ch. 7-8 (PDF page = printed + 19), Cabral (2017) Section 7.2.
Game trees follow Tadelis's convention: play flows top to bottom, payoffs are a vertical
list with player 1 on top.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from _figstyle import C, apply, save

from math import log
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle


# ---------------------------------------------------------------- tree drawing ----------
def Dn(who, moves):
    """Decision node labelled `who` with ordered moves [(action, child), ...]."""
    return ("D", who, moves)


def Tn(*payoffs):
    return ("T", payoffs)


def fmt(u):
    return f"{u:g}".replace("-", "−")


def draw_tree(ax, tree, good=(), warn=(), info=(), title=None, leaf_gap=1.0, pay_color=None):
    """Draw `tree` top-down on `ax`.

    good / warn: paths (tuples of actions from the root) whose final edge is drawn in the
    'good' (equilibrium) or 'warn' (eliminated / non-credible) colour.
    info: groups of decision-node paths joined by a dashed line (one information set).
    pay_color: {leaf path: colour} for payoff text.
    Returns {path: (x, y)}.
    """
    pos, leaves = {}, []

    def place(node, path, depth):
        if node[0] == "T":
            x = len(leaves) * leaf_gap
            leaves.append(path)
        else:
            xs = [place(c, path + (a,), depth + 1) for a, c in node[2]]
            x = sum(xs) / len(xs)
        pos[path] = (x, -depth)
        return x

    place(tree, (), 0)

    def draw(node, path):
        x, y = pos[path]
        if node[0] == "T":
            col = (pay_color or {}).get(path, C["ink"])
            ax.text(x, y - 0.1, "\n".join(fmt(u) for u in node[1]), ha="center", va="top",
                    fontsize=10, color=col, linespacing=1.25)
            return
        for a, c in node[2]:
            p = path + (a,)
            x2, y2 = pos[p]
            if p in good:
                col, lw, ls = C["good"], 3.2, "-"
            elif p in warn:
                col, lw, ls = C["warn"], 2.6, "--"
            else:
                col, lw, ls = C["ref"], 1.3, "-"
            ax.plot([x, x2], [y, y2], color=col, lw=lw, ls=ls, zorder=1, solid_capstyle="round")
            side = -1 if x2 < x else 1
            ax.text((x + x2) / 2 + 0.1 * side, (y + y2) / 2 + 0.05, a, ha="left" if side > 0 else "right",
                    va="bottom", fontsize=10.5, color=col if col != C["ref"] else C["ink"], style="italic")
            draw(c, p)
        ax.plot(x, y, "o", ms=6.5, color=C["ink"], zorder=3)
        ax.text(x, y + 0.1, node[1], ha="center", va="bottom", fontsize=10.5, weight="semibold")

    draw(tree, ())
    for group in info:
        pts = sorted(pos[p] for p in group)
        ax.plot([p[0] for p in pts], [p[1] for p in pts], ls=(0, (3, 3)), color=C["hi"], lw=1.6, zorder=0)
    xs = [p[0] for p in pos.values()]
    ys = [p[1] for p in pos.values()]
    ax.set_xlim(min(xs) - 0.6, max(xs) + 0.6)
    ax.set_ylim(min(ys) - 0.75, max(ys) + 0.35)
    ax.set_axis_off()
    if title:
        ax.set_title(title, fontsize=10.5)
    return pos


# ------------------------------------------------- 1. BoS: sequential vs simultaneous ----
def bos_trees():
    """Tadelis Figs. 7.7 and 7.8 (p. 138): same moves, different information for player 2."""
    bos = Dn("1", [("O", Dn("2", [("o", Tn(2, 1)), ("f", Tn(0, 0))])),
                   ("F", Dn("2", [("o", Tn(0, 0)), ("f", Tn(1, 2))]))])
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(10, 3.8))
    draw_tree(a1, bos, title="Sequential: 2 sees 1's move (2 information sets)")
    pos = draw_tree(a2, bos, info=[[("O",), ("F",)]],
                    title="Simultaneous: one information set $h_2$")
    x = (pos[("O",)][0] + pos[("F",)][0]) / 2
    a2.text(x, pos[("O",)][1] - 0.13, "$h_2$", color=C["hi"], ha="center", va="top")
    a1.text(-0.55, -2.55, "$S_2=\\{oo,of,fo,ff\\}$: 4 plans", color=C["main"])
    a2.text(-0.55, -2.55, "$S_2=\\{o,f\\}$: 2 plans", color=C["main"])
    save(fig, "L03-bos-sequential-vs-simultaneous")
    return 2 * 2, 2


# --------------------------------------------- 2. BoS normal form: 3 NE, 1 SPE ----------
def bos_normal_form():
    """Tadelis p. 143 (matrix) and p. 157 (SPE): rows O, F; columns oo, of, fo, ff."""
    cols = ["oo", "of", "fo", "ff"]
    pay = {("O", "o"): (2, 1), ("O", "f"): (0, 0), ("F", "o"): (0, 0), ("F", "f"): (1, 2)}
    M = {(r, c): pay[(r, c[0] if r == "O" else c[1])] for r in "OF" for c in cols}
    ne = [(r, c) for (r, c), u in M.items()
          if u[0] >= max(M[(rr, c)][0] for rr in "OF") and u[1] >= max(M[(r, cc)][1] for cc in cols)]
    spe = ("O", "of")
    fig, ax = plt.subplots(figsize=(7.4, 2.9))
    for j, c in enumerate(cols):
        ax.text(j + 0.5, 2.25, c, ha="center", fontsize=12, style="italic")
    for i, r in enumerate("OF"):
        ax.text(-0.25, 1.5 - i, r, ha="center", va="center", fontsize=12)
        for j, c in enumerate(cols):
            y0 = 1 - i
            face = "white"
            if (r, c) == spe:
                face = "#dcefe4"
            ax.add_patch(Rectangle((j, y0), 1, 1, facecolor=face, edgecolor=C["ref"], lw=1))
            if (r, c) in ne:
                ax.add_patch(Rectangle((j + 0.06, y0 + 0.06), 0.88, 0.88, fill=False,
                                       edgecolor=C["good"] if (r, c) == spe else C["warn"], lw=2.2))
            u = M[(r, c)]
            ax.text(j + 0.5, y0 + 0.5, f"{u[0]}, {u[1]}", ha="center", va="center", fontsize=12)
    ax.text(2, -0.35, "boxed: the three pure Nash equilibria (O, oo), (O, of), (F, ff)   "
            "shaded: the unique subgame-perfect one, (O, of)", ha="center", fontsize=9.5, color=C["ink"])
    ax.text(-0.25, 2.25, "1 \\ 2", ha="center", fontsize=10, color=C["ref"])
    ax.set_xlim(-0.6, 4.1)
    ax.set_ylim(-0.6, 2.6)
    ax.set_axis_off()
    save(fig, "L03-bos-normal-form")
    return sorted(ne), M


# --------------------------------------------- 3. Centipede: backward induction ----------
def centipede():
    """Tadelis Fig. 8.8 (p. 159): stop payoffs (1,1), (0,3), (2,2), (1,4); end (3,3)."""
    stops = [(1, 1), (0, 3), (2, 2), (1, 4)]
    end = (3, 3)
    movers = ["1", "2", "1", "2"]
    cont = ["C", "c", "C", "c"]
    stop = ["N", "n", "N", "n"]
    # backward induction: the mover at k stops iff stopping beats the value of continuing
    val = end
    choice = [None] * 4
    for k in range(3, -1, -1):
        i = int(movers[k]) - 1
        if stops[k][i] > val[i]:
            choice[k], val = "stop", stops[k]
        else:
            choice[k] = "cont"
    fig, ax = plt.subplots(figsize=(9, 3.2))
    for k in range(4):
        x = 2 * k
        ccol = C["good"] if choice[k] == "cont" else C["warn"]
        scol = C["good"] if choice[k] == "stop" else C["ref"]
        ax.plot([x, x + 2], [0, 0], color=ccol, lw=3 if choice[k] == "cont" else 2.2,
                ls="-" if choice[k] == "cont" else "--")
        ax.plot([x, x], [0, -1], color=scol, lw=3.2 if choice[k] == "stop" else 1.3)
        ax.plot(x, 0, "o", color=C["ink"], ms=7, zorder=3)
        ax.text(x, 0.15, movers[k], ha="center", weight="semibold")
        ax.text(x + 1, 0.08, cont[k], ha="center", style="italic")
        ax.text(x + 0.12, -0.5, stop[k], style="italic")
        ax.text(x, -1.1, f"({stops[k][0]}, {stops[k][1]})", ha="center", va="top")
        ax.text(x, -1.55, f"step {4 - k}", ha="center", va="top", fontsize=8.5, color=C["ref"])
    ax.text(8.15, 0, f"({end[0]}, {end[1]})", va="center")
    ax.text(4, 0.6, "Backward induction stops at every node: the outcome is (1, 1), "
            "though continuing to the end gives (3, 3)", ha="center", fontsize=9.5, color=C["ink"])
    ax.set_xlim(-0.6, 9.3)
    ax.set_ylim(-1.9, 0.8)
    ax.set_axis_off()
    save(fig, "L03-centipede-backward-induction")
    return val, choice


# --------------------------------------------- 4. Voluntary BoS: subgames ---------------
def voluntary_bos():
    """Tadelis Figs. 8.4 and 8.7 (pp. 155, 159): two proper subgames; two pure SPE."""
    tree = Dn("1", [("Y", Dn("1", [("O", Dn("2", [("o", Tn(2, 1)), ("f", Tn(0, 0))])),
                                   ("F", Dn("2", [("o", Tn(0, 0)), ("f", Tn(1, 2))]))])),
                    ("N", Tn(1.5, 1.5))])
    fig, axs = plt.subplots(1, 3, figsize=(11.5, 3.9), gridspec_kw=dict(width_ratios=[2.2, 1, 1]))
    pos = draw_tree(axs[0], tree, info=[[("Y", "O"), ("Y", "F")]],
                    title="Two proper subgames: the whole game, and the one at $x_1$")
    x1 = pos[("Y",)]
    axs[0].add_patch(FancyBboxPatch((x1[0] - 1.75, -3.68), 3.5, 2.96, boxstyle="round,pad=0.05",
                                    fill=False, ec=C["main"], lw=1.6, ls="-"))
    axs[0].text(x1[0] - 1.7, -0.78, "subgame at $x_1$", color=C["main"], fontsize=9.5, va="top")
    # reduced games: replace the subgame by the payoffs of each of its pure NE
    for ax, (ne, u) in zip(axs[1:], [("(O, o)", (2, 1)), ("(F, f)", (1, 2))]):
        red = Dn("1", [("Y", Tn(*u)), ("N", Tn(1.5, 1.5))])
        pick = ("Y",) if u[0] > 1.5 else ("N",)
        draw_tree(ax, red, good={pick}, title=f"subgame plays {ne}")
    save(fig, "L03-voluntary-bos-subgames")
    return [("YO", "o") if 2 > 1.5 else None, ("NF", "f") if 1 < 1.5 else None]


# --------------------------------------------- 5. Entry: threat and commitment ----------
def entry_commitment():
    """Cabral Figs. 7.7-7.8 (pp. 168-170). Payoffs (entrant, incumbent); the figures print
    (-10, 10) after (enter, retaliate); the text of p. 168 gives the incumbent -10 there.
    The bond costs the incumbent 40 if it does not retaliate (p. 169)."""
    M, DE, DI, FE, FI, BOND = 50, 10, 20, -10, 10, 40
    plain = Dn("E", [("out", Tn(0, M)),
                     ("in", Dn("I", [("acc", Tn(DE, DI)), ("ret", Tn(FE, FI))]))])
    bonded = Dn("I", [("no bond", Dn("E", [("out", Tn(0, M)),
                                           ("in", Dn("I", [("acc", Tn(DE, DI)), ("ret", Tn(FE, FI))]))])),
                      ("bond", Dn("E", [("out", Tn(0, M)),
                                        ("in", Dn("I", [("acc", Tn(DE, DI - BOND)), ("ret", Tn(FE, FI))]))]))])
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11.5, 4.3), gridspec_kw=dict(width_ratios=[1, 1.9]))
    draw_tree(a1, plain, good={("in",), ("in", "acc")}, warn={("in", "ret")},
              title="Fig. 7.7: 'retaliate' is a non-credible threat")
    # SPE with the bond: incumbent retaliates after a bond (10 > -20), entrant stays out
    ret_after_bond = FI > DI - BOND
    good = {("no bond", "in"), ("no bond", "in", "acc"), ("bond",),
            ("bond", "out") if ret_after_bond else ("bond", "in"),
            ("bond", "in", "ret") if ret_after_bond else ("bond", "in", "acc")}
    draw_tree(a2, bonded, good=good, leaf_gap=1.05,
              title="Fig. 7.8: a bond of 40 makes retaliation credible")
    save(fig, "L03-entry-commitment")
    spe_plain = (DE, DI) if DI > FI else (0, M)
    spe_bond = (0, M) if ret_after_bond else (DE, DI - BOND)
    return spe_plain, spe_bond, spe_bond[1] - spe_plain[1]


# --------------------------------------------- 6. Stackelberg vs Cournot ----------------
A, CST = 100.0, 10.0          # Tadelis p. 160: p = 100 - q, c_i(q_i) = 10 q_i


def r(q):
    """Best response (8.1), p. 160: (90 - q)/2, floored at 0."""
    return np.maximum(0.0, (A - CST - q) / 2)


def pi(q1, q2):
    return (A - q1 - q2 - CST) * q1


def stackelberg_vs_cournot():
    qc, qs1 = (A - CST) / 3, (A - CST) / 2
    qs2 = float(r(qs1))
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(10.6, 4.4))
    q = np.linspace(0, 90, 400)
    a1.plot(q, r(q), color=C["main"], label="firm 2's best response $q_2=(90-q_1)/2$")
    a1.plot(r(q), q, color=C["ref"], label="firm 1's best response (Cournot only)")
    for level, col, lab in [(pi(qs1, qs2), C["good"], "leader isoprofit 1012.5"),
                            (pi(qc, qc), C["hi"], "leader isoprofit 900")]:
        qq = np.linspace(5, 89, 400)
        iso = A - CST - qq - level / qq
        m = (iso >= 0) & (iso <= 90)
        a1.plot(qq[m], iso[m], color=col, lw=1.3, ls="--", label=lab)
    a1.plot(qc, qc, "o", color=C["hi"], ms=8)
    a1.annotate("Cournot (30, 30)", (qc, qc), xytext=(8, 8), textcoords="offset points", color=C["hi"])
    a1.plot(qs1, qs2, "o", color=C["good"], ms=8)
    a1.annotate("Stackelberg (45, 22.5)", (qs1, qs2), xytext=(8, 6), textcoords="offset points",
                color=C["good"])
    a1.set(xlabel="$q_1$ (leader)", ylabel="$q_2$ (follower)", xlim=(0, 90), ylim=(0, 90),
           title="Leader picks its point on firm 2's reaction curve")
    a1.legend(fontsize=8.3, loc="upper right")
    q1 = np.linspace(0, 90, 400)
    red = pi(q1, r(q1))                       # (8.2): the leader's reduced profit
    a2.plot(q1, red, color=C["main"], label="$\\pi_1(q_1, q_2(q_1))$, eq. (8.2)")
    a2.axhline(pi(qc, qc), color=C["ref"], lw=1, ls="--")
    a2.text(2, pi(qc, qc) + 25, "Cournot profit 900", color=C["ref"], fontsize=9)
    a2.plot(qc, pi(qc, float(r(qc))), "o", color=C["hi"], ms=7)
    a2.annotate("$q_1=30$: firm 2 replies 30,\nprofit 900 (available, not chosen)", (qc, 900),
                xytext=(-10, -62), textcoords="offset points", color=C["hi"], fontsize=9)
    a2.plot(qs1, pi(qs1, qs2), "o", color=C["good"], ms=8)
    a2.annotate("$q_1=45$: profit 1012.5", (qs1, pi(qs1, qs2)), xytext=(8, 6),
                textcoords="offset points", color=C["good"])
    a2.set(xlabel="$q_1$", ylabel="leader's profit", xlim=(0, 90), ylim=(0, 1150),
           title="First-mover advantage: 1012.5 - 900 = +112.5")
    a2.legend(fontsize=8.5, loc="lower center")
    save(fig, "L03-stackelberg-vs-cournot")
    return (qs1, qs2, pi(qs1, qs2), (A - qs1 - qs2 - CST) * qs2), (qc, pi(qc, qc))


# --------------------------------------------- 7. Hyperbolic discounting ----------------
def hyperbolic():
    """Tadelis Section 8.3.4 (pp. 166-169), beta = 1/2, delta = 1, u = ln, K = 1.
    Self 2 plays x2 = 2K2/3, x3 = K2/3 (p. 168). Self 1's payoff from x1 is
    ln x1 + .5 ln(2(1-x1)/3) + .5 ln((1-x1)/3), whose derivative is 1/x1 - 1/(1-x1)."""
    v1 = lambda x: np.log(x) + 0.5 * np.log(2 * (1 - x) / 3) + 0.5 * np.log((1 - x) / 3)
    x = np.linspace(0.05, 0.95, 500)
    xstar = x[np.argmax(v1(x))]
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(10.6, 4.0))
    a1.plot(x, v1(x), color=C["main"], label="self 1's payoff given self 2's reply")
    a1.plot(0.5, v1(0.5), "o", color=C["good"], ms=8)
    a1.annotate("max at $x_1=K/2$", (0.5, v1(0.5)), xytext=(-20, 12), textcoords="offset points",
                color=C["good"])
    a1.plot(2 / 3, v1(2 / 3), "o", color=C["warn"], ms=7)
    a1.annotate("printed $x_1=2K/3$ (p. 169)", (2 / 3, v1(2 / 3)), xytext=(6, -26),
                textcoords="offset points", color=C["warn"])
    a1.set(xlabel="$x_1/K$", ylabel="$v_1$ (K = 1)", title="Sophisticated self 1: the correct optimum",
           ylim=(-4.5, -1.5))
    a1.legend(fontsize=9, loc="lower center")
    plans = {"exponential, $\\delta=1$\n(p. 168)": (1 / 3, 1 / 3, 1 / 3),
             "self 1's ideal\n(commitment)": (1 / 2, 1 / 4, 1 / 4),
             "sophisticated SPE\n(correct)": (1 / 2, 1 / 3, 1 / 6),
             "sophisticated SPE\n(as printed)": (2 / 3, 2 / 9, 1 / 9)}
    cols = [C["ref"], C["main"], C["good"], C["warn"]]
    w = 0.2
    for k, ((lab, xs), col) in enumerate(zip(plans.items(), cols)):
        a2.bar(np.arange(3) + (k - 1.5) * w, xs, w, color=col, label=lab.replace("\n", " "))
    a2.set_xticks(range(3), ["$x_1$", "$x_2$", "$x_3$"])
    a2.set(ylabel="share of K", title="Consumption plans, $\\beta=1/2$")
    a2.legend(fontsize=7.8, loc="upper right")
    save(fig, "L03-hyperbolic-discounting")
    return xstar, v1(0.5) > v1(2 / 3)


if __name__ == "__main__":
    apply()
    plt.rcParams["axes.titlesize"] = 10.5
    assert bos_trees() == (4, 2)                                         # |S_2| = 2 x 2 vs 2
    ne, M = bos_normal_form()
    assert ne == [("F", "ff"), ("O", "of"), ("O", "oo")]                 # p. 145
    assert M[("O", "of")] == (2, 1) and M[("F", "of")] == (1, 2)         # matrix, p. 143
    val, choice = centipede()
    assert val == (1, 1) and choice == ["stop"] * 4                      # p. 159
    assert voluntary_bos() == [("YO", "o"), ("NF", "f")]                 # E_SPE, p. 158
    assert entry_commitment() == ((10, 20), (0, 50), 30)                 # value 30, p. 170
    (q1, q2, p1, p2), (qc, pc) = stackelberg_vs_cournot()
    assert (q1, q2, p1, p2) == (45, 22.5, 1012.5, 506.25) and (qc, pc) == (30, 900)   # p. 161
    xstar, ok = hyperbolic()
    assert abs(xstar - 0.5) < 2e-3 and ok
    print("L03 figures written; all checks pass")
