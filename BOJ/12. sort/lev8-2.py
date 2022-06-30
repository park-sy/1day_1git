#220120 / 정렬 / 1181 / 단어정렬
import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    arr.append(input().strip())

arr2 = list(set(arr))
arr3 = []
for i in arr2:
    arr3.append([i, len(i)])

arr4 = sorted(arr3, key=lambda x: (x[1], x[0]))
    
for i in range(len(arr4)):
    print(arr4[i][0])
