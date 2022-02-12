#220212 / 큐,덱 / 18258 / 큐2

import sys
input = sys.stdin.readline
n = int(input())
arr = []
top = 0
rear = -1
for i in range(n):
    a = list(map(str, input().split()))

    if a[0] == 'push':
        arr.append(int(a[1]))
        rear += 1
    elif a[0] == 'pop':
        if top <= rear:
            print(arr[top])
            top += 1
        else:
            print(-1)  
    elif a[0] == 'size':
        print(rear - top+1)
    elif a[0] == 'empty':
        if top > rear:
            print(1)
        else:
            print(0)
    elif a[0] == 'front':
        if top > rear:
            print(-1)
        else: print(arr[top])
    else:
        if top > rear:
            print(-1)
        else:print(arr[rear])
