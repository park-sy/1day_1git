# 220129 / 동적계획법1 / 1932 / 정수삼각형
"""
0
01
012
0123


"""
n = int(input())
level = []
for i in range(n):
    level.append(list(map(int, input().split())))



for i in range(1,n):
    for j in range(i+1):
        if j == 0:
            level[i][j] += level[i-1][j]
        elif j == i:
            level[i][j] += level[i-1][j-1]
        else:
            level[i][j] += max(level[i-1][j-1], level[i-1][j])
    
print(max(level[n-1]))