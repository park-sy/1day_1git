# 220724 / 멀쩡한 사각형
import math
def solution(w,h):
    g = math.gcd(w,h)
    total = w * h
    
    return total -(w+h-g)