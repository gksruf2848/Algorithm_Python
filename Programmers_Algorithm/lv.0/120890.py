def solution(array, n):
    array.append(n)
    array = sorted(array)
    i = array.index(n)
    
    if array[i] == array [0]:
        return array [1]
    elif array[i] == array [-1]:
        return array[-2]
    elif array[i] - array[i-1] == array[i+1] - array[i]:
        return array[i-1]
    elif array[i] - array[i-1] > array[i+1] - array[i]:
        return array[i+1]
    else:
        return array[i-1]