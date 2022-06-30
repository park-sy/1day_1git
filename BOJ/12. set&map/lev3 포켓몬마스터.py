# 220512 / 집합과맵 / 1620 / 나는야 포켓몬 마스터 이다솜
import sys
input = sys.stdin.readline

n,m = map(int,input().split())

pdic = {}
for i in range(1,n+1):
    pok = input().rstrip()
    pdic[i] = pok
    pdic[pok] = i

for _ in range(m):
    ans = input().rstrip()
    if ans.isdigit():
        print(pdic[int(ans)])
    else:
        print(pdic[ans])
