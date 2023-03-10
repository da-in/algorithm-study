def solution(routes):
    answer = 0
    routes.sort(key=lambda x:x[0])
    min_num = -300001
    for r in routes:
        if r[0] <= min_num:
            min_num = min(r[1], min_num)
        else:
            min_num = r[1]
            answer += 1
    return answer