# 220510 / 집합과 맵 / 10815 / 숫자카드

n = int(input())
sg = list(map(int,input().split()))
m = int(input())
comp = list(map(int,input().split()))

for i in comp:
    if i in sg:
        print(1, end=' ')
    else:
        print(0, end=' ')