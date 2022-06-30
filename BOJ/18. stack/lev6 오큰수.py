# 220211 / 스택 / 17298 / 오큰수

n = int(input())
nums = list(map(int,input().split()))
nge = []
ans = [-1]*n
nge.append(0)
for i in range(1,n):
    while nge and nums[nge[-1]] < nums[i]:
        ans[nge.pop()] = nums[i]
    nge.append(i)


print(*ans)
