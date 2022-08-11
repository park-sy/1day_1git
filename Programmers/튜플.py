# 220811 / 튜플
import re
def solution(s):
    answer = []
    tmp = re.split("[{}]",s)

    k = []
    for i in tmp:
        if i and i != ",":
            k.append(i)

    a = []
    for i in k:
        a.append(list(map(int, i.split(","))))

    a.sort(key = lambda x : len(x))

    for i in a:
        for w in answer:
            i.remove(w)
        answer.append(i[0])
            
    return answer