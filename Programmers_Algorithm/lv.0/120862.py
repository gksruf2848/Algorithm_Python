def solution(numbers):
    answer = 0
    for i in range(len(numbers)):
        print(i)
        for j in range(i, len(numbers)):
            print(i,j)
            if answer < numbers[i]*numbers[j]:
                answer = numbers[i]*numbers[j]
    return answer

print(solution([1, 2, -3, 4, -5]))