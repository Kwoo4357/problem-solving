#공항
import sys
input = sys.stdin.readline


def find(i):
    if i == position[i]:
        return i
    position[i] = find(position[i])
    return position[i]


position = [0] + [i for i in range(1, int(input()) + 1)]
is_docked = [False for _ in range(len(position))]
count = 0

for _ in range(int(input())):
    gi = int(input())
    t = find(gi)
    while is_docked[t]:
        t = find(t-1)
    if not t:
        break
    position[gi] = t
    is_docked[t] = True
    count += 1

print(count)