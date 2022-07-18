# 220717 / 정렬 / 실패율
def solution(n, stages):
    answer = []
    p = len(stages)
    
    d = [0] *(n+2)
    for i in stages:
        d[i] += 1
    
    temp = []
    for i in range(1,n+1):
        if d[i] == 0:
            temp.append([0,i])
        else:
            temp.append([d[i]/p,i])
            p -= d[i]
    temp = sorted(temp, key = lambda x : (-x[0],x[1]))
    for i in temp:
        answer.append(i[1])
    print(temp)
    return answer