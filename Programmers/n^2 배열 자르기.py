# n^2 배열 자르기 / 220913
def solution(n, left, right):
    answer = [0] * (right - left +1)
    for i in range(left, right + 1):
        d = i // n
        m = i % n
        answer[i-left] = m + 1 if m > d else d + 1

    return answer