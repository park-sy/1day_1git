#220209 / 정수론과 조합론 / 2004 / 조합 0의 개수

a, b = map(int, input().split())

def fin_num(n, k):
    cnt = 0
    while n:
        n = n // k
        cnt += n
    return cnt

five = fin_num(a,5) - fin_num(b,5) - fin_num(a-b, 5)
two = fin_num(a,2) - fin_num(b,2) - fin_num(a-b, 2)

print(min(five,two))