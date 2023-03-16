def solution(routes):
    answer = 1
    routes.sort(key=lambda x: x[1])
    cam=routes[0][1]
    for r in routes[1:]:
        if r[0]>cam:
            cam=r[1]
            answer+=1
    return answer