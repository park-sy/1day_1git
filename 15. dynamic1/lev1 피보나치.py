#220125 / 동적계획법1 / 1003 / 피보나치 함수


N = int(input())
for i in range(N):
    arr = [[1,0],[0,1]]
    n = int(input())
    if n == 0:
        print(1,0)
    elif n == 1:
        print(0,1)
    else:
        for j in range(2,n+1):
            arr.append([arr[j-2][0]+arr[j-1][0],arr[j-2][1]+arr[j-1][1]])
        print(arr[n])
