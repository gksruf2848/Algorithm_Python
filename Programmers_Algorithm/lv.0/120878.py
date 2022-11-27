def solution(a, b):
    for i in reversed(range(1, min(a, b) + 1)):
        if a % i == 0 and b % i == 0:
            b = b // i
            break
    a = 2
    while(b >= a):
        if b % a == 0:
            if a != 2 and a != 5:
                return 2
            b = b // a
        else:
            a += 1
    return 1