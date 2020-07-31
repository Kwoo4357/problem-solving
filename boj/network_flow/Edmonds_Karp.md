### 에드몬드-카프 알고리즘

BFS 방식으로 네트워크 플로우 문제를 푸는 방법.

쉽게 생각하면 플로우가 흐를 수 있는 용량이 남은 경로로 계속 flow를 흘려보내서,
 최종적으로 Source에서 Sink로 도착하는 flow가 최대가 되도록 하는 방법이라고 할 수 있다.
 
 [BOJ 6086 최대유량](6086.py) 문제는 network flow에서 최대 유량을 찾는 가장 기본적인 형태인데, 
 이 문제를 푸는 에드몬드-카프 알고리즘은 다음과 같은 코드로 구현 가능하다.
 
 ```python
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
```

위에서 source, sink 변수와 flow, capacity, adj 리스트는 미리 정의되어있다고 가정한다.  

BFS 안쪽에선 아직 경로가 닿지 않았고, 남은 용량이 있는 노드를 찾아 간선을 탐색한다.  
이후 sink까지 탐색이 완료되면 경로 한개를 완성 시키고 BFS를 종료한다.
즉, BFS 한번에 경로 한 개가 찾아진다.  
BFS가 종료되면 찾은 경로를 거꾸로 따라가면서 남은 용량이 가장 적은 간선을 기준으로 flow를 흘려보낸다.  
이 과정을 더 이상 sink에 닿는 경로를 찾을 수 없을 때까지 반복한다.