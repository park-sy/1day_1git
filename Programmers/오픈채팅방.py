#220726 / 오픈채팅방
def solution(record):
    n = len(record)
    message = []
    user = {}
    for i in range(n):
        k = record[i].split(" ")
        if k[0] == "Enter":
            user[k[1]] = k[2]
            message.append([1,k[1]])
        elif k[0] == "Leave":
            message.append([0,k[1]])
        else:
            user[k[1]] = k[2]
    answer = []
    for q,u in message:
        if q == 1:
            answer.append("%s님이 들어왔습니다."%user[u])
        elif q==0:
            answer.append("%s님이 나갔습니다."%user[u])
    
    
    return answer