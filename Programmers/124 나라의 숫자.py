# 220726 / 124 나라의 숫자
def solution(n):
    answer = ''

    while n:
        if n % 3 == 0:
            answer = str(4) + answer
            n = n//3 -1
        else:
            answer = str(n%3) + answer
            n = n//3

    return answer