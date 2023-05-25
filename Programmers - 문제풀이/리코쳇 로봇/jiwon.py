from collections import deque

def solution(board):
    answer = 0
    max_x,max_y = len(board[0]),len(board)
    start_x,start_y,end_x,end_y = 0,0,0,0
    visited = [[-1 for _ in range(max_x)] for _ in range(max_y)]
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]=='R':
                start_x,start_y = j,i
            if board[i][j]=='G':
                end_x,end_y = j,i
    
    q = deque()
    q.append([start_x,start_y,0])
    while q:
        x,y,answer = q.popleft()
        if x==end_x and y==end_y:
            return answer
        
        for i in range(4):
            new_x,new_y = x,y
            while 0<=new_x+dx[i]<max_x and 0<=new_y+dy[i]<max_y and board[new_y+dy[i]][new_x+dx[i]]!='D':
                new_x+=dx[i]
                new_y+=dy[i]
            if visited[new_y][new_x]==-1:
                visited[new_y][new_x] = answer
                q.append([new_x,new_y,answer+1])
    
    return -1