from collections import deque

m, n, k = map(int, input().split())

board = [[0] * n for _ in range(m)]
result = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    de = deque()
    de.append((x, y))
    board[x][y] = 1
    size = 1

    while de:
        x, y = de.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 0:
                board[nx][ny] = 1
                de.append((nx, ny))
                size += 1
    result.append(size)

for _ in range(k) :
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(m - y1 - 1, m - y2 - 1, -1):
            board[j][i] = 1

for i in range(n):
    for j in range(m):
        if board[j][i] == 0:
            bfs(j, i)

result.sort()
print(len(result))
for i in result:
    print(i, end=' ')
