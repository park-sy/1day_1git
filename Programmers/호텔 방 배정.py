# 220804 / 호텔방배정
import sys
sys.setrecursionlimit(10000000) 

def solution(k, room_number):
    
    answer = []
    parent = dict()
    
    def find(x):
        if x not in parent:
            parent[x] = x + 1
            return x
        
        parent[x] = find(parent[x]) + 1
        return parent[x] - 1
    
    
    for i in room_number:
        empty = find(i)
        answer.append(empty)
            
        
    
    return answer
