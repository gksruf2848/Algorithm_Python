lst = [i for i in range(1, 31)]
for i in range(28):
    lst.remove(int(input()))
print(str(lst[0])+'\n'+str(lst[1]))