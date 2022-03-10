# 220310 / 투포인터 / 2470 / 두 용액
import sys
n = int(input())
a = list(map(int, input().split()))
a.sort()
srt = 0
end = n-1
id = sys.maxsize
ans = [0,0]


while srt < end:
    if id == 0:
        break
    tmp = a[srt] + a[end] 

    if abs(tmp) < id:
        id = abs(tmp)
        ans[0],ans[1] = a[srt],a[end]
    
    if tmp < 0:
        srt += 1
    else:
        end -= 1
    
print(*ans)