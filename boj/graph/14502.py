# 연구소
from collections import deque
from itertools import combinations

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
ans = 0

for walls in combinations([(i, j) for i in range(n) for j in range(m) if not lab[i][j]], 3):
    lab_copy = [lab[i].copy() for i in range(n)]
    q = deque((i, j) for i in range(n) for j in range(m) if lab_copy[i][j] == 2)

    while q:
        i, j = q.popleft()
        for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            y, x = i+di, j+dj
            if 0 <= y < n and 0 <= x < m and not lab_copy[y][x] and (y, x) not in walls:
                lab_copy[y][x] = 2
                q.append((y, x))

    ans = max(ans, sum(1 for i in range(n) for j in range(m) if not lab_copy[i][j]))

print(ans-3)