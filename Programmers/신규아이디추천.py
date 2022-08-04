# 220804 / 신규 아이디 추천

from collections import deque
def solution(new_id):
    # 1
    id = new_id.lower()
    #2
    id2 = []

    for i in id:
        oi = ord(i)
        if 47 < oi < 58 or 96 < oi < 123 or oi == 45 or oi == 95 or oi == 46:
            id2.append(i)

        
    #3
    id3 = deque([])
    fg = 0
    for i in id2:
        if i != ".":
            fg = 0
            id3.append(i)
        elif i == "." and fg == 0:
            fg = 1
            id3.append(i)
    #4
    while id3 and id3[0] == ".":
        id3.popleft()
    while id3 and id3[-1] == ".":
        id3.pop()
    
    #5
    if not id3:
        id3.append("a")
    #6
    id4 = []
    for i in id3:
        id4.append(i)
    if len(id4) >= 16:
        id4 = id4[:15]
        if id4[-1] == ".":
            id4.pop()
    
    #7
    while len(id4) < 3:
        id4.append(id4[-1])
    
    answer = ''
    for i in id4:
        answer += i
    return answer