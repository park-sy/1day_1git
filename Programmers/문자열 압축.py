# 220921 / 문자열 압축
def solution(s):
    answer = 1001
    n = len(s)
    
    for i in range(1,n+1):
        temp = ""
        pre = s[:i]
        cnt = 1
        for j in range(i,n,i):
            if pre == s[j:j+i]:
                cnt += 1
            else:
                if cnt == 1:
                    temp += pre
                else:
                    temp += str(cnt)+pre
                pre = s[j:j+i]
                cnt = 1
        
        if cnt == 1:
            temp += pre
        else:
            temp += str(cnt)+pre
        answer = min(len(temp),answer)
    return answer