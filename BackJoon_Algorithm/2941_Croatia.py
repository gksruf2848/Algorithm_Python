str = input()

#print(len(str) - str.count('c=') - str.count('c-') - str.count('dz=') - str.count('d-')
#    - str.count('lj') - str.count('nj') - str.count('s=') - str.count('z='))

for i in ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']:
    str = str.replace(i, 'a')
print(len(str))