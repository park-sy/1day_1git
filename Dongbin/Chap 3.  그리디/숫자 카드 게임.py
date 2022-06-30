# 220630 / 그리디 / 숫자 카드 게임
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
max_card = 0
for _ in range(n):
    min_card = min(list(map(int,input().split())))
    max_card = max(max_card,min_card)

print(max_card)
