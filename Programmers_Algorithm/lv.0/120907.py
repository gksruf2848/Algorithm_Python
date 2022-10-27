def solution(quiz):
    imsi = []
    answer = []
    for i in quiz:
        imsi = i.split(" = ")
        if eval(imsi[0]) == int(imsi[1]):
            answer.append("O")
        else:
            answer.append("X")
    return answer