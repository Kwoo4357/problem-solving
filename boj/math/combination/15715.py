#배열과 gcd
from math import *
from itertools import *
import random


def is_prime(n):
    for d in range(2, int(sqrt(n)) + 1):
        if n % d == 0:
            return False
    return True


def pollard_rho(n):
    if is_prime(n):
        return [n] if n != 1 else []
    if not n % 2:
        return [2] + pollard_rho(n//2)
    x = random.randrange(2, n)
    y = x
    c = random.randrange(1, n)
    d = 1

    while d == 1:
        x = (x ** 2 + c) % n
        y = (y ** 2 + c) % n
        y = (y ** 2 + c) % n
        d = gcd(abs(x - y), n)
        if d == n:
            return pollard_rho(n)

    return pollard_rho(n//d) + pollard_rho(d)


N, num = map(int, input().split())
c = list(map(int, input().split()))
ans = 1

for i in range(1, len(c)):
    if c[i-1] % c[i]:
        ans = 0
        break
    p_set = set(pollard_rho(c[i-1]//c[i]))
    candidate = num // c[i]
    temp = 0
    for r in range(1, len(p_set) + 1):
        t = sum(candidate // prod(combination) for combination in combinations(p_set, r))
        temp += t if r & 1 else -t
    ans = (candidate-temp)*ans % (10**9+7)

print(ans)
