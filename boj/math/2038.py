# 골롱 수열
k = int(input())
s, t, i = [0, 1], 1, 1

while i := (i+1):
    if s[t] < i:
        t += 1
    s.append(s[-1]+t)
    if s[-1] >= k:
        break

print(i if k-1 else 1)
