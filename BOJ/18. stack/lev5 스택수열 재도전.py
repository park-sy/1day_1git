# 220426 / 스택 / 1874 / 스택수열
import sys
input = sys.stdin.readline

n = int(input())
cnt = 1
stk = []
prt = []
for _ in range(n):
    num = int(input())

    while(cnt <= num):
        stk.append(cnt)
        prt.append('+')
        cnt += 1
    
    if stk[-1] == num:
        prt.append('-')
        stk.pop()

if stk:
    print('NO')
else:
    for i in range(len(prt)):
        print(prt[i])