from collections import deque
def solution(plans):
    answer = []
    plans.sort(key=lambda x: -( (int(x[1].split(":")[0])*60) + (int(x[1].split(":")[1])) ))
    stk=[]
    time=0
    while plans:
        if stk and time<int(plans[-1][1].split(":")[0])*60 + (int(plans[-1][1].split(":")[1])):
            plan=stk.pop()
            name=plan[0]
            t=time
            cost=plan[2]
        else:
            plan=plans.pop()
            name=plan[0]
            t=(int(plan[1].split(":")[0])*60) + (int(plan[1].split(":")[1]))
            cost=int(plan[2])

        if plans:
            t2=(int(plans[-1][1].split(":")[0])*60) + (int(plans[-1][1].split(":")[1]))
        
            if cost+t >t2:
                stk.append([name,t2,cost+t-t2])
                time=t2
                continue

        answer.append(name)
        time=cost+t

    
    for s in reversed(stk):
        answer.append(s[0])
    


        
        
    
    
    return answer
