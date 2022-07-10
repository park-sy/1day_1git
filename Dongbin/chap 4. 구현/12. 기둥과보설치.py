def solution(n, build_frame):
    k = len(build_frame)
    answer = []

    for i in range(k):
        x,y,a,b = build_frame[i]
        if b == 0:
            answer.remove([x,y,a])
            if not possible(answer):
                answer.append([x,y,a])
        if b == 1:
            answer.append([x,y,a])
            if not possible(answer):
                answer.pop()
            

    return sorted(answer)

def possible(answer):
    for x,y,a in answer:
        if a == 0:
            if y== 0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
                continue
            return False
        elif a == 1:
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1],y,1 in answer and [x+1,y,1] in answer):
                continue
            return False
    return True

