# 221012 / 단어 뒤집기2 / 17413

sen = input()

flag = 0
temp = ""
new_sen = ""
for i,w in enumerate(sen):
    if w == "<":
        new_sen += temp[::-1]
        flag = 1
        temp = ""

    if not flag and w == " ":
        new_sen += temp[::-1]+" "
        temp = ""
        continue 
    temp += w

    if w == ">":
        flag = 0
        new_sen += temp
        temp = ""

new_sen += temp[::-1]
print(new_sen)