import math

def solution(n):
    answer = 1
    for i in range(2, n + 1):
        if math.factorial(i) > n:
            answer = i - 1
            break
    return answer






print(solution(3628799))
print(solution(3628000))
print(solution(720))
print(solution(719))
print(solution(1000))
print(solution(3628800))