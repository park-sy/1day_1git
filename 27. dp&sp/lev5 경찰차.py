# 220317 / dp&sp / 2618 / 경찰차
import sys
input = sys.stdin.readline

n = int(input())
w = int(input())
road = [[0 for _ in range(n+1)] for _ in range(n+1)]

pr1,pc1 = 1,1
pr2,pc2 = n,n
ord = []
sum = 0
for i in range(w):
    r,c = map(int,input().split())
    d1 = abs(pr1-r) + abs(pc1-c)
    d2 = abs(pr2-r) + abs(pc2-c)  
    if d1 < d2:
        ord.append(1)
        sum += d1
        pr1, pc1 = r, c
    else:
        ord.append(2)
        sum += d2
        pr2, pc2 = r, c

print(sum)
for i in range(w):
    print(ord[i])

        