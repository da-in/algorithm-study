from collections import deque

def bfs(start, end, roads):
    visited = [0 for _ in range(len(roads))]
    q = deque()
    distance=0
    
    for idx, road in enumerate(roads):
        s,e = road
        if s==start:
            q.append([s,e,1])
            visited[idx] = 1
    
    while q:
        s,e,d = q.popleft()
        distance = d
        if e==end:
            return d
        for idx, road in enumerate(roads):
            new_a,new_b = road
            if e==new_a and visited[idx]==0:
                visited[idx]=1
                d+=1
                q.append([s,e,d])
    
    return distance if distance>0 else -1
        

def solution(n, roads, sources, destination):
    # source>destination인 경우
    # source<destination인 경우
    # source==destination인 경우
    answer = []
    for a,b in roads:
        a,b = min(a,b), max(a,b)
    roads.sort(key=lambda x:x[0])
    
    for source in sources:
        if source>destination:
            distance = bfs(destination,source,roads)
        elif source<destination:
            distance = bfs(source,destination,roads)
        else:
            distance = 0
        answer.append(distance)
    
    return answer

# from collections import deque

# def bfs(destination, graph, distance):
#     q = deque([destination])
#     distance[destination]=0
    
#     while q:
#         x = q.popleft()
#         for node in graph[x]:
#             if distance[node]==-1:
#                 print(node)
#                 q.append(node)
#                 distance[node] = distance[x]+1
    
#     return distance
        

# def solution(n, roads, sources, destination):
#     graph = [[] for _ in range(n+1)]
#     for s, e in roads:
#         graph[s].append(e)
#         graph[e].append(s)
        
#     distance = [-1 for _ in range(n+1)]
#     distance = bfs(destination,graph,distance)
    
#     return [distance[source] for source in sources]