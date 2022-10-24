def solution(numbers):
    item = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i, val in enumerate(item):
        numbers = numbers.replace(val, str(i))
    return int(numbers)