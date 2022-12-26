l = int(input())
a = sorted(list(map(int,input().split())))
input()
b = list(map(int,input().split()))

for i in b:
    lt = 0
    rt = l - 1
    
    answer = 0
    while lt <= rt:
        mid = (lt+rt) // 2
        if a[mid] == i:
            answer = 1
            break
        elif a[mid] > i:
            rt = mid - 1
        else:
            lt = mid + 1
    print(answer)


'''
시간 초과 코드

input()
a = list(map(int,input().split()))
input()
b = list(map(int,input().split()))

for i in b:
    if i in a:
        print(1)
    else:
        print(0)
'''