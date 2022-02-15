# 211224 / 문자열 단계 8
# 문제번호 5622 / 다이얼

list1 = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']


word = input().upper()
sum = 0
for i in word:
    for j in list1:
        if i in j:
            sum += list1.index(j) + 3

print(sum)
