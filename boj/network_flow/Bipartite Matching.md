## 이분 매칭
네트워크 플로우에서 특수한 경우에 사용할 수 있는 방법.  
쉽게 말해서, 두개의 그룹으로 나눠 최대한 많은 매칭을 만드는 알고리즘이다.  

출발 그룹의 요소들은 도착 그룹의 요소들에 대한 후보 리스트를 가지고 있다(인접 리스트와 비슷하게 이해할 수 있을듯)  


```python
def dfs(x, visited):
    visited[x] = 1
    for c in candidate[x]:
        if allocation[c] < 0 or not visited[allocation[c]] and dfs(allocation[c], visited):
            allocation[c] = x
            return 1
    return 0
```

이를 해결하는 간단한 방법으로, 위와 같은 dfs를 이용할 수 있다.  

아이디어를 설명하자면 이미 할당되어 있는 노드가 아니거나, 
할당되어있더라도 해당 노드와 매칭되어 있는 출발 노드가 다른 도착 노드에 연결될 수 있다면 출발 노드를 할당할 수 있다.  

visited는 dfs에서 무한한 사이클을 막기 위해 관리한다.

[BOJ 2188 축사 배정 문제(기초적인 이분 매칭 문제)](2188.py)에서 위와 같은 dfs 방법을 이용해
 기본적인 이분 매칭 문제를 해결하는 코드를 살펴 볼 수 있다.
