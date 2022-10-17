def solution(n, numlist):
    answer = []
    for i in numlist:
        if (i / n).is_integer():
            answer.append(i)
    return answer