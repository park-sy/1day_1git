# 220728 / 프로그래머스 레벨3
def solution(A, B):
    n = len(A)
    answer = 0
    A.sort()
    B.sort()
    id = 0
    for i in range(n):
        for j in range(id,n):
            if B[j] > A[i]:
                answer += 1
                id = j + 1
                break
            
        
        
    return answer