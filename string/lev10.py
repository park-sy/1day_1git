# 211225 / 문자열 단계 10
# 문제번호 1316 / 그룹 단어 체커

n = int(input())
count = 0
for i in range(n):
    word = input()
    d={}
    for j in range(len(word)):
        if d.get(word[j]) == None:
            d[word[j]] = 1
        elif word[j] == word[j-1]:
            pass
        else: d[word[j]] += 1
    num = 1
    for i in d:
        if d.get(i) > 1:
            num = 0
    count += num

print(count)
    
