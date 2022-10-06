str = input()

print(len(str) - str.count('c=') - str.count('c-') - str.count('dz=') * 2 - str.count('d-')
    - str.count('lj') - str.count('nj') - str.count('s=') - str.count('z='))