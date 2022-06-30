# 220408 / 기하 / 11758 / CCW
x = []
y = []
for _ in range(3):
    xn, yn = map(int,input().split())
    x.append(xn)
    y.append(yn)

temp = x[0]*y[1] + x[1]*y[2] + x[2]*y[0] - (y[0]*x[1] + y[1]*x[2] + y[2]*x[0])

if temp > 0:
    print(1)
elif temp < 0:
    print(-1)
else: print(0)