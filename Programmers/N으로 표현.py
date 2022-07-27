#220727 / N으로 표현

def solution(N, number):
    answer = -1
    dp = []
    
    for i in range(1,9):
        case = set()
        check = int(str(N)*i)
        case.add(check)
        
        for j in range(0,i-1):
            for op1 in dp[j]:
                for op2 in dp[-j-1]:
                    case.add(op1-op2)
                    case.add(op1 + op2)
                    case.add(op1*op2)
                    if op2 != 0:
                        case.add(op1//op2)
        if number in case:
            answer = i
            break
        
        dp.append(case)
    
    
    
    return answer

def dfs(n,seq,dp):
    
    for i in dp[n-1]:
        dfs()

