import sys
from collections import deque

N, L, R = map(int, input().split())
people_list = [[int(i) for i in sys.stdin.readline().split()] for _ in range(N)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
result = 0

def bfs(i,j):
    q = deque()
    q.append((i,j))
    visited[i][j] = True
    union = [(i,j)]
    people_sum = people_list[i][j]
    while q:
        x, y = q.popleft()
        for d in range(4):
            new_x = x + dx[d]
            new_y = y + dy[d]
            if new_x<0 or new_x>=N or new_y<0 or new_y>=N:
                continue
            if visited[new_x][new_y]:
                continue
            if L<= abs(people_list[x][y] - people_list[new_x][new_y]) <= R:
                visited[new_x][new_y] = True
                q.append((new_x,new_y))
                union.append((new_x,new_y))
                people_sum+=people_list[new_x][new_y]

    for (x,y) in union:
        people_list[x][y] = people_sum//len(union)

    return len(union)

while True:
    visited = [[False for _ in range(N)] for _ in range(N)]
    is_move = False

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                if bfs(i,j)>1:
                    is_move = True
                    

    if not is_move:
        break

    result+=1

print(result)