# 220713/ 정렬 / 안테나

n = int(input())
h = list(map(int,input().split()))

h.sort()
print(h[(n-1)//2])