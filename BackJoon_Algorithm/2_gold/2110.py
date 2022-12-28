from sys import stdin
n, c = map(int, stdin.readline().split())
houses = []
for i in range(n):
    houses.append(int(stdin.readline()))
houses.sort()

lt, rt = 1, houses[-1] - houses[0]
answer = 0
while lt <= rt:
    mid = (lt + rt) // 2
    current = houses[0]
    cnt = 1
    
    for i in range(1,n):
        if houses[i] >= current + mid:
            current = houses[i]
            cnt += 1
    
    if cnt < c:
        rt = mid - 1
    else:
        lt = mid + 1
        answer = mid

print(answer)
