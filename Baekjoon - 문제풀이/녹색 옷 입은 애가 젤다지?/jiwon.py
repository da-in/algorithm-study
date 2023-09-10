import sys
from collections import deque

# 상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
problem = 0

while True:
    N = int(sys.stdin.readline())

    if N==0:
        break

    problem+=1

    cave_list = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
    visited = [[False for _ in range(N)] for _ in range(N)]
    result_list = []

    q = deque()
    # x, y, result
    q.append([0, 0, 0])
    visited[0][0] = True

    while q:
        print(q)
        x, y, result = q.popleft()
        print(x,y,result)
        
        if x==N-1 and y==N-1:
            result_list.append(result)
            print("results: ",result_list)
            continue

        for i in range(4):
            new_x, new_y = x+dx[i], y+dy[i]

            if new_x<0 or new_x>=N or new_y<0 or new_y>=N:
                continue
            if not visited[new_x][new_y]:
                q.append([new_x, new_y, result+cave_list[new_x][new_y]])
                visited[new_x][new_y] = True

    print(f"Problem {problem}: {min(result_list)}")