# 220106 / 기본수학2 레벨9
# 4153 / 직각삼각형

while True:
    n = list(map(int,input().split()))
    if n[0] == n[1] == n[2] == 0:
        break

    if n[0]**2 + n[1]**2 + n[2]**2 == (max(n)**2)*2:
        print('right')
    else: print('wrong')
