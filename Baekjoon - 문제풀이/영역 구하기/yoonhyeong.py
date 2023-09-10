from collections import deque

M, N, K = map(int, input().split())  # M이 세로, N이 가로

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

paper = [[0] * N for _ in range(M)]


for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            paper[j][i] += 1


def bfs(x, y):
    q = deque()
    q.append((x, y))
    count = 1

    while q:
        x, y = q.popleft()
        for k in range(4):
            move_x = x + dx[k]
            move_y = y + dy[k]
            if 0 <= move_x < N and 0 <= move_y < M and paper[move_y][move_x] == 0:
                paper[move_y][move_x] = 1
                q.append((move_x, move_y))
                count += 1
    return count

result = []

for i in range(N):
    for j in range(M):
        if paper[j][i] == 0:
            paper[j][i] = 1
            count = bfs(i, j)
            result.append(count)

print(len(result))
result = sorted(result)
for i in result:
    print(i, end=' ')

