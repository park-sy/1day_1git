# 220902 / 방금 그곡
def solution(m, musicinfos):
    answer = '(None)'
    m = returnstr(m)
    play_time = 0
    for i in musicinfos:
        detail = i.split(',')
        time = timecal(detail[0],detail[1])
        lyc = returnstr(detail[3])
        ly = len(lyc)
        new_str = ""
        for minute in range(time):
            new_str += lyc[minute%ly]
        if m in new_str:
            if time > play_time:
                answer = detail[2]
                play_time = time

    return answer


def timecal(a,b):
    at,am = a.split(":")
    bt,bm = b.split(":")
    return int(bt)*60+int(bm) - int(at)*60-int(am)

def returnstr(lyc):
    lyc = lyc.replace("C#",'c')
    lyc = lyc.replace("D#",'d')
    lyc = lyc.replace("F#",'f')
    lyc = lyc.replace("G#",'g')
    lyc = lyc.replace("A#",'a')
    return lyc
    
    
    
    