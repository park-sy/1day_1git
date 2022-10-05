n,m = map(int,input().split())

arr = list(map(int,input().split()))

start = 0
end = max(arr)

while start <= end:
    mid = (start+end)//2

    cnt = 0
    for i in arr:
        cnt += max(0,i-mid)
    if cnt < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1


from bisect import bisect_left, bisect_right

arr = []
target = 1
a = bisect_left(arr, target)
b = bisect_right(arr,target)
print(b-a)

import heapq
def solution(stones, k):
    answer = 0
    n = len(stones)
    start = 0
    end = max(stones)
    
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        possible = True

        for i in range(n):
            if stones[i] < mid:
                cnt += 1
                if cnt >= k:
                    possible = False
                    break
            else:
                cnt = 0
                
        if possible:
            answer = mid
            start = mid + 1
        else:
            end = mid -1
            
    return answer