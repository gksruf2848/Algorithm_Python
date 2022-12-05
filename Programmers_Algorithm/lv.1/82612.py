def solution(price, money, count):
    answer = (price + price * count) * count * 0.5 - money
    return answer if answer > 0 else 0