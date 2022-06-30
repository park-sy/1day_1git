# 220210 / 스택 / 9012 / 괄호
import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    brk = input().strip()
    brl = 0
    for j in range(len(brk)):
        if brl < 0:
            break
        if brk[j] =='(':
            brl +=  1
        else: brl -=1
    if brl == 0:
        print('YES')
    else: print('NO')
