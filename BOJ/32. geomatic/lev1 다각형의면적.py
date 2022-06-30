# 220407 / 기하 / 2166 / 다각형의 면적
import sys
input = sys.stdin.readline

n = int(input())
fig = []
sum1, sum2 = 0,0
for _ in range(n):
    fig.append(list(map(int,input().split())))

for i in range(n):
    if i == n - 1:
        sum1 += fig[i][0]*fig[0][1]
        sum2 += fig[i][1]*fig[0][0]
        break
    sum1 += fig[i][0]*fig[i+1][1]
    sum2 += fig[i][1]*fig[i+1][0]

print(round(0.5*abs(sum1-sum2),1))