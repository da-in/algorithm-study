from collections import deque

def bfs(maps,visited,x,y,rlen,clen):
    # 상, 하, 좌, 우
    dx=[0,0,-1,1]
    dy=[1,-1,0,0]
    
    q = deque()
    q.append((x,y))
    visited[x][y]=1
    temp=0
    
    while q:
        x,y = q.popleft()
        temp+=int(maps[x][y])
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=clen or ny<0 or ny>=rlen:
                continue
            if maps[nx][ny]!='X' and visited[nx][ny]==0:
                visited[nx][ny]=1
                q.append((nx,ny))
    return temp
    
def solution(maps):
    answer=[]
    maps=[[int(i) if i!='X' else i for i in m] for m in maps]
    visited=[[0 if i!='X' else 1 for i in m] for m in maps]
    rlen=len(maps[0])
    clen=len(maps)
    
    for i in range(clen):
        temp=0
        for j in range(rlen):
            if maps[i][j]!='X' and visited[i][j]==0:
                temp = bfs(maps,visited,i,j,rlen,clen)
                answer.append(temp)
                
                
    return sorted(answer) if answer else [-1]