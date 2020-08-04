# 재미있는 숫자 놀이
from collections import deque
from math import gcd

n, k = map(int, input().split())
c = sorted(list(map(int, input().split())))
ans = 0
q = deque((c[i], 1, i) for i in range(k))

while q:
    p, ea, i = q.popleft()
    if p > n:
        continue
    ans += n//p if ea&1 else -(n//p)

    for j in range(i+1, k):
        q.append((p*c[j]//gcd(p, c[j]), ea+1, j))

print(ans)
