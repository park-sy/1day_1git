# 220727 / 입국심사
import sys
def solution(n, times):
    answer = sys.maxsize
    
    left = min(times)
    right = max(times) * n
    
    
    while left <= right:
        mid = (left+right) // 2
        cnt = 0 
        
        for i in times:
            cnt += mid // i

        if cnt < n:
            left = mid + 1
        else:
            answer = min(mid,answer)
            right = mid - 1
            
        
    return answer