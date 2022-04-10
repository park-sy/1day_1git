# 220410 / 동적계획법 2 / 10942 / 팰린드롬?
import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int,input().split()))
m = int(input())

dp = [[0 for _ in range(n)]for _ in range(n)]

for i in range(n):
    for start in range(n):
        end = start + i
        if end >= n:
            break
        if start == end:
            dp[start][end] = 1
        elif start + 1 == end:
            if num[start] == num[end]: dp[start][end] = 1
        elif num[start] == num[end] and dp[start+1][end-1]:
            dp[start][end] = 1

for _ in range(m):
    n1, n2 = map(int,input().split())
    print(dp[n1-1][n2-1])