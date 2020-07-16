# 게시판
for _ in range(int(input())):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    print((x2-x1)*(y2-y1) - (max((min(x2, x4)-max(x1, x3)), 0)*max((min(y2, y4)-max(y1, y3)), 0)))