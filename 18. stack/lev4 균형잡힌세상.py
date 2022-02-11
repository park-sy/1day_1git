# 220211 / 스택 / 4949 / 균형잡힌 세상

while 1:
    w = input()
    if w == '.':
        break
    res = True
    stk = []
    for i in w:
        if i == '(' or i == '[':
            stk.append(i)
        elif i == ')':
            if not stk or stk[-1] == '[':
                res = False
                break  
            stk.pop()

        elif i == ']':
            if not stk or stk[-1] == '(':
                res = False
                break  
            stk.pop()

    if res == True and not stk:
        print('yes')
    else: print('no')   



