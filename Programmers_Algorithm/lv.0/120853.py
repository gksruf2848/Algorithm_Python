def solution(s):
    answer = []
    s = s.split(" ")
    for i in range(len(s)-1):
        if s[i+1] != "Z" and s[i] != "Z":
            answer.append(s[i])
    if s[-1] != "Z":
        answer.append(s[-1])
    return sum(list(map(int,answer)))