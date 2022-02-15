# 211229 / 기본수학1 단계 9
# 1011 / fly me to the alpha centauri
"""
1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
1 2 3 3 4 4 5 5 5 6 6 6 7 7 7 7 8 8 8 8 9 9 9 9 9
"""
T = int(input())
for i in range(T):
    x,y = map(int,input().split())
    distance = y - x
    count = 0
    move = 1
    move_plus = 0
    while move_plus < distance:
        count+=1
        move_plus += move
        if count % 2 == 0:
            move += 1

    print(count)
    