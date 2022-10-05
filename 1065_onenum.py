def find_onenum(x):
    a, b, c = int(x/100), int(x/10%10), int(x%10)
    if b-a == c-b:
        return True
    else:
        return False

n = int(input())

if n == 1000:
    print(144)
elif n < 100:
    print(n)
else:
    cnt = 99
    for i in range(100, n+1):
        if find_onenum(i):
            cnt += 1
    print(cnt)
