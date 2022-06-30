# 220107 / 기본수학2 레벨 11
# 1002 / 터렛

def point(x, y, r):
    list1 =[]
    y2 = r
    for i in range(r+1):
        while i**2 + y2**2 > r**2 and y2 >=0:
            y2 -= 1
        
        if i**2 + y2**2 == r**2:
            list1.append([x+i,y+y2])
            list1.append([x-i,y+y2])
            list1.append([x-i,y-y2])
            list1.append([x+i,y-y2])
    list2 = []
    for i in list1:
        if i not in list2:
            list2.append(i)
    return list2

T = int(input())

for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    list1 = point(x1,y1,r1)
    list2 = point(x2,y2,r2)
    count = 0
    for i in list1:
        for j in list2:
            if i == j:
                count+=1
                break
                
    print(count)

    
