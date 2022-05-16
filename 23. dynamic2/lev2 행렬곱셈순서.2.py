# 220516 / dp2 / 11049 / 행렬 곱셈 순서
import sys
input = sys.stdin.readline
def multimrx(A,B):
    return A[0] * B[0] * B[1]

n = int(input())
mrx = []
for _ in range(n):
    mrx.append(list(map(int,input().split())))

dp = [[0]*(n) for _ in range(n)]

for i in range(1, n):
    for j in range(n - i):
        x = j + i
        dp[j][x] = 2 ** 32
        for k in range(j, x):
            dp[j][x] = min(dp[j][x], dp[j][k] + dp[k + 1][x] + mrx[j][0] * mrx[k][1] * mrx[x][1])


print(dp[0][n - 1])
