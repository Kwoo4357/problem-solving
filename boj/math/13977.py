#이항계수와 쿼리
import sys
input = sys.stdin.readline

mod = 10**9+7
fact = [1, 1]
for i in range(2, 4000001):
    fact.append(fact[-1]*i%mod)

for i in range(int(input())):
    n, r = map(int, sys.stdin.readline().split())
    print((fact[n] * pow(fact[r]*fact[n-r], mod-2, mod)) % mod)