# 220214 / 큐,덱 / 5430 / AC
import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    p = input().strip()
    n = int(input().strip())
    arr = input().strip()
    if n == 0 and 'D' in p:
        print('error')
        continue
    arr = list(arr[1:-1].split(','))
    e = False
    cnt = 0
    for j in p:
        if j == 'R':
            cnt += 1        
        else:
            if len(arr) == 0:
                e = True
                break
            else:
                if cnt % 2 == 0:
                    arr.pop(0)
                else:
                    arr.pop()

    if e == True:
        print('error')
    else:
        if cnt % 2 == 0:
            print("["+",".join(arr)+"]")
        else:
            print("["+",".join(arr[::-1])+"]")
