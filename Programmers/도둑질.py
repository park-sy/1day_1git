# 220727/도둑질

def solution(money):
    n = len(money)
    money2 = money[1:]
    
    dp1 = [0] *(n-1)
    dp2 = [0] *(n-1)
    dp1[0] = money[0]
    dp1[1] = max(money[0],money[1])
    dp2[0] = money2[0]
    dp2[1] = max(money2[0],money2[1])
    
    for i in range(2,n-1):
        dp1[i] = max(dp1[i-2]+money[i],dp1[i-1])
        dp2[i] = max(dp2[i-2]+money2[i],dp2[i-1])

    answer = max(dp1[-1],dp2[-1])
    return answer