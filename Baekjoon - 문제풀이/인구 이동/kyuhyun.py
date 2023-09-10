from collections import deque
N, L, R = map(int, input().split(" "))

town = []
res = 0
d = [[0, 1], [1, 0], [-1, 0], [0, -1]]

for i in range(N):
    val = list(map(int, input().split(" ")))
    town.append(val)

def bfs(i, j):
    together_town = deque()
    union_town = []
    visit[i][j] = 1
    together_town.append([i, j])
    union_town.append([i, j])

    while together_town:
        y, x = together_town.popleft()
        val = town[y][x]

        for dy, dx in d:
            ny = y + dy
            nx = x + dx
            if ny >= N or ny < 0 or nx >= N or nx < 0:
                continue
            if visit[ny][nx] == 1:
                continue
            if L <= abs(val - town[ny][nx]) <= R:
                visit[ny][nx] = 1
                together_town.append([ny, nx])
                union_town.append([ny, nx])
    return union_town

while True:
    visit = [[0 for _ in range(N)] for _ in range(N)]
    flag = 0
    for i in range(N):
        for j in range(N):
            if visit[i][j] == 0:
                union = bfs(i, j)

                if len(union) > 1:
                    flag = 1
                    people = sum(town[y][x] for y, x in union) // len(union)

                    for y, x in union:
                        town[y][x] = people
    if flag == 0:
        break
    res += 1
print(res)
