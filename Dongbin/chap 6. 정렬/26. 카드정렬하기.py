# 220717 / 정렬 / 카드정렬하기
import sys,heapq
input = sys.stdin.readline

n = int(input())
card = []
for i in range(n):
    heapq.heappush(card,int(input()))


res = 0
while n > 1:
    a = heapq.heappop(card)
    b = heapq.heappop(card)
    temp = a+b
    res += temp
    heapq.heappush(card,temp)
    n -= 1

print(res)


# 10 20 30 40 // 30
# 30 30 40 50   // 90
# 60 40 50// 190