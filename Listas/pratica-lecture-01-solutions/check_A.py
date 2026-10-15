"""Checks every finite-game claim in items 1-8, 10, 14, 16-19 (matrices, dominance, IESDS rounds).

IESDS follows the lecture's definition (Lecture 1, slide 29): in round k every strategy that is
strictly dominated by a pure strategy, given the opponents' round-(k-1) sets, is removed at once.
Run: python check_A.py  -> prints "all A checks passed" or fails on the first wrong claim.
"""
from fractions import Fraction as F
from itertools import product


def dominated(i, si, S, u, strict=True):
    """Return the strategies of player i in S[i] that dominate si given S_{-i} (strictly or weakly)."""
    others = [S[j] for j in range(len(S)) if j != i]
    out = []
    for ti in S[i]:
        if ti == si:
            continue
        diffs = []
        for rest in product(*others):
            p, q = list(rest), list(rest)
            p.insert(i, ti)
            q.insert(i, si)
            diffs.append(u(i, tuple(p)) - u(i, tuple(q)))
        if strict and all(d > 0 for d in diffs):
            out.append(ti)
        if not strict and all(d >= 0 for d in diffs) and any(d > 0 for d in diffs):
            out.append(ti)
    return out


def iesds(S, u):
    """Run IESDS; return (list of per-round removals, surviving sets)."""
    S = [list(s) for s in S]
    rounds = []
    while True:
        rem = [[s for s in S[i] if dominated(i, s, S, u)] for i in range(len(S))]
        if not any(rem):
            return rounds, S
        rounds.append(rem)
        S = [[s for s in S[i] if s not in rem[i]] for i in range(len(S))]


def bimatrix(rows, cols, cells):
    """Two-player game from a dict {(r, c): (u1, u2)}; returns (S, u)."""
    return [rows, cols], (lambda i, p: cells[p][i])


def table(rows, cols, vals):
    return {(r, c): vals[a][b] for a, r in enumerate(rows) for b, c in enumerate(cols)}


def pure_ne(S, u):
    ne = []
    for p in product(*S):
        ok = True
        for i in range(len(S)):
            for t in S[i]:
                q = list(p)
                q[i] = t
                if u(i, tuple(q)) > u(i, p):
                    ok = False
        if ok:
            ne.append(p)
    return ne


# ---- item 1: Tadelis 3.2 penalty kicks (win 1, lose -1); kicker rows, goalie columns
cells = {(k, g): ((-1, 1) if k == g else (1, -1)) for k in "LR" for g in "LR"}
S, u = bimatrix(list("LR"), list("LR"), cells)
assert all(sum(v) == 0 for v in cells.values())
assert iesds(S, u) == ([], [list("LR"), list("LR")])
assert pure_ne(S, u) == []

# ---- item 2: Tadelis 3.4 stag hunt
cells = table("SH", "SH", [[(3, 3), (0, 1)], [(1, 0), (1, 1)]])
S, u = bimatrix(list("SH"), list("SH"), cells)
assert iesds(S, u)[0] == []
assert pure_ne(S, u) == [("S", "S"), ("H", "H")]
assert cells["S", "S"][0] > cells["H", "S"][0] == cells["H", "H"][0] > cells["S", "H"][0]

# ---- item 3: Munoz-Garcia Ex. 2 (tree Fig. 1.3 -> matrix)
leaf = {("H", "a"): (0, 10), ("H", "r"): (0, 0), ("M", "a"): (5, 5), ("M", "r"): (0, 0),
        ("L", "a"): (10, 0), ("L", "r"): (0, 0)}
S2 = ["".join(x) for x in product("ar", repeat=3)]
assert len(S2) == 8
cells = {(m, s): leaf[m, s["HML".index(m)]] for m in "HML" for s in S2}
assert cells["L", "aar"] == (0, 0)            # the book's Fig. 1.4 prints (10, 0) here
book_L = {"aaa": (10, 0), "aar": (10, 0), "arr": (0, 0), "rrr": (0, 0), "rra": (10, 0),
          "raa": (10, 0), "ara": (10, 0), "rar": (0, 0)}
