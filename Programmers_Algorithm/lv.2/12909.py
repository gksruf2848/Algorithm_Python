from collections import deque

def solution(s):
    q = deque()
    q.append(s[0])
    
    for i in range(1, len(s)):
        q.append(s[i])
        if len(q) > 1:
            if q[-2] == '(' and q[-1] == ')':
                q.pop()
                q.pop()
            
    return True if len(q) == 0 else False