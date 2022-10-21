from string import ascii_letters

def solution(my_string):
    table = str.maketrans(ascii_letters, ' ' * 52)      # 알파벳을 모두 공백처리함
    my_string = list(my_string.translate(table).split(' '))    # 공백을 기준으로 분리한다.

    while '' in my_string:
        my_string.remove('') # 잉여공백들을 모두 제거

    return sum(list(map(int, my_string)))