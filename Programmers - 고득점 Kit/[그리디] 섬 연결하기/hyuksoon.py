def solution(n, costs):
    answer = 0
    costs.sort(key= lambda x: (x[2]))
    data=[[costs[0][0],costs[0][1]]]
    answer+=costs[0][2]
        
    visit=[-1 for i in range(n)]
    visit[costs[0][0]]=0
    visit[costs[0][1]]=0
    for i in costs[1:]:
        print(data)
        print(visit)
        print("")
        if visit[i[0]] !=-1 and visit[i[1]] !=-1 and visit[i[0]]!=visit[i[1]] :
            answer+=i[2]
            print(max(visit[i[0]],visit[i[1]]))
            maxnum=max(visit[i[0]],visit[i[1]])
            minnun=min(visit[i[0]],visit[i[1]])
            for i in data[maxnum]:
                data[minnun].append(i)
                visit[i]=minnun
        elif visit[i[0]] !=-1 and visit[i[1]] ==-1:
            answer+=i[2]
            data[visit[i[0]]].append(i[1])
            visit[i[1]]= visit[i[0]]
        elif visit[i[0]] ==-1 and visit[i[1]] !=-1:
            answer+=i[2]
            data[visit[i[1]]].append(i[0])
            visit[i[0]]= visit[i[1]]
        elif visit[i[0]] ==-1 and visit[i[1]] ==-1:
            answer+=i[2]
            visit[i[0]]=len(data)
            visit[i[1]]=len(data)
            data.append([i[0],i[1]])
            
        else:
            print(i)
            
            
        
    print(data)
    return answer

print(solution(4,[[0,1,3],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))