def solution(array, commands):
    answer = []
    for i in commands:
        imsi = sorted([array[j] for j in range(i[0]-1,i[1])])
        answer.append(imsi[i[2]-1])
    return answer