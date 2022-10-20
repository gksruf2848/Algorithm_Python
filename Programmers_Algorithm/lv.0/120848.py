def solution(n):
    answer = 1
    for i in range(2, n+1):
        print(i, answer)
        if answer < n:
            answer *= i
            print(i, answer)
        else:
            print(i, answer)
            answer = i - 1
            break
    return answer

print(solution(3628800))