def solution(s, n):
    answer = ''
    low = 'abcdefghijklmnopqrstuvwxyz'
    up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in s:
        if i in low:
            tmp = low.index(i)
            answer += low[(tmp+n)%26]
        elif i in up:
            tmp = up.index(i)
            answer += up[(tmp+n)%26]
        else:
            answer += i
    return answer
    