def solution(score):
    s = [sum(i) for i in score]
    s_s = sorted(s,reverse=True)
    return [s_s.index(i)+1 for i in s]