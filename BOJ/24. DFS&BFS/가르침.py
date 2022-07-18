# 220718 / dfs bfs / 1062 / 가르침
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
word = []
for _ in range(n):
    word.append(input().rstrip())

s = ["a","n","t","i","c"]
learn = [0] *(26)
for i in s:
    learn[ord(i)-ord("a")] = 1

if m < 5:
    print(0)
    sys.exit()
elif m == 26:
    print(n)
    sys.exit()

res = 0
def dfs(idx,cnt):
    global res
    if cnt == m - 5:
        res = max(res,check())
        return
    for i in range(idx,26):
        if not learn[i]:
            learn[i] = 1
            dfs(i,cnt+1)
            learn[i] = 0


def check():
    cnt = n
    for i in range(n):
        for j in word[i]:
            if not learn[ord(j)-ord("a")]:
                cnt -= 1
                break

    return cnt

dfs(0,0)
print(res)