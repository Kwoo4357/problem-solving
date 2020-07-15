# 소수 쌍
def dfs(x, v):
    v[x] = 1
    for t in a[x]:
        if d[t] < 0 or not v[d[t]] and dfs(d[t], v):
            d[t] = x
            return 1
    return 0


is_p = [1]*2001
for i in range(2, 50):
    if is_p[i]:
        for j in range(i*i, 2001, i):
            is_p[j] = 0

n = int(input())
s = list(map(int, input().split()))
a = [[j for j in range(n) if is_p[s[i]+s[j]]] for i in range(n)]
ans = []

for _ in range(len(a[0])):
    d = [-1]*51
    if all(dfs(i, [0]*51) for i in range(n)):
        ans.append(s[d.index(0)])
        a[0].remove(d.index(0))

print(*sorted(ans or [-1]))