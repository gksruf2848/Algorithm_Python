one, two, three = map(int, input().split())

if one == two == three:
    print(10000 + one * 1000)
elif one == two or one == three:
    print(1000 + one * 100)
elif two == three:
    print(1000 + three * 100)
else:
    print(max(one, two, three) * 100)