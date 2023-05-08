from collections import deque
def BFS(end_point, visit, dq, maps):
        res_min = 10001
        dx = [1, 0 , -1, 0]
        dy = [0, 1 , 0, -1]
        while dq:
            y, x, res = dq.popleft()

            if maps[y][x] == end_point:
                if res < res_min:
                    res_min = res
                    continue
            res += 1

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if (nx < 0 or nx > len(maps[0])-1) or (ny < 0 or ny > len(maps) -1):
                    continue
                if visit[ny][nx] == 1:
                    continue
                if maps[ny][nx] == 'X':
                    continue
                dq.append([ny, nx, res])
                visit[ny][nx] = 1

        if res_min == 10001:
            return -1
        return res_min
    
def solution(maps):

    visit1 = [[0] * len(maps[0]) for _ in range(len(maps))]
    visit2 = [[0] * len(maps[0]) for _ in range(len(maps))]

    dq = deque()
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == 'S':
                dq.append([i, j, 0])
                visit1[i][j] = 1
                min_l = BFS('L', visit1, dq, maps)
                if min_l == -1:
                    return -1
            elif maps[i][j] == 'L':
                dq.append([i, j, 0])
                visit2[i][j] = 1
                min_e = BFS('E', visit2, dq, maps)
                if min_e == -1:
                    return -1
    return min_l + min_e
