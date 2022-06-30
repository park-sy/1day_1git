# 211219 1차원 배열 단계 7
# 문제번호 4344 / 평균은 넘겠지
import sys

C = int(input())
for i in range(C):
    arr = list(map(int,sys.stdin.readline().split()))
    sum = 0
    count = 0
    for j in range(arr[0]):
        sum = sum + arr[j+1]
    aver = sum /arr[0]
    
    for j in range(arr[0]):
        if arr[j+1] > aver :
            count = count + 1
    
    print('%.3f%%'%(count/arr[0]*100))
    
