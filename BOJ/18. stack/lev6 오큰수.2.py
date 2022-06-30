# 220504 / 스택 / 17298 / 오큰수

n = int(input())
nums = list(map(int,input().split()))

stk = [0]
ans = [-1]*n
for i in range(1,n):
    while stk and nums[stk[-1]] < nums[i]:
        ans[stk.pop()] = nums[i]
    stk.append(i)


print(*ans)
    

