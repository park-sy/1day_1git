#220116 / 정렬 / 2751 / 수정렬하기2
N = int(input())
num = []

for i in range(N):
    num.append(int(input()))
    
num.sort()

for i in num:
    print(i)