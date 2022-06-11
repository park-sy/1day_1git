# 220611 / 트리 / 5639 / 이진검색트리
import sys
input = sys.stdin.readline
pre = []
while True:
    try:
        n = int(input())
        pre.append(n)
    except:
        break

def postorder(left,right):
    if left > right:
        return
    id = right + 1
    for i in range(left,right):
        if pre[left] < pre[i]:
            id = i
            break
    postorder(left+1,id-1)
    postorder(id,right)
    print(pre[left])

postorder(0,len(pre)-1)
        