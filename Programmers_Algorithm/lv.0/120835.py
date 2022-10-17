def solution(emergency):
    dic = {}
    #딕셔너리로 변환해주고 정렬
    for i in range(len(emergency)):
        dic[i] = emergency[i]
    dic = sorted(dic, key=lambda x:dic[x], reverse=True)
    
    #인덱스 값과 매칭해넣기
    for i in range(len(emergency)):
        emergency[dic[i]] = i + 1
    return emergency

lst = [30, 10, 23, 6, 100]
print(solution(lst))