def solution(balls, share):
    a, b = 1, 1
    for i in range(balls - share + 1, balls + 1):
        a *= i
        print(i, end=' ')
    print()
    for i in range(1, share + 1):
        b *= i
        print(i, end=' ')
    return a/b

print(solution(30,20))