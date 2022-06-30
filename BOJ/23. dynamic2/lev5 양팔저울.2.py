# 220519 /  dp2 / 2629 / 양팔저울
import sys
input = sys.stdin.readline

n = int(input())
chu = [0]+list(map(int,input().split()))
m = int(input())
chk = [0]+list(map(int,input().split()))

dp = [[0]*(501*i) for i in range(n)]
possible = []

def dfs(now, left, right):
    new = abs(left- right)

    if new not in possible:
        possible.append(new)
    
    if now == n:
        return

    if dp[now][new] == 0:
        dfs(now + 1, left + chu[now], right)
        dfs(now + 1, left, right + chu[now])
        dfs(now + 1, left, right)
        dp[now][new] = 1

dfs(0,0,0)
for i in chk:
    if i in possible:
        print('Y', end=' ')
    else:
        print('N', end=' ')
