import sys
from functools import lru_cache as cache
from collections import deque

with open("D7input.txt") as f:
    D = f.read().strip()

G = [list(row) for row in D.splitlines()]
R = len(G)
C = len(G[0])


for r in range(R):
    for c in range(C):
        if G[r][c] == 'S':
            sr, sc = r, c

def in_bounds(r, c):
    return 0 <= r < R and 0 <= c < C

@cache
def score(r, c):
    if r + 1 == R:
        return 1

    if G[r + 1][c] != '^':
        return score(r + 1, c)

    total = 0
    if in_bounds(r + 1, c - 1):
        total += score(r + 1, c - 1)
    if in_bounds(r + 1, c + 1):
        total += score(r + 1, c + 1)

    return total

p1 = 0
Q = deque([(sr, sc)])
SEEN = set()

while Q:
    r, c = Q.popleft()
    if (r, c) in SEEN:
        continue
    SEEN.add((r, c))

    if r + 1 == R:
        continue

    if G[r + 1][c] == '^':
        # Split point
        if in_bounds(r + 1, c - 1):
            Q.append((r + 1, c - 1))
        if in_bounds(r + 1, c + 1):
            Q.append((r + 1, c + 1))
        p1 += 1
    else:
        Q.append((r + 1, c))

print(p1)

p2 = score(sr, sc)
print(p2)
