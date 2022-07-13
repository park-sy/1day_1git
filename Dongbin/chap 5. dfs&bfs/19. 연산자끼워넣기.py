# 220713 / dfs bfs / 연산자 끼워넣기
import sys
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
nums = list(map(int,input().split()))
o = list(map(int,input().split()))

mnum = [INF,-INF]

temp = nums[0]
for i in range(1,n):
    temp = nums[i]

def dfs(num, seq,a,b,c,d):
    if seq == n :
        mnum[0] = min(num,mnum[0])
        mnum[1] = max(num,mnum[1])
        return 
    oper = [a,b,c,d]
    for op in range(4):
        if oper[op]:
            if op == 0:
                dfs(num+nums[seq],seq+1,a-1,b,c,d)
            elif op == 1:
                dfs(num-nums[seq],seq+1,a,b-1,c,d)
            elif op == 2:
                dfs(num*nums[seq],seq+1,a,b,c-1,d)
            elif op == 3:
                if num <0:
                    temp = (-num//nums[seq])*(-1)
                    dfs(temp,seq+1,a,b,c,d-1)
                else: dfs(num//nums[seq],seq+1,a,b,c,d-1)

dfs(nums[0],1,o[0],o[1],o[2],o[3])
print(mnum[1])
print(mnum[0])