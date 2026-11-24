"""Checks every number and equilibrium claim in the ten Lecture 7 solutions (items 61-70):
sol-tadelis-15-1, sol-munoz-garcia-9-1, sol-tadelis-15-3, sol-tadelis-12-5, sol-munoz-garcia-9-2,
sol-tadelis-12-6, sol-tadelis-15-5, sol-tadelis-16-4, sol-mwg-13-c-5, sol-tadelis-16-8.
Exact arithmetic (fractions, sympy); thresholds are tested on both sides; off-path beliefs are
searched on a grid of step 1/60.

Run: python check_G_L07.py  -> one line per item and "all G L07 checks passed",
or an AssertionError on the first wrong claim.
"""
from fractions import Fraction as F
from itertools import product

import sympy as sp

EPS = F(1, 1000)
GRID = [F(k, 60) for k in range(61)]


# ----------------------------------------------------------------- generic two-type signaling game
def signaling(prior, allowed, replies, u):
    """Pure BNE and pure PBE of a sender-receiver game.

    prior: {type: prob}; allowed: {type: [messages]}; replies: {message: [receiver actions]}
    (empty list = the message ends the game); u(t, m, a) -> (sender, receiver), a is None
    after a terminal message. Returns (bne, pbe): lists of (sender profile, receiver profile);
    pbe entries carry, for each off-path message, the set of grid beliefs (prob of the first
    type) that make the reply optimal.
    """
    types = list(prior)
    msgs = sorted({m for t in types for m in allowed[t]})
    active = [m for m in msgs if replies.get(m)]
    S = [dict(zip(types, c)) for c in product(*(allowed[t] for t in types))]
    R = [dict(zip(active, c)) for c in product(*(replies[m] for m in active))]

    def us(t, m, r):
        return u(t, m, r.get(m))[0]

    def ur_ex(s, r):
        return sum(prior[t] * u(t, s[t], r.get(s[t]))[1] for t in types)

    def sender_ok(s, r):
        return all(us(t, s[t], r) >= us(t, m, r) for t in types for m in allowed[t])

    def reply_value(m, a, belief):
        return sum(belief[t] * u(t, m, a)[1] for t in belief)

    bne, pbe = [], []
    for s in S:
        for r in R:
            if not sender_ok(s, r):
                continue
            if ur_ex(s, r) == max(ur_ex(s, r2) for r2 in R):
                bne.append((s, r))
            ok, offpath = True, {}
            for m in active:
                senders = [t for t in types if s[t] == m]
                if senders:
                    tot = sum(prior[t] for t in senders)
                    bel = {t: prior[t] / tot for t in senders}
                    ok &= reply_value(m, r[m], bel) == max(reply_value(m, a, bel) for a in replies[m])
                else:
                    can = [t for t in types if m in allowed[t]]
                    beliefs = [{can[0]: F(1)}] if len(can) == 1 else \
                        [{can[0]: g, can[1]: 1 - g} for g in GRID]
                    good = [b[can[0]] for b in beliefs
                            if reply_value(m, r[m], b) == max(reply_value(m, a, b) for a in replies[m])]
                    ok &= bool(good)
                    offpath[m] = good
            if ok:
                pbe.append((s, r, offpath))
    return bne, pbe


def prof(s, r):
    """Compact label of a profile, e.g. 'R,L | U'."""
    return ",".join(s.values()) + " | " + ",".join(r.values())


# ===================================================== 61. Tadelis 15.1 (Equilibrium Selection)
U151 = {("A", "L"): (0, 4), ("A", "M"): (0, 1), ("A", "R"): (4, 0),
        ("B", "L"): (4, 0), ("B", "M"): (0, 1), ("B", "R"): (0, 4),
        ("C", "L"): (1, 3), ("C", "M"): (1, 3), ("C", "R"): (1, 3)}
P1, P2 = "ABC", "LMR"


def u_mix(x, y):
    """Expected payoffs of mixed profile x over P1, y over P2."""
    return tuple(sum(x[i] * y[j] * U151[(a, b)][k] for i, a in enumerate(P1) for j, b in enumerate(P2))
                 for k in (0, 1))


def is_ne(x, y):
    v1, v2 = u_mix(x, y)
    pure = lambda n, i: tuple(F(int(i == j)) for j in range(n))
    return all(u_mix(pure(3, i), y)[0] <= v1 for i in range(3)) and \
        all(u_mix(x, pure(3, j))[1] <= v2 for j in range(3))


