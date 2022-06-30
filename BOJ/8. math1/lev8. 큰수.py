# 220424 / 기본수학1 / 10757 / 큰수 A+B
a,b =map(str,input().split())
ans = []
i = -1
plus = 0

while(1):
    if i*-1 >= len(a)+1 and i*-1 >= len(b)+1:
        if plus == 1:
            ans.append(1)
        break
    elif i*-1 >= len(a)+1 and i*-1 < len(b)+1:
        k = int(b[i]) + plus
    elif i*-1 >= len(b)+1 and i*-1 < len(a)+1:
        k = int(a[i]) + plus
    else: 
        k = int(a[i])+int(b[i]) + plus
        

    if k >= 10:
        ans.append(k%10)
        plus = 1
    else: 
        ans.append(k)
        plus = 0
    i -= 1

for i in range(1,len(ans)+1):
    print(ans[-i],end='')