def solution(arrows):
    answer = 0
    start = (0, 0)
    visit = {}
    visit_dir = {}
    visit[start] = 1
    route = {0: [-1, 0], 1: [-1, 1], 2: [0, 1], 3: [1, 1],
         4: [1, 0], 5: [1, -1], 6: [0, -1], 7: [-1, -1]}

    for val in arrows:
        for _ in range(2):
            dy, dx = route[val]
            y, x = start
            ny, nx = y+dy, x+dx
            if (ny, nx) in visit and ((y, x), (ny, nx)) not in visit_dir:
                answer += 1
            else:
                visit[(ny, nx)] = 1
            visit_dir[((y, x), (ny, nx))] = 1
            visit_dir[((ny, nx), (y, x))] = 1
            start = (ny, nx)
    return answer
