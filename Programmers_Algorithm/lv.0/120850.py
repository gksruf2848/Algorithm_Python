from string import ascii_letters

def solution(my_string):
    table = str.maketrans('','',ascii_letters)
    return sorted(list(map(int,my_string.translate(table))))