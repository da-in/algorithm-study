def solution(plans):
    working = []
    answer = []
    cur_time = 0

    def cal_time(s):
        h, m = map(int, s.split(":"))
        return h * 60 + m    

    plans = list(map(lambda x : [x[0], cal_time(x[1]), int(x[2])], plans))
    plans.sort(key=lambda x : x[1])


    for plan in plans:
        name, st_time, work_time = plan
        gap_time = st_time - cur_time
        while working and gap_time > 0:
            if working[-1][1] > gap_time:
                working[-1][1] -= gap_time
                break
            else:
                gap_time -= working[-1][1]
                done , _ = working.pop()
                answer.append(done)
        working.append([name,work_time])
        cur_time = st_time

    while working:
        name, _ = working.pop()
        answer.append(name)
    return answer
