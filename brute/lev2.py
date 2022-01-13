#220113 / 브루트포스 / 2231 / 분해합

N = int(input())

make = []

n1 = 100001
n2 = 10001
n3 = 1001
n4 = 101
n5 = 11
n6 = 2
result = 1000000
count = 0
for i1 in range(10):
    for i2 in range(10):
        for i3 in range(10):
            for i4 in range(10):
                for i5 in range(10):
                    for i6 in range(10):
                        if i1*n1 + i2*n2 + i3*n3 + i4*n4 + i5*n5 + n6*i6 == N:
                            count += 1
                            result = min(result, 100000*i1 + 10000*i2 + 1000*i3 + 100*i4 + 10*i5 + 1*i6)

if count == 0 :
    print(0)
else:
    print(result)