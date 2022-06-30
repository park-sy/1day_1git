# 220206 / 그리디 알고리즘 / 1541 / 잃어버린 괄호

"""
1. 입력을 숫자, +- 로 나눠 받기
2. - 앞에서 괄호치기
"""


f = list(input().split('-'))

s_list = []
for i in range(len(f)):
    if '+' in f[i]:
        s = list(map(int, f[i].split('+')))
        s_list.append(sum(s))
    else:
        s_list.append(int(f[i]))

res = s_list[0]*2
for i in s_list:
    res -= i

print(res)
