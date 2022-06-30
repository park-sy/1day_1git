# 220505 / 큐,덱 / 5430 / AC
import sys 
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    imp = input().strip()
    n = int(input())
    nums = input().strip()
    nums = deque(list(nums[1:-1].split(',')))
    if 'D' in imp and n == 0:
        print('error')
        continue
    err = False
    rnum = 0
    for i in range(len(imp)):
        if imp[i] == 'D':
            if not nums:
                err = True
                break
            if rnum % 2 == 0:
                nums.popleft()
            else:
                nums.pop()
        else:
            rnum += 1
    nums = list(nums)
    if err:
        print('error')
    else:
        if rnum % 2 == 0:
            print("["+",".join(nums)+"]")
        else:
            print("["+",".join(nums[::-1])+"]")
