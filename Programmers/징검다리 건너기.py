# 220829 / 징검다리 건너기

def solution(stones, k):
    start = 0
    end = max(stones)
    
    while start <= end:
        mid = (start + end) //2
        print(start,end,mid)
        cnt = 0
        for t in stones:
            if t <= mid:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break
        if cnt >= k:
            end = mid - 1
        else:
            start = mid + 1
            
    return start