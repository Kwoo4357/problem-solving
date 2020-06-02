#캔디 분배
for _ in range(int(input())):
    k, c = map(int, input().split())
    try:
        ans = k+1 if c == 1 or k == 1 else pow(c, -1, k)
        print(ans if ans <= 1e9 else "IMPOSSIBLE")
    except:
        print("IMPOSSIBLE")