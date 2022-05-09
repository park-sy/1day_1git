# 220509 / 이분탐색 / 12015 / 가장 긴 증가하는 부분 수열 2

n = int(input())
nums = list(map(int,input().split()))
seq = [0]

for i in nums:
    if seq[-1] < i:
        seq.append(i)
    else:
        left, right = 0,len(seq)
        while left < right:
            middle = (left+right)//2

            if seq[middle] < i:
                left = middle + 1
            else:
                right = middle
        seq[right] = i
print(len(seq)-1)


            

