from collections import deque

# 8,10,11 런타임 에러
def solution(x, y, n):
    if x==y:
        return 0
    
    q = deque([x])
    l = [0]*1000000
    
    temp=x
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