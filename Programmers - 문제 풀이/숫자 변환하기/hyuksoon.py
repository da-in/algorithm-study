from collections import deque

def solution(x, y, n):
    global answer
    answer = -1
    data={}
    q=deque([[x,0]])
    
    while q:
        tar,cnt=q.popleft()
        
        if tar==y:
            return cnt
        if tar>y**2:
            return -1
        if tar+n not in data or data[tar+n]>cnt+1:
            data[tar+n]=cnt+1
            q.append([tar+n,cnt+1])
        
        if tar*2 not in data or data[tar*2]>cnt+1:
            data[tar*2]=cnt+1
            q.append([tar*2,cnt+1])
        if tar*3 not in data or data[tar*3]>cnt+1:
            data[tar*3]=cnt+1
            q.append([tar*3,cnt+1])
     
        
        
    return answer