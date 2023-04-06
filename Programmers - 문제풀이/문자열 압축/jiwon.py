from collections import deque

def solution(s):
    answer = len(s)
    for step in range(1, len(s)//2+1):
        sl=[]
        
        for i in range(0, len(s), step):
            sl.append(s[i:i+step])
        
        temp=sl[0]
        temp_answer=len(sl[0])
        n=1
        n_len=1
        
        for i in sl[1:]:
            if temp==i:
                n+=1
                if n==2 or n_len<len(str(n)):
                    temp_answer+=1
                    n_len=len(str(n))
            elif temp!=i:
                temp_answer+=len(i)
                temp=i
                n=1
        answer=min(answer,temp_answer)
        step+=1
        
    return answer