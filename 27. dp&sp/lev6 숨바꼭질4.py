# 220603 / dp&sp / 13913 / 숨바꼭질 4
from collections import deque

n,m = map(int,input().split())

dp = [0]*(100001)
move = [0]*(100001)
def path(x):
    arr = []
    temp = x
    for _ in range(dp[x]+1):
        arr.append(temp)
        temp = move[temp]
    print(*arr[::-1])

def bfs(start):
    q = deque([start])

    while q:
        x = q.popleft()
        if x == m:
            print(dp[x])
            path(x)
            return 
        for i in (x+1, x-1, x*2):
            if 0<=i<=100000 and dp[i]==0:
                q.append(i)
                dp[i] = dp[x] + 1
                move[i] = x
        


bfs(n)
