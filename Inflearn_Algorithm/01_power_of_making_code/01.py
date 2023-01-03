def solution(n, k):
    answer = -1
    cnt = 0
    for i in range(1, n+1):
        if n % i == 0:
            cnt += 1
        if cnt == k:
            answer = i
            break
    print(answer)

solution(6, 3)
