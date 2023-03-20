'''
###############################

못품

###############################
'''
from collections import deque
def solution(game_board, table):
    answer = 0
   
    
    visit=[[False for i in range(len(game_board[0]))]for j in range(len(game_board))]
    dy=[1,-1,0,0]
    dx=[0,0,1,-1]
    data=[]
    
    def rot(l):
        temp=[]
        for i in l:
            if i[0]<=0 and i[1]>=0:
                temp.append([-i[0],i[1]])
            elif i[0]<=0 and i[1]<=0: 
                temp.append([i[0],-i[1]])
            elif i[0]>=0 and i[1]<=0: 
                temp.append([-i[0],i[1]])
            elif i[0]>=0 and i[1]>=0: 
                temp.append([i[0],-i[1]])
        return temp

    
        
    def bfs(i,j):
        q=deque()
        q.append([i,j])
        shape=[]
        shape.append([i,j])
        while q:
            y,x=q.popleft()
            for d in range(4):
                nx=x+dx[d]
                ny=y+dy[d]
                if 0<=ny<len(game_board) and 0<=nx<len(game_board[0]) and not visit[ny][nx] and game_board[ny][nx]==0:
                    visit[ny][nx]=True
                    q.append([ny,nx])
                    shape.append([ny,nx])
        return shape
    def bfs2(i,j):
        q=deque()
        q.append([i,j])
        shape=[]
        shape.append([i,j])
        while q:
            y,x=q.popleft()
            for d in range(4):
                nx=x+dx[d]
                ny=y+dy[d]
                if 0<=ny<len(table) and 0<=nx<len(table[0]) and not visit2[ny][nx] and table[ny][nx]==1:
                    visit2[ny][nx]=True
                    q.append([ny,nx])
                    shape.append([ny,nx])
        return shape
    def calc(data):
        a=[]
        for i in data:
            main=i
            temp1=[]
            for j in data:
                temp1.append([j[0]-main[0],j[1]-main[1]])
            a.append(sorted(temp1))
            temp2=rot(temp1)
            temp3=rot(temp2)
            temp4=rot(temp3)
            a.append(sorted(temp2))
            a.append(sorted(temp3))
            a.append(sorted(temp4))

        return a
    cnt=0
    dict_game={}        
    for i in range(len(game_board)):
        for j in range(len(game_board[0])):
            if not visit[i][j] and game_board[i][j]==0:
                visit[i][j]=True
                a=bfs(i,j)
                temp=calc(a)
                
                dict_game[cnt]=temp
                cnt+=1
    dict_table={}        
    visit2=[[False for i in range(len(table[0]))]for j in range(len(table))]

    cnt=0
    for i in range(len(table)):
        for j in range(len(table[0])):
            if not visit2[i][j] and table[i][j]==1:
                visit2[i][j]=True
                a=bfs2(i,j)
                temp=calc(a)
                
                dict_table[cnt]=temp    
                cnt+=1   
    for i in range(len(dict_table)):
        for tar in dict_table[i]:
            # print("tar",tar)
            ck=True
            if ck:
                    for j in range(len(dict_game)):
                        if dict_game[j]!=False:
                            if ck:
                                for plz in dict_game[j]:
                                    # print("plz",plz)
                                    if plz==tar:
                                        print(plz,tar)
                                        dict_game[j]=False
                                        answer+=1
                                        ck=False
                                        break
                            if not ck:
                                break
                    
            if not ck:
                break
            ck=True
    
    # print(" ")
    # print(dict_table)
    return answer
