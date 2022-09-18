# 220918 / 여행경로
def solution(tickets):
    answer = []
    
    d = {}
    for st, de in tickets:
        if st not in d:
            d[st] = []
        d[st].append(de)

    for i in d:
        d[i].sort(reverse=True)
    
    stk = ["ICN"]
    while stk:
        a = stk.pop()
        if a not in d or not d[a]:
            answer.append(a)
        else:
            stk.append(a)
            stk.append(d[a].pop())

    return answer[::-1]