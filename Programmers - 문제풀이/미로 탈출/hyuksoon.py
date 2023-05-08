from collections import deque
def solution(maps):
    answer = 0
    global lx
    global ly
    lx=0
    ly=0
    def bfs(y,x,target):
        global lx
        global ly
        
        visit=[[False for i in range(len(maps[0]))]for j in range(len(maps))]
        dx=[0,0,1,-1]
        dy=[1,-1,0,0]
        q=deque([[y,x,0]])
        visit[y][x]=True
        while q:
            
            y,x,count=q.popleft()
            for d in range(4):
                nx=x+dx[d]
                ny=y+dy[d]
                if 0<=ny<len(maps) and 0<=nx<len(maps[0]) and maps[ny][nx]!="X" and not visit[ny][nx]:
                    visit[ny][nx]=True
                    if maps[ny][nx]==target:
                        ly=ny
                        lx=nx
                        return count+1
                    q.append([ny,nx,count+1])
        return -1
                    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j]=="S":
                y,x=i,j
                break
    result1=bfs(y,x,"L")
    if result1==-1:
        return -1
    answer+=result1
    result2=bfs(ly,lx,"E")
    if result2==-1:
        return -1
    answer+=result2
    
    return answer
