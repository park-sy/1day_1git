# 220727 / 기능개발
def solution(progresses, speeds):
    n = len(progresses)
    days = [0]*n
    for i in range(n):
        k = (100-progresses[i]) // speeds[i]
        r = (100-progresses[i]) % speeds[i]
        if r:
            k += 1
        days[i] = k

    cnt = 0
    answer = []
    day = days[0]

    for i in range(n):
        if day >= days[i]:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            day = days[i]
    answer.append(cnt)
    
    
    return answer


print(solution([93],[1]))