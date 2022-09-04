# 220904 / n진수 게임
def solution(n, t, m, p):
    answer = ''
    cnt = 0
    num = 0
    seq = 0

    while cnt < t:
        word = convert(num,n)

        for w in word:
            if seq % m == p-1:
                answer+=w
                cnt += 1
                if cnt == t: break
            seq += 1
        num += 1

    return answer


def convert(num,n):
    temp = "0123456789ABCDEF"
    q,r = divmod(num,n)
    if q== 0:
        return temp[r]
    else:
        return convert(q,n) + temp[r]
    
