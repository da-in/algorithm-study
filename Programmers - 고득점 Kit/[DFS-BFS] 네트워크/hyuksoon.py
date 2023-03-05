from collections import deque
def solution(n, computers):
    
    def bfs(n):
        global visit
        visit[n]=True
        q=deque([n])
        print(n)
        while q:
            target=q.popleft()
            for c in computers[target]:
                if c==1 and not visit[c]:
                    visit[c]=True
                    q.append(c)
        return 1
                    
            
    answer = 0
    global visit
    visit=[False]*n
    for i in range(n):
        if not visit[i]:
            answer+=bfs(i) 
        
    
    return answer