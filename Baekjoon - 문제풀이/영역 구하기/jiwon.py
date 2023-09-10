import sys
from collections import deque

M, N, K = map(int, sys.stdin.readline().split())
squares = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]

paper = [[0 for _ in range(N)] for _ in range(M)]

for x1, y1, x2, y2 in squares:
    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)

    for i in range(y1, y2):
        for j in range(x1, x2):
            paper[i][j] = 1

dx = [0,0,-1,1]
dy = [1,-1,0,0]

visited = [[False for _ in range(N)] for _ in range(M)]

def bfs(X, Y):
    q = deque()
    q.append([X, Y])
    if paper[Y][X]==1 or visited[Y][X]:
        return 0
    visited[Y][X] = True
    result = 1
    while q:
        x, y = q.popleft()

        for i in range(4):
            new_x = x+dx[i]
            new_y = y+dy[i]

            if new_x<0 or new_x>=N or new_y<0 or new_y>=M:
                continue
            if paper[new_y][new_x]==1:
                continue

            if not visited[new_y][new_x]:
                visited[new_y][new_x] = True
                q.append([new_x,new_y])
                
                result+=1

    return result

results = []

for i in range(M):
    for j in range(N):
        temp = bfs(j,i)
        if temp!=0:
            results.append(temp)

results.sort()
print(len(results))
for i in results:
    print(i, end=' ')
    