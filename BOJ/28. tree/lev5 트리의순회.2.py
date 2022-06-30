# 220609 / 트리 / 5639 / 트리의 순회
import sys 
input = sys.stdin.readline

n = int(input())
inod = list(map(int,input().split()))
post = list(map(int,input().split()))

def find_location(val, arr):
    for i in range(len(arr)):
        if arr[i] == val:
            index = i
    return index

def pre(inod,post):
    root = post[-1]
    print(root, end = ' ')
    if len(inod) <= 1 or len(post) <= 1:
        return
    id1 = find_location(root, inod)
    if id1 >= len(inod): return
    id2 = find_location(inod[id1+1],post)
    pre(inod[:id1],post[:id2])
    pre(inod[id1+1:],post[id2:-1])

pre(inod,post)