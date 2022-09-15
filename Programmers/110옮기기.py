# 220915 / 110 옮기기
import re
def solution(s):
    answer = []
    
    for word in s:
        stk = []
        cnt = 0 
        for w in word:
            if w == "0" and stk[-2:] == ["1","1"]:
                cnt += 1
                stk.pop()
                stk.pop()
            else:
                stk.append(w)
        new_word = "".join(stk)
        for _ in range(cnt):
            new_word = find(new_word)
        answer.append(new_word)
                
    
    return answer

def find(word):
    n = len(word)
    for i in range(n-1,-1,-1):
        if word[i] == "0":
            return word[:i+1]+"110"+word[i+1:]
    
    return "110"+word
    