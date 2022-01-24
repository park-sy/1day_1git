# 220124 / 백트래킹 / 9663 / N-Queen


N = int(input())
s = []
cnt = [0]

def queen(start):

    if len(s) == N:
        print(s)
        cnt[0] += 1
        return
        
    for i in range(start, N+1):
        for j in range(1,N+1):
            t = False
            for k in range(len(s)):
                if (s[k][1] == j) or (i-k == abs(s[k][1]-s[i][1])):
                    t = True
                    break

            if t == True:
                continue
         
            s.append([i,j])
            queen(i+1)
            s.pop()
            
queen(1)
print(cnt[0])