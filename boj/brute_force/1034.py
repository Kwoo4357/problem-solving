# 램프
from collections import Counter

n, _ = map(int, input().split())
lamp = [tuple(i for c, i in zip(input(), range(50)) if c == '0') for _ in range(n)]
k = int(input())
ans = 0

while k >= 0:
    ans = max(ans, max(Counter([a for a in lamp if len(a) == k]).values() or [0]))
    k -= 2

print(ans)
