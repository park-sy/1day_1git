# 220702 / 이진탐색 / 부품찾기

n = int(input())
l = list(map(int,input().split()))
m = int(input())
d = list(map(int,input().split()))

l.sort()

def binarysearch(num):
    left = 0
    right = n-1
    
    while left <= right:
        middle = (left + right) // 2
        if l[middle] == num:
            return True
        elif l[middle] < num:
            left = middle + 1
        else:
            right = middle - 1

    return False

for i in d:
    if binarysearch(i):
        print('yes', end = ' ')
    else:
        print('no', end = ' ')
