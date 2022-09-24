from collections import defaultdict
from copy import deepcopy
def solution(commands):
    answer = []

    g = [[""]*5 for _ in range(5)]
    d = defaultdict(set)
    m = [[set()]*5 for _ in range(5)]
    

    for c in commands:
        print(c)
        c = c.split()
        lc = len(c)
        if c[0] == "UPDATE":
            if lc == 3:
                w1,w2 = c[1],c[2]
                while d[w1]:
                    x,y = d[w1].pop()
                    g[x][y] = w2
                    d[w2].add((x,y))
            else:
                r,c,w = int(c[1]),int(c[2]),c[3]
                pre = g[r][c]
                g[r][c] = w
                d[w].add((r,c))
                
                for x,y in m[r][c]:
                    g[x][y] = w
                    m[r1][c1].add((x,y))
                    d[w].add((x,y))
                    d[pre].remove((x,y))

                
        elif c[0] == "MERGE":
            r1,c1,r2,c2 = int(c[1]),int(c[2]),int(c[3]),int(c[4])
            word = g[r1][c1]
            g[r2][c2] = word
            d[word].add((r2,c2))
            for x,y in m[r2][c2]:
                g[x][y] = word
                m[r1][c1].add((x,y))
                d[word].add((x,y))
            m[r2][c2] = m[r1][c1]
            
            m[r1][c1].add((r2,c2))
            m[r2][c2].add((r1,c1))

        elif c[0] == "UNMERGE":
            r1,c1 = int(c[1]),int(c[2])
            temp = g[r1][c1]

            while m[r1][c1]:
                x,y = m[r1][c1].pop()
                g[x][y] = ""
            g[r1][c1] = temp

        else:
            r1,c1 = int(c[1]),int(c[2])
            print(r1,r2)
            if g[r1][c1] == "":
                answer.append("EMPTY")
            else:
                answer.append(g[r1][c1])
        
        for i in g:
            print(i)
        
    return answer

inp = [
["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]
]

output = [
    
["EMPTY", "group"]
]


len_sol = len(inp)
for i in range(len_sol):
    commands =inp[i]
    ans = solution(commands)
    print(i+1,"번째:",ans, end = ' ')
    if ans == output[i]:
        print("  pass")
    else:
        print("  fail")