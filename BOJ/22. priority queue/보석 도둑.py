# 220720 / 힙 / 보석도둑
import sys, heapq
input = sys.stdin.readline

n, m = map(int,input().split())
bag = []
jew = []
for _ in range(n):
    w,v = map(int,input().split())
    jew.append([w,v])


for _ in range(m):
    bag.append(int(input()))
jew.sort()
bag.sort()

hq = []
res = 0
for i in range(m):
    while jew and bag[i] >= jew[0][0]:
        heapq.heappush(hq,(-jew[0][1]))
        heapq.heappop(jew)

    if hq:
        v= heapq.heappop(hq)
        res -= v
    elif not jew: break

print(res)
