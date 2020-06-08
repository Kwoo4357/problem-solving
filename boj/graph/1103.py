# 게임
from functools import lru_cache
import sys
sys.setrecursionlimit(9**9)


@lru_cache(maxsize=2048)
def dfs(x, y):
    if board[y][x] == 'H':
        return 0
    if (y, x) in visited:
        print(-1)
        exit()

    visited.append((y, x))
    d = board[y][x]
    result = max(dfs(x+dx, y+dy) if 0 <= x+dx < m and 0 <= y+dy < n else 0 for dx, dy in [(d, 0), (-d, 0), (0, d), (0, -d)])
    visited.pop()
    return 1 + result


n, m = map(int, input().split())
board = [[int(c) if c != 'H' else 'H' for c in input()] for _ in range(n)]
visited = []
print(dfs(0, 0))