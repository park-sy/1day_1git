#20708 / 구현 / 문자열 압축

def solution(s):

    n = len(s)
    answer = n
    for i in range(1,n//2+1):
        pre = s[0:i]
        cnt = 1
        comp = ""
        for j in range(i,n,i):
            if pre == s[j:j+i]:
                cnt += 1
            else:
                comp += str(cnt) + pre if cnt >=2 else pre
                pre = s[j:j+i]
                cnt = 1
                
        comp += str(cnt) + pre if cnt >=2 else pre 
        answer = min(len(comp),answer)               
        
    
    return answer