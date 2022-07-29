# 220729 / 11062 / 카드게임
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())

    card = list(map(int,input().split()))
    dp = [[0]*n for _ in range(n)]
    turn = True if n%2 == 1 else False
    for size in range(n):
        for i in range(n- size):
            if size == 0:
                dp[i][i+size] = card[i] if turn else 0
            elif turn:
                dp[i][i+size] = max(dp[i+1][i+size] + card[i],dp[i][i+size-1]+card[i+size])
            else:
                dp[i][i+size] = min(dp[i+1][i+size],dp[i][i+size-1])
        turn = not turn

    print(dp[0][n-1])