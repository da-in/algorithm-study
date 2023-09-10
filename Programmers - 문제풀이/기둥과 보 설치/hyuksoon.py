def solution(n, build_frame):
    answer = []
    data=[[[False,False,False] for i in range(n+1)] for j in range(n+1)]
    
        
    
    for build in build_frame:
        x,y,a,b=build
        if a==0:
            if b==1:
                if y==0 or data[y][x][0] or data[y][x][1]:
                    data[y+1][x][0]=True
            else:
                if data[y+2][x][0] and not data[y+1][x][1]:
                    continue
                if data[y+1][x][1] :
                    if x-1<0:
                        continue
                    if not (data[y+1][x][2] and data[y+1][x-1][1]):
                        continue
                if data[y+1][x][2]:
                    if x+1>=n:
                        continue
                    if not (data[y+1][x][1] and data[y+1][x+1][2]):
                        continue
                data[y+1][x][0]=False
                    
        else:
            if b==1:
                if data[y][x][0] or data[y][x+1][0] or (data[y][x][1] and data[y][x+1][2]):
                    data[y][x][2]=True
                    data[y][x+1][1]=True
            else:
                if data[y+1][x][0] and not data[y][x][0] and data[y][x][1] and data[y][x][2]:
                    continue
                if data[y][x][1] :
                    flag=False
                    if not data[y][x-1][0]:
                        flag=True
                    if not data[y][x][0]:
                        flag=True
                    else:
                        flag=False
                    
                    if not (data[y][x-1][1] and data[y][x][2]):
                        flag=True
                    else:
                        flag=False
                    if flag:
                        continue
                if data[y][x][2] :
                    flag=False
                    if not data[y][x][0]:
                        flag=True
                    if not data[y][x+1][0]:
                        flag=True
                    else:
                        flag=False
                    
                    if not (data[y][x][1] and data[y][x+1][2]):
                        flag=True
                    else:
                        flag=False
                    if flag:
                        continue
                data[y][x][2]=False
                data[y][x+1][1]=False
                
    for i in range(n+1):
        for j in range(n+1):
            if data[i][j][0]:
                answer.append([j,i-1,0])
            if data[i][j][2]:
                answer.append([j,i,1])
                
    answer.sort()
    return answer
