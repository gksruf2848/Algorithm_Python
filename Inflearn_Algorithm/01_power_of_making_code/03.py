n, k = map(int, input().split())
cards = list(map(int, input().split()))

imsi = set()
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            imsi.add(cards[i]+cards[j]+cards[m])

print(sorted(imsi)[len(imsi)-k])