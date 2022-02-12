#220212 / 큐,덱 / 1966 / 프린터 큐
import sys


t = int(input())

for i in range(t):
    n, k = map(int,input().split())
    arr = list(map(int,sys.stdin.readline().split()))
    cnt = 0
    if n == 1:
        print(1)
    else:
        while True:
            if len(arr) == 1:
                cnt+=1
                print(cnt)
                break
            if arr[0] < max(arr[1:]):
                arr.append(arr.pop(0))
                if k == 0:
                    k = len(arr) - 1
                else:
                    k -= 1
                
            else:
                arr.pop(0)
                cnt+=1
                if k == 0:
                    print(cnt)
                    break
                else:
                    k -= 1
