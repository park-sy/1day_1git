# 220207 / 정수론과 조합론 / 2981 / 검문
from re import A
import sys
input = sys.stdin.readline

def gcd(a,b):
    if b > a:
        temp = a
        a = b
        b = temp

    while b>0:
        a,b = b, a%b
    return a
n = int(input())
arr = [0]*n
for i in range(n):
    arr[i]= int(input())
arr.sort()
interval = []
for i in range(1,n):
    interval.append(arr[i]-arr[i-1])

pre = interval[0]
for i in range(1,n-1):
    pre = gcd(pre, interval[i])

ans = []
for i in range(2, int(pre**0.5)+1):
    if pre % i == 0:
        ans.append(i)

ans.append(pre)
for i in ans:
    print(i, end=' ')

