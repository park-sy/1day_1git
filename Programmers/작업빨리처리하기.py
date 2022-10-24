# 221024 / 작업 빨리 처리하기
from collections import Counter
def solution(task):
    answer = 0
    c = Counter(task)

    for i in c.values():
        if i == 1: return -1
        b = i // 3
        d = i % 3
        answer += b + (d != 0 )

    return answer