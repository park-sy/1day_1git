# 220411 / 동적계획법 2 / 2629 / 양팔저울

n = int(input())
wei = list(map(int,input().split()))
m = int(input())
mar = list(map(int,input().split()))

dp = [[0 for _ in range((i+1)*500+1)]for i in range(n+1)]

def cal(num, weight):
    if num > n:
        return
    if dp[num][weight]:
        return

    dp[num][weight] = 1
    cal(num+1, weight)
    cal(num+1, weight + wei[num-1])
    cal(num+1, abs(weight - wei[num-1]))


cal(0,0)
for i in mar:
    if i > 30*500:
        print("N", end =' ')
    elif dp[n][i]:
        print("Y", end =' ')
    else:
        print("N", end =' ')