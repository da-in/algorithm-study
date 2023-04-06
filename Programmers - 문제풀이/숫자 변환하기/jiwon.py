from collections import deque

def solution(x, y, n):
    q = deque([x])
    l = [0]*1000000
    l[x]=1
    
    while q and temp<y:
        temp = q.popleft()
        
        if temp+n<=y and l[temp+n]==0:
            l[temp+n]=l[temp]+1
            q.append(temp+n)
        if temp*2<=y and l[temp*2]==0:
            l[temp*2]=l[temp]+1
            q.append(temp*2)
        if temp*3<=y and l[temp*3]==0:
            l[temp*3]=l[temp]+1
            q.append(temp*3)
        
    
    return l[y] if l[y]!=0 else -1