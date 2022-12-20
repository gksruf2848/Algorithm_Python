from itertools import permutations

def solution(numbers):
    answer = list(permutations(numbers,len(numbers)))

    for i in range(len(answer)):
        answer[i] = list(map(str, answer[i]))
        answer[i] = ''.join(answer[i])
    
    return max(answer)