#220105 / 기본수학2 레벨 7
#1082 / 직사각형에서 탈출

x,y,w,h = map(int,input().split())
distance = []

distance.append(x-0)
distance.append(y-0)
distance.append(w-x)
distance.append(h-y)

print(min(distance))
