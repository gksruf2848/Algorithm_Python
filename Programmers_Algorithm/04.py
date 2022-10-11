def solution(array):
    dic = {}
    for i in array:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
        print(dic)
    max = max(dic.values())
    for i in range(len(dic)):
        if dic[i] == max:
            
    
    return max(dic.values())

arr = [1,2,3,3,4,5]
print(solution(arr))