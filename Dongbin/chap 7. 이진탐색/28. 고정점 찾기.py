# 220719 / 이진탐색 / 고정점 찾기
n = int(input())
nums = list(map(int,input().split()))


left = 0
right = n
res = 0
while left <= right:
    mid = (left + right) // 2
    temp = nums[mid]
    if temp == mid:
        res = mid
        break
    elif temp < mid:
        left = mid + 1
    else:
        right = mid - 1

print(res)