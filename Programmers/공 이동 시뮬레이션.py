# 220911 / 공 이동 시뮬레이션
def solution(n, m, x, y, queries):
    answer = 0
    queries.reverse()
    sx,sy,ex,ey = x,y,x,y
    for q, move in queries:
        if q == 0:
            if sy == 0:
                ey = min(m-1,ey+move)
            else:
                if sy + move >=m: return 0
                sy = min(m-1,sy+move)
                ey = min(m-1,ey+move)
        elif q == 1:
            if ey == m-1:
                sy = max(0,sy-move)
            else:
                if ey - move < 0: return 0
                sy = max(0,sy-move)
                ey = max(0,ey-move)
        elif q == 2:
            if sx == 0:
                ex = min(n-1,ex+move)
            else:
                if sx + move >= n: return 0
                sx = min(n-1,sx+move)
                ex = min(n-1,ex+move)
        else:
            if ex == n-1:
                sx = max(0,sx-move)
            else:
                if ex - move < 0: return 0
                sx = max(0,sx-move)
                ex = max(0,ex-move)

    answer = (ex - sx+1) * (ey - sy+1)
    
    return answer