assert [s for s in book_L if book_L[s] != cells["L", s]] == ["aar"]
S, u = bimatrix(list("HML"), S2, cells)
assert iesds(S, u)[0] == []                    # no strictly dominated strategy for anyone
# accepting at H and M weakly dominates any plan that rejects there; the reply at L never
# changes player 2's payoff, so plans differing only at L are payoff-equivalent for her
assert all("aaa" in dominated(1, s, S, u, strict=False) for s in S2 if "r" in s[:2])
assert dominated(1, "aar", S, u, strict=False) == [] and all(cells[m, "aaa"][1] == cells[m, "aar"][1] for m in "HML")

# ---- item 4: Munoz-Garcia Ex. 5 prisoners' dilemma (years in jail as negative payoffs)
cells = table(["C", "N"], ["C", "N"], [[(-5, -5), (0, -15)], [(-15, 0), (-1, -1)]])
S, u = bimatrix(["C", "N"], ["C", "N"], cells)
assert dominated(0, "N", S, u) == ["C"] and dominated(1, "N", S, u) == ["C"]
assert iesds(S, u)[1] == [["C"], ["C"]]
assert all(a > b for a, b in zip(cells["N", "N"], cells["C", "C"]))  # (N,N) Pareto dominates

# ---- item 5: Munoz-Garcia Ex. 13
cells = table("UMD", "LR", [[(-10, 10), (0, 12)], [(-12, 0), (2, 2)], [(-9, 0), (1, 0)]])
S, u = bimatrix(list("UMD"), list("LR"), cells)
assert dominated(0, "U", S, u) == ["D"] and dominated(0, "M", S, u) == [] and dominated(0, "D", S, u) == []
assert dominated(1, "L", S, u) == [] and dominated(1, "L", S, u, strict=False) == ["R"]
r, surv = iesds(S, u)
assert r == [[["U"], []]] and surv == [["M", "D"], ["L", "R"]]
assert dominated(1, "L", surv, u, strict=False) == ["R"]   # weak, not strict, after round 1
assert dominated(0, "D", [["M", "D"], ["R"]], u) == ["M"]  # weak route: drop L, then M beats D

# ---- item 6: Tadelis 4.5
cells = table("UMD", "LCR", [[(6, 8), (2, 6), (8, 2)], [(8, 2), (4, 4), (9, 5)], [(8, 10), (4, 6), (6, 7)]])
S, u = bimatrix(list("UMD"), list("LCR"), cells)
r, surv = iesds(S, u)
assert r == [[["U"], []], [[], ["C"]]] and surv == [["M", "D"], ["L", "R"]]
assert dominated(0, "U", S, u) == ["M"] and dominated(1, "C", [["M", "D"], list("LCR")], u) == ["R"]
assert dominated(0, "D", surv, u, strict=False) == ["M"]
assert pure_ne(S, u) == [("M", "R"), ("D", "L")]
assert dominated(1, "L", [["M"], ["L", "R"]], u) == ["R"]          # weak route: drop D -> (M, R)
assert dominated(1, "C", [["M", "D"], list("LCR")], u) == ["R"]   # without U, C loses to R

# ---- item 7: Gibbons 1.2
cells = table("TMB", "LCR", [[(2, 0), (1, 1), (4, 2)], [(3, 4), (1, 2), (2, 3)], [(1, 3), (0, 2), (3, 0)]])
S, u = bimatrix(list("TMB"), list("LCR"), cells)
r, surv = iesds(S, u)
assert r == [[["B"], []], [[], ["C"]]] and surv == [["T", "M"], ["L", "R"]]
assert dominated(0, "B", S, u) == ["T"] and dominated(1, "C", S, u) == []
assert dominated(1, "C", [["T", "M"], list("LCR")], u) == ["R"]
assert pure_ne(S, u) == [("T", "R"), ("M", "L")]

# ---- item 8: Munoz-Garcia Ex. 9 battle of the sexes
cells = table("FO", "FO", [[(3, 1), (0, 0)], [(0, 0), (1, 3)]])
S, u = bimatrix(list("FO"), list("FO"), cells)
assert iesds(S, u) == ([], [["F", "O"], ["F", "O"]])
assert all(dominated(i, s, S, u, strict=False) == [] for i in (0, 1) for s in "FO")

