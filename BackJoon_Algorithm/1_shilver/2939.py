n = int(input())
cnt = 0
rst = -1

while n >= 0:
    if n%5 == 0:
        cnt += n // 5
        rst = cnt
        break
    n -= 3
    cnt += 1

print(rst)