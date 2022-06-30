#220114 / 브루트포스 / 1436 / 영화감독 숌

N = int(input())

count = 0
num = 665
while count < N:
    num+=1
    if '666' in str(num):
        count+=1

print(num)