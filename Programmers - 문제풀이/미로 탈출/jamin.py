# 레버를 지나야 출구를 열 수 있다
# BFS?

from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(start,end,maps):
    q = deque()
    
    col = len(maps) #세로!!
    row = len(maps[0])  #가로!!
    
    visited = [[False]*row for _ in range(col)]
    
    for i in range(col):
        for j in range(row):
            if maps[i][j] == start:     #S또는 L인 시작 좌표 찾는다
                q.append([i,j,0])
                visited[i][j] = True
                break
    
    while q:
        x,y,time = q.popleft()
        
        if maps[x][y] == end:
            return time
        
        for k in range(4):
            posX = x + dx[k]
            posY = y + dy[k]
            
            if 0<= posX < col and 0 <= posY < row:
                if not visited[posX][posY] and maps[posX][posY] != 'X':     # 방문하지 않았고 벽이 아니라면
                    visited[posX][posY] = True      # 방문처리
                    q.append([posX,posY,time+1])     # 시간 + 1
    return -1   # 탈출 불가한 경우
        
def solution(maps):
    answer = 0
    S_to_L = bfs('S','L',maps)
    L_to_E = bfs('L','E',maps)
    
    if S_to_L != -1 and L_to_E != -1:   # 둘 다 탈출 가능하다면
        return S_to_L+L_to_E
    
    return -1