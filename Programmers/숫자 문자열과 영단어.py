# 220902 / 숫자 문자열과 영단어 
def solution(s):
    answer = ""
    tmp = ""
    d = {        
        'zero':0,
        'one' : 1,
        'two' : 2,
        'three':3,
        'four':4,
        'five':5,
        'six':6,
        'seven':7,
        'eight':8,
        'nine':9}

            
    for i in s:
        if ord(i) < 97:
            answer += i
        else:
            tmp += i
            
            if tmp not in d: continue
            answer += str(d[tmp])
            tmp = ""
    

    return int(answer)