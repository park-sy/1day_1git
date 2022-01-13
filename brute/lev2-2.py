#220113 / 브루트포스 / 2231 / 분해합

N = int(input())

for i in range(1,N+1):
    num = i + sum(list(map(int, str(i))))
    
    if num == N:
        print(i)
        break
    if i == N:
        print(0)