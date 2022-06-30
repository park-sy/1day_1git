# 220216 / 분할정복 / 11444 / 피보나치6
# 행렬 곱셈을 응용해 피보나치 수를 구하는 문제

fibo = [[1],[1]]
co = [[1,1],[1,0]]

def power(a, b, m):
    if b == 1:
        return m
    elif b == 2:
        return matrix(m,m)
    else:
        temp = power(a, b // 2, m) 
        if b % 2 == 0:
            return matrix(temp,temp) 
        else:
            return matrix(matrix(temp,temp), m) 

def matrix(m1,m2):
    mat = []
    for i in range(2):
        row = []
        for j in range(len(m2[0])):
            rst = 0
            for k in range(2):
                rst += m1[i][k]*m2[k][j]
            row.append(rst%1000000007)
        mat.append(row)
    return mat

n = int(input())
if n <3:
    print(1)
else:
    result = matrix(power(2,n-2, co),fibo)
    print(result[0][0]%1000000007)