# ---- item 10: Tadelis 3.7 streetlamp, three players, s_i = 1 contributes
def lamp(i, p):
    return 3 * (sum(p) >= 2) - p[i]
S = [[0, 1]] * 3
assert iesds(S, lamp)[0] == []
assert [lamp(i, (1, 1, 0)) for i in range(3)] == [2, 2, 3]
assert [lamp(i, (1, 0, 0)) for i in range(3)] == [-1, 0, 0]
assert [lamp(i, (1, 1, 1)) for i in range(3)] == [2, 2, 2]
assert pure_ne(S, lamp) == [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0)]

# ---- item 14: Munoz-Garcia Ex. 12
cells = table("FCB", "FCB", [[(0, 5), (2, 4), (2, 3)], [(2, 3), (0, 5), (3, 2)], [(5, 0), (2, 4), (2, 3)]])
S, u = bimatrix(list("FCB"), list("FCB"), cells)
assert all(dominated(0, s, S, u) == [] for s in "FCB")
assert dominated(1, "B", S, u) == ["C"] and dominated(1, "F", S, u) == dominated(1, "C", S, u) == []
r, surv = iesds(S, u)
assert r == [[[], ["B"]], [["C"], []]] and surv == [["F", "B"], ["F", "C"]]
assert dominated(0, "F", [list("FCB"), ["F", "C"]], u, strict=False) == ["B"]
assert dominated(0, "F", S, u, strict=False) == ["B"] and dominated(0, "C", S, u) == []

# ---- item 16: Tadelis 4.7 campaigning (row player's win probability; column gets 1 - pi)
pi = {("P", "P"): F(1, 2), ("P", "B"): 0, ("P", "N"): F(3, 10), ("B", "B"): F(1, 2),
      ("N", "B"): F(6, 10), ("N", "N"): F(1, 2)}
for (a, b), v in list(pi.items()):
    pi[b, a] = 1 - v
cells = {(a, b): (pi[a, b], 1 - pi[a, b]) for a in "PBN" for b in "PBN"}
assert all(cells[a, b] == tuple(reversed(cells[b, a])) for a in "PBN" for b in "PBN")  # symmetric
S, u = bimatrix(list("PBN"), list("PBN"), cells)
assert dominated(0, "P", S, u) == ["B", "N"]
r, surv = iesds(S, u)
assert r == [[["P"], ["P"]], [["B"], ["B"]]] and surv == [["N"], ["N"]]
assert [pi["B", "P"], pi["N", "P"], pi["B", "N"]] == [1, F(7, 10), F(4, 10)]

# ---- item 17: Tadelis 4.3 discrete first-price auction, v1 = 3, v2 = 5
def fpa(b1, b2):
    if b1 > b2:
        return (3 - b1, 0)
    if b1 < b2:
        return (0, 5 - b2)
    return (F(3 - b1, 2), F(5 - b2, 2))
cells = {(a, b): fpa(a, b) for a in range(3) for b in range(3)}
S, u = bimatrix([0, 1, 2], [0, 1, 2], cells)
assert [cells[0, b] for b in range(3)] == [(F(3, 2), F(5, 2)), (0, 4), (0, 3)]
assert [cells[1, b] for b in range(3)] == [(2, 0), (1, 2), (0, 3)]
assert [cells[2, b] for b in range(3)] == [(1, 0), (1, 0), (F(1, 2), F(3, 2))]
assert all(dominated(0, s, S, u) == [] for s in range(3))
assert dominated(1, 0, S, u) == [2] and dominated(1, 1, S, u) == dominated(1, 2, S, u) == []
assert dominated(0, 0, S, u, strict=False) == [1] and dominated(1, 0, S, u, strict=False) == [1, 2]
r, surv = iesds(S, u)
assert r == [[[], [0]], [[0], []], [[], [1]], [[1], []]] and surv == [[2], [2]]
assert dominated(0, 1, [[0, 1, 2], [1, 2]], u) == [] and dominated(0, 1, [[0, 1, 2], [1, 2]], u, strict=False) == [2]

