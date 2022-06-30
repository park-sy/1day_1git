#220212 / 큐,덱 / 11866 / 요세푸스 문제 0

n, k = map(int,input().split())

yose = [i for i in range(1,n+1)]
od = []
l = n
dex = k - 1 
while True:
    
    od.append(yose.pop(dex))
    if len(yose)== 0:
        break
    dex = (dex + k - 1)%len(yose)

print("<",end='')
for i in range(n):
    if i == n-1:
        print(od[i],end='>')
    else:
        print(od[i],end=', ')