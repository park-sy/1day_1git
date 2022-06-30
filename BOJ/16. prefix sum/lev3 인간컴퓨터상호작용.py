# 220419 / 누적합 / 16139 / 인간컴퓨터 상호작용
import sys
input = sys.stdin.readline

sen = input().rstrip()
n = int(input())
dp = [[0]*26 for _ in range(len(sen)+1)]

for i in range(1,len(sen)+1):
    x = ord(sen[i-1] - ord("a"))
    for j in range(26):
        if j == x:
            dp[i][j] = dp[i-1][j] + 1
            continue
        dp[i][j] = dp[i-1][j]

for _ in range(n):
    word, start, end = input().rstrip().split()
    word = ord(word) - ord("a")
    start = int(start)
    end = int(end)

    ans = dp[end + 1][word] - dp[start][word]
    sys.stdout.write(str(ans) + "\n")