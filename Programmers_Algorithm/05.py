def solution(denum1, num1, denum2, num2):
    answer = [denum1 * num2 + denum2 * num1, num1 * num2]
    for i in reversed(range(2, min(answer))):
        if answer[0] % i == 0 and answer[1] % i == 0:
            answer[0] //= i
            answer[1] //= i
    return answer