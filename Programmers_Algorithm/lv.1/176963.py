def solution(name, yearning, photo):
    answer = []
    for i in range(len(photo)):
        for j in range(len(photo[i])):
            for k in range(len(name)):
                if photo[i][j] == name[k]:
                    photo[i][j] = yearning[k]
            if isinstance(photo[i][j], str):
                photo[i][j] = 0
        answer.append(sum(photo[i]))
    return answer