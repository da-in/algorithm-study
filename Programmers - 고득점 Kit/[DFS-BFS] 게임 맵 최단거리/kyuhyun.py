from collections import deque
def solution(maps):
    point = deque()
    max_x = len(maps[0])
    max_y = len(maps)
    move = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    # 방문처리 배열
    visit = [([0] * max_x) for i in range(max_y)]
    # 시작노드 넣기
    point.append([0, 0])
    visit[0][0] = 1
    

    while point:
        y, x = point.popleft()
        if x == max_x-1 and y == max_y-1:
            return visit[-1][-1]
        for move_y, move_x in move:
            nx = x + move_x
            ny = y + move_y
            if (nx < 0 or nx >= len(maps[0])) or (ny < 0 or ny >= len(maps)):
                continue
            if visit[ny][nx] != 0:
                continue
            if maps[ny][nx] == 1:
                point.append([ny, nx])
                visit[ny][nx] = visit[y][x] + 1
    return -1

