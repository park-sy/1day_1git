#  220903 / 압축
def solution(msg):
    answer = []
    d = {}
    for i in range(1,27):
        d[chr(64+i)] = i
    last_idx = 26
    
    temp = ''
    n = len(msg)
    start = 0

    while start < n:
        temp = ''
        idx = start
        for next in range(idx,n):
            temp += msg[next]
            
            if temp not in d:
                answer.append(d[temp[:-1]])
                d[temp] = last_idx + 1
                last_idx += 1
                break
            start += 1
        if start == n:
            answer.append(d[temp])     
    return answer
