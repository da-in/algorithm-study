from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    
    ##두배 만들기
    for r in rectangle:
        r[0]*=2
        r[1]*=2
        r[2]*=2
        r[3]*=2
    characterX*=2
    characterY*=2
    itemX*=2
    itemY*=2
    
    
    def isIn(y,x):
            dx2=[1,-1,1,-1,0,0,1,-1]
            dy2=[1,-1,-1,1,1,-1,0,0]
            for d in range(8):
                nx=x+dx2[d]
                ny=y+dy2[d]
                ck=True
                for rect in rectangle:
                    q,w,e,r=rect
                    
                    if 0<=ny<102 and 0<=nx<102:
                        if q<=nx<=e and w<=ny<=r:
                            ck=False
                if ck:
                    return ck
            return ck
        
    def cango(y,x):
                ck=False
                for rect in rectangle:
                    q,w,e,r=rect
                    if q<=x<=e and (y==w or y==r):
                        ck=True
                    elif w<=y<=r and (x==q or x==e):
                        ck=True
                return ck

    data=[[0 for i in range(102)]for j in range(102)]
    
    for rect in rectangle:
        q,w,e,r=rect
        for i in range(w,r+1):
            if isIn(i,e):
                data[i][e]=1
        for i in range(w,r+1):
            if isIn(i,q):
                data[i][q]=1
        for i in range(q,e+1):
            if isIn(w,i):
                data[w][i]=1
        for i in range(q,e+1):
            if isIn(r,i):
                data[r][i]=1
                
    def bfs(y,x):
        visit=[[False for i in range(102)]for j in range(102)]
        q=deque()
        q.append([y,x,0])
        visit[y][x]=True
        while q:
            y,x,cnt=q.popleft()
            if y==itemY and x==itemX:
                return cnt
            ck=True
            for d in range(4):
                nx=x+dx[d]
                ny=y+dy[d]
                nx2=x+(dx[d]/2)
                ny2=y+(dy[d]/2)
                if cango(ny2,nx2) and 0<=ny<102 and 0<=nx<102 and not visit[ny][nx] and data[ny][nx]==1:
                    visit[ny][nx]=True
                    ck=False
                    q.append([ny,nx,cnt+1])
        return cnt
                    
    return bfs(characterY,characterX)//2

            
    