from collections import deque
def solution(n, edge):
    answer = 0
    data=[[]for i in range(n+1)]
    visit=[-1]*(n+1)
    for i in edge:
        data[i[0]].append(i[1])
        data[i[1]].append(i[0])
    q=deque()
    q.append(1)
    visit[1]=0
    while q:
        temp=q.popleft()
        for t in data[temp]:
            if visit[t]==-1:
                q.append(t)
                visit[t]=visit[temp]+1
                
    val=0
    for i in range(1,len(visit)):
        if visit[i]>val:
            val=visit[i]
            answer=1
        elif visit[i]==val:
            answer+=1
    return answer