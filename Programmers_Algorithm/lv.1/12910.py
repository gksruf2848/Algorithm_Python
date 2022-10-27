def solution(arr, divisor):
    answer = [i for i in arr if i%divisor == 0]
    return sorted(answer) if len(answer) != 0 else [-1]

#빈 리스트를 false로 인식하기 때문에 or 연산자를 사용할 수도 있음 (대박)
def solution(arr, divisor):
    return sorted([i for i in arr if i%divisor == 0]) or [-1]