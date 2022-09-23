# 220923 / 베스트 엘범

from collections import defaultdict
def solution(genres, plays):
    answer = []
    n = len(genres)
    m = len(set(genres))
    g = {}
    
    total = [[0,[]] for i in range(m)]
    
    idx = 0
    for i in range(n):
        genre = genres[i]
        if genre not in g:
            g[genre] = idx
            total[idx][0] += plays[i]
            total[idx][1].append([plays[i],i])
            idx += 1
        else:
            total[g[genre]][0] += plays[i]
            total[g[genre]][1].append([plays[i],i])
    
    total.sort(reverse=True)
    
    for genre in total:
        a = sorted(genre[1], key = lambda x : (-x[0],x[1]))
        cnt = 0
        for play, idx in a:
            if cnt > 1: break
            answer.append(idx)
            cnt += 1
        
    
    return answer