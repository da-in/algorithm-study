from collections import deque

n, m = map(int, input().split())
map = []
ans = 'IMPOSSIBLE'

for i in range(n):
    map.append(list(input()))
    if 'J' in map[i]:
        q = deque([(0, i, map[i].index('J'))])

for i in range(n):
    for j in range(m):
        if map[i][j] == 'F':
            q.append((-1, i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    time, x, y = q.popleft()

    # 지훈이 탈출
    if time > -1 and map[x][y] != 'F':
        if x == 0 or y == 0 or x == n - 1 or y == m - 1:
            ans = time + 1
            break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
      
        if 0 <= nx < n and 0 <= ny < m and map[nx][ny] != '#':
            # 지훈이 이동
            if time > -1 and map[nx][ny] == '.':
                map[nx][ny] = '*'
                q.append((time + 1, nx, ny))
            # 불 퍼뜨리기
            elif time == -1 and map[nx][ny] != 'F':
                map[nx][ny] = 'F'
                q.append((-1, nx, ny))

print(ans)
