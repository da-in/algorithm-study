# import sys
# sys.setrecursionlimit(10000)
def solution(n, wires):
    answer = 100
    
    data=[[]for i in range(n+1)]
    for w in wires:
        data[w[0]].append(w[1])
        data[w[1]].append(w[0])
        
        
    def find(tar,ex,visit):
        count=0
        visit[tar]=True
        for i in data[tar]:
            if i==ex:
                continue
            if not visit[i]:
                count+=1
                count+=find(i,ex,visit)
        return count
    
    for w in wires:
        visit=[False]*(n+1)
        visit[w[0]]=True
        visit[w[1]]=True
        
        a=find(w[0],w[1],visit)
        b=find(w[1],w[0],visit)
        
        answer=min(answer,abs(a-b))

    return answer
