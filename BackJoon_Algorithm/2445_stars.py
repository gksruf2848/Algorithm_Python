n = int(input())

for _ in range(n):
    print('*'*(_+1) + ' '*(n-1-_)*2 + '*'*(_+1))
for _ in range(n-1):
    print('*'*(n-1-_) + ' '*(_+1)*2 + '*'*(n-1-_))