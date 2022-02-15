# 220123 / 백트래킹 / 15651 / N과 M(3)

N, M = map(int, input().split())

s = []
def dsf():
    if len(s) == M:
        print(" ".join(map(str, s)))
        return

    for i in range(1, N+1):
        s.append(i)
        dsf()
        s.pop()

dsf()