pure_ne = [(a, b) for a in P1 for b in P2
           if U151[(a, b)][0] == max(U151[(x, b)][0] for x in P1)
           and U151[(a, b)][1] == max(U151[(a, y)][1] for y in P2)]
assert pure_ne == [("C", "M")]
simplex12 = [(F(i, 12), F(j, 12), F(12 - i - j, 12)) for i in range(13) for j in range(13 - i)]
found = [(x, y) for x in simplex12 for y in simplex12 if is_ne(x, y)]
fam1 = lambda x, y: x == (0, 0, 1) and y[0] <= F(1, 4) and y[2] <= F(1, 4)
mixed = ((F(1, 2), F(1, 2), F(0)), (F(1, 2), F(0), F(1, 2)))
assert all(fam1(x, y) or (x, y) == mixed for x, y in found) and mixed in found
assert all((x, y) in found for x in [(0, 0, 1)] for y in simplex12 if fam1(x, y))
assert is_ne((0, 0, 1), (F(1, 4), F(1, 2), F(1, 4)))                       # boundary in
assert not is_ne((0, 0, 1), (F(1, 4) + EPS, F(1, 2) - EPS, F(1, 4)))        # just outside
# M is never a best reply at {x2, x3}: max(4mu, 4(1-mu)) >= 2 > 1 for every belief
assert all(max(4 * m, 4 * (1 - m)) >= 2 > 1 for m in GRID)
# PBE: family 1 needs m = 0, so l + r = 1, contradicting l, r <= 1/4; mixed profile: mu = 1/2
assert F(1, 4) + F(1, 4) < 1 and 4 * F(1, 2) == 2 > 1 and u_mix(*mixed)[0] == 2 > 1
print("Tadelis 15.1: pure BNE (C,M); BNE = {C with l,r <= 1/4} + (A/2+B/2, L/2+R/2); "
      "only the mixed one is a PBE (mu = 1/2)")

# ======================================== 62. Munoz-Garcia Ch. 9 Ex. 1 (separating and pooling)
def u91(t, m, a):
    if m == "L":
        return (2, 0)
    return {("H", "U"): (3, 2), ("H", "D"): (1, 0), ("L", "U"): (1, 0), ("L", "D"): (1, 1)}[(t, a)]


bne, pbe = signaling({"H": F(1, 2), "L": F(1, 2)}, {"H": ["L", "R"], "L": ["L", "R"]},
                     {"R": ["U", "D"]}, u91)
labels = sorted(prof(s, r) for s, r, _ in pbe)
assert labels == ["L,L | D", "R,L | U"], labels
pool = [o for s, r, o in pbe if prof(s, r) == "L,L | D"][0]["R"]
assert max(pool) == F(1, 3) and min(pool) == 0                             # q <= 1/3
q = sp.symbols("q")
assert sp.solve(sp.Eq(2 * q, 1 - q), q) == [sp.Rational(1, 3)]
print("MG 9.1: PBE = separating (R,L') with U, q = 1; pooling (L,L') with D, q <= 1/3")

# ================================================ 63. Tadelis 15.3 (Trust Thy Neighbor)
def tn_payoffs(p, a1, aN, aJ):
    """(u1, expected u2) with types N (x=1, y=0) and J (x=0, y=1)."""
    if a1 == "L":
        return (F(0), F(0))
    u1 = p * (1 if aN == "D" else -1) + (1 - p) * (1 if aJ == "D" else -1)
    u2 = p * (1 if aN == "D" else 0) + (1 - p) * (1 if aJ == "T" else 0)
    return (u1, u2)


def tn_bne(p):
    out = []
    for a1, aN, aJ in product("LS", "DT", "DT"):
        v1, v2 = tn_payoffs(p, a1, aN, aJ)
        ok1 = v1 >= max(tn_payoffs(p, b, aN, aJ)[0] for b in "LS")
        ok2 = v2 >= max(tn_payoffs(p, a1, bN, bJ)[1] for bN in "DT" for bJ in "DT")
        if ok1 and ok2:
            out.append(a1 + ";" + aN + aJ)
    return out


assert sorted(tn_bne(F(3, 4))) == ["L;TD", "L;TT", "S;DT"]
pbe_tn = lambda p: [e for e in tn_bne(p) if e.endswith("DT")]             # N delivers, J trashes
assert pbe_tn(F(3, 4)) == ["S;DT"]
for p in [F(k, 20) for k in range(21)]:
    assert "L;TT" in tn_bne(p) and "L;TT" not in pbe_tn(p)                   # (d): no p works
    assert tn_payoffs(p, "S", "D", "T")[0] == 2 * p - 1
