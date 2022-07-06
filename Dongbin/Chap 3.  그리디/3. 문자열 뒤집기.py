# 220706 / 그리디 / 문자열 뒤집기

nums = list(map(int,input()))

cnt = [0,0]

cnt[nums[0]] = 1

for i in range(1,len(nums)):
    pre = nums[i-1]
    now = nums[i]
    if now != pre:
        cnt[now] += 1

print(min(cnt))
        
