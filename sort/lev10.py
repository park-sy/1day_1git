# 220120 / 정렬 / 18870 / 좌표 압축
import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
arr2 = list(set(arr))
arr2.sort()
arr_dict = {}
for i in range(len(arr2)):
    arr_dict[arr2[i]] = i

for i in range(N):
    print(arr_dict[arr[i]], end=' ')
# for i in range(N):
#     cnt = 0
#     for j in arr2:
#         if arr[i] > j:
#             cnt += 1
#     print(cnt, end=' ')
