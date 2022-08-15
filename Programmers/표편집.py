# 220815 / 표편집

def solution(n, k, cmd):
    answer = ["O" for _ in range(n)]
    col = {i:[i-1,i+1] for i in range(n)}
    stk = []
    col[0] = [None,1]
    col[n-1] = [n-2, None]
 
    for c in cmd:
        q = list(map(str,c.split()))
        
        if q[0] == "C":
            answer[k] = "X"
            prev, next = col[k]
            stk.append([prev,k,next])
            if next == None:
                k = col[k][0]
            else:
                k = col[k][1]
            if prev == None:
                col[next][0] = None
            elif next == None:
                col[prev][1] = None
            else:
                col[prev][1] = next
                col[next][0] = prev
                
        elif q[0] == "Z":
            prev, now, next = stk.pop()
            answer[now] = "O"
            if prev == None:
                col[next][0] = now
            elif next == None:
                col[prev][1] = now
            else:
                col[next][0] = now
                col[prev][1] = now
                
        elif q[0] == "U":
            for _ in range(int(q[1])):
                k = col[k][0]
        elif q[0] == "D":
            for _ in range(int(q[1])):
                k = col[k][1]

    
        
    return "".join(answer)