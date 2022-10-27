def solution(babbling):
    answer = 0
    for i in babbling:
        i = i.replace("aya", "A").replace("ye", "B").replace("woo","C").replace("ma","D")
        if i.isupper():
            answer += 1
            imsi = "X"
            for j in range(len(i)):
                if i[j] == imsi:
                    answer -= 1
                    break
                imsi = i[j]
    return answer