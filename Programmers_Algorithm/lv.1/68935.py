def solution(n):
    imsi = []
    answer = 0
    while(n>0):
        imsi.append(n%3)
        n = n // 3
    imsi.reverse()
    for i in range(len(imsi)):
        answer += imsi[i] * (3**i)
    return answer