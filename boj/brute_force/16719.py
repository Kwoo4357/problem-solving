# ZOAC

s = input()
n = len(s)
v = [0]*n
while not all(v):
    v[min([x for x in range(n) if not v[x]], key=lambda x: "".join(s[i] for i in range(n) if v[i] or i == x))] = 1
    print("".join(s[i] for i in range(n) if v[i]))