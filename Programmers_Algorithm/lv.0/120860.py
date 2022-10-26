def solution(dots):
    answer = 0
    for i in range(1,4):
        if dots[0][0] != dots[i][0] and dots[0][1] != dots[i][1]:
            answer = (dots[0][0] - dots[i][0]) * (dots[0][1] - dots[i][1])
            break
    return abs(answer)