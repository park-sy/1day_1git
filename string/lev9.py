# 211225 / 문자열 단계 9
# 문제번호 2941 / 크로아티아 알파벳

cro = ['c=','c-','dz=','d-','lj','nj','s=','z=']

word = input()

for i in cro:
    word = word.replace(i,'a')

print(len(word))
