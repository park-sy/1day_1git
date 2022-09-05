# 220905 / k진수에서 소수 개수 구하기
def solution(n, k):
    answer = 0
    a = convert(n,k)

    dig = ""
    for i in a:
        if i == "0":
            answer += check(dig)
            dig = ""
        else:
            dig += i
    answer += check(dig)

    return answer

def convert(num,base):
    temp = "0123456789"
    q,r = divmod(num,base)
    if q == 0:
        return temp[r]
    else: return convert(q,base) + temp[r]

def check(num):
    
    if not num or num == "1":
        return 0
    num = int(num)
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return 0
    return 1