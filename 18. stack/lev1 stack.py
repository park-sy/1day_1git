# 220210 / 스택 / 10828 / 스택
import sys
input = sys.stdin.readline
n = int(input())
arr = []

for i in range(n):
    a = list(map(str, input().split()))

    
    if a[0] == 'push':
        arr.append(int(a[1]))
    elif a[0] == 'pop':
        if arr:
            print(arr.pop())
        else:
            print(-1)  
    elif a[0] == 'size':
        print(len(arr))
    elif a[0] == 'empty':
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(arr) == 0:
            print(-1)
        else: print(arr[-1])
    
"""
# 220210 / 스택 / 10828 / 스택
import sys
input = sys.stdin.readline
arr = []
n = int(input())

for i in range(n):
    a = input()
    a1 = a.split()
    if a1[0] == 'push':
        arr.append(int(a1[1]))
    else:
        if a == 'pop':
            if len(arr) == 0:
                print(-1)
            else:
                print(arr.pop())   
        elif a == 'size':
            print(len(arr))
        elif a == 'empty':
            if len(arr) == 0:
                print(1)
            else:
                print(0)
        else:
            if len(arr) == 0:
                print(-1)
            else: print(arr[-1])
    
이건 왜 안될까
"""