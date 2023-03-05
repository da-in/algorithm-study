def solution(n, computers):
    answer = 0
    route = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and not i == j:
                route[i].append(j)

    visited = [0] * n
    togo = []
    
    for i in range(n):
        if visited[i] == 0 and route[i]:
            togo.append(i)
            answer += 1

        while togo:
            start = togo.pop()
            visited[start] = 1

            for computer in route[start]:
                if visited[computer] == 0:
                    togo.append(computer)

    
    return answer + visited.count(0)
