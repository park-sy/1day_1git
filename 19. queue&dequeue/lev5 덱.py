# 220213 / 큐,덱 / 10866 / 덱
import sys
input = sys.stdin.readline


n = int(input())
d = []
for i in range(n):
    a = list(map(str, input().split()))

    if a[0] == 'push_front':
        d = d[::-1]
        d.append(int(a[1]))
        d = d[::-1]

    elif a[0] == 'push_back':
        d.append(int(a[1]))
    
    elif a[0] == 'pop_front':
        if not d:
            print(-1)
        else:
            print(d.pop(0))
    elif a[0] == 'pop_back':
        if not d:
            print(-1)
        else:
            print(d.pop())
    elif a[0] == 'size':
        print(len(d))
    elif a[0] == 'empty':
        if not d:
            print(1)
        else:
            print(0)
    elif a[0] == 'front':
        if not d:
            print(-1)
        else:
            print(d[0])
    else:
        if not d:
            print(-1)
        else:
            print(d[-1])