def solution(s):
    if len(s) == 1:
        return s
    
    s = sorted(list(s))
    answer = ''
    
    if s[0] != s[1]:
        answer += s[0]
    for i in range(1, len(s)-1):
        if s[i-1] != s[i] and s[i] != s[i+1]:
            answer += s[i]
    if s[-1] != s[-2]:
        answer += s[-1]
        
    return answer