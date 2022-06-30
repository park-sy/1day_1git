#220103 / 기본수학2 레벨 5
#4948 / 베르트랑 공준


while True:
    n = int(input())
    if n == 0:
        break
    sum = 0
    for i in range(n+1,n*2+1):
        a = int(i**0.5)
        dec = False
        for j in range(2, a+1):
            if i % j == 0:
                dec = True
                break
        if dec == False:
            sum += 1
    print(sum)
            