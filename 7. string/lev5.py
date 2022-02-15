# 211223 / 문자열 단계 5
# 문제번호 1157 / 단어 공부

word = input().upper()

b = {}

for i in word:
    if b.get(i) == None:
        b[i] = 1
    else:
        b[i] += 1

max = max(b.values())

key = ''
sump = 0
for i in b:
    if b[i] == max:
        key = i
        sump += 1
if sump == 1:
    print(key)
else:
    print("?")
