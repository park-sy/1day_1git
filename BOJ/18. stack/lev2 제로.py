# 220210 / 스택 / 10773 / 제로
import sys
input = sys.stdin.readline
n = int(input())
stk = []
for i in range(n):
    k = int(input())
    if k == 0:
        stk.pop()
    else:
        stk.append(k)

print(sum(stk))