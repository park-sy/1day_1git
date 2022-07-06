# 220706 / 그리디 / 곱하기 혹은 더하기

nums = list(map(int,input()))

res = 0

for i in nums:
    res = max(res*i,res+i)

print(res)