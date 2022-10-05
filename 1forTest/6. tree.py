# trie 구조
def solution(words):
    answer = 0
    trie = {}
    for word in words:
        cur_trie = trie
        for w in word:
            cur_trie.setdefault(w, [0, {}])
            cur_trie[w][0] += 1
            cur_trie = cur_trie[w][1]
    print(cur_trie,trie)
    for word in words:
        cur_trie = trie
        for i in range(len(word)):
            w = word[i]
            if cur_trie[w][0] == 1:
                break
            cur_trie = cur_trie[w][1]
        answer += (i + 1)
    return answer


    # 220828 / 동굴 탐험
from collections import deque

def solution(n, path, order):

    g = [[] for _ in range(n)]
    for a,b in path:
        g[a].append(b)
        g[b].append(a)
    
    visit = [0] *(n)
    pre = [0] * n
    for a,b in order:
        pre[b] = a
    q = deque([0])
    after = {}
    cnt = 0
    while q:
        now = q.popleft()
        
        if pre[now] and not visit[pre[now]]:
            after[pre[now]] = now
            continue
        visit[now] = 1
        cnt += 1
        
        for next in g[now]:
            if not visit[next]:
                q.append(next)
                
        if now in after:
            q.append(after[now])
            
    return n == cnt


# 220906 / 양과 늑대
def solution(info, edges):
    global answer
    answer = 0
    n = len(info)
    visit = [0] * n
    visit[0] = 1
    def dfs(sheep,wolf):
        global answer
        if sheep <= wolf:
            return
        answer = max(sheep,answer)
        
        for p,c in edges:
            iswolf = info[c]
            if visit[p] and not visit[c]:
                visit[c] = 1
                dfs(sheep+(iswolf==0),wolf+(iswolf==1))
                visit[c] = 0
    dfs(1,0)           
    
    return answer