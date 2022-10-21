def solution(n):
    answer = []
    flag = True
    while(flag == True):
        for i in range(2, n + 1):
            print(i, n, flag, answer)
            if(n == i):
                answer.append(i)
                flag = False
            elif(n % i == 0):
                answer.append(i)
                n = n // i
                break
    return sorted(list(set(answer)))

print(solution(12))