n, m = map(int,input().split())
trees = list(map(int,input().split()))

lt, rt = 0, max(max(trees), m)
while lt <= rt:
    mid = (lt + rt) // 2
    sum = 0
    for tree in trees:
        if mid < tree:
            sum += tree - mid
    if sum >= m:
        lt = mid + 1
    else:
        rt = mid - 1
print(mid)