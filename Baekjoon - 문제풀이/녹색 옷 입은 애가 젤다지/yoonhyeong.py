from collections import deque

# 좌우상하
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    graph[y][x] = coins[y][x]

    while q:
        x, y = q.popleft()
        for i in range(4):
            move_x = x + dx[i]
            move_y = y + dy[i]
            if 0 <= move_x < N and 0 <= move_y < N:
                if graph[move_y][move_x] > coins[move_y][move_x] + graph[y][x]: # 해당 좌표에 해당하는 경로의 값보다 더 작은 경로가 발견되면
                    graph[move_y][move_x] = coins[move_y][move_x] + graph[y][x] # 해당 좌표 최소 경로 갱신
                    q.append((move_x, move_y))


count = 0
while True:
    N = int(input())
    if N == 0:
        break
    coins = deque([list(map(int, input().split())) for _ in range(N)])
    graph = deque([1e9] * N for _ in range(N))
    bfs(0, 0)
    count += 1
    print("Problem " + str(count) + ": " + str(graph[N-1][N-1]))
