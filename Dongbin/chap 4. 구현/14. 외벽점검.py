# 220712 / 구현 / 외벽점검
from itertools import permutations

def solution(n, weak, dist):
    
    length = len(weak)
    for i in range(length):
        weak.append(weak[i])
    answer = len(dist) + 1
    
    for i in range(length):
        for j in list(permutations(dist,len(dist))):
            count = 1
            position = weak[i] + j[count-1]
            for k in range(i,i+length):
                if position < weak[k]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[k] + j[count-1]
            answer = min(answer,count)
            
    if answer > len(dist):
        return -1  
    return answer

        
    
    