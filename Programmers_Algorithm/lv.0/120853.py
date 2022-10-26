def solution(s):
    answer, i = 0, 1
    s = s.split(' ')
        
    while(i < len(s) and i >= 0):
        if s[0] == 'Z':
            s.pop(0)
            
        print(i, s)
        if s[i] == 'Z':
            if s[i-1] != 'Z':
                s.pop(i)
                s.pop(i-1)
                i -= 2
            else:
                s.pop(i)
                i -= 1
        i += 1
    
    return sum(list(map(int,s)))


print(solution("Z Z 10 20 Z Z 1"))