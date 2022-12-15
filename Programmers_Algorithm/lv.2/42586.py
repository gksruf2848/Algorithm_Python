import math

def solution(progresses, speeds):
    lst = []
    answer = []
    
    for i in range(len(progresses)):
        lst.append(math.ceil((100-progresses[i]) / speeds[i]))
        
    imsi = lst[0]
    cnt = 1
    for i in range(1, len(lst)):
        if imsi < lst[i]:
            answer.append(cnt)
            imsi = lst[i]
            cnt = 1
        else:
            cnt += 1
    answer.append(cnt)
    return answer
    