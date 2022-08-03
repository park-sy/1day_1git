# 220803 / 1987 / 알파벳
import sys
input = sys.stdin.readline
dx = [0,0,-1,1]
dy = [-1,1,0,0]
n,m = map(int,input().split())
g = []
for _ in range(n):
    g.append(input().rstrip())


ans = 0
alpa = [0] * 26
def dfs(a,b,cnt):
    global ans
    ans = max(ans,cnt)
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
       
        if 0 <= x < n and 0 <= y < m:
            tmp = ord(g[x][y]) - ord("A")
            if not alpa[tmp]:
                alpa[tmp] = 1
                dfs(x,y,cnt+1)
                alpa[tmp] = 0



alpa[ord(g[0][0]) - ord("A")] = 1
dfs(0,0,1)
print(ans)
