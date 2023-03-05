from collections import deque
def solution(maps):
    m=len(maps)
    n=len(maps[0])
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    visit=[[False for i in range(n)]for j in range(m)]
    q=deque([[0,0]])
    while q:
        y,x=q.popleft()
        
        for d in range(4):
            ny=y+dy[d]
            nx=x+dx[d]
            if 0<=ny<m and 0<=nx<n and not visit[ny][nx] and maps[ny][nx]==1:
                visit[ny][nx]=True
                maps[ny][nx]+=maps[y][x]
                if ny==m-1 and nx==n-1:
                    return maps[ny][nx]
                q.append([ny,nx])
                
    return maps[m-1][n-1] if maps[m-1][n-1]!=1 else -1
