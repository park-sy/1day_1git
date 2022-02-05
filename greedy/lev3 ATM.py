# 220205 / 그리디 알고리즘 / 11399 / ATM

n = int(input())
t = list(map(int,input().split()))

t.sort()
s = 0
t1 = []
for i in range(n):
    s += t[i]
    t1.append(s)
print(sum(t1))