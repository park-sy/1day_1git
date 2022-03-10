# 220310 / 투포인터 / 3273 / 두 수의 합

n = int(input())
arr = list(map(int,input().split()))
arr.sort()
x = int(input())
cnt = 0
start = 0
end = 0


while start < end:
    tmp = arr[start] + arr[end]
    if tmp == x:
        cnt += 1
    if tmp < x:
        start += 1
        continue
    end -= 1

print(cnt)
