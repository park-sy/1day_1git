# 220820 / 두 큐 합 같게 만들기
from collections import deque
def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    flag = len(q1) *2 + 2
    
    s1 = sum(q1)
    s2 = sum(q2)

    while s1 != s2:
        if s1 > s2:
            t = q1.popleft()
            q2.append(t)
            s1 -= t
            s2 += t
        else:
            t = q2.popleft()
            q1.append(t)
            s1 += t
            s2 -= t
            
        answer += 1
        if answer > flag:
            return -1
    return answer