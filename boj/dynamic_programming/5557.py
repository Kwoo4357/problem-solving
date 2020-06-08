# 1학년
n = int(input())
numbers = list(map(int, input().split()))

dp = [[0]*41 for _ in range(n)]
dp[0][numbers[0]] = 1

for i in range(1, n):
    ni = numbers[i]
    for j in range(21):
        dp[i][j+ni] += dp[i-1][j]
        dp[i][j-ni] += dp[i-1][j]

print(dp[n-2][numbers[-1]])