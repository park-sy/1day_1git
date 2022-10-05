


import operator
dict = {'A' : 1, 'D' : 4, 'C' : 3, 'B' : 2}
sdict = sorted(dict.items(), key=operator.itemgetter(1))# 인자값에 있는 key=operator.itemgetter(0)는 정렬하고자 하는 키 값을 0번째 인덱스 기준으로 하겠다는 것입니다.# 0번째 인자는 Key입니다.