assert pbe_tn(F(1, 2) - EPS) == ["L;DT"] and pbe_tn(F(1, 2) + EPS) == ["S;DT"]
print("Tadelis 15.3: p = 3/4 BNE (S;D,T), (L;T,T), (L;T,D); PBE (S;D,T) only; "
      "(L;T,T) is a non-PBE BNE for every p; trust iff 2p-1 >= 0")

# ======================================== 64. Tadelis 12.5 (Not All That Glitters)
x, p = sp.symbols("x p", nonnegative=True)
cond_mean = sp.integrate(x, (x, 0, p / 3)) / (p / 3)
assert sp.simplify(cond_mean - p / 6) == 0
owner = sp.simplify(4 * cond_mean - p)
assert sp.simplify(owner + p / 3) == 0                                      # -p/3 for p <= 3
assert sp.integrate(4 * x - p, (x, 0, 1)) == 2 - p                           # all sell, p >= 3
assert all(owner.subs(p, F(k, 10)) < 0 for k in range(1, 31))
assert all(2 - F(k, 10) < 0 for k in range(30, 60))
assert sp.integrate(3 * x, (x, 0, 1)) == sp.Rational(3, 2)
assert sp.integrate(4 * x - 3 * x, (x, 0, 1)) == sp.Rational(1, 2)          # lost surplus
# a seller set concentrated near p/3 would be profitable: why the argument uses ALL x < p/3
assert 4 * F(1, 3) * F(9, 10) - 1 > 0
print("Tadelis 12.5: x(p) = p/3; E[4x - p | x <= p/3] = -p/3 < 0 (2 - p if p >= 3): "
      "no trade, prospector 3x (mean 3/2), owner 0, lost surplus 1/2")

# ======================================== 65. Munoz-Garcia Ch. 9 Ex. 2 (job-market signaling)
def u92(t, m, a):
    return {("H", "N", "M"): (10, 10), ("H", "N", "C"): (4, 4), ("H", "E", "M"): (6, 10),
            ("H", "E", "C"): (0, 4), ("L", "N", "M"): (10, 0), ("L", "N", "C"): (4, 4),
            ("L", "E", "M"): (3, 0), ("L", "E", "C"): (-3, 4)}[(t, m, a)]


bne, pbe = signaling({"H": F(1, 2), "L": F(1, 2)}, {"H": ["E", "N"], "L": ["E", "N"]},
                     {"E": ["M", "C"], "N": ["M", "C"]}, u92)
labels = sorted(prof(s, r) for s, r, _ in pbe)
assert labels == ["E,N | M,C", "N,N | C,M", "N,N | M,M"], labels           # replies: after E, after N
nn = {prof(s, r): o["E"] for s, r, o in pbe if "E" in o}
assert max(nn["N,N | C,M"]) == F(2, 5) and min(nn["N,N | M,M"]) == F(2, 5)  # q <= 2/5 C, q >= 2/5 M
assert {"E,E", "N,E"}.isdisjoint({",".join(s.values()) for s, _, _ in pbe})
# education costs: H pays 4, L pays 7 (10-6, 10-3); the firm hires a manager iff belief >= 2/5
assert (10 - 6, 10 - 3) == (4, 7) and 10 * F(2, 5) == 4
print("MG 9.2: PBE = separating [EN'] (M after E, C' after N); pooling [NN'] with any q "
      "(M if q >= 2/5, C if q <= 2/5); [NE'] and [EE'] fail")

# ======================================== 66. Tadelis 12.6 (Reap and Weep)
th, w = sp.symbols("theta w", nonnegative=True)
a_owner = sp.integrate(sp.Rational(3, 2) * th - w, (th, 0, w)) / w
assert sp.simplify(a_owner + w / 4) == 0                                    # -w/4
assert sp.integrate(sp.Rational(3, 2) * th - w, (th, 0, 1)) == sp.Rational(3, 4) - w
assert sp.integrate(th, (th, 0, 1)) == sp.Rational(1, 2)                    # surplus in (b)
c_owner = sp.integrate(sp.Rational(3, 2) * th - w, (th, 0, 2 * w)) / (2 * w)
assert sp.simplify(c_owner - w / 2) == 0                                    # +w/2 for w <= 1/2
S = sp.integrate(sp.Rational(3, 2) * th, (th, 0, 2 * w)) + sp.integrate(th / 2, (th, 2 * w, 1))
assert sp.expand(S - (sp.Rational(1, 4) + 2 * w**2)) == 0
assert S.subs(w, sp.Rational(1, 2)) == sp.Rational(3, 4) and S.subs(w, 0) == sp.Rational(1, 4)
assert sp.solve(sp.Eq(S, sp.Rational(1, 2)), w) == [sp.sqrt(2) / 4]
assert (sp.Rational(3, 4) - w).subs(w, sp.Rational(3, 4)) == 0               # break-even wage
print("Tadelis 12.6: (a) E[1.5 theta - w | theta <= w] = -w/4: no trade, surplus 1/2; "
      "(c) w/2 > 0, accepted up to 3/4, surplus 1/4 + 2w^2 up to 3/4 (= 1/2 at w = sqrt2/4)")

