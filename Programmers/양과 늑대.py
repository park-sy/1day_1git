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