from collections import deque

def solution(want, number, discount):
    answer = 0
    
    for i in range(len(discount)-9):
        d_want = dict(zip(want,number))
        q=deque(discount[i:i+10]) 
        
        for _ in range(10):
            temp = q.popleft()
            if temp in want and d_want[temp]>0:
                d_want[temp]-=1
            else:
                continue
                
        if sum(d_want.values())==0:
            answer+=1
    
    return answer