# 220826 / 캐시


def solution(cacheSize, cities):
    answer = 0
    if cacheSize == 0:
        return len(cities)*5
    lq = 0
    d = {}

    for i,c in enumerate(cities):
        city = c.lower()
        
        if lq < cacheSize:
            if city not in d:
                lq += 1
                answer += 5
            else:
                answer += 1
            d[city] = i
        else:
            if city in d:
                d[city] = i
                answer += 1
            else:
                last = min(d, key=d.get)
                del(d[last])
                d[city] = i
                answer += 5
       
    return answer