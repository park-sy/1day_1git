# 220913 / 다단계 칫솔 판매
def solution(enroll, referral, seller, amount):
    n = len(enroll)
    answer = [0] *(n+1)
    d = {}  
    parent = [i for i in range(n + 1)]  

    for i in range(n):
        d[enroll[i]] = i + 1

    for i in range(n):
        if referral[i] == "-":  
            parent[i + 1] = 0
        else:
            parent[i + 1] = d[referral[i]]

        
    def find(number,res):
        if parent[number] == number or res // 10 == 0:
            answer[number] += res
            return
        answer[number] += res - res//10
        find(parent[number],res//10)
            
    
    for i in range(len(seller)):
        find(d[seller[i]],amount[i] * 100)

    return answer[1:]