# 221011 / 방번호 / 1475
room = list(map(int,input()))

nums = [0] * 10
for i in room:
    nums[i] += 1

nums[9] += nums[6] + 1
nums[6] = 0
nums[9] //= 2

print(max(nums))