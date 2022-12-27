T = int(input())
for i in range(T):
    N, s, e, k = map(int, input().split())
    lst = list(map(int, input().split()))

    print("#%d %d" %(i+1, sorted(lst[s-1:e])[k-1]))
