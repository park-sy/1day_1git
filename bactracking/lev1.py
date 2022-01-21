# 220121 / 백트래킹/ 15649 / N과 M(1)

N, M = map(int, input().split())

s = []
def dsf():
    if len(s) == M:
        print(" ".join(map(str, s)))
        return
    
    for i in range(1, N+1):
        if i in s:
            continue
        s.append(i)
        dsf()
        s.pop()

dsf()
