# 220213 / 큐,덱 / 1021 / 회전하는큐
import sys
input = sys.stdin.readline
def locr(arr, loc, n):
    cnt = 0
    while True:
        if arr[loc] == n:
            return cnt, loc
        cnt+= 1
        loc += 1
        if loc == len(arr):
            loc = 0

def locl(arr, loc, n):
    cnt = 0
    while True:
        if arr[loc] == n:
            return cnt, loc
        cnt += 1
        loc -= 1
        if loc < 0:
            loc = len(arr) -1



n, m = map(int, input().split())
ord = list(map(int, input().split()))
arr = [i for i in range(1,n+1)]
cnt = 0
loc = 0
for i in ord: # 2 9 5
    left, l = locl(arr,loc,i)
    right, r = locr(arr, loc, i)
    if left < right:
        cnt += left
        loc = l
        arr.pop(loc)
        if loc == len(arr):
            loc = 0

    else: 
        cnt+= right
        loc = r
        arr.pop(loc)
        if loc == len(arr):
            loc = 0

    
print(cnt)