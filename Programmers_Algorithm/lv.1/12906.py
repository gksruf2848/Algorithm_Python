from collections import deque

def solution(arr):
    q = deque([-1])
    for _ in arr:
        if q[-1] != _:
            q.append(_)
    q.popleft()
    return list(q)