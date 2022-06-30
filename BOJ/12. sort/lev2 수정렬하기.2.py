# 220614 / 정렬 / 2751 / 수 정렬하기
import sys, heapq
input = sys.stdin.readline

def swap(a,b):
    temp = nums[a]
    nums[a] = nums[b]
    nums[b] = temp
    return a

def adjust(root,b):
    tmp = nums[root]
    child = root*2
    while child <= b:
        if child < b and nums[child] < nums[child+1]:
            child += 1
        if nums[root] > nums[child]:
            break
        else:
            nums[child//2] = nums[child]
            child *= 2
    nums[child//2] = tmp

n = int(input())
nums = [0]
for i in range(n):
    heapq.heappush(nums,int(input()))

for i in range(n-1 ,0, -1):
    print(swap(1, i+1))
    adjust(1,i)
