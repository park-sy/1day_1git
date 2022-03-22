# 220322 / 트리 / 5639 / 이진검색트리
import sys
sys.setrecursionlimit(10**6)

preorder = []
while True:
    try:
        num=int(input())
        preorder.append(num)
    except:
        break

n = len(preorder)

def divide(left,right): 
    if left > right: 
        return 
    else:
        id = right + 1
        for i in range(left+1,right+1):
            if preorder[left] < preorder[i]:
                id = i
                break
        
        divide(left+1,id-1)
        divide(id,right) 
        print(preorder[left]) 
    
divide(0,n-1)