# 220511 / 집합과 맵 / 14425 / 문자열 집합

n, m = map(int,input().split())

strs = []
for _ in range(n):
    strs.append(input())
strs = set(strs)
cnt = 0
for _ in range(m):
    a = input()
    if a in strs:
        cnt+= 1

print(cnt)
