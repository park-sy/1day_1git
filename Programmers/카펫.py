# 221023 / 카펫
def solution(brown, yellow):
    answer = []
    r = 1
    l = brown + yellow
    
    for i in range(1,l+1):
        if l / i != l//i: continue
        col = i
        row = l // i
        if (row-2)*(col-2) == yellow:
            answer.append(row)
            answer.append(col)
            break
    return answer