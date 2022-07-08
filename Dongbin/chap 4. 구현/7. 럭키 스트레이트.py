# 220708 / 구현 / 럭키 스트레이트

nums = list(map(int,input()))
n = len(nums)

if sum(nums[:n//2]) == sum(nums[n//2:]):
    print("LUCKY")
else:
    print("READY")

