# 220825 / 길 찾기 게임
import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)
def solution(nodeinfo):
    preanswer = []
    postanswer = []
    def preorder(arr,answer):
        root = arr[0]
        larr = []
        rarr = []
        
        for i in range(1,len(arr)):
            if root[0] > arr[i][0]:
                larr.append(arr[i])
            else:
                rarr.append(arr[i])
        answer.append(root[2])
        if larr:
            preorder(larr,answer)
        if rarr:
            preorder(rarr,answer)
            
    def postorder(arr,answer):
        root = arr[0]
        larr = []
        rarr = []
        
        for i in range(1,len(arr)):
            if root[0] > arr[i][0]:
                larr.append(arr[i])
            else:
                rarr.append(arr[i])
        
        if larr:
            postorder(larr,answer)
        if rarr:
            postorder(rarr,answer)
        answer.append(root[2])
        
    n = len(nodeinfo)
    for i in range(1,n+1):
        nodeinfo[i-1].append(i)

    node = sorted(nodeinfo, key = lambda x : (-x[1], x[0]))
    preorder(node,preanswer)
    postorder(node,postanswer)
    return [preanswer,postanswer]