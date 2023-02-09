from collections import deque
def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    visit = [False] * (n + 1)
    line = [0] * (n + 1)

    for e1, e2 in edge: # edge 정보 바탕으로 bfs실행할 배열 생성
        graph[e1].append(e2)
        graph[e2].append(e1)
    
    bfs(graph, 1, visit, line)
    max_line = max(line)
    for l in line:
        if l == max_line:
            answer += 1
    return answer

def bfs(graph, start, visit, line):
    queue = deque([start])
    visit[start] = True
    line[1] = 0
    
    while queue:
        v = queue.popleft()
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visit[i]:
                queue.append(i)
                visit[i] = True
                line[i] = line[v] + 1