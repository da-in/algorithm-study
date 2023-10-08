from collections import deque
m, n = map(int, input().split(" "))

tomato = []
q = deque()
flag = 0

for _ in range(n) :
    tmp = list(map(int, input().split(" ")))
    tomato.append(tmp)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    global res
    while q:
        time, y, x = q.popleft()
        res = time

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if tomato[ny][nx] == 1 or tomato[ny][nx] == -1:
                continue
            q.append([time + 1, ny, nx])
            tomato[ny][nx] = 1

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            q.append([0, i, j])
bfs()
for i in range(n):
    if 0 in tomato[i]:
        flag = 1
        break

if flag == 1:
    print(-1)
else:
    print(res)
        
