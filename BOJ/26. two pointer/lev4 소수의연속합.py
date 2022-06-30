# 220312 / 투포인터 / 1644 / 소수의 연속합
def sosu(n):
    arr = []
    for i in range(2, n+1):
        judge = False
        if i == 1:
            judge = True
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                judge = True
                break
        if judge == False:
            arr.append(i)
    return arr

n = int(input())
if n == 1:
    print(0)
else:
    a = sosu(n)

    srt = 0
    end = 0
    sum = a[0]
    cnt = 0

    while srt < len(a):
        if end == len(a)-1:
            if sum == n:
                cnt += 1
            sum -= a[srt]
            srt += 1
        
        else:            
            if sum == n:
                cnt += 1
                sum -= a[srt]
                srt += 1
            elif sum > n:
                sum -= a[srt]
                srt += 1
            else:
                end += 1
                sum += a[end]

    print(cnt)