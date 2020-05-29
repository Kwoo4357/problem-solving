## Disjoint-set

서로소 집합.  
즉 공통 요소가 없는 집합.  
트리구조를 이용해 find(트리 루트 찾기), union(트리 합치기) 연산을 정의해서 구현한다  
간단하게는 parent 배열(Python에서는 list)을 사용해서 구현 가능  


find 연산을 최적화하는 간단한 방법으로 경로 압축 최적화라는 게 있음.  
이를 수행하면 find 될때마다 부모를 계속 루트로 바꿔주기 때문에 루트까지의 경로(find 연산의 비용)가 짧아지는 기대효과가 있음  
Python 코드로는 다음과 같다
```python
def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x]) #부모를 root로 바꿔줌
    return parent[x]
```

대입연산자가 대입 결과를 반환하는 언어였다면 4~5번 라인들을 축약 가능할텐데..  
Python은 대입 연산자 반환 결과가 None이라서 저렇게 써야하는 것 같다.  
Python에서 대입 연산자가 왜 아무 값도 반환하지 않는지 이유는 아래 stackoverflow 질문에 설명되어 있음.  
<https://stackoverflow.com/questions/4869770/why-does-python-assignment-not-return-a-value>  

비슷한 기능을 하는(대입 결과를 반환하는) 연산자인 :=(walrus operator)는 왜인지 모르겠는데 사용처가 매우 제한되어있다. if, while의 조건문 안에서 사용할 수 있는 정도인듯  
아마 walrus operator가 아무데서나 사용 가능했다면

```python
def find(x):
    return x if parent[x] == x else parent[x] := find(parent[x])
```
정도로 쓸 수도 있었을듯  
물론 이정도로 축약하면 가독성을 오히려 해칠 수도 있다.