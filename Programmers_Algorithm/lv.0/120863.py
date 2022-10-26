def solution(polynomial):
    answer = [0,0]
    polynomial = polynomial.split(' + ')

    for i in polynomial:
        if i == 'x':
            answer[0] += 1
        elif i[-1] == 'x':
            answer[0] += int(i[:-1])
        else:
            answer[1] += int(i)
            
    if answer[0] == 0 and answer[1] == 0:
        return "0"
    elif answer[0] == 0:
        return str(answer[1])
    elif answer[0] == 1 and answer[1] == 0:
        return "x"
    elif answer[0] == 1:
        return "x + " + str(answer[1])
    elif answer[1] == 0:
        return str(answer[0]) + "x"
    else:
        return str(answer[0]) + "x + " + str(answer[1])