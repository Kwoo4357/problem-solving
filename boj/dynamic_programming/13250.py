# 주사위 게임
dp = [0.]*(10**6+8)
ex_six = 0

for i in range(1, int(input()) + 1):
    dp[i] = ex_six/6 + 1.
    ex_six = ex_six - dp[i-6] + dp[i]

print(max(dp))
