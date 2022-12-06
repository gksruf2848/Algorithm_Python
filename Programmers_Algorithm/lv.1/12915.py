def solution(strings, n):
    answer = {}
    for _ in range(len(strings)):
        answer[strings[_][n]] = strings[_]
    return sorted()