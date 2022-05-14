# 220514 / 우선순위 큐 / 1655 / 가운데를 말해요
import heapq, sys
input = sys.stdin.readline

lheap = []
rheap = []

n = int(input())
for i in range(n):
    a = int(input())
    if len(lheap) - len(rheap) == 0:
            heapq.heappush(lheap,(-a,a))   
    else:
            heapq.heappush(rheap,(a,a))

    if len(rheap) > 0 and lheap[0][1] > rheap[0][1]:
        l1, l2 = heapq.heappop(lheap)
        r1, r2 = heapq.heappop(rheap)
        heapq.heappush(rheap, (-l1, l2)) 
        heapq.heappush(lheap, (-r1,r2))             

    print(lheap[0][1])