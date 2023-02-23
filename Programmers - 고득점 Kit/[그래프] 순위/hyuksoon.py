def solution(n, results):
    answer = 0
    w={}
    l={}
    for i in results:
        x,y=i
        if x in w:
            w[x].append(y)
        else:
            w[x]=[y]
        if y in l:
            l[y].append(x)
        else:
            l[y]=[x]
    def dfs(x,hash,temp):
        cnt=0
        if x in hash:
            for i in hash[x]:
                if i not in temp:
                    temp.append(i)
                    cnt+=1
                    cnt+=dfs(i,hash,temp)
        return cnt

                
    
    for i in range(1,n+1):
        if dfs(i,w,[])+ dfs(i,l,[])==n-1:
            answer+=1
            
    return answer