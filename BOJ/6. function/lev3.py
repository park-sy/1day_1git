# 211221 함수 단계 3
# 문제번호 1065 / 한수

def han(n):
    num = n
    div = list(map(int,list(str(n))))
    for i in range(len(div)):
        if len(div) == 1 or len(div) == 2:
            break
        else:
            k = div[1] - div[0]
            if i == len(div)-1:
                break
            elif div[i+1] - div[i] != k:
                num = 0
    return num

N = int(input())
count = 0
for i in range(N):
    if han(i+1) != 0:
        count += 1

print(count)