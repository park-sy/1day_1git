# 220812 / 순위 검색
import bisect
from itertools import combinations
from collections import defaultdict
def solution(info, query):
    answer = []
    d = defaultdict(list)

    n = len(info)
    for i in range(n):
        tp = info[i].split(" ")
        mkey = tp[:-1]
        mval = int(tp[-1])
        for j in range(5):
            case = list(combinations([0,1,2,3], j))
            for c in case:
                tmp = mkey.copy()
                for idx in c:
                    tmp[idx] = "-"
                key = ''.join(tmp)
                d[key].append(mval) 
                
    for k in d:
        d[k].sort()

    for q in query:
        q = q.replace("and ","")
        q = q.split()
        tkey = ''.join(q[:-1])
        tval = int(q[-1])
        cnt = 0
        if tkey in d:
            tlist = d[tkey]
            idx = bisect.bisect_left(tlist,tval)
            cnt = len(tlist) - idx
        answer.append(cnt)
    return answer