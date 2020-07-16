# 행렬식과 GCD
from math import *

n = int(input())
fi = [0, 1]
for _ in range(10**5):
    fi.append((fi[-1]+fi[-2])%(10**9+7))
print(sum(fi[gcd(i+2, n+1)] for i in range(n))%(10**9+7))