def solution(s):
    answer = [-1]
    for i in range(1,len(s)):
        cnt = 0
        for j in reversed(range(i)):
            cnt += 1
            if s[i] == s[j]:
                break
            elif j == 0:
                cnt = -1
                break
        answer.append(cnt)
    return answer