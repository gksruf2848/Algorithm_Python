def solution(a, b, n):
    answer = 0
    while n >= a:
        tmp = n // a
        answer += tmp * b
        n = n - (tmp * a) + (tmp * b)
    return answer