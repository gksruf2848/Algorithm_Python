def solution(answers):
    answer = [0,0,0]
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    l = len(answers)
    for i in range(l):
        if answers[i] == one[i%5]:
            answer[0] += 1
        if answers[i] == two[i%8]:
            answer[1] += 1
        if answers[i] == three[i%10]:
            answer[2] += 1
    max_score = max(answer)
    return [i+1 for i in range(3) if max_score == answer[i]]