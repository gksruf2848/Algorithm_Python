a = [1, 1, 2, 2, 2, 8]
b = input().split(' ')

for i in range(len(a)):
    print(a[i] - int(b[i]), end=" ")