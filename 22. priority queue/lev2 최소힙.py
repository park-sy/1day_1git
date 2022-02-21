# 220221 / 우선순위 큐 / 1927 / 최소힙

import heapq, sys
input = sys.stdin.readline
heap = []

n = int(input())
for i in range(n):
    a = int(input())
    if a == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap,a)


