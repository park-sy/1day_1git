# 220919 / 단어변환 2
from collections import defaultdict,deque
import sys
INF = sys.maxsize
def solution(begin, target, words):

    d = defaultdict(list)
    visit = defaultdict(int)
    words.append(begin)
    for i in words:
        visit[i] = 0
        for j in words:
            if i == j: continue
            if check(i,j) == 1:
                d[i].append(j)        
    
    def bfs(start):
        q = deque()
        q.append(start)
        visit[start] = 0
        
        while q:
            now = q.popleft()
            for next in d[now]:
                if not visit[next]:
                    visit[next] = visit[now] + 1
                    q.append(next)
    bfs(begin)
    return visit[target]

def check(a,b):
    cnt = 0
    for i,j in zip(a,b):
        if i != j: cnt += 1
    return cnt