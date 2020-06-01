#다이아몬드 광산
import sys
input = sys.stdin.readline

r, c = map(int, input().split())
mine = [[int(c) for c in input().rstrip()] for _ in range(r)]
rd = [mine[i].copy() for i in range(r)]
ld = [mine[i].copy() for i in range(r)]
ans = max(mine[0])

for i in range(1, r):
    for j in range(c):
        if mine[i][j]:
            rd[i][j] = rd[i-1][j-1] + 1 if j > 0 else rd[i][j]
            ld[i][j] = ld[i-1][j+1] + 1 if j < c-1 else ld[i][j]
            t = min(rd[i][j], ld[i][j])
            temp = max([a+1 for a in range(ans, t) if rd[i-a][j+a] > a and ld[i-a][j-a] > a] + [0]) if t > ans else 0
            ans = max(ans, temp)

print(ans)