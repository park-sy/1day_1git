# 211221 함수 단계 2
# 문제번호 4673 / 셀프 넘버

def d(n):
   arr = list(map(int,list(str(n))))
   num = n + sum(arr)
   return num

arr =[]
for i in range(10000):
    arr.append(i+1)

for i in range(10000):
    if d(i) in arr:
        arr.remove(d(i))

for i in range(len(arr)):
    print(arr[i])