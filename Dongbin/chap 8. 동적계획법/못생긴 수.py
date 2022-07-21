# 220721 / dp / 못생긴 수
n = int(input())

dp = [0] * (10**5)

dp[1] = 1
cnt = 1
i = 1
while cnt < n:
    i += 1
    for k in [i/2,i/3,i/5]:
        if int(k) == k and dp[int(k)]:
            dp[i] = cnt
            cnt += 1
            print(i,cnt)
            break
            

print(i)
