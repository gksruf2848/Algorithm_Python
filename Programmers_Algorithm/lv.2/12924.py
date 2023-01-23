def solution(n):
    answer = 0
    for i in range(1, n+1):
        s = 0
        j = i
        while s <= n:
            if s == n:
                answer += 1
                break
            s += j
            j += 1
    return answer