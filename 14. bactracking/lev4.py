# 220123 / 백트래킹 / 15652 / N과 M(4)

N, M = map(int, input().split())

s = []
def dsf(start):
    if len(s) == M:
        print(" ".join(map(str, s)))
        return

    for i in range(start, N+1):
        s.append(i)
        dsf(i)
        s.pop()

dsf(1)