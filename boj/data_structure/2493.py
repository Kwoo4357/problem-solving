# 탑
n = int(input())
ans = [0]*n
towers = [*map(int, input().split())]
s = []

for i in range(n)[::-1]:
    while s and towers[s[-1]] < towers[i]:
        ans[s.pop()] = i+1
    s.append(i)

print(*ans)