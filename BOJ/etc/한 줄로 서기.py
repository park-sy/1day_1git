# 221014 / 한 줄로 서기 / 1138
import sys
input = sys.stdin.readline

n = int(input())
nl = list(map(int,input().split()))

sol = [0]*n

for i in range(n):
    temp = nl[i]
    cnt = 0
    now = 0
    
    while cnt < temp:
        if sol[now] == 0: cnt += 1
        now += 1
    while sol[now] != 0:
        now += 1
    sol[now] = i + 1


print(*sol)
