def solution(numbers, direction):
    answer = numbers
    if direction == "right":
        for i in range(len(numbers)):
            print(answer, numbers)
            answer[(i+1)%len(numbers)] = numbers[i]
    else:
        for i in range(len(numbers)):
            answer[i] = numbers[(i+1)%len(numbers)]
    return answer


arr = [1, 2, 3]
print(solution(arr, "right"))