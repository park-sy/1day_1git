#220126 / 동적계획법1 / 9184 /신나는 함수 실행

warr = [[[-1 for k in range(21)] for j in range(21)] for i in range(21)]

def w(a,b,c):


    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if warr[a][b][c] != -1:
        return warr[a][b][c]
    elif a < b and b < c:
        warr[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return warr[a][b][c]
    else:
        warr[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return warr[a][b][c]


while 1:
    a, b, c = map(int, input().split())
    if a == b == c == -1:
        break

    if a <= 0 or b <= 0 or c <= 0:
        print('w(%d, %d, %d) = %d'%(a,b,c,1))
    else:
        print('w(%d, %d, %d) = %d'%(a,b,c,w(a,b,c)))

