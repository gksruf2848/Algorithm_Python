def solution(my_string):
    table = str.maketrans('','','qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')
    answer = list(map(int,my_string.translate(table)))
    return sum(answer)