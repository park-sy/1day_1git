# 220819 / 광고삽입
def solution(play_time, adv_time, logs):
    pl = convertSec(play_time)
    ad = convertSec(adv_time)

    use = [0]*(pl+1)
    for i in logs:
        s,e = i.split("-")
        use[convertSec(s)] += 1
        use[convertSec(e)] -= 1
    
    for i in range(1,pl):
        use[i] += use[i-1]
    for i in range(1,pl):
        use[i] += use[i-1]
        
    res = 0
    ans = 0
    for i in range(ad-1, pl):
        temp = use[i] - use[i-ad]
        if temp > res:
            res = temp
            ans = i - ad + 1
                      
    return convert(ans)


def convertSec(time):
    time = list(map(int,time.split(":")))
    return time[0]*3600 + time[1]*60 + time[2]

def convert(time):
    h = str(time // 3600).zfill(2)
    m = str((time % 3600)//60).zfill(2)
    s = str(((time % 3600)%60)).zfill(2)
    t = [h,m,s]
    res = ':'.join(t)
    return res
