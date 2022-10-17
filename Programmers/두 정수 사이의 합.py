# 221017 / 두 정수 사이의 합
def solution(a, b):
    answer = 0
    
    if a == b:
        answer += a*2
    elif b < a:
        a,b = b,a
    
    for i in range(a,b+1):
        answer += i
        
    return answer