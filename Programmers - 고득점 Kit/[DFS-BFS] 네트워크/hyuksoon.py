from collections import deque
def solution(n, computers):
    
    def bfs(n):
        global visit
        visit[n]=True
        q=deque([n])
        while q:
            target=q.popleft()
            for idx,c in enumerate(computers[target]):
                if c==1 and not visit[idx]:
                    visit[idx]=True
                    q.append(idx)
        return 1
                    
            
    answer = 0
    global visit
    visit=[False]*n
    for i in range(n):
        if not visit[i]:
            answer+=bfs(i) 
        
    
    return answer