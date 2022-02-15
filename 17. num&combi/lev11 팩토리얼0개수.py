#  220208 / 정수론과 집합론 / 1676 / 팩토리얼 0의 개수

n = int(input())
f = 1
cnt = 0
for i in range(2, n+1):
    f *= i

fl = list(map(int,list(str(f))))
fl2 = fl[::-1]
    
for i in range(len(fl)):
    if fl2[i] == 0:
        cnt += 1
    else:
        break    

 

print(cnt)
