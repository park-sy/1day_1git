# 220205 / 그리디 알고리즘 / 1931 / 회의실 배정
"""
0 6
1 4 
2 13
3 5
----3 8
5 7
----5 9
6 10
8 11
----8 12
12 14
"""
n = int(input())
m = []
for i in range(n):
    m.append(list(map(int,input().split())))

m = sorted(m,key = lambda x: x[0])
m = sorted(m,key = lambda x: x[1])


last = 0
cnt = 0
for i,j in m:
    if i >= last:
        cnt += 1
        last = j

print(cnt)