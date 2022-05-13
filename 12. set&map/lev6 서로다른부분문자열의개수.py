# 220513 / 집합과맵 / 11478 / 서로 다른 부분 문자열의 개수

s = input().strip()
slen = len(s)
sec = []
for i in range(1,slen+1):
    for j in range(slen+1-i): 
        sec.append(s[j:j+i])
sec = set(sec)
print(len(sec))