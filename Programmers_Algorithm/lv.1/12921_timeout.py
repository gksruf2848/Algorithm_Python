def sosu(n):
    for i in range(2,n):
        if n%i==0:
            return 0
    return 1

def solution(n):
    answer = 0
    for i in range(2,n+1):
        if sosu(i):
            answer += 1
        
    return answer