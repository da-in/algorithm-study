from collections import deque
def bfs(x, y, visit, map):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    total = 0
    st = deque()
    st.append([x, y])
    visit[x][y] = 1

    while st:
        x, y = st.popleft()
        total += int(map[x][y])

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or ny >= len(map[0]) or nx >= len(map):
                continue
            if visit[nx][ny] == 1 or map[nx][ny] == 'X':
                continue
            st.append([nx, ny])
            visit[nx][ny] = 1
    return visit, total

def solution(maps):
    answer = []
    visit = [[0] * len(maps[0]) for _ in range(len(maps))]
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] != 'X' and visit[i][j] == 0:
                visit, total = bfs(i, j, visit, maps)
                answer.append(total)
                
    if not answer:
        return [-1]
    
    answer.sort()
    return answer
