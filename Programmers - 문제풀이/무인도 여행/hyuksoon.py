from collections import deque
def solution(maps):
    answer = []
    ck=[[False for i in range(len(maps[0]))]for j in range(len(maps))]
    dy=[0,0,1,-1]
    dx=[1,-1,0,0]
    def bfs(y,x):
        ck[y][x]=True
        q=deque([[y,x]])
        cnt=int(maps[y][x])
        while q:
            i,j=q.popleft()
            for d in range(4):
                ny=i+dy[d]
                nx=j+dx[d]
                if 0<=ny<len(maps) and 0<=nx<len(maps[0]) and maps[ny][nx]!='X' and not ck[ny][nx]:
                    ck[ny][nx]=True
                    cnt+=int(maps[ny][nx])
                    q.append([ny,nx])
        return cnt
                    
            
        
        
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j]!='X' and not ck[i][j]:
                answer.append(bfs(i,j))
    if answer:
        return sorted(answer)
    else:
        return [-1]

    