# 220814 / 후보키
from itertools import combinations
def solution(relation):
    row = len(relation)
    col = len(relation[0])
    ckey = []
    for i in range(1,col+1):
        ckey.extend(combinations(range(col),i))
        
    unique = []
    for c in ckey:
        tmp = [tuple(item[key] for key in c) for item in relation]
        if len(set(tmp)) == row:
            unique.append(c)
    
    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i + 1, len(unique)):
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                answer.discard(unique[j])
    return len(answer)