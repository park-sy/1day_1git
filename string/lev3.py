# 211222 / 문자열 단계 3
# 문제번호 10809 / 알파벳 찾기

S = list(input())

A = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in A:
    for j in range(len(S)):
        if i not in S:
            print(-1,end=' ')
            break
        elif i == S[j] :
            print(j,end=' ')
            break

