##뤼카의 정리
이항 계수를 효율적으로 구하는 방법 중 하나?  
수론과 조합론에서 이용

소수 m에 대해서, nCr % m 의 값을 효율적으로 구함

음이 아닌 정수 n, r, 소수 m에 대해 뤼카의 정리는 다음과 같은 합동식  
nCr === prod(n<sub>i</sub>Cr<sub>i</sub>) (0<=i<=k) (mod m)   
위에서 첨자 i가 붙은 것은 n, r을 m진법으로 전개 했을 때의 계수.

Python 코드로 표현하면 다음과 같음.(예를 들어 n, r, m이 각각 200, 100, 17)
```python
n, r, m = 200, 100, 17
result = 1
while n or r:
    result = result * binomial[n % m][r % m] % m
    n //= m
    r //= m
```
낮은 숫자의 이항 계수는 이미 구해져있다고 가정한다.

m이 낮은 문제에서 효율적일듯.