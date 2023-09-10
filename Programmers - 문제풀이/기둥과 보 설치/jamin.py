#기둥: 바닥, 보의 한쪽 끝, 다른 기둥
#보: 한쪽 끝이 기둥 위, 양쪽 끝이 다른 보와 연결

def solution(n, build_frame):
    answer = [[]]
    wall = [[0 for _ in range(n+1)] for _ in range(n+1) ]
    print(wall)
    
    for frame in build_frame:
        x = frame[0]
        y = frame[1]
        #설치
        if frame[3] == 1:
            #기둥 설치
            if frame[2] ==0:
                if y==0 or wall[y][x]>=1:
                    wall[y+1][x] = 1
                    answer.append([x,y,0])
                else:
                    continue
            
            #보 설치
            else:
                if wall[y][x] == 1:
                    wall[y][x+1] = 2
                    answer.append([x,y,1])
                elif wall[y][x+1] ==1:
                    wall[y][x] = 2
                    answer.append([x,y,1])
                elif wall[y][x] >=1 and wall[y][x+1]>=1:
                    wall[y][x] = 2
                    answer.append([x,y,1])
                else:
                    continue
            
        #삭제
        else:
            #기둥
            if frame[2] ==0:
                if wall[y+1][x] == 1:
                    continue
                elif wall[y+1][x] ==2 and wall[y+1][x+1]>=2:
                    continue
                elif wall[y+1][x] ==2 and wall[y+1][x-1]>=2:
                    continue
                else:
                    answer.remove([x,y,0])
                    wall[y][x] = 0
            #보
            else:
                if wall[y][x] ==2 and wall[y][x+1] >2:
                    continue
                elif wall[y][x] >2 and wall[y][x+1] ==2:
                    continue
                else:
                    answer.remove([x,y,1])
                    wall[y][x] = 0
                
    answer.remove([])
    answer = sorted(answer,key=lambda x:(x[0], x[1]))
    return answer