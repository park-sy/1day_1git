# 220323 / 트리 / 4803 / 트리
def treenum(g):
    flag = True
    stk = [g]
    while stk:
        node = stk.pop()
        if visit[node]:
            flag = False
        visit[node] = 1
        for i in tree[node]:
            if not visit[i]:
                stk.append(i)
    return flag

num = 0
while True:
    n, m = map(int,input().split())
    if n == m == 0:
        break
    tree = [[]for _ in range(n+1)]
    visit = [False]*(n+1)

    for i in range(m):
        n1, n2 = map(int,input().split())
        tree[n1].append(n2)
        tree[n2].append(n1)

    result = 0
    num += 1
    for i in range(1,n+1):
        if visit[i]:
            continue
        if treenum(i):
            result += 1

    print('Case %d: '%num,end='')
    if result == 0 :print('No trees.')
    elif result == 1: print('There is one tree.')
    else: print('A forest of %d trees.'%result)