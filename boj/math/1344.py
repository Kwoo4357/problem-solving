# 축구
from math import comb

a, b = int(input())/100, int(input())/100
np = [0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18]
a = sum(a**i * (1-a)**(18-i) * comb(18, i) for i in np)
b = sum(b**i * (1-b)**(18-i) * comb(18, i) for i in np)

print(1 - a*b)
