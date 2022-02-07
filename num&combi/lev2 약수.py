# 220207 / 정수론과 조합론 / 1037 / 약수
import sys 
input = sys.stdin.readline()
n = int(input())

common = list(map(int, input().split()))

print(min(common)*max(common))