def solution(my_string):
    answer = []
    for i in list(my_string):
        if i not in answer:
            answer.append(i)
    return ''.join(answer)