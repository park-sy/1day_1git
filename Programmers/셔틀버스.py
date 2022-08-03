#220803 / 셔틀버스
def solution(n, t, m, timetable):
    answer = ''
    k = len(timetable)
    last = n * m
    crew = []
    for i in timetable:
        crew.append(hourtominute(i))
    crew.sort()
    
    bus = [9*60 + t*i for i in range(n)]
    res,i = 0,0
    for tm in bus:
        cnt = 0
        while cnt < m and i < k and crew[i] < tm:
            i += 1
            cnt += 1
        if cnt < m:
            res = tm
        else: res = crew[i-1] - 1
        
    
    answer = str(res//60).zfill(2) + ":" + str(res%60).zfill(2)
    return answer

def hourtominute(time):
    hour, minute = map(int,time.split(":"))
    
    return hour * 60 + minute