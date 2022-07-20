# 220720 / 이진탐색 / 가사 검색

import bisect

def solution(words, queries):
    answer = []
    arr = [[]for _ in range(10001)]
    rarr = [[]for _ in range(10001)]
    for word in words:
        l = len(word)
        arr[l].append(word)
        rarr[l].append(word[::-1])
    
    for i in range(1,10001):
        arr[i].sort()
        rarr[i].sort()
        
    for q in queries:
        if q[0] != "?":
            print(q.replace("?","a"),q.replace("?","z"))
            res = cnt_byrange(arr[len(q)], q.replace("?","a"),q.replace("?","z"))
        else:
            res = cnt_byrange(rarr[len(q)], q[::-1].replace("?","a"),q[::-1].replace("?","z"))
        answer.append(res)    
        
    return answer



def cnt_byrange(a, l, r):
    r = bisect.bisect_right(a,r)
    l = bisect.bisect_left(a,l)
    return r-l
    

                
        
            
        
            