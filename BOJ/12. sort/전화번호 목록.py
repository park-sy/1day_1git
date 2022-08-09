# 220810 / 5052 / 전화번호 목록
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    num = []
    for _ in range(n):
        num.append(input().rstrip())
    num.sort()
    flag = 0
    print(num)
    for i in range(n-1):
        k = len(num[i])
        if num[i] == num[i+1][:k]:
            print("NO")
            flag = 1
            break
    if not flag:
        print("YES")