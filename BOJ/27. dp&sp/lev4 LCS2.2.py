# 220602 / DP & SP / 9252 / LCS2

st1 = [0] + input().rstrip()
st2 = [0] + input().rstrip()

l1, l2 = len(st1), len(st2)
dp = [[""]*(l2) for _ in range(l1)]

for i in range(1,l1):
    for j in range(1,l2):
        if st1[i] == st2[j]:
            dp[i][j] = dp[i-1][j-1] + st1[i]
        else:
            if len(dp[i - 1][j]) > len(dp[i][j - 1]):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]
print(len(dp[-1][-1]))
print(dp[-1][-1])
