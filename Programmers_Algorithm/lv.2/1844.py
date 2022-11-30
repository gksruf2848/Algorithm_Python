from collections import deque

def solution(maps):
    answer = -1
    
    d = [[0,1],[0,-1],[1,0],[-1,0]]
    check = []
    for i in range(len(maps)):
        check.append([False for _ in range(len(maps[0]))])

    q = deque()
    q.append([0,0,False,0])
    
    while(len(q)>0):
        tmp = q.pop()
        #목표에 도달했을 경우
        if tmp[0] == len(maps)-1 and tmp[1] == len(maps[0])-1:
            answer = tmp[3] #cnt
            break
        
        for i in range(4):
            xx = tmp[0] + d[i][0]
            yy = tmp[1] + d[i][1]
            
            
            #범위 밖으로 벗어나는지 확인
            if (xx not in range(len(maps))) or (yy not in range(len(maps[0]))):
                continue
            
            #벽인지 확인
            if maps[xx][yy] == 0:
                continue
                
            
            #다녀왔던 곳인지 확인
            if check[xx][yy] == True:
                continue
            
            check[xx][yy] = True
            q.append([xx,yy,check,tmp[3]+1])
            check[xx][yy] = False        
    
    return answer