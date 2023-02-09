from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    dist = [-1] * (n + 1)
    d = 0
    q = deque([(1, 0)])

    for e in edge:
        a, b = e
        graph[a].append(b)
        graph[b].append(a)

    while q:
        cur, d = q.popleft()
        dist[cur] = d
        for nxt in graph[cur]:
            if dist[nxt] < 0:
                dist[nxt] = 0
                q.append((nxt, d + 1))

    return dist.count(max(dist))
