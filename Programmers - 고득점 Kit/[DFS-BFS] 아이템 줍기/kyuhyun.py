from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    
    d = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    _map = [[-2 for _ in range(102)] for _ in range(102)]
    visit = [[0 for _ in range(102)] for _ in range(102)]

    for point in rectangle:
        st_x, st_y, ed_x, ed_y = map(lambda x : x* 2, point)
        for i in range(st_x, ed_x+1):
            for j in range(st_y, ed_y +1):
                if st_x < i < ed_x and st_y < j < ed_y:
                    _map[j][i] = -1
                elif _map[j][i] != -1:
                    _map[j][i] = 0              
        
    route = deque()
    route.append([characterY * 2, characterX * 2])        

    while route:
        y, x = route.popleft()
    
        if y == itemY * 2 and x == itemX * 2:
            return visit[y][x] // 2

        for dy, dx in d:
            ny = y + dy
            nx = x + dx
            if _map[ny][nx] == 0 and visit[ny][nx] == 0:
                route.append([ny, nx])
                visit[ny][nx] = visit[y][x] + 1
