# 220707 / 그리디 / 무지의 먹방 라이브
import heapq

def solution(food_times, k):
    answer = 0
    n = len(food_times)
    sumtimes = sum(food_times)
    if sum(food_times) <= k:
        return -1
    
    q = []
    for i in range(n):
        heapq.heappush(q,(food_times[i],i+1))

    pretime = 0
    sumtime = 0
    while sumtime + (q[0][0] - pretime) * n <= k:
        now = heapq.heappop(q)[0]
        sumtime += (now - pretime) * n
        n -= 1
        pretime = now
                
    result = food_times.sorted(q, ket = lambda x : x[1])
    return result[(k-sumtime) % n]