def solution(numlist, n):
    answer = []
    insi = 0
    for i in range(len(numlist)):
        min_n = 10000
        for j in range(len(numlist)):
            if n - numlist[j] == min_n:
                pass
            elif abs(n - numlist[j]) <= min_n:
                min_n = abs(n - numlist[j])
                imsi = j
        answer.append(numlist.pop(imsi))
    return answer


print(solution([1, 2, 3, 4, 5, 6],4))