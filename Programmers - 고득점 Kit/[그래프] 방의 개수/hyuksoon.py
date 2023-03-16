def solution(arrows):
    answer = 0
    hash={}
    dy=[-1,-1,0,1,1,1,0,-1]
    dx=[0,1,1,1,0,-1,-1,-1]
    y,x=0,0
    hash[(0,0)]=[]
    for i in arrows:
        ny=y+dy[i]
        nx=x+dx[i]
        nx2=x+(dx[i]/2)
        ny2=y+(dy[i]/2)
            
        if (ny,nx) in hash:
            if (y,x) not in hash[(ny,nx)]:
                answer+=1
                hash[(ny,nx)].append((y,x))
                hash[(y,x)].append((ny,nx))
        else:
            hash[(ny,nx)]=[]
            hash[(ny,nx)].append((y,x))
            hash[(y,x)].append((ny,nx))
        if dy[i]!=0 and dx[i]!=0 :
            if (ny2,nx2) in hash:
                if (y,x) not in hash[(ny2,nx2)]:
                    answer+=1
                    hash[(ny2,nx2)].append((y,x))
                    hash[(ny2,nx2)].append((ny,nx))
                    
                    hash[(y,x)].append((ny2,nx2))
                    hash[(ny,nx)].append((ny2,nx2))
            else:
                hash[(ny2,nx2)]=[]
                hash[(ny2,nx2)].append((y,x))
                hash[(ny2,nx2)].append((ny,nx))
                
                hash[(y,x)].append((ny2,nx2))
                hash[(ny,nx)].append((ny2,nx2))


        
        x=nx
        y=ny
    return answer