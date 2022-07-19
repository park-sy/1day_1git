# 220719 / 이진탐색 / 정렬된 배열에서 특정 수의 개수 구하기
import sys,bisect
input = sys.stdin.readline

n,x = map(int,input().split())
nums = list(map(int,input().split()))


l = bisect.bisect_left(x,nums)
r = bisect.bisect_right(x,nums)

print(r-l)