# ======================================== 67. Tadelis 15.5 (Entry again)
PAY155 = {("T", "S", "A"): (4, 6), ("T", "S", "F"): (2, 4), ("T", "B", "A"): (6, 4),
          ("T", "B", "F"): (4, 2), ("W", "S", "A"): (-2, 6), ("W", "S", "F"): (-6, 8),
          ("W", "B", "A"): (0, 4), ("W", "B", "F"): (-6, 2)}
# derive the table from the story: market 10, shares, fight costs 4 (T), 2/8 (W), entry cost 6 (W)
assert PAY155[("T", "S", "F")] == (10 * F(2, 10), 10 * F(8, 10) - 4)
assert PAY155[("T", "B", "F")] == (10 * F(4, 10), 10 * F(6, 10) - 4)
assert PAY155[("W", "S", "F")] == (0 - 6, 10 - 2) and PAY155[("W", "B", "F")] == (0 - 6, 10 - 8)


def u155(t, m, a):
    return (0, 10) if m == "X" else PAY155[(t, m, a)]


bne, pbe = signaling({"T": F(1, 2), "W": F(1, 2)}, {"T": ["S", "B"], "W": ["S", "B", "X"]},
                     {"S": ["A", "F"], "B": ["A", "F"], "X": []}, u155)
lab = lambda s, r: s["T"] + s["W"] + "," + r["S"] + r["B"]
assert sorted(lab(s, r) for s, r in bne) == ["BB,AA", "BB,FA", "BX,AA", "BX,FA", "SX,AF"]
inc = {lab(s, r): sum(F(1, 2) * u155(t, s[t], r.get(s[t]))[1] for t in "TW") for s, r in bne}
assert inc == {"BB,AA": 4, "BB,FA": 4, "BX,AA": 7, "BX,FA": 7, "SX,AF": 8}
assert sorted(lab(s, r) for s, r, _ in pbe) == ["BB,AA", "BB,FA", "BX,AA", "BX,FA"]
for s, r, o in pbe:                                                           # mu_W after S
    g = o["S"]                                                                # grid of Pr(T | S)
    assert (max(g) == F(1, 2)) if r["S"] == "F" else (min(g) == F(1, 2))
assert all(PAY155[(t, "B", "A")][1] > PAY155[(t, "B", "F")][1] for t in "TW")
print("Tadelis 15.5: BNE (SX,AF) (BB,AA) (BB,FA) (BX,AA) (BX,FA); incumbent prefers (SX,AF) = 8, "
      "not PBE (A beats F after B); PBE: BB or BX, A after B, F after S iff Pr(W|S) >= 1/2")

# ======================================== 68. Tadelis 16.4 (School Choice)
PROD = {("E", "B"): (2, 12), ("E", "S"): (0, 4), ("G", "B"): (8, 10), ("G", "S"): (2, 2)}
WAGE = {"H": 6, "L": 2}


def u164(t, m, a):
    cost, prod = PROD[(t, m)]
    return (WAGE[a] - cost, (prod if a == "H" else F(prod, 2)) - WAGE[a])


assert [u164("E", "B", "H"), u164("G", "S", "L")] == [(4, 6), (0, -1)]
for pr in [F(k, 20) for k in range(1, 20)]:
    bne, pbe = signaling({"E": pr, "G": 1 - pr}, {"E": ["B", "S"], "G": ["B", "S"]},
                         {"B": ["H", "L"], "S": ["H", "L"]}, u164)
    assert [prof(s, r) for s, r, _ in pbe] == ["B,S | H,L"]
    if pr == F(1, 2):
        assert sorted(prof(s, r) for s, r in bne) == ["B,S | H,L", "S,S | L,L"]
assert all(u164(t, "B", "H")[1] > u164(t, "B", "L")[1] and u164(t, "S", "L")[1] > u164(t, "S", "H")[1]
           for t in "EG")                                                     # dominance per set
