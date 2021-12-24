import heapq
import sys
input = sys.stdin.readline
n = int(input())
heap = []
for _ in range(n):
    a = int(input())
    if a == 0:
        if len(heap) != 0:
            print(heapq.heappop(heap) * (-1))
        else:
            print(0)
    else:
        heapq.heappush(heap, a * (-1))
