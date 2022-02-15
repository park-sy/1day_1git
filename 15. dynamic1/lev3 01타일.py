# 220127 / 동적계획법1 / 1904 / 01타일


n = int(input())
odd = []
even = []
cnt = 0
if n % 2 == 0:           
    for i in range(int(n/2)):
        if i == 0:
            even.append(2)
        else:
            even.append(even[i-1]*2+1)
    print(even[int(n/2)-1])

if n % 2 == 1:
    for i in range(int(n+1/2)-1): 

        if i == 0:
            odd.append(1)
        else:
            print(odd)
            odd.append(odd[i-1]*3-2+i+1)
    print(odd[int(n+1/2)-2])


"""
1
001 100 111
00001 00100 00111 10000
10011 11001 11111
 11110 


"""