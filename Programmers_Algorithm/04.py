from pyparsing import counted_array


def solution(array):
    answer = -1
    max_key = 0
    dic = {}

    #딕셔너리 자료형에 값, 빈도를 입력해넣는다.
    for i in array:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    max_key = max(dic.values())

    for i in dic:
        if dic[i] == max_key and answer != -1:
            answer = -1
            break
        elif dic[i] == max_key:
            answer = i
    return answer

arr = [1, 1, 2, 2]
print(counted_array(arr, 1))

print(solution(arr))