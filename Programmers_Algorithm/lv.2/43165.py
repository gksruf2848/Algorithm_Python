def dfs(numbers, target, k, n, s):
    if k == n:  # k번째 수가 n개의 수 중 마지막 수일 경우
        if s == target:  # 총합이 target과 같으면
            return 1  # 해당 경우의 수 1 반환
        else:
            return 0  # 아니면 0 반환
    else:  # k번째 수가 n개의 수 중 마지막 수가 아닐 경우
        cnt = 0  # 해당 경우의 수 카운트
        cnt += dfs(numbers, target, k+1, n, s + numbers[k])  # k번째 수를 더한 경우
        cnt += dfs(numbers, target, k+1, n, s - numbers[k])  # k번째 수를 빼는 경우
        return cnt  # 해당 경우의 수 반환

def solution(numbers, target):
    n = len(numbers)  # numbers의 원소 개수
    return dfs(numbers, target, 0, n, 0)  # dfs 함수 호출