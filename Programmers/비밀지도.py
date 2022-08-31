# 220831 / 비밀지도
def solution(n, arr1, arr2):
    answer = [[" "]*n for _ in range(n)]
    
    for i,k in enumerate(arr1):
        temp = str(bin(k)[2:]).zfill(n)
        for j in range(n):
            if temp[j] =="1":
                answer[i][j] = '#'
                
    for i,k in enumerate(arr2):
        temp = str(bin(k)[2:]).zfill(n)
        for j in range(n):
            if temp[j] =="1":
                answer[i][j] = '#'
    ans = []
    for i in answer:
        ans.append("".join(i))
    
    return ans