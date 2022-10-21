import math

def solution(n):
    answer = 1
    for i in range(2, 12):
        if math.factorial(i) > n:
            answer = i - 1
            break
    return answer

print(solution(1))