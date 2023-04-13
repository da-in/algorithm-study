from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(maps, col, row, i, j, visited):
    visited[i][j] = True
    q = deque()
    q.append([i,j])
    num = 0
    
    while q:
        c, r = q.popleft()
        num += int(maps[c][r])
        
        for k in range(4):
            x = c + dx[k]
            y = r + dy[k]
            
            
            if 0<=x<col and 0<=y<row:
                if not visited[x][y] and maps[x][y] != 'X':
                    visited[x][y] = True
                    q.append([x,y])
                    
            else:
                continue 
    return num   

def solution(maps):
    answer = []
    
    for i in range(len(maps)):
        maps[i] = list(maps[i]) # 2차원 배열로 재선언

    col = len(maps) #4 세로!!
    row = len(maps[0])  #5 가로!!

    visited = [[False]*row for _ in range(col)]

    for i in range(col):
        for j in range(row):
            if not visited[i][j] and maps[i][j] != 'X':
                answer.append(bfs(maps, col, row, i, j, visited))
            
                    
    if answer:   
        answer.sort()
    else:
        answer = [-1]
    
    return answer