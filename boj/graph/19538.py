# 루머
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
near = [[]] + [list(map(int, input().split()[:-1])) for _ in range(n)]
input()
q = deque(list(map(int, input().split())))
rumor = [[] for _ in range(n + 1)]
ans = [-1]*(n+1)
yet = [1]*(n+1)

for a in q:
    yet[a] = 0
    ans[a] = 0

while q:
    i = q.popleft()
    for t in near[i]:
        rumor[t].append(ans[i])
        if yet[t] and len(rumor[t]) >= len(near[t])/2:
            q.append(t)
            yet[t] = 0
            ans[t] = max(rumor[t]) + 1

print(*ans[1:])