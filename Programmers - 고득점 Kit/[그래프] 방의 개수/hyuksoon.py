def solution(arrows):
    answer = 0
    hash={}
    dy=[-1,-1,0,1,1,1,0,-1]
    dx=[0,1,1,1,0,-1,-1,-1]
    y,x=0,0
    hash["00"]=[]
    for i in arrows:
        ny=y+dy[i]
        nx=x+dx[i]
        nx2=x+(dx[i]/2)
        ny2=y+(dy[i]/2)
            
        if str(ny)+str(nx) in hash:
            if str(y)+str(x) not in hash[str(ny)+str(nx)]:
                answer+=1
                hash[str(ny)+str(nx)].append(str(y)+str(x))
                hash[str(y)+str(x)].append(str(ny)+str(nx))
        else:
            hash[str(ny)+str(nx)]=[]
            hash[str(ny)+str(nx)].append(str(y)+str(x))
            hash[str(y)+str(x)].append(str(ny)+str(nx))
        if dy[i]!=0 and dx[i]!=0 :
            if str(ny2)+str(nx2) in hash:
                if str(y)+str(x) not in hash[str(ny2)+str(nx2)]:
                    answer+=1
                    hash[str(ny2)+str(nx2)].append(str(y)+str(x))
                    hash[str(ny2)+str(nx2)].append(str(ny)+str(nx))
                    
                    hash[str(y)+str(x)].append(str(ny2)+str(nx2))
                    hash[str(ny)+str(nx)].append(str(ny2)+str(nx2))
            else:
                hash[str(ny2)+str(nx2)]=[]
                hash[str(ny2)+str(nx2)].append(str(y)+str(x))
                hash[str(ny2)+str(nx2)].append(str(ny)+str(nx))
                
                hash[str(y)+str(x)].append(str(ny2)+str(nx2))
                hash[str(ny)+str(nx)].append(str(ny2)+str(nx2))


        
        x=nx
        y=ny
    return answer