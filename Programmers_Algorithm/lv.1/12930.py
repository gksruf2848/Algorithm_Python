def solution(s):
    index = 0
    s = list(s.lower())
    for i in range(len(s)):
        if s[i] == ' ':
            index = -1
        elif index % 2 == 0:
            s[i] = s[i].upper()
        index += 1
    return ''.join(s)