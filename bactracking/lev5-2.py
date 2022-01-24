# 220124 / 백트래킹 / 9663 / N-Queen

def queen(n):
    if n == N:
        global cnt
        cnt += 1
    else:
        for i in range(N):
            if clist[i]:
                continue
            chess[n] = i
            if check(n):
                clist[i] = True
                queen(n+1)
                clist[i] = False


def check(n):
    for i in range(n):
        if (chess[n] == chess[i]) or (n-i == abs(chess[n]-chess[i])):
            return False
    return True

N = int(input())
chess = [0 for i in range(N)]
clist = [False for _ in range(N)]
cnt = 0

queen(0)

print(cnt)