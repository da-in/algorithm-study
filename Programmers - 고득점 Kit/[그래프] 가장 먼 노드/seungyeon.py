from collections import deque
def main():
    n = 6
    vertex=[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
    print(solution(n,vertex))

def solution(n,edge):
    answer = 0

    adj = [[] for i in range(n+1)]
    visited = [0]*(n+1)

    # 인접 행렬 만들기 
    for i,j in edge:
        adj[i].append(j)
        adj[j].append(i)
    
    # 초기값
    q = deque([1])
    visited[1] = 1

    bfs(1,adj,visited)

    for i in visited:
        if i == max(visited):
            answer += 1
    return answer

def bfs(start,adj,visited): # start 에서 시작해 갈 수 있는 모든 정점
    que = deque([start])
    visited[1] = 1

    while que:
        v = que.popleft()
        for i in adj[v]:
            if not visited[i]:
                visited[i] = visited[v] + 1
                que.append(i)






    

if __name__ == "__main__":
    main()