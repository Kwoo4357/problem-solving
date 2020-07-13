# 상어의 저녁식사
def dfs(x, visited):
    visited[x] = 1
    for c in candidate[x]:
        if eat[c] < 0 or not visited[eat[c]] and dfs(eat[c], visited):
            eat[c] = x
            return 1
    return 0


n = int(input())
shark_stat = sorted([tuple(map(int, input().split())) for _ in range(n)])
candidate = [[j for j in range(i) if all(si >= sj for si, sj in zip(shark_stat[i], shark_stat[j]))] for i in range(n)]
eat = [-1] * 51

print(n - sum(dfs(i, [0]*n) for i in range(n) for _ in '..'))