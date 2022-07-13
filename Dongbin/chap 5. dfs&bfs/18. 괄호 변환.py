# 220713 / dfs bfs / 괄호 변환
from collections import deque
def solution(p):
    return dfs(p)

def dfs(p):
    if not p:
        return ""
    
    flag = 0
    for i in range(len(p)):
        if p[i] == "(":
            flag += 1
        else: flag -= 1
        if flag == 0:
            flag = i
            break
    u = p[:i+1]
    v = p[i+1:]
    
    if check(u):
        newp = u + dfs(v)
    else:
        newp = "("
        newp += dfs(v) + ")"
        for i in range(1,len(u)-1):
            if u[i] == ")":
                newp += "("
            else: newp += ")"
    return newp

def check(p):
    flag = 0
    for i in p:
        if i == "(":
            flag += 1
        else: flag -= 1
        if flag < 0:
            return False
    return True
        
        
            