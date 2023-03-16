def solution(routes):
    routes.sort(key=lambda x: x[1])

    camera = 0
    last_loc = -30000

    for start, end in routes:
        if start > last_loc:
            camera += 1
            last_loc = end

    return camera
