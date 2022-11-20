def solution(n):
    if n % 2 == 1:
        return 2
    else:
        for i in range(1, n//2 + 1):
            if n % i == 1:
                return i
        return n - 1