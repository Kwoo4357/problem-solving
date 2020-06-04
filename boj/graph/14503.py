# 로봇 청소기
n, m, r, c, d = map(int, input().split() + input().split())
room = [list(map(int, input().split())) for _ in range(n)]

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
count = 1
d = 4-d

while True:
    room[r][c] = 2

    for i in range(d - 4, d):
        dr, dc = directions[i]
        if not room[r+dr][c+dc]:
            r += dr
            c += dc
            count += 1
            d = (i+1) % 4
            break

    if room[r][c]:
        dr, dc = directions[(d + 1) % 4]
        if room[r+dr][c+dc] == 1:
            break
        r += dr
        c += dc

print(count)