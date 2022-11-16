def solution(num, total):
    a = int(total / num - num / 2 + 1 / 2)
    return [i for i in range(a, int(a+num))]