# 221013 / 톱니바퀴 / 14891 
import sys
from collections import deque
input = sys.stdin.readline

cyc = []
for _ in range(4):
    cyc.append(deque(map(int,input().rstrip())))

n = int(input())


def check(num,d):
    rotate = [[num-1,d]]
    d1 = d*-1
    for i in range(num-1,3):
        if cyc[i][2] == cyc[i+1][6]: break
        rotate.append([i+1,d1])
        d1 *= -1
    d2 = d*-1
    for i in range(num-1,0,-1):
        if cyc[i][6] == cyc[i-1][2]: break
        rotate.append([i-1,d2])
        d2 *= -1
    return rotate

for _ in range(n):
    num, d = map(int,input().split())

    rot = check(num,d)
    for num, d in rot:
        if d == 1: cyc[num].appendleft(cyc[num].pop())
        else: cyc[num].append(cyc[num].popleft())

ans = 0
score = [1,2,4,8]
for i in range(4):
    if cyc[i][0] == 1:
        ans += score[i]

print(ans)