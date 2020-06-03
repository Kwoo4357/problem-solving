# 이항 계수 4
n, k, mod = map(int, input().split())
c = [[0 for _ in range(mod + 1)] for _ in range(mod + 1)]
ans = 1

for i in range(mod):
    c[i][0] = 1
    for j in range(1, i + 1):
        c[i][j] = (c[i - 1][j - 1] + c[i - 1][j]) % mod

while n or k:
    ans = ans * c[n % mod][k % mod] % mod
    n //= mod
    k //= mod

print(ans)