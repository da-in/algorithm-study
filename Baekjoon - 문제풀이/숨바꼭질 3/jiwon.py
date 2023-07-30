from collections import deque

def solution():
    q = deque([a])

    while q:
        temp = q.popleft()
        if temp==b:
            return visited[b]
        
        if 0<=temp*2<=100000 and visited[temp*2]==-1:
            visited[temp*2] = visited[temp]
            q.appendleft(temp*2)
        if 0<=temp-1<=100000 and visited[temp-1]==-1:
            visited[temp-1] = visited[temp]+1
            q.append(temp-1)
        if 0<=temp+1<=100000 and visited[temp+1]==-1:
            visited[temp+1] = visited[temp]+1
            q.append(temp+1)



a,b = map(int, input().split()) # a:수빈, b:동생
visited = [-1 for _ in range(100001)]
visited[a] = 0
print(solution())
