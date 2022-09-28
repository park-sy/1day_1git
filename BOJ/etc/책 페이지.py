# 220928 / 책 페이지
n = int(input())
ln = len(str(n))
dp = [[0]*10 for _ in range(ln)]
number = str(n)

if n < 10:
    for i in range(1,n+1):
        dp[0][i] = 1
    print(*dp[0])
    exit()

for i in range(10):
    dp[0][i] = 1
dp[0][0] = 0
for i in range(1,ln-1):
    for j in range(10):
        if j == 0:
            dp[i][j] += dp[i-1][j]*10 - 1 + 10**(i)
        else:
            dp[i][j] += dp[i-1][j]*10 + 10**i

for i,num in enumerate(number):
    num = int(num)
    if i == ln-1:
        for j in range(num+1):
            dp[ln-1][j] += 1
        break
    
    for j in range(10):
        if j == num: 
            # 999 1000
            dp[ln-1][j] += int(number[i+1:]) + 1     
        if j < num:
            if j == 0:
                if i != 0: 
                    dp[ln-1][j] += 10**(ln-i-1)
            else:
                dp[ln-1][j] += 10**(ln-i-1)

        if j == 0:
            dp[ln-1][j] += dp[ln-2-i][j+1] * (num)
        else:
            dp[ln-1][j] += dp[ln-2-i][j] * (num)

dp[ln-1][0] += dp[ln-2][0] - dp[ln-2][1]
print(*dp[ln-1])
