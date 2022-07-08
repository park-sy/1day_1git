# 220708 / 구현 / 문자열 재정렬

sen = input().rstrip()

res = 0
arr = []
for i in sen:
    if ord(i) >= 65:
        arr.append(i)
    else: res += int(i)

arr.sort()
if res != 0:
    arr.append(res)
for i in arr:
    print(i,end='')