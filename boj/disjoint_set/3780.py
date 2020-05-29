#네트워크 연결
import sys
input = sys.stdin.readline


def find(i):
    if i == parent[i]:
        return i, 0
    center, cost_sum = find(parent[i])
    parent[i], cost[i] = center, cost_sum + cost[i]
    return parent[i], cost[i]


for _ in range(int(input())):
    parent = [0] + [i for i in range(1, int(input())+1)]
    cost = [0 for _ in range(len(parent))]

    while True:
        command, *args = input().split()
        if command == 'O':
            break

        if command == 'E':
            i = int(*args)
            print(find(i)[1])
        else:
            i, j = map(int, args)
            j_center, j_cost = find(j)
            parent[i], cost[i] = j_center, j_cost + abs(i-j)%1000