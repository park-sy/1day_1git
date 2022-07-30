# 220730 / 징검다리
def solution(distance, rocks, n):

    s = len(rocks)
    rocks.sort()
    
    d = [0] * (s+1)
    pre = 0
    print(rocks)
    for i in range(s+1):
        if i == s: 
            d[i] = distance - pre
        else : 
            d[i] = rocks[i] - pre
            pre = rocks[i]
    print(d)
    left = 0
    right = distance
    target = s + 1 - n
    res = 0
    while left <= right:
        mid = (left+right) // 2
        
        cnt = 0
        l = 0
        for i in range(s+1):
            l += d[i]
            if mid > l: continue
            else:
                cnt += 1
                l = 0
                
        if cnt >= target:
            res = max(res,mid)
            left = mid + 1
        else: 
            right = mid - 1
           
    return res

print(solution(25,[2, 14, 11, 21, 17], 2))