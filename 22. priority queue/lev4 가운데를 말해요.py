# 220221 / 우선순위 큐 / 1655 / 가운데를 말해요
import heapq, sys
input = sys.stdin.readline
lheap = []
rheap = []

n = int(input())
for i in range(n):
    a = int(input())
    if i == 0:
        heapq.heappush(lheap,(-a,a))
    elif i == 1:
        if  a < lheap[0][1]:
            a1, a2 = heapq.heappop(lheap)
            heapq.heappush(rheap,(-a1, a2))
            heapq.heappush(lheap,(-a,a))
        else:
            heapq.heappush(rheap,(a,a))
    else:
        if len(lheap) - len(rheap) == 0:
            if a > rheap[0][1]:
                (a1, a2) = heapq.heappop(rheap)
                heapq.heappush(lheap,(-a1, a2))
                heapq.heappush(rheap,(a,a))
            else:
                heapq.heappush(lheap,(-a,a))
            
        else:
            if a < lheap[0][1]:
                a1, a2 = heapq.heappop(lheap)
                heapq.heappush(rheap,(-a1, a2))
                heapq.heappush(lheap,(-a,a))
            else:
                heapq.heappush(rheap,(a,a))            

    print(lheap[0][1])



