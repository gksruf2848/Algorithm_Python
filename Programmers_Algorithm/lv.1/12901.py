def solution(a, b):
    days = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    answer = 0
    for i in range(1,a):
        if i in [1,3,5,7,8,10,12]:
            answer += 31
        elif i in [4,6,9,11]:
            answer += 30
        elif i == 2:
            answer += 29
    answer += b
    return days[answer%7]