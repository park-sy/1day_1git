# 220627 / dp3 / 11723 / 집합
import sys
input = sys.stdin.readline

n = int(input())
S = set()

for _ in range(n):
    query = input().strip().split()
    if len(query) == 1:
        if query[0] == 'all':
            S = set([i for i in range(1, 21)])
        elif query[0] == 'empty':
            S = set()
    else:
        q, num = query[0], qduery[1]
        num = int(num)
        if q == 'add':
            S.add(num)
        elif q == 'remove':
            S.discard(num)
        elif q == 'check':
            if num in S:
                print(1)
            else: print(0)
        elif q == 'toggle':
            if num in S:
                S.discard(num)
            else: S.add(num)

            
