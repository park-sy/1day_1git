# 220806 / 작업 처리하기
from collections import Counter
tasks = [1,1,2,2]
c = Counter(tasks).most_common()

ans = 0
for i in c:
    if i[1] == 1:
        print(-1)
        break
    ans += (i[1]-1)//3 + 1

print(ans)
