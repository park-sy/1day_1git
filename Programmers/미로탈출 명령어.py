# 230110 / 미로 탈출 명령어
import heapq
def solution(n, m, x, y, r, c, k):
    answer = ''
    dx = [1,0,0,-1]
    dy = [0,-1,1,0]
    dw = ['d','l','r','u']

    if (abs(x-r)+abs(y-c)) % 2 != k % 2: return "impossible"

    q = [["",0,x-1,y-1]]
    while q:
        str, cnt, ax, ay = heapq.heappop(q)
        if (ax, ay) == (r-1,c-1) and cnt == k: return str
        
        if abs(ax-r+1)+abs(ay-c+1) > k - cnt: continue
        for i in range(4):
            nx = ax + dx[i]
            ny = ay + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                heapq.heappush(q, [str+dw[i], cnt+1, nx, ny])
    
    return "impossible"