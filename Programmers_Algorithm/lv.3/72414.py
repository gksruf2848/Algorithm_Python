def solution(play_time, adv_time, logs):
    play_time, adv_time = change_form(play_time), change_form(adv_time)
    for i in range(len(logs)):
        logs[i] = [change_form(logs[i][0:8]),change_form(logs[i][9:17])]
    
    #타임라인 만들기
    all_time = [0 for i in range(play_time + 1)]
    
    #시청 시작 지점, 끝 지점을 체크해준다.
    for i in range(len(logs)):
        all_time[logs[i][0]] = 1
        all_time[logs[i][1]] = -1
    
    #체크를 바탕으로 중간 지점을 1로 채움
    for i in range(1, len(all_time)):
        all_time[i] = all_time[i] + all_time[i-1]
    
    #코드를 한 번 더 실행하여 누적합을 구함
    for i in range(1, len(all_time)):
        all_time[i] = all_time[i] + all_time[i-1]
        
    
    
    
    return all_time

#형태를 초 형태로 바꿔줌
def change_form(time):
    time = list(map(int,time.split(':')))
    return time[0] * 60 * 60 + time[1] * 60 + time[2]