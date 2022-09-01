# 220901 / 양궁 대회
from copy import deepcopy

def solution(n, info):
    global score,answer
    answer = []
    score = 0 

    def dfs(s,cnt, num):
        global score,answer
        if cnt == n:
            v = check(s)
            if score < v:
                score = v
                answer = [s]
            elif score == v:
                answer.append(s)
            return
        
        
        for i in range(num,11):
            temp = deepcopy(s)
            temp[i] += 1
            dfs(temp,cnt+1,i)

            
    def check(ans):
        r,c = 0,0
        k = 0
        for i,j in zip(info,ans):
            k += 1
            if i == 0 and j == 0: continue
            if i >= j:
                r += 11 - k
            else:
                c += 11 - k
            
        if c > r:
            return c - r
        return -1
    
    init = [0]*11
    dfs(init,0,0)

    if score == 0:
        return [-1]
    answer.sort(key=lambda x : x[::-1],reverse=True)

    return answer[0]
