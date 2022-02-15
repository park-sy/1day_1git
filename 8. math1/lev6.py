# 211228 / 기본수학1 단계 6
# 2775 / 부녀회장이될테야

T = int(input())

for x in range(T):
    k = int(input())
    n = int(input())
    arr = []
    num = 0
    for i in range(k+1):
        for j in range(n):
            if i == 0:
                num = num + 1
                arr.append(num)
            else:
                if j == 0:
                    arr[j] = 1
                else:
                    arr[j] = arr[j] + arr[j-1]                
    print(arr[n-1])




