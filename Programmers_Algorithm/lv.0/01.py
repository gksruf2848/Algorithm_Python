def solution(arr):
    answer = 0

    a = list(map(int, arr[1:-1].split(',')))
    answer = sum(a)/len(a)
    
    return answer

#print(solution(input()))