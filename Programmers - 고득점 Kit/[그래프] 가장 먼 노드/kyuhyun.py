from collections import deque

def solution(n, edge):
    
    graph = [[] for i in range(n+1)]

    for x, y in edge:
        graph[x].append(y)
        graph[y].append(x)

    cnt = [0] * (n+1)
    q = deque([1])
    cnt[1] = 1

    while q:
        idx = q.popleft()

        for v in graph[idx]:
            if cnt[v] == 0:
                cnt[v] += cnt[idx] + 1
                q.append(v)

    return cnt.count(max(cnt))
