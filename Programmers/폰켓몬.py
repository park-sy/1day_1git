# 220808 / 폰켓몬

from collections import Counter
def solution(nums):
    answer = 0
    n = len(nums)
    
    c = Counter(nums)
    k = len(c)
    if k > n//2:
        answer = n//2
    else:
        answer = k

    return answer