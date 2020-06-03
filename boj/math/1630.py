# 오민식
from math import *


def get_prime_list(n):
    is_prime = [True for _ in range(n + 1)]
    for i in range(2, int(sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i * 2, n + 1, i):
                is_prime[j] = False
    return [i for i in range(2, n + 1) if is_prime[i]]


n = int(input())
p_list = get_prime_list(n)
ans = 1

for p in p_list:
    ans = ans * p**int(log(n, p)) % 987654321

print(ans)