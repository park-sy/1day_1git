# 220919 / 단어 변환 1
from collections import defaultdict
import sys
INF = sys.maxsize
def solution(begin, target, words):
    global answer
    answer = INF
    d = defaultdict(list)
    visit = {}
    words.append(begin)
    for i in words:
        visit[i] = 0
        for j in words:
            if i == j: continue
            if check(i,j) == 1:
                d[i].append(j)        
    
    def dfs(now,cnt):
        global answer
        if now == target:
            answer = min(answer,cnt)
        for next in d[now]:
            if not visit[next]:
                visit[next] = 1
                dfs(next,cnt+1)
                visit[next] = 0
    visit[begin] = 1
    dfs(begin,0)
    if answer == INF:
        return 0
    return answer

def check(a,b):
    cnt = 0
    for i,j in zip(a,b):
        if i != j: cnt += 1
    return cnt