# 님 게임 3
_, x = int(input()), 0
stones = list(map(int, input().split()))
xor = [x := x ^ i for i in stones][-1]
print(len([1 for s in stones for i in range(s) if not xor^s^i]) if xor else 0)