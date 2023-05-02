def solution(n, build_frame):
    answer = []
    pillar = [[False for _ in range(n+1)] for _ in range(n+1)]
    fabric = [[False for _ in range(n+1)] for _ in range(n+1)]
    
    def check_build(x,y, kind):
        if kind==0:
            if y==0 or fabric[y][x]==True or fabric[y][x-1]==True or (y>=1 and pillar[y-1][x]==True):
                pillar[y][x]=True
        else:
            if pillar[y-1][x]==True or pillar[y-1][x+1]==True or (1<=x and fabric[y][x-1]==True and fabric[y][x+1]==True):
                fabric[y][x]=True
        
    
    for frame in build_frame:
        x,y,a,b = frame
        if a==0: # 기둥
            if b==1 and y<=n: # 설치
                check_build(x,y,0)
            else: # 삭제
                if fabric[y][x]==True:
                    if not (pillar[y][x+1]==False and fabric[y][x-1]==True and fabric[y][x+1]==True):
                        pillar[y][x]=False
                elif pillar[y][x]==True:
                    if not (pillar[y][x]==True and pillar[y][x-1]==False and pillar[y][x]==False):
                        pillar[y][x]=False
                else:
                    pillar[y][x]=False
        else: # 천
            if b==1 and y>=1 and x<=n-1: # 설치
                check_build(x,y,1)
            else: # 삭제
                if 1<=x<=n-1 and fabric[y][x-1]==True and fabric[y][x+1]==True:
                    if (pillar[y-1][x-1]==True or pillar[y-1][x]==True) and (pillar[y-1][x]==True or pillar[y-1][x+1]==True):
                        fabric[y][x]=False
                elif x>=1 and fabric[y][x-1]==True:
                    if pillar[y-1][x-1]==True or pillar[y-1][x]==True:
                        fabric[y][x]=False
                elif x<=n-2 and fabric[y][x+1]==True:
                    if pillar[y-1][x+1]==True or pillar[y-1][x+2]==True:
                        fabric[y][x]=False
                elif pillar[y][x]==True:
                    if x>=1 and fabric[y][x-1]==True:
                        fabric[y][x]=False
                        print("#1-1",x,y,fabric[y][x])
                    elif pillar[y-1][x]==True:
                        fabric[y][x]=False
                        print("#1-2",x,y,fabric[y][x])
                elif x<=n-1 and pillar[y][x+1]==True:
                    if fabric[y][x+1]==True or pillar[y-1][x+1]:
                        fabric[y][x]=False
    
    for y in range(n+1):
        for x in range(n+1):
            if pillar[y][x]==True:
                answer.append([x,y,0])
            elif fabric[y][x]==True:
                answer.append([x,y,1])
    
    return sorted(answer, key=lambda x:(x[0],x[1],x[2]))