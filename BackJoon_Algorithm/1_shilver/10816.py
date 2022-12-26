from sys import stdin
l = int(stdin.readline())
a = sorted(list(map(int,stdin.readline().split())))
stdin.readline()
m = list(map(int,stdin.readline().split()))

dic = {}
for i in a:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

for i in m:
    if i in dic:
        print(dic[i], end=' ')
    else:
        print(0, end=' ')