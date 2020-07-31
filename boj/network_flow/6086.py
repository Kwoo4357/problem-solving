# 최대 유량
from collections import deque

size = 130
capacity = [[0]*size for _ in range(size)]
flow = [[0]*size for _ in range(size)]
adj = [[] for _ in range(size)]

for _ in range(int(input())):
    a, b, c = input().split()
    a, b, c = ord(a), ord(b), int(c)
    capacity[a][b] += c
    capacity[b][a] += c
    adj[a].append(b)
    adj[b].append(a)

ans = 0
source = ord('A')
sink = ord('Z')

while 1:
    prev = [-1]*size
    q = deque([source])

    while q:
        curr = q.popleft()
        for after in adj[curr]:
            if prev[after] < 0 and capacity[curr][after] > flow[curr][after]:
                q.append(after)
                prev[after] = curr

                if after == sink:
                    break

    if prev[sink] < 0:
        break

    i = sink
    curr_flow = 9e9
    while i != source:
        curr_flow = min(curr_flow, capacity[prev[i]][i]-flow[prev[i]][i])
        i = prev[i]

    i = sink
    while i != source:
        flow[prev[i]][i] += curr_flow
        flow[i][prev[i]] -= curr_flow
        i = prev[i]

    ans += curr_flow

print(ans)
