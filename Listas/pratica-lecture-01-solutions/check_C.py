"""Checks the proof and auction items: 11 (Tadelis 4.1), 12 (Tadelis 4.2), 20 (MWG 8.B.4),
22 (MWG 8.B.7), 23 (MWG 8.B.3), 24 (Tadelis 4.4). Proofs get randomized sanity checks on
finite games; auction claims are checked exhaustively on bid grids.

Run: python check_C.py  -> prints "all C checks passed" or fails on the first wrong claim.
"""
import random
from fractions import Fraction as F
from itertools import product

random.seed(20261013)


def rand_game(n1, n2, lo=0, hi=4):
    return [[(random.randint(lo, hi), random.randint(lo, hi)) for _ in range(n2)] for _ in range(n1)]


def pay(G, i, r, c):
    return G[r][c][i]


def beats(G, i, a, b, R, C, strict=True):
    """Does strategy a of player i beat b given the opponent's set (strictly / '>=' everywhere)?"""
    opp = C if i == 0 else R
    cell = (lambda s, o: pay(G, 0, s, o)) if i == 0 else (lambda s, o: pay(G, 1, o, s))
    d = [cell(a, o) - cell(b, o) for o in opp]
    return all(x > 0 for x in d) if strict else all(x >= 0 for x in d)


def dominated_set(G, i, R, C):
    own = R if i == 0 else C
    return {b for b in own if any(beats(G, i, a, b, R, C) for a in own if a != b)}


def iesds_max(G):
    R, C = set(range(len(G))), set(range(len(G[0])))
    while True:
        d0, d1 = dominated_set(G, 0, R, C), dominated_set(G, 1, R, C)
        if not d0 and not d1:
            return R, C
        R, C = R - d0, C - d1


def iesds_random_order(G):
    """Delete a random nonempty subset of currently dominated strategies of one random player."""
    R, C = set(range(len(G))), set(range(len(G[0])))
    while True:
        d = [dominated_set(G, 0, R, C), dominated_set(G, 1, R, C)]
        movers = [i for i in (0, 1) if d[i]]
        if not movers:
            return R, C
        i = random.choice(movers)
        pick = set(random.sample(sorted(d[i]), random.randint(1, len(d[i]))))
        if i == 0:
            R = R - pick
        else:
            C = C - pick


# ---- item 11 (Tadelis 4.1) and slide 29: a strict dominant-strategy equilibrium is the only
# dominant-strategy equilibrium (even with the '>=' notion of weak dominance) and the only
# IESDS survivor.
found = 0
for _ in range(20000):
    n1, n2 = random.choice([(2, 2), (2, 3), (3, 2)])
    G = rand_game(n1, n2)
    R, C = set(range(n1)), set(range(n2))
    sd = [[a for a in (R if i == 0 else C) if all(beats(G, i, a, b, R, C) for b in (R if i == 0 else C) if b != a)]
          for i in (0, 1)]
    if sd[0] and sd[1]:
        found += 1
        wd = [[a for a in (R if i == 0 else C) if all(beats(G, i, a, b, R, C, strict=False) for b in (R if i == 0 else C))]
              for i in (0, 1)]
        assert wd == sd                       # no other weakly dominant strategy exists
        assert iesds_max(G) == ({sd[0][0]}, {sd[1][0]})
assert found > 100

# ---- item 12 (Tadelis 4.2)
MP = [[(1, -1), (-1, 1)], [(-1, 1), (1, -1)]]  # matching pennies
for i in (0, 1):
    assert not any(all(beats(MP, i, a, b, {0, 1}, {0, 1}, strict=False) for b in (0, 1)) for a in (0, 1))
EX = [[(2, 3), (0, 1)], [(2, 1), (0, 0)]]      # rows U, D; columns L, R (example in item12)
wd1 = [a for a in (0, 1) if all(beats(EX, 0, a, b, {0, 1}, {0, 1}, strict=False) for b in (0, 1))]
assert wd1 == [0, 1]                           # both U and D are weakly dominant ('>=' sense)
assert beats(EX, 1, 0, 1, {0, 1}, {0, 1})      # L strictly dominates R for player 2
assert EX[0][0][1] > EX[1][0][1]               # player 2 prefers (U, L) to (D, L)
# under the lecture's definition (>= everywhere, > somewhere) a player has at most one
# weakly dominant strategy: two would each have to beat the other strictly somewhere
for _ in range(20000):
    G = rand_game(3, 2, 0, 2)
    R, C = {0, 1, 2}, {0, 1}
    lect = [a for a in R if all(beats(G, 0, a, b, R, C, strict=False)
                                and any(G[a][c][0] > G[b][c][0] for c in C) for b in R if b != a)]
    assert len(lect) <= 1