# ---- item 18: Tadelis 4.10 popsicle stands, 25 people per tower, ties split
def stands(i, p):
    me, other = p[i], p[1 - i]
    return sum(F(25) if abs(t - me) < abs(t - other) else F(25, 2) if abs(t - me) == abs(t - other) else 0
               for t in range(1, 6))
S = [[1, 2, 3, 4, 5]] * 2
assert stands(0, (2, 3)) == 50 and stands(1, (2, 3)) == 75          # the book's example
for s1, s2 in product(range(1, 6), repeat=2):                      # closed form in item18
    if s1 < s2:
        assert stands(0, (s1, s2)) == F(25 * (s1 + s2 - 1), 2)
assert dominated(0, 1, S, stands) == [2, 3, 4] and dominated(0, 5, S, stands) == [2, 3, 4]
r, surv = iesds(S, stands)
assert r == [[[1, 5], [1, 5]], [[2, 4], [2, 4]]] and surv == [[3], [3]]
assert [stands(0, (1, s)) for s in range(1, 6)] == [F(125, 2), 25, F(75, 2), 50, F(125, 2)]
assert [stands(0, (2, s)) for s in range(1, 6)] == [100, F(125, 2), 50, F(125, 2), 75]
assert [stands(0, (3, s)) for s in range(1, 6)] == [F(175, 2), 75, F(125, 2), 75, F(175, 2)]
assert [stands(0, (4, s)) for s in range(1, 6)] == [75, F(125, 2), 50, F(125, 2), 100]
assert [stands(0, (5, s)) for s in range(1, 6)] == [F(125, 2), 50, F(75, 2), 25, F(125, 2)]
br = {s2: max(range(1, 6), key=lambda s1: stands(0, (s1, s2))) for s2 in (1, 3, 5)}
assert br == {1: 2, 3: 3, 5: 4}
walk = lambda a, b: sum(25 * min(abs(t - a), abs(t - b)) for t in range(1, 6))
assert walk(3, 3) == 150 and walk(2, 4) == 75 and min(walk(a, b) for a in range(1, 6) for b in range(1, 6)) == 75
assert stands(0, (2, 4)) == stands(1, (2, 4)) == F(125, 2)

# ---- item 19: Munoz-Garcia Ex. 16, strict vs weak deletion
cells = table("UCD", "LMR", [[(2, 1), (1, 1), (0, 0)], [(1, 2), (3, 1), (2, 1)], [(2, -2), (1, -1), (-1, -1)]])
S, u = bimatrix(list("UCD"), list("LMR"), cells)
assert iesds(S, u) == ([], [list("UCD"), list("LMR")])            # IESDS has no bite


def weak_route(S, steps):
    """Apply a list of (player, strategy) weak deletions, asserting each is weakly dominated."""
    S = [list(s) for s in S]
    for i, s in steps:
        assert dominated(i, s, S, u, strict=False), (i, s)
        S[i].remove(s)
    return S


S1 = weak_route(S, [(0, "D"), (1, "R"), (1, "M"), (0, "C")])
assert S1 == [["U"], ["L"]]
assert dominated(1, "R", [["U", "C"], list("LMR")], u) == ["L"]   # strict after D is gone
S2 = weak_route(S, [(1, "R")])
assert S2 == [list("UCD"), ["L", "M"]]
assert all(dominated(i, s, S2, u, strict=False) == [] for i in (0, 1) for s in S2[i])
assert dominated(0, "D", S, u, strict=False) == ["U"] and dominated(1, "R", S, u, strict=False) == ["M"]
# deleting every weakly dominated strategy at once in each round also ends at (U, L)
T = [list(s) for s in S]
while True:
    rem = [[s for s in T[i] if dominated(i, s, T, u, strict=False)] for i in (0, 1)]
    if not any(rem):
        break
    T = [[s for s in T[i] if s not in rem[i]] for i in (0, 1)]
assert T == [["U"], ["L"]]

print("all A checks passed")
