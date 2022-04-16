# 220416 / 백트래킹 / 14889 / 스타트와 링크
import sys
input = sys.stdin.readline

n = int(input())

team = []
for _ in range(n):
    team.append(list(map(int,input().split())))

ans = sys.maxsize
visit = [False]*(n)
def dfs(idx, cnt):
    global ans
    if cnt == int(n/2):
        start, link = 0,0
        for i in range(n):
            for j in range(n):
                if visit[i] and visit[j]:
                    start += team[i][j]
                elif not visit[i] and not visit[j]:
                    link += team[i][j]
        ans = min(ans, abs(start-link))

    for i in range(idx,n):
        if visit[i]:
            continue
        visit[i] = True
        dfs(i+1,cnt+1)
        visit[i] = False

dfs(0,0)
print(ans)