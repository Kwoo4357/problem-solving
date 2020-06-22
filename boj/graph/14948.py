# 군대 탈출하기
from collections import deque

n, m = map(int, input().split())
army = [list(map(int, input().split())) for _ in range(n)]
level = [[[9e9] * m for _ in range(n)] for _ in range(2)]
d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
q = deque()
q.append((0, 0, 0))
level[0][0][0] = army[0][0]

while q:
    jumped, y, x = q.popleft()
    for dy, dx in d:
        i, j = y+dy, x+dx
        if 0 <= i < n and 0 <= j < m and level[jumped][i][j] > max(level[jumped][y][x], army[i][j]):
            q.append((jumped, i, j))
            level[jumped][i][j] = max(level[jumped][y][x], army[i][j])

        i, j = i+dy, j+dx
        if not jumped and 0 <= i < n and 0 <= j < m and level[1][i][j] > max(level[0][y][x], army[i][j]):
            q.append((1, i, j))
            level[1][i][j] = max(level[0][y][x], army[i][j])

print(min(level[0][n-1][m-1], level[1][n-1][m-1]))
