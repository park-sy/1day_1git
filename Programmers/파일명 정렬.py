# 220904 / 파일명 정렬
def solution(files):
    answer = []
    file_spl = []
    for i,file in enumerate(files):
        num = 0
        end = 0
        for j,w in enumerate(file):
            if num and not w.isdigit():
                end = j
                break
            elif not num and w.isdigit():
                num = j

        a = file[:num].lower()
        if end == 0: b = int(file[num:])  
        else: b = int(file[num:end])

        file_spl.append([a,b,i])

    file_spl.sort()
    for a,b,c in file_spl:
        answer.append(files[c])
    return answer