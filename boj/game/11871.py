# 님 게임 홀짝
_, x = int(input()), 0
stones = [(s+1)//2 if s & 1 else (s-1)//2 for s in map(int, input().split())]
xor = [x := x ^ i for i in stones][-1]
print("koosaga" if xor else "cubelover")