# 220713 / 정렬 / 국영수
import sys
input = sys.stdin.readline

n = int(input())
student = []
for _ in range(n):
    name, kor, eng, math = map(str,input().split())
    student.append([name,int(kor),int(eng),int(math)])


student = sorted(student, key = lambda x : (-x[1], x[2], -x[3], x[0]))

for i in range(n):
    print(student[i][0])
