# 220104 / 기본 수학 2 레벨 6
# 9020 / 골드바흐의 추측
def find_prime(n):
    prime = True
    if n == 1:
        prime = False
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                prime = False
                break
    return prime




T = int(input())

for a in range(T):
    i = int(input())
    num = int(i / 2)
    dec1 = 0
    dec2 = 0
    for j in range(num, i):
        if find_prime(j) == True:
            dec2 = j
            dec1 = i - j

            if find_prime(dec1) == True:
                print(dec1, dec2)
                break




        
