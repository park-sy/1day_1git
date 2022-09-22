# 220922 / 키패드누르기
from collections import deque
def solution(numbers, hand):
    answer = ''
    g = [[j+i*3 for j in range(1,4)] for i in range(4)]
    print(g)
    l = [1,4,7]
    r = [3,6,9]
    
    left_hand, right_hand = 10, 12
    for i in numbers:
        if i in l:
            answer+='L'
            left_hand = i
        elif i in r:
            answer+='R'
            right_hand = i
        else:
            a = distance(left_hand,i)
            b = distance(right_hand,i)

            if a == b:
                if hand == "right":
                    answer+='R'
                    right_hand = i
                else:
                    answer+="L"
                    left_hand = i
            elif a > b:
                answer+='R'
                right_hand = i
            else:
                answer+='L'
                left_hand = i
    return answer

def distance(now,n):

    if now == n:
        return 0
    if n == 0:
        n = 11
    if now == 0:
        now = 11
    nx,ny = (now-1)//3, (now-1)%3
    tx,ty = (n-1)//3, (n-1)%3
    
    
        
    return abs(nx-tx)+abs(ny-ty)
