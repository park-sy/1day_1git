# 220311 / 최단경로 / 1860 / 부분합
import sys
n, s = map(int,input().split())
a = list(map(int,input().split()))

srt = 0
end = 0
sum = a[0]
rst = sys.maxsize
while srt < n:
    if end == n - 1:
        if sum >= s:
            if end - srt < rst:
                rst = end - srt
        sum -= a[srt]
        srt += 1
     
    else:            
        if sum >= s:
            if end - srt < rst:
                rst = end - srt
            sum -= a[srt]
            srt += 1
        else:
            end += 1
            sum += a[end]
    
print(0 if rst == sys.maxsize else rst+1)