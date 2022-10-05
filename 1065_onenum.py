n = int(input())

if n == 1000:
    print(144)
elif n < 100:
    print(n)
else:
    cnt = 99
    for i in range(100, n+1):
        if i//10%10 - i//100 == i%10 - i//10%10:
            cnt += 1
    print(cnt)