# ---- item 20 (MWG 8.B.4): every deletion order ends at the same set (finite games)
for _ in range(3000):
    G = rand_game(random.randint(2, 5), random.randint(2, 5), 0, 6)
    target = iesds_max(G)
    for _ in range(5):
        assert iesds_random_order(G) == target
# weak deletion is order dependent (Munoz-Garcia Ex. 16 game, item 19): two different end sets
W = [[(2, 1), (1, 1), (0, 0)], [(1, 2), (3, 1), (2, 1)], [(2, -2), (1, -1), (-1, -1)]]


def wdominated(G, i, R, C):
    own = R if i == 0 else C
    opp = C if i == 0 else R
    cell = (lambda s, o: pay(G, 0, s, o)) if i == 0 else (lambda s, o: pay(G, 1, o, s))
    return {b for b in own for a in own if a != b
            and all(cell(a, o) >= cell(b, o) for o in opp) and any(cell(a, o) > cell(b, o) for o in opp)}


ends = set()
for _ in range(400):
    R, C = {0, 1, 2}, {0, 1, 2}
    while True:
        d = [wdominated(W, 0, R, C), wdominated(W, 1, R, C)]
        movers = [i for i in (0, 1) if d[i]]
        if not movers:
            break
        i = random.choice(movers)
        s = random.choice(sorted(d[i]))
        R, C = (R - {s}, C) if i == 0 else (R, C - {s})
    ends.add((frozenset(R), frozenset(C)))
assert (frozenset({0}), frozenset({0})) in ends                       # (U, L)
assert (frozenset({0, 1, 2}), frozenset({0, 1})) in ends              # six profiles

# ---- item 22 (MWG 8.B.7): a mixture never beats every pure strategy in its support
for _ in range(20000):
    k = random.randint(2, 4)
    payoffs = [random.randint(-5, 5) for _ in range(k)]       # u_i(s^j, s_-i), j in support
    wts = [random.randint(1, 9) for _ in range(k)]
    mix = F(sum(w_ * p for w_, p in zip(wts, payoffs)), sum(wts))
    assert mix <= max(payoffs) and not all(mix > p for p in payoffs)

# ---- item 23 (MWG 8.B.3): second-price auction, bids on a grid, random tie-break
def spa(v, b, others):
    """Expected payoff of bidder with value v and bid b against the other bids (list)."""
    h = max(others)
    if b > h:
        return F(v - h)
    if b < h:
        return F(0)
    ties = 1 + sum(o == h for o in others)
    return F(v - h, ties)


bids = range(0, 9)
for n_others in (1, 2):
    profiles = list(product(bids, repeat=n_others))
    for v in (0, 3, 8):
        for b in bids:
            if b == v:
                continue
            d = [spa(v, v, o) - spa(v, b, o) for o in profiles]
            assert all(x >= 0 for x in d) and any(x > 0 for x in d)   # v weakly dominates b
        wd = [b for b in bids if all(spa(v, b, o) >= spa(v, c, o) for c in bids for o in profiles)]
        assert wd == [v]                                              # unique weakly dominant bid

# ---- item 24 (Tadelis 4.4): proxy bidding, two bidders, rival's highest proxy h
# (i) increment -> 0: price = h, which is the second-price auction above.
# (ii) bids in cents, increment one cent, price = min(own proxy, h + 1), random tie-break.
def proxy(v, b, h):
    if b > h:
        return F(v - min(b, h + 1))
    if b < h:
        return F(0)
    return F(v - b, 2)


v = 1000
H = range(990, 1011)
for b in range(990, 1011):
    d = [proxy(v, v, h) - proxy(v, b, h) for h in H]
    if b > v:
        assert all(x >= 0 for x in d) and any(x > 0 for x in d)      # (a) holds exactly
    if b <= v - 3:
        assert all(x >= 0 for x in d) and any(x > 0 for x in d)      # (b) holds for b <= v - 3 cents
d = [proxy(v, v - 1, h) - proxy(v, v, h) for h in H]
assert all(x >= 0 for x in d) and max(d) == F(1, 2)                   # v - 1 cent weakly beats v
assert [proxy(v, v - 2, h) for h in H] == [proxy(v, v, h) for h in H] # v - 2 cents is equivalent
assert all(proxy(v, v, h) == 0 for h in range(v - 1, 1011))           # truthful bid earns 0 once h >= v - 1

print("all C checks passed")
