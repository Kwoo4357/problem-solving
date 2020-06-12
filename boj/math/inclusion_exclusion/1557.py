# 제곱 ㄴㄴ
from collections import deque


def in_ex(n):
    result = 0
    q = deque((sq_prime[i], 1, i) for i in range(len(sq_prime)) if sq_prime[i] <= n)

    while q:
        p, ea, i = q.popleft()
        result += n//p if ea & 1 else -(n//p)

        for j in range(i+1, len(sq_prime)):
            if p*sq_prime[j] > n:
                break
            q.append((p*sq_prime[j], ea+1, j))

    return result


LIMIT = int(10**5)+2
isprime = [True for i in range(LIMIT)]
sq_prime = []
k = int(input())

for i in range(2, LIMIT):
    if isprime[i]:
        sq_prime.append(i**2)
        for j in range(i**2, LIMIT, i):
            isprime[j] = False

left, right = 1, 2*k
while left <= right:
    mid = (left+right)//2
    c = mid-in_ex(mid)
    left, right = (left, mid-1) if c >= k else (mid+1, right)

print(left)