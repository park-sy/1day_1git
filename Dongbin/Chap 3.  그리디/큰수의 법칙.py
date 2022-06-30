# 220630 / 그리디 / 큰수의 법칙
import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
nums = list(map(int,input().split()))

nums.sort(reverse=True)
res = 0

for i in range(m):
    if i % k == 1 and i != 1:
        res += nums[1]
    else: res += nums[0]   
print(res)