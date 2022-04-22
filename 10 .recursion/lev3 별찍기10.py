# 220422 / 재귀 / 2447 / 별찍기 10

n = int(input())

def star(a):
    div = a//3
    if a == 3:
        g[1] =['*',' ','*']
        g[0][:3] = g[2][:3] = ['*','*','*']
        return
    star(div)

    for i in range(0,a, div):
        for j in range(0,a,div):
            if i == div and j == div:
                continue
            for k in range(div):
                g[i+k][j:j+div] = g[k][:div]



g =[[' 'for _ in range(n)] for _ in range(n)]
star(n)
for i in range(n):
    for j in range(n):
        print(g[i][j],end='')
    print('')