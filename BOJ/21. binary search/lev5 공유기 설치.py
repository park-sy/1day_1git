# 220220 / 이분탐색 / 2110 / 공유기설치
import sys
input = sys.stdin.readline
n ,c = map(int,input().split())
router = []
for i in range(n):
    router.append(int(input().strip()))

router.sort()


start, end = 1, router[n-1]

while 1:

    mid = (start + end)// 2
    if start > end:
        print(mid)
        break
    cnt, id = 1, router[0]
    for i in range(1,n):
        if id + mid <= router[i]:
            cnt += 1
            id = router[i]
            if cnt > c:
                break

    if cnt >= c:
        start = mid + 1
    elif cnt < c:
        end = mid - 1

