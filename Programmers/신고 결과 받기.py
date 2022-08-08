# 220808 / 신고 결과 받기
from collections import Counter
def solution(id_list, report, k):
    n = len(id_list)
    id = {}
    for i in range(n):
        id[id_list[i]] = i
        
    rep = set(report)
    d = {}
    for name in rep:
        a,b = name.split(" ")
        if b not in d:
            d[b] = 1
        else: d[b] += 1
    answer = [0] * n
    for name in rep:
        a,b = name.split(" ")
        if d[b] >= k:
            answer[id[a]] += 1
    return answer