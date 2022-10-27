def solution(a, b):
    return sum([i for i in range(min(a,b), max(a,b)+1)])

#for문을 쓸 필요가 없었다
def solution(a, b):
    return sum(range(min(a,b), max(a,b)+1))