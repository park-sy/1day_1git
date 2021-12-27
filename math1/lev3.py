# 211226 / 기본수학1 단계 3
# 문제번호 1193 / 분수찾기
# 1 2 3 4 5 6 7 8 9 10
# 1 1 2 3 2 1 1 2 3 4 5 4 3 2 1
# 1 2 1 1 2 3 4 3 2 1 1 2 3 4 5 6 5 4 3 2 1
# 2 3 3 4 4 4 5 5 5 5 6 6 6 6  

# 1  2  6  7  15 16
# 3  5  8  14
# 4  9  13
# 10 12
# 11
n = int(input())

line = 0
end = 0
while n > end:
    line += 1
    end += line

diff = end - n
if line%2 == 0: #짝수 라인 일때
    top = line - diff
    bottom = diff + 1
else:
    top = diff + 1
    bottom = line - diff

print("%d/%d"%(top,bottom))




