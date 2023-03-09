from itertools import combinations
def solution(n, wires):
    answer = 100
    
    for kind in list(combinations(wires, n-2)):
        visit = [0] * n
        graph = [[] for _ in range(n+1)]
        route = []

        for x, y in kind:
            graph[x].append(y)
            graph[y].append(x)

        route.append(1)

        while route:
            st = route.pop()
            visit[st-1] = 1

            for en in graph[st]:
                if visit[en-1] == 0:
                    route.append(en)
                    visit[en-1] = 1

        v = visit.count(1)
        if answer > abs((n - v) - v):
            answer = abs((n - v) - v)
    return answer
