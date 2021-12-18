# 1차원 배열 단계 1
# 문제번호 10818 / 최소, 최대
import sys

num = int(input())
data = list(map(int,sys.stdin.readline().split()))


print(min(data), max(data))