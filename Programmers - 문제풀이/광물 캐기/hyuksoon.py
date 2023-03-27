from itertools import permutations


def solution(picks, minerals):
    answer = 0
    data=[]
    life={"diamond":[1,5,25],"iron":[1,1,5],"stone":[1,1,1]}
    
    
    cnt=0
    temp=[0,0,0]
    for m in minerals:
        if m=="diamond":
            temp[0]+=1
        elif m=="iron":
            temp[1]+=1
        else:
            temp[2]+=1
        cnt+=1
        if cnt==5:
            cnt=0
            data.append(temp)
            temp=[0,0,0]
    if temp!=[0,0,0]:
        data.append(temp)
    
    data=sorted(data[:sum(picks)],key=lambda x:(-x[0],-x[1],-x[2]))
    
    for i in data:
        if picks[0]>0:
            answer+=i[0]+i[1]+i[2]
            picks[0]-=1
        elif picks[1]>0:
            answer+=(i[0]*5)+i[1]+i[2]
            picks[1]-=1
        elif picks[2]>0:
            answer+=(i[0]*25)+(i[1]*5)+i[2]
            picks[2]-=1
        else:
            break
    return answer
