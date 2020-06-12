# K번째 수
n, k = int(input()), int(input())
left, right = 1, k

while left <= right:
    mid = (left + right) // 2
    count = sum(mid // i if n > mid // i else n for i in range(1, n+1))
    left, right = (left, mid-1) if count >= k else (mid+1, right)

print(left)