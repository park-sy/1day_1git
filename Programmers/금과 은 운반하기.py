# 220912 / 금과 은 운반하기
def solution(a, b, g, s, w, t):
    answer = (10**9) * (10 ** 5) * 4
    start, end = 0, (10**9) * (10 ** 5) * 4
    n = len(g)
    while start <= end:
        mid = (start+end) // 2
        gold = 0
        silver = 0
        total = 0
        
        for i in range(n):
            ng = g[i]
            ns = s[i]
            nw = w[i]
            nt = t[i]
            
            move_cnt = mid //(nt*2)
            
            if mid % (nt*2) >= nt:
                move_cnt += 1
            
            gold += ng if (ng < move_cnt*nw) else move_cnt * nw
            silver += ns if (ns < move_cnt*nw) else move_cnt * nw
            total += ng + ns if (ng+ns < move_cnt * nw) else move_cnt * nw
        
        if gold >= a and silver >=b and total >= a+ b:
            end = mid - 1
            answer = min(answer,mid)
        else:
            start = mid + 1
    return answer