# 220922 / 야근 지수
import heapq
def solution(n, works):
    answer = 0
    q = []
    
    for i in works:
        heapq.heappush(q,-i)
    
    cnt = 0
    while cnt < n:
        if not q:
            return 0
        w = heapq.heappop(q)
        if w == 0: continue
        heapq.heappush(q,w+1)
        cnt += 1

    for i in q:
        answer += (i**2)
    return answer

