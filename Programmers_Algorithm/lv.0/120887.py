def solution(i, j, k):
    item = ''
    for _ in range(i, j+1):
        item += str(_)
    return list(map(str,item)).count(str(k))