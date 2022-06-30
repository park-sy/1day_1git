# 220531 / 투포인터 / 1450 / 냅색문제
import sys
input = sys.stdin.readline

n,c = map(int,input().split())
s = list(map(int,input().split()))

lw = s[:n//2]
rw = s[n//2:]
ls = []
rs = []
def brute(arr, ans, l, w):
    if l >= len(arr):
        ans.append(w)
        return
    brute(arr,ans,l+1,w)
    brute(arr,ans,l+1,w+arr[l])

def twopointer(arr, target, start, end):
    while start < end: 
        mid = (start + end) // 2 
        if arr[mid] <= target: 
            start = mid + 1 
        else: end = mid 
    return end    

brute(lw, ls, 0, 0) 
brute(rw, rs, 0, 0) 
rs.sort() 

cnt = 0 
for i in ls: 
    if c - i < 0: 
        continue 
    cnt += twopointer(rs, c - i, 0, len(rs)) 
    
print(cnt)