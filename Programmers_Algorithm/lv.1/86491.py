def solution(sizes):
    w, h = 0, 0
    for i in range(len(sizes)):
        sizes[i].sort()
        if w < sizes[i][0]:
            w = sizes[i][0]
        if h < sizes[i][1]:
            h = sizes[i][1]
    return w*h