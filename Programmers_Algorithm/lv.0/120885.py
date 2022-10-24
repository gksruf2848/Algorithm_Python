def solution(bin1, bin2):
    return format(int(('0b'+bin1),2) + int(('0b'+bin2),2), 'b')