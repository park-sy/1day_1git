# 220207 / 정수론과 조합론 / 5086 / 배수와약수

while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    
    if b % a == 0:
        print('factor')
    elif a % b == 0:
        print('multiple')
    else: print('neither')