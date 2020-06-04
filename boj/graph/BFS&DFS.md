## BFS breadth first search
기준 노드에서 일단 인접 노드를 모두 탐색한 후 다음 노드를 처리 하는 방법.  
Queue 자료구조 이용해서 쉽게 구현할 수 있음.  
1. init으로, Queue에 처음 처리할 노드 삽입
2. Queue에서 pop된 노드를 처리하고 해당 노드의 인접 노드를 모두 큐에 넣음
3. 2를 반복. visited 같은 요소를 관리해서 모두 방문하면 종료.

예시코드로 보면 다음과 같음.
```python
from collections import deque #deque은 양쪽에서 삽입/삭제 가능한 Queue형 자료구조

q = deque([0]) # 시작 노드는 0
visited = [False for _ in range(len(node_list))]

while q: #큐가 빌 때까지
    node = q.popleft() #가장 먼저 삽입된 요소 pop
    visited[node] = True

    for link_node in link_list[node]:
        #link_list는 node의 인접 노드 리스트를 관리하는 2차원 리스트라고 가정
        if not visited[link_node]:
            q.append(link_node)
```
재귀를 사용하지 않기 때문에 일반적으로 dfs 보다 성능이 좋은듯.  

---
## DFS depth first search
DFS는 기준 노드에서 시작해서 하나의 인접 노드를 깊게 탐색한 후 다음 인접노드를 탐색한다.  
연결을 따라 깊게 파고 들어간다고 이해하면 편할듯.  
DFS는 재귀적으로 간단하게 구현할 수 있음.