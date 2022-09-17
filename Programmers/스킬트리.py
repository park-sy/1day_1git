# 220917 / 스킬트리
def solution(skill, skill_trees):
    answer = 0
    
    parent = [-1]*26
    n = len(skill)
    for i in range(1,n):
        parent[ord(skill[i])-65] = ord(skill[i-1])-65
    for t in skill_trees:
        visit = [0]*26
        flag = 0
        for s in t:
            pre = parent[ord(s)-65]
            if pre != -1 and not visit[parent[ord(s)-65]]:
                flag =1
                break
            visit[ord(s)-65] = 1
        if not flag: answer += 1
        
    return answer