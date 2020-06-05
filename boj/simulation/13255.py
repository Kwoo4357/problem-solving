# 동전 뒤집기
n, k = int(input()), int(input())
a = list(map(int, input().split()))
u = n

for i in a:
    u = u*(1-i/n)+(n-u)*(i/n)

print(u)