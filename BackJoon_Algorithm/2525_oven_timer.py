lst = input().split(' ')

h = int(lst[0])
m = int(lst[1])
cook = int(input())

tmp = m + cook

if tmp >= 60:
    h += int(tmp / 60)
    m = tmp % 60
    if h > 23:
        h -= 24
else:
    m = tmp

print(h, m)