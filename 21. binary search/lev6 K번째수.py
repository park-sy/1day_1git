# 220220 / 이분탐색 / 1300 / K번째 수

n = int(input())
k = int(input())

left, right = 1, k
while left <= right:

    mid = (left + right) // 2

    temp = 0
    for i in range(1,n+1):
        temp += min(mid//i,n)

    if temp >= k:
        ans = mid
        right = mid -1
    else:
        left = mid + 1

print(ans)