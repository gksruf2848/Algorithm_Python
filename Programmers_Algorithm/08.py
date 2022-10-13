def solution(n):
    answer = 1
    for i in range(max(n, 6), n * 6 + 1):
        if n % i == 0 and 6 % i == 0:
            answer = i // 6
    return answer

print(solution(10))