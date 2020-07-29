# 루머
import sys
from collections import deque

input = sys.stdin.readline
f = lambda x: int(x)-1

n = int(input())
near = [list(map(f, input().split()[:-1])) for _ in range(n)]
input()
q = deque(list(map(f, input().split())))

rumor = [0]*n
ans = [-1]*n
for a in q:
    ans[a] = 0

while q:
    i = q.popleft()
    for t in near[i]:
        rumor[t] += 1
        if ans[t] < 0 and rumor[t] >= len(near[t])/2:
            q.append(t)
            ans[t] = ans[i]+1

print(*ans)