import sys

N, D = map(int, sys.stdin.readline().split())

g = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dis = [i for i in range(D + 1)]

for i in range(D + 1):
    dis[i] = min(dis[i], dis[i - 1] + 1)

    for start, end, d in g:
        if i == start and end <= D and dis[i] + d < dis[end]:
            dis[end] = dis[i] + d

print(dis[D])

# [list(map(int, sys.stdin.readline().split())) for _ in range(N)] : 이차원 배열 입력
