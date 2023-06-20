def solution(k, m, score):
    score.sort()
    return sum(score[len(score)-m*i] * m for i in range(1,len(score)//m+1))