# 220701 / 정렬 / 성적이 낮은 순서로 학생 출력하기
n = int(input())
std = []
for _ in range(n):
    name, score = map(str, input().split())
    std.append([name, int(score)])

std = sorted(std, key = lambda x : x[1])

for i in range(n):
    print(std[i][0], end = ' ')