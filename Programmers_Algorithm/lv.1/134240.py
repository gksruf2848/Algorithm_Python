def solution(food):
    answer = []
    for i in range(len(food)):
        if food[i]%2 == 1:
            food[i] -= 1
    for i in range(1, len(food)):
        for j in range(food[i]//2):
            answer.append(str(i))
    return ''.join(answer) + '0' + ''.join(reversed(answer))