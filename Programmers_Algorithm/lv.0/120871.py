def solution(n):
    i = 0
    cnt = 0
    while(cnt < n):
        i += 1
        if i%3 != 0 and '3' not in list(str(i)):
            cnt += 1
    return i