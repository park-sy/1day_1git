# 220320 / 트리 / 1991 / 트리 순회
n = int(input())

tree = [[]for _ in range(n+1)]
for i in range(n):
    p,n1,n2 = map(str,input().split())
    a,b,c = ord(p),ord(n1),ord(n2)
    tree[a-65].append(b-65)
    tree[a-65].append(c-65)

def forder(start):
    if start == -19:
        return
    else:
        print(chr(start+65),end='')
        forder(tree[start][0])
        forder(tree[start][1])

def morder(start):
    if start == -19:
        return
    else:
        morder(tree[start][0])
        print(chr(start+65),end='')
        morder(tree[start][1])
def border(start):
    if start == -19:
        return
    else:
        border(tree[start][0])
        border(tree[start][1])
        print(chr(start+65),end='')

forder(0)
print('')
morder(0)
print('')
border(0)