"""Checks every number in Resolucao/mini-case-lecture-01.tex (Lecture 1 mini case, slides 31-33).

Two chains pick one of 7 blocks simultaneously; 1 customer per block; customers buy from the
nearest store and split evenly on ties. Run: python Resolucao/mini-case-lecture-01-check.py
"""
from fractions import Fraction as F
from itertools import combinations_with_replacement

N = 7
BLOCKS = range(1, N + 1)


def u(a, b):
    """Customers served by the store at block a when the rival is at block b (brute force)."""
    total = F(0)
    for j in BLOCKS:
        da, db = abs(j - a), abs(j - b)
        total += 1 if da < db else F(1, 2) if da == db else 0
    return total


def u_formula(a, b):
    """Closed form of the solution's equation (1)."""
    if a < b:
        return F(a + b - 1, 2)
    if a == b:
        return F(N, 2)
    return F(2 * N + 1 - a - b, 2)


# (a) closed form and constant sum
for a in BLOCKS:
    for b in BLOCKS:
        assert u(a, b) == u_formula(a, b), (a, b)
        assert u(a, b) + u(b, a) == N
print("(a) matrix u_A(s_A, s_B), rows s_A, columns s_B:")
for a in BLOCKS:
    print(a, [float(u(a, b)) for b in BLOCKS])


def dominates(x, y, rivals):
    """x strictly dominates y against every rival block in `rivals`."""
    return all(u(x, b) > u(y, b) for b in rivals)


# (b) block 1 strictly dominated by block 2; differences shown in the solution
assert dominates(2, 1, BLOCKS)
assert [u(2, b) - u(1, b) for b in BLOCKS] == [F(5, 2), F(5, 2), F(1, 2), F(1, 2), F(1, 2), F(1, 2), F(1, 2)]
best_reply = {b: [a for a in BLOCKS if u(a, b) == max(u(x, b) for x in BLOCKS)] for b in BLOCKS}
assert best_reply[1] == [2] and best_reply[4] == [4]
assert not any(all(dominates(x, y, BLOCKS) for y in BLOCKS if y != x) for x in BLOCKS)
print("(b) best replies:", best_reply)

# (c) IESDS, all strictly dominated (pure) strategies removed each round
S = set(BLOCKS)
rounds = []
while True:
    removed = {y for y in S if any(dominates(x, y, S) for x in S if x != y)}
    if not removed:
        break
    rounds.append(sorted(removed))
    S -= removed
assert rounds == [[1, 7], [2, 6], [3, 5]] and S == {4}
# Each survivor of round k-1 is a best reply to some rival block still alive: not dominated even by mixtures.
assert best_reply[2] == [3] and best_reply[6] == [5] and best_reply[3] == [4]
# Round-3 elimination of 3 needs the rival in {3,4,5}: against 2, block 3 beats 4.
assert u(3, 2) > u(4, 2)
# Round-2 elimination of 2 needs the rival out of block 1: against 1, block 2 beats 3.
assert u(2, 1) > u(3, 1)
print("(c) IESDS rounds removed:", rounds, "survivor:", S, "payoff:", u(4, 4))


def walk(a, b):
    """Total blocks walked when every customer uses the nearer store."""
    return sum(min(abs(j - a), abs(j - b)) for j in BLOCKS)


# (d) welfare
best = min(walk(a, b) for a, b in combinations_with_replacement(BLOCKS, 2))
argmin = [(a, b) for a, b in combinations_with_replacement(BLOCKS, 2) if walk(a, b) == best]
assert best == 6 and argmin == [(2, 5), (2, 6), (3, 6)]
assert walk(4, 4) == 12
assert walk(2, 6) == 6 and u(2, 6) == u(6, 2) == F(7, 2)
assert u(3, 6) == 4 and u(2, 5) == F(3, 1)  # from (2,6), moving inward gains; (2,5) is unequal
print("(d) min total walk:", best, "at", argmin, "; IESDS profile (4,4) walks", walk(4, 4))
print("all checks passed")
