# 220120 / 정렬 / 1181 / 단어정렬


N = int(input())
word = {}
for i in range(N):
    key = input()
    word[key] = len(key)


word_list = []
cnt =0
for i in word:
    word_list.append([i,word[i]])
    cnt+=1

words= sorted(word_list, key = lambda x:(x[1],x[0]))
print(words)
for i in range(cnt):
    print(words[i][0])