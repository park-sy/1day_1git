# 220703 / 이진탐색 / 떡볶이 떡 만들기
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
dd = list(map(int,input().split()))

result = 0
start = 0
end = max(dd)
while start <= end:
    mid = (start+end) // 2
    res = 0
    for i in dd:
        if i > mid:
            res += i - mid
    if res < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1


print(result)