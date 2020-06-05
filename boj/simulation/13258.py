# 복권 + 은행
n = int(input())
kang, *rest = map(int, input().split())
rest = sum(rest)
j, c = int(input()), int(input())

for _ in range(c):
    cash = kang+rest
    kang += j*kang/cash
    rest += j*rest/cash

print(kang)