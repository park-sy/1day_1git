# 220404 / 트리에서 동적 계획법 / 2213 / 트리의 독립집합
import sys
input = sys.stdin.readline

n = int(input())
wei = [0] + list(map(int,input().split()))
graph = [[]for _ in range(n+1)]
dp = [[0,0] for _ in range(n+1)]
visit = [False for _ in range(n+1)]

for _ in range(n-1):
    n1,n2 = map(int,input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)


def dfs(start):
    visit[start] = True
    dp[start][0] = wei[start]
    dp[start][1] = 0
    for i in graph[start]:
        if not visit[i]:
            dfs(i)
            dp[start][0] += dp[i][1]
            dp[start][1] += max(dp[i][0],dp[i][1])

trace_result=[]
trace_check = [False for _ in range(n+1)]
def Trace(cur,pre):
    trace_check[cur]= True
 
    if pre==0:
        for i in graph[cur]:#현재노드는 포함할수없음
            if not trace_check[i]:
                Trace(i,1)
    else:#이전노드가 포함되어있지않다면
        if dp[cur][0] > dp[cur][1]:  # 현재노드를 포함한 부분이 더크다면
            trace_result.append(cur)  # 현재노드 포함
            for i in graph[cur]:
                if not trace_check[i]:
                    Trace(i, 0)
        else:  # 현재노드를 포함하지 않은부분이 크다면
            for i in graph[cur]:
                if not trace_check[i]:
                    Trace(i, 1)

dfs(1)
print(max(dp[1][0],dp[1][1]))
Trace(1,1)
trace_result.sort()
print(*trace_result)