# 220128 / 동적계획법1 / 1149 / RGB거리

"""
3 3*2*2 12
4 3*2*2*2 
값이 크면 바로 패스

"""
n = int(input())
cost = []
for i in range(n):
    cost.append(list(map(int, input().split())))



for i in range(1,n):
    cost[i][0] += min(cost[i-1][1],cost[i-1][2])
    cost[i][1] += min(cost[i-1][0],cost[i-1][2])
    cost[i][2] += min(cost[i-1][1],cost[i-1][0])

print(min(cost[n-1][0],cost[n-1][1],cost[n-1][2]))