# 축사 배정
def dfs(x, visited):
    visited[x] = 1
    for w in want[x]:
        if allocation[w] < 0 or not visited[allocation[w]] and dfs(allocation[w], visited):
            allocation[w] = x
            return 1
    return 0


n = int(input().split()[0])
allocation = [-1]*(n+1)
want = [list(map(int, input().split()[1:])) for _ in range(n)]
print(sum(dfs(i, [0]*n) for i in range(n)))