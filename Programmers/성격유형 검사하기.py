# 220822 / 성격유형 검사하기
def solution(survey, choices):
    answer = ''
    n = len(survey)
    idx ={}
    sv = ["R","T","C","F","J","M","A","N"]
    for i in sv:
        idx[i] = 0
    
    for i in range(n):
        w = survey[i]
        if choices[i] < 4:
            idx[w[0]] += abs(choices[i] - 4)
            print(w[0],idx[w[0]])
        else:
            idx[w[1]] += abs(choices[i] - 4)
            print(w[1],idx[w[1]])
    
    for i in range(0,8,2):
        if idx[sv[i]] < idx[sv[i+1]]:
            answer += sv[i+1]
        else: answer += sv[i]
    
    return answer