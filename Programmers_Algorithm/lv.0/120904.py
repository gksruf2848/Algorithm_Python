def solution(num, k):
    return list(str(num)).index(str(k)) + 1 if str(k) in list(str(num)) else -1

#좀 더 가독성 좋게 정리한 방식
def solution(num, k):
    num_list = list(map(int,str(num)))
    return num_list.index(k) + 1 if k in num_list else -1