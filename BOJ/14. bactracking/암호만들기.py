# 220920 / 암호만들기
import sys
input = sys.stdin.readline

n,m = map(int,input().split())

e = ['a','e','i','o','u']

st = list(map(str,input().split()))
st.sort()

def dfs(pw,s,t,idx):
    if s+t == n:
        if s > 0 and t > 1:
            print(pw)
        return

    for i in range(idx,m):
        if st[i] in e:
            dfs(pw+st[i],s+1,t,i+1)
        else:
            dfs(pw+st[i],s,t+1,i+1)
        

dfs("",0,0,0)