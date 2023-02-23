from heapq import heappop
from heapq import heappush
def solution(operations):
    
    global hPlus
    global hMinus
    global data
    hPlus=[]
    hMinus=[]
    data={}
    def input(temp):
        
        global hPlus
        global hMinus
        op=temp.split(" ")[0]
        num=int(temp.split(" ")[1])
        if op=="I":
            heappush(hPlus,[-num,num])
            heappush(hMinus,[num,num])
            if num in data:
                data[num]+=1
            else:
                data[num]=1
        else:
            if num==1 :
                while hPlus:
                    popData=heappop(hPlus)[1]
                    if data and popData in data:
                        data[popData]-=1
                        if data[popData]==0:
                            del data[popData]
                        break
                    else:
                        continue
            elif num==-1 :
                while hMinus:
                    popData=heappop(hMinus)[1]
                    if data and popData in data:
                        data[popData]-=1
                        if data[popData]==0:
                            del data[popData]
                        break
                    else:
                        continue
            
                
        
        
    
    for temp in operations:
        input(temp)

    if data:
        return [max(data.keys()),min(data.keys())]
    else:
        return [0,0]