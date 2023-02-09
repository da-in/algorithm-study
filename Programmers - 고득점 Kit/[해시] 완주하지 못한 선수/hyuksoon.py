def solution(participant, completion):
    answer = ''
    h={}
    for p in participant:
        if p not in h:
            h[p]=1
        else:
            h[p]+=1
    
    for c in completion:
        h[c]-=1
        if h[c]==0:
            del h[c]
    for i in h:
        return i