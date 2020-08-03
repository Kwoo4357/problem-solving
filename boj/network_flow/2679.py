# 맨체스터의 도로
from collections import deque

for _ in range(int(input())):
    n, e, source, sink = map(int, input().split())
    capacity = [[0]*n for _ in range(n)]
    flow = [[0]*n for _ in range(n)]
    adj = [[] for _ in range(n)]

    for _ in range(e):
        u, v, w = map(int, input().split())
        capacity[u][v] += w
        adj[u].append(v)
        adj[v].append(u)

    total, max_route = 0, 0

    while 1:
        prev = [-1]*n
        prev[source] = source
        q = deque([source])

        while q:
            curr = q.popleft()
            for t in adj[curr]:
                if prev[t] < 0 and capacity[curr][t] > flow[curr][t]:
                    q.append(t)
                    prev[t] = curr

                    if t == sink:
                        break

        if prev[sink] < 0:
            break

        curr_flow, route_capacity = 9e9, 9e9

        i = sink
        while i != source:
            curr_flow = min(curr_flow, capacity[prev[i]][i]-flow[prev[i]][i])
            route_capacity = min(route_capacity, capacity[prev[i]][i])
            i = prev[i]

        i = sink
        while i != source:
            flow[prev[i]][i] += curr_flow
            flow[i][prev[i]] -= curr_flow
            i = prev[i]

        total += curr_flow
        max_route = max(max_route, route_capacity)

    print("%.3f"%(total/max_route))
