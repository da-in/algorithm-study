from collections import deque
import sys

N, L, R = map(int, input().split())
people = [list(map(int, input().split())) for _ in range(N)]
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)


def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = True
    union = [(x, y)]

    while q:
        x, y = q.popleft()

        for i in range(4):
            x1, y1 = x + dx[i], y + dy[i]

            if 0 <= x1 < N and 0 <= y1 < N and not visited[x1][y1]:
                if L <= abs(people[x1][y1] - people[x][y]) <= R:
                    q.append((x1, y1))
                    visited[x1][y1] = True
                    union.append((x1, y1))

    return union


result = 0
while True:
    visited = [[False] * N for _ in range(N)]
    unions = []

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                union = bfs(i, j)
                if len(union) > 1:
                    unions.append(union)

    if not unions:
        break

    result += 1

    for union in unions:
        pop = sum([people[x][y] for x, y in union]) // len(union)
        for x, y in union:
            people[x][y] = pop

print(result)