# 230107 / 1,2,3 떨어트리기
def solution(edges, target):
    global flag
    answer = []
    
    flag = 0
    n = len(target) + 1
    g = [[] for i in range(n)]
    for a,b in edges:
        g[a].append(b)
        
    len_g = [0] * n
    now_g = [0] * n
    locations = [[] for i in range(n)]
    for i in range(n):
        len_g[i] = len(g[i])
        g[i].sort()
    
    def fall_tree(now):
        global flag
        if not len_g[now]:
            idx = len(answer)
            if target[now-1]:
                if target[now-1] > 3:
                    answer.append(3)
                    target[now-1] -= 3
                else:
                    answer.append(target[now-1])
                    target[now-1] = 0
                    
            else:
                flags = True
                for i in locations[now]:
                    if answer[i] > 1:
                        answer[i] -= 1
                        answer.append(1)
                        flags = False
                        break
                if flags: flag = 1

            locations[now].append(idx)
            if flag == 0 and sum(target) == 0:
                flag = 2

            return

        next = now_g[now]
        now_g[now] = (next+1)%len_g[now]
        
        fall_tree(g[now][next])
        return
    
    def distribute(target_len, now_len, now_sum, target_sum):
        if target_len == now_len:
            if target_sum - now_sum == 0:
                return True
            return False
        for i in range(1,4):
            if now_len + 1 < target_len and (target_sum - now_sum - i) / (target_len - now_len - 1) > 3: continue
            arr.append(i)
            if distribute(target_len, now_len+1, now_sum+i, target_sum):
                return True
            arr.pop()
            
    while(not flag):
        fall_tree(1)
    
    if flag == 1:
        return [-1]
    
    for loc in locations:
        if not loc: continue
        arr = []
        temp = 0
        for i in loc:
            temp += answer[i]
        distribute(len(loc), 0, 0, temp)
        
        for i, num in enumerate(arr):
            answer[loc[i]] = arr[i]

    return answer