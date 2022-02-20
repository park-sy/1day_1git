# 220220 / 이분탐색 / 12015 / 가장 긴 증가하는 부분 수열 2

n = int(input())
A = list(map(int,input().split()))
m = [0]


for i in A:
    if m[-1] < i:
        m.append(i)
    else:
        left, right = 0, len(m)
        while left < right:
            mid = (left + right) // 2
            
            if m[mid] < i :
                left = mid + 1
            else:
                right = mid
        m[right] = i

print(len(m)-1)

                