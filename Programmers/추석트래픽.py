# 220802 / 추석트래픽

def solution(lines):
    answer = 0
    q = []
    for time in lines:
        temp = time.split(" ")
        e = end(temp[1])
        s = start(e[0],temp[2])
        e[0] += 999
        q.append(s)
        q.append(e)
    q.sort()
    
    cnt = 0
    for i in q:
        cnt -= i[1]
        answer = max(answer, cnt)
    return answer

def end(time):
    hms = time.split(":")
    hour = int(hms[0]) * 3600
    minute = int(hms[1]) * 60
    sec = int(hms[2][:2])
    msec = int(hms[2][3:])   
    res = (hour+ minute + sec) * 1000 + msec
    return [res, 1]

def start(time, req):
    tmp = int (float(req[:-1])*1000)
    res = time - tmp + 1
    return [res,-1]