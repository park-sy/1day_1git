# 220216 / 분할정복 / 10830 / 행렬제곱
def power(a, b, m):
    if b == 1: # b의 값이 1이면 a % C를 return한다.
        return m
    elif b == 2:
        return matrix(a, m,m)
    else:
        temp = power(a, b // 2, m) # a^(b // 2)를 미리 구한다.
        if b % 2 == 0:
            return matrix(a, temp,temp) # b가 짝수인 경우
        else:
            return matrix(a, matrix(a, temp,temp), m) # b가 홀수인 경우


def matrix(n,m1,m2):
    mat = []
    for i in range(n):
        row = []
        for j in range(n):
            rst = 0
            for k in range(n):
                rst += m1[i][k]*m2[k][j]
            row.append(rst)
        mat.append(row)
    
    for i in range(n):
        for j in range(n):
            mat[i][j] %= 1000
    return mat

n, b = map(int,input().split())
m = []
C = 1000
for i in range(n):
    m.append(list(map(int,input().split())))
result = power(n,b,m)
for i in range(n):
    for j in range(n):
        print(result[i][j]%1000,end=' ')
    print('')
