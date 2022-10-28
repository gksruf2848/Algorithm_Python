def solution(my_str, n):
    answer = []
    l = len(my_str)
    for i in range(l // n):
        answer.append(my_str[i*n:i*n+n])
    if l % n != 0:
        answer.append(my_str[l%n*-1:])
    return answer