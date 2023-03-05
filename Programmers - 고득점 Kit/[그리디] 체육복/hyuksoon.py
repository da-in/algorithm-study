def solution(n, lost, reserve):
    answer = 0
    pp=[]
    reserve.sort()
    lost.sort()
    data={}
    losts=len(lost)
    for i in lost:
        data[i]=True
        if i in reserve:
            data[i]=False
            losts-=1
    
    for r in reserve:
        if r not in data:
            if r-1 in data and data[r-1]:
                data[r-1]=False
                losts-=1
            elif r+1 in data and data[r+1]:
                data[r+1]=False
                losts-=1
                
    return n-losts
