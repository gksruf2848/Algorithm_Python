from collections import deque

def solution(A, B):
    if A == B:
        return 0

    A, B = deque(A), deque(B)
    answer = -1
    for i in range(len(B)):
        A.rotate(1)
        if A == B:
            answer = i + 1
            break
    return answer