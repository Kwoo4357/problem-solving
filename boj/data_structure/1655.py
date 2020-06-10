from heapq import *
import sys
input = sys.stdin.readline

min_heap, max_heap = [1e9], []
odd = 1

for _ in range(int(input())):
    t = int(input())
    heappush(max_heap if odd else min_heap, -t if odd else t)

    if min_heap[0] < -max_heap[0]:
        temp = -heappop(min_heap)
        heappush(min_heap, -heappop(max_heap))
        heappush(max_heap, temp)

    print(-max_heap[0])
    odd = 1-odd
