def solution(spell, dic):
    spell = sorted(spell)
    for i in dic:
        i = sorted(list(i))
        if i == spell:
            return 1
    return 2