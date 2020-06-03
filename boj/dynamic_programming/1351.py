# 무한 수열
from functools import lru_cache

n, p, q = map(int, input().split())


@lru_cache
def a(i):
    if i == 0:
        return 1
    return a(i//p)+a(i//q)


print(a(n))