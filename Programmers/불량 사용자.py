#220816 / 불량 사용자
from itertools import permutations
def solution(user_id, banned_id):
    answer = []
    def check(u,b):
        if len(u) != len(b):
            return 0
        for i,j in zip(u,b):
            if j == '*': continue
            if i != j: return 0
        return 1

    for i in permutations(user_id,len(banned_id)):
        cnt = 0
        for a,b in zip(i,banned_id):
            cnt += check(a,b)
        if cnt == len(banned_id):
            if set(i) not in answer:
                answer.append(set(i))

    return len(answer)


solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"])
# * 매칭 id 찾기
# 조합

def solution1(user_id, banned_id):
    answer = set()
    n = len(banned_id)
    m = len(user_id)
    visit = [0] * n
    visitu = [0] *m
    tmp = []
    def dfs(cnt):
        if cnt == n:
            t = sorted(tmp)
            answer.add(tuple(t))
            return
            
        for b in range(n):
            if not visit[b]:
                for u in range(m):
                    if not visitu[u]:
                        if len(banned_id[b]) == len(user_id[u]):
                            flag = 0
                            for i in range(len(banned_id[b])):
                                if banned_id[b][i] == "*":continue
                                if banned_id[b][i] != user_id[u][i]: 
                                    flag = 1
                                    break 
                            if not flag:
                                visit[b] = 1
                                visitu[u] = 1
                                tmp.append(u)
                                dfs(cnt+1)
                                visit[b] =0
                                visitu[u] = 0
                                tmp.pop()
    dfs(0)

    return len(answer)
