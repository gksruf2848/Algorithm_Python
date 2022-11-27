def solution(lines):
    answer = 0
    all = [0 for i in range(201)]
    for i in range(3):
        for j in range(lines[i][0] + 100, lines[i][1] + 100):
            all[j] += 1

    for i in range(0, 201):
        if all[i] != 0 and all[i] != 1:
            answer += 1
    return answer