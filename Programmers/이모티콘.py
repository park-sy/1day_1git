#220925 / 이모티콘
from copy import deepcopy
def solution(users, emoticons):
    answer = [0,0]
    n = len(emoticons)

    def dfs(emo,idx):
        print(idx)
        if idx == n:
            print(emo)
            total = 0
            sub = 0
            for sale, price in users:
                u_total = 0
                for i, e in enumerate(emo):
                    if e >= sale:
                        u_total += emoticons[i]*(100-sale)
                if price < u_total:
                    sub += 1
                else:
                    total += u_total
            if answer[0] <= sub:
                answer[0] = sub
                if answer[1] <= total:
                    answer[1] = total
            return 

            
            

        new_emo = deepcopy(emo)
        for i in [10,20,30,40]:
            new_emo.append(i)
            dfs(new_emo,idx+1)

    dfs([],0)
    return answer