# 큰 수
from math import *
for _ in range(int(input())):
    x = int(input())
    print(int(x*log10(x/e)+log10(2*pi*x)/2)+1)
