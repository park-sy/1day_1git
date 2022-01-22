# 220122 / 백트래킹/ 15649 / N과 M(2)

N, M = map(int, input().split())

s = []
s2 = []
def dsf():
    if len(s) == M:
        print(" ".join(map(str, s)))
        return
    
    for i in range(1, N+1):
        t = False
        if i in s :
            continue
        for j in range(len(s)):
            if i <= s[j]:
                t = True
        if t == True:
            continue
        s.append(i)
        dsf()
        s.pop()

dsf()