print("Tadelis 16.4: p = 1/2 BNE (BS,HL), (SS,LL); unique PBE (BS,HL) for every p "
      "(H dominant after B, L dominant after S)")

# ======================================== 69. MWG 13.C.5 (advertising under a regulated price)
lam, vH, vL, pp = sp.symbols("lambda v_H v_L p", positive=True)
thr = sp.solve(sp.Eq(lam * vH + (1 - lam) * vL, pp), lam)[0]
assert sp.simplify(thr - (pp - vL) / (vH - vL)) == 0
VH, PR, VL, CH, CL = 10, 6, 4, 3, 1
assert thr.subs({pp: PR, vL: VL, vH: VH}) == sp.Rational(1, 3)


def u135(t, A, a):
    v, c = (VH, CH) if t == "H" else (VL, CL)
    return (PR - c - A, v - PR) if a == "buy" else (-A, 0)


ADS = list(range(5))
bne, pbe = signaling({"H": F(1, 2), "L": F(1, 2)}, {"H": ADS, "L": ADS},
                     {A: ["buy", "no"] for A in ADS}, u135)
assert pbe and all(s["H"] == s["L"] for s, _, _ in pbe)                     # pooling only
assert not any(s["H"] != s["L"] for s, _, _ in pbe)
# imitation: low type's gain from copying A_H exceeds the high type's own margin by c_H - c_L
cH, cL, AH, AL = sp.symbols("c_H c_L A_H A_L")
assert sp.simplify((pp - cL - AH) - (pp - cH - AH) - (cH - cL)) == 0
assert all(PR - CL - A > PR - CH - A for A in range(50))
print(f"MWG 13.C.5: buy iff lambda >= (p - v_L)/(v_H - v_L) (= 1/3 in the example); "
      f"{len(pbe)} pure PBE, all pooling, no separating PBE")

# ======================================== 70. Tadelis 16.8 (Beer or Quiche)
def u168(t, m, a):
    pref = 1 if (t, m) in (("S", "B"), ("W", "Q")) else 0
    u1 = pref + (2 if a == "N" else 0)
    u2 = (2 if a == "D" else 1) if t == "W" else (0 if a == "D" else 1)
    return (u1, u2)


bne, pbe = signaling({"W": F(1, 10), "S": F(9, 10)}, {"W": ["B", "Q"], "S": ["B", "Q"]},
                     {"B": ["D", "N"], "Q": ["D", "N"]}, u168)
assert sorted(prof(s, r) for s, r in bne) == ["B,B | N,D", "Q,Q | D,N"]     # replies after B, Q
assert sorted(prof(s, r) for s, r, _ in pbe) == ["B,B | N,D", "Q,Q | D,N"]
for s, r, o in pbe:
    off = "Q" if s["W"] == "B" else "B"
    assert min(o[off]) == F(1, 2) and max(o[off]) == 1                        # Pr(W | off) >= 1/2
dB, dQ = sp.symbols("d_B d_Q")
gainS = (1 + 2 * (1 - dB)) - (0 + 2 * (1 - dQ))
gainW = (0 + 2 * (1 - dB)) - (1 + 2 * (1 - dQ))
assert sp.simplify(gainS - gainW - 2) == 0                                   # Surly gains 2 more
assert sp.simplify(gainS.subs(dQ, sp.solve(gainW, dQ)[0])) == 2              # W indifferent -> S strict


def eq_dominated(t, m, eq):
    """Message m is equilibrium-dominated for type t: eq payoff > best payoff from m."""
    return eq[t] > max(u168(t, m, a)[0] for a in "DN")


eqQ = {"W": 3, "S": 2}                    # pooling on quiche, no duel
eqB = {"W": 2, "S": 3}                    # pooling on beer, no duel
assert eq_dominated("W", "B", eqQ) and not eq_dominated("S", "B", eqQ)
assert u168("S", "B", "N")[0] > eqQ["S"]                                      # S breaks pooling on Q
assert eq_dominated("S", "Q", eqB) and not eq_dominated("W", "Q", eqB)
assert u168("W", "Q", "D")[0] < eqB["W"]                                      # mu(Q)=1 -> duel deters W
print("Tadelis 16.8: BNE = PBE = pooling on beer (D after Q, Pr(W|Q) >= 1/2) and on quiche "
      "(D after B, Pr(W|B) >= 1/2); no separating; quiche fails the intuitive criterion")

print("all G L07 checks passed")
