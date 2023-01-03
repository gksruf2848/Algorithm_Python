from collections import deque

def solution(n, lost, reserve):
    answer = [2 if i+1 in reserve else 1 for i in range(n)]
    for i in lost:
        answer[i-1] -= 1

    answer = deque(answer)
    answer.appendleft(-1)
    answer.append(-1)

    for i in range(1,len(answer)):
        '''
        if answer[i] == 0 and i == 0:
            if answer[i+1] == 2:
                answer[i+1] -= 1
                answer[0] += 1
        elif answer[i] == 0 and i == n-1:
            if answer[i-1] == 2:
                answer[i-1] -= 1
                answer[n] += 1
                '''
        if answer[i] == 0:
            if answer[i-1] == 2:
                answer[i-1] -= 1
                answer[i] += 1
            elif answer[i+1] == 2:
                answer[i+1] -= 1
                answer[i] += 1

    return n - answer.count(0)