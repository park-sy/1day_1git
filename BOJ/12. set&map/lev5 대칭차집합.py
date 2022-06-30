# 220513 / 집합과맵 / 1269 / 대칭 차집합

n,m = map(int,input().split())
A = set(list(map(int,input().split())))
B = set(list(map(int,input().split())))
a = (A-B)
b = (B-A)

print(len(a)+len(b))
