from collections import deque

def bfs(x,y,xy,maps):
    dx=[0,0,-1,1]
    dy=[1,-1,0,0]
    rows = len(maps)
    cols = len(maps[0])
    
    q = deque()
    q.append((x,y))

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or ny<0 or nx>=rows or ny>=cols:
                continue
            if maps[nx][ny]!="X" and maps[nx][ny]==0:
                maps[nx][ny]=maps[x][y]+1
                if [nx,ny]==xy:
                    return maps[nx][ny]
                q.append((nx,ny))
    return maps[xy[0]][xy[1]]

def new_map(maps):
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j]=="X":
                continue
            maps[i][j]=0
    return maps

def solution(maps):
    end_num=0
    start_xy, end_xy, lever_xy = 0,0,0
    lever_num,end_num = 0,0
    
    for i in range(len(maps)):
        temp=[]
        for j in range(len(maps[0])):
            temp.append(maps[i][j])
        maps[i]=temp
        
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j]=="S":
                start_xy=[i, j]
            if maps[i][j]=="E":
                end_xy=[i, j]
            if maps[i][j]=="L":
                lever_xy=[i, j]
    
    maps = new_map(maps)
    
    lever_num = bfs(start_xy[0], start_xy[1], lever_xy, maps)
    if lever_num>0:
        maps = new_map(maps)
        end_num = bfs(lever_xy[0], lever_xy[1], end_xy, maps)
    else:
        return -1
    
    return lever_num+end_num if end_num>0 else -1