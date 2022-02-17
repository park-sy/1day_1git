# 220216 / 분할정복 / 6549 / 히스토그램에서 가장 큰 직사각형
# 히스토그램에서 가장 큰 직사각형을 찾는 문제. 분할 정복으로도 풀 수 있고, 
# 스택으로 풀 수도 있습니다.

import sys 
input = sys.stdin.readline

while True:
    h = list(map(int, sys.stdin.readline().split())) + [0]
    if h[0] == 0:
        break
    n = h[0]
    stack = [(1,h[1])]
    res = 0
    for i in range(2,n+2):
        w = i
        #나보다 stack에 있는 h가 더 높으면 꺼내서 (나의 높이 * 너비)
        while stack and stack[-1][1] > h[i]:
            w, hi = stack.pop()
            res = max(res, (i-w)*hi)
        stack.append((w, h[i]))
    print(res)





