#220721 / dp / 편집거리

a = input().rstrip()
b = input().rstrip()

la = len(a)
lb = len(b)
diff = abs(la-lb)

dp = [[0] * (lb+1) for _ in range(la+1)] 
for i in range(1,la+1):
    for j in range(1,lb+1):
        dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        if a[i-1] == b[j-1]:
            dp[i][j] += 1

print(diff + la - dp[-1][-1])
        