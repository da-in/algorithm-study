import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
original_roads = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
roads = []
result = []

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

q = deque()

def bfs(x,y,cnt):
    q.append([x,y,cnt])

    while q:
        x, y, cnt = q.pop()

        if roads[x][y]==1:
            result.append([x,y,cnt])
            roads[x][y]=-1

        for i in range(4):
            new_x = x+dx[i]
            new_y = y+dy[i]

            if new_x<0 or new_x>=N or new_y<0 or new_y>=N:
                continue

            if roads[new_x][new_y]==-1:
                continue

            if roads[new_x][new_y]!=1:
                roads[new_x][new_y]=-1

            q.append([new_x, new_y, cnt+1])


for i in range(N):
    for j in range(N):
        if original_roads[i][j]==2:
            result = []
            roads = [[i for i in original_roads[j]] for j in range(N)]
            bfs(i,j,0)
            print(result)