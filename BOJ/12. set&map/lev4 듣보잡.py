# 220513 / 집합과맵 / 1764 / 듣보잡
import sys
input = sys.stdin.readline

n,m = map(int,input().split())

d = []
for _ in range(n):
    d.append(input().rstrip())

d = set(d)
cnt = 0
db = []
for _ in range(m):
    bo = input().strip()
    if bo in d:
        db.append(bo)
        cnt+=1
print(cnt)
db = sorted(db)
for i in db:
    print(i)