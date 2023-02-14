from collections import deque
def main():
    print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    visited=[[False for i in range(m)] for j in range(n)]
    if maps[n-2][m-1] == 0 and maps[n-1][m-2] == 0:
        return -1

    return bfs(maps,0,0,visited)

def bfs(maps,x,y,visited):

    n = len(maps)
    m = len(maps[0])
    que = deque([(x,y)])
    visited[x][y] = True
    cnt = {(x,y):0}

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if maps[nx][ny] == 1:
                    if (nx,ny) == (n-1,m-1): return cnt[(x,y)] + 2
                    que.append((nx,ny))
                    cnt[(nx,ny)] = cnt[(x,y)] + 1
                    visited[nx][ny] = True
    

if __name__ == "__main__":
    main()