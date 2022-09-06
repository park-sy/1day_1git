# 220906 / 주차 요금 계산
import math
def solution(fees, records):
    answer = []
    rec = []
    for i in records:
        rec.append(list(map(str,i.split())))

    rec.sort(key = lambda x : (x[1],x[0]))
    print(rec)
    in_time = 0
    out_time = -1
    sum_time = 0
    number = rec[0][1]
    for i in rec:
        if number == i[1]:
            if i[2] == "IN":
                in_time = convert(i[0])
            else:
                out_time = convert(i[0])
                sum_time += out_time - in_time
        else:
            if in_time > out_time:
                sum_time += convert("23:59") - in_time
            answer.append(calculate(sum_time,fees))
            in_time = convert(i[0])
            out_time = -1
            sum_time = 0
            number = i[1]
    if in_time > out_time:
        sum_time += convert("23:59") - in_time
    answer.append(calculate(sum_time,fees))
            
        
    return answer

def convert(s):
    a,b = s.split(":")
    return int(a)*60+int(b)

def calculate(time,fees):
    if time <= fees[0]:
        return fees[1]
    return math.ceil((time - fees[0])/fees[2])*fees[3] + fees[1]