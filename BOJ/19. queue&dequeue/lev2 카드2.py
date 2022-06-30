#220212 / 큐,덱 / 2164 / 카드2

n = int(input())
card = [i for i in range(1,n+1)]
cnt = 0
rear = len(card) -1
if n != 1:
    while True:
        if rear - cnt == 1:
            break
        cnt+=1
        card.append(card[cnt])
        cnt+=1
        rear+=1

print(card[rear])
