# 220228 / DFS와BFS / 1697 / 숨바꼭질
from collections import deque
import sys
n,k = map(int,input().split())
c = [0] * 100001
c[n] = 1
queue = deque([n])

while queue:
    a = queue.popleft()
    if a - 1 >= 0:
        if c[a-1] == 0:
            c[a-1] = c[a] + 1 
            queue.append(a-1)  

    if a + 1 <= 100000:
        if c[a+1] == 0:
            c[a+1] = c[a] + 1 
            queue.append(a+1)  

    if a * 2 <= 100000:
        if c[a*2] == 0:
            c[a*2] = c[a] + 1
            queue.append(a*2)

    if c[k] != 0:
        print(c[k] -1)
        break
