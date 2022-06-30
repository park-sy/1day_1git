# 220206 / 그리디 알고리즘 / 13305 / 주유소
import sys

input = sys.stdin.readline

n = int(input())
l = list(map(int,input().split()))
p = list(map(int,input().split()))

for i in range(1, len(p)):
    if p[i] > p[i-1]:
        p[i] = p[i-1]

p.pop()
a = min(p)

res = 0
for i in range(n-1):
    if p[i] == a:
        res += p[i]*sum(l[i:])
        break
    else:
        res += p[i]*l[i]
    
print(res)