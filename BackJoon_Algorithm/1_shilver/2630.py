num = int(input())
s = [list(map(int, input().split())) for i in range(num)]
result = [0, 0]

def fun(x, y, n):
  l = s[x][y]
  for i in range(x,x+n):
    for j in range(y,y+n):
      if s[i][j] != l:
        n //= 2
        fun(x,y,n)
        fun(x+n,y,n)
        fun(x,y+n,n)
        fun(x+n,y+n,n)
        return
  if l == 0:
    result[0] += 1
  else:
    result[1] += 1

fun(0,0,num)
print(result[0])
print(result[1])