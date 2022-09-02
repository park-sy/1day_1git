# 220902 / 다트 게임
def solution(dartResult):
    answer = 0
    res = dartResult.replace('10','k')
    stk = []
    for i in res:
        if i.isdigit():
            stk.append(int(i))
        elif i == 'k':
            stk.append(10)
        elif i == "S":
            stk[-1] **= 1
        elif i == "D":
            stk[-1] **= 2
        elif i == "T":
            stk[-1] **= 3
        elif i == '*':
            stk[-1] *= 2
            if len(stk) >1:
                stk[-2] *= 2
        else:
            stk[-1] *= -1

    return sum(stk)