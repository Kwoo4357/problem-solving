# 방 번호
n = int(input())
cost = list(map(int, input().split()))
dp = ['0']*(int(input())+1)

for i in range(n)[::-1]:
    c = cost[i]
    for b in range(c, len(dp)):
        dp[b] = dp[b-c]+str(i) if int(dp[b]) <= int(dp[b-c]+str(i)) else dp[b]

print(int(dp[-1]))
