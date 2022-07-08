#220708 / 구현 / 자물쇠와 열쇠
def solution(key, lock):

    n,m = len(lock), len(key)
    new_lock = [[0]*(n*3) for _ in range(n*3)]
    
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]
    
    for rotation in range(4):
        key = rolling(key,m)
        for x in range(n*2):
            for y in range(n*2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                if check(new_lock,n):
                    return True
                for i in range(m):
                    for j in range(m):
                        new_lock[x][y] -= key[i][j]
                        
    return False


def rolling(arr,m):
    arr2 = [[0]*m for _ in range(m)]
    
    for i in range(m):
        for j in range(m):
            arr2[j][n-i-1] = arr[i][j]
            
    return arr2

def check(chk,n):
    for i in range(n):
        for j in range(n):
            if chk[i+n][j+n] != 1:
                return False
    return True