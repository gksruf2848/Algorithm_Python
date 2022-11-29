from collections import deque

def solution(priorities, location):
    a = deque(priorities)
    cnt = 0
    while(len(a)>0):
        print(list(a),location)
        if max(a) > a[0]:
            if location == 0:
                location += len(a) - 1
            else:
                location -= 1
            a.rotate(-1)
        else:
            cnt += 1
            if location == 0:
                return cnt
            location -= 1
            a.popleft()