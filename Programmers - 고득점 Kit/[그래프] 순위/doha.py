def solution(n, results):
    answer = 0
    graph = [[0]*(n+1) for _ in range(n+1)]

    for result in results:
        win = result[0]
        lose = result[1]
        graph[win][lose] = win
        graph[lose][win] = win

    for _ in range(2):
        for win in range(1,n+1):
            for lose in range(1,n+1):
                if win == graph[win][lose]:
                    dfs(graph, lose, win)
    
    for i in range(1, n+1):
        cnt = 0
        
        for j in range(1, n+1):
            if graph[i][j] == 0:
                cnt += 1
                
        if cnt == 1:
            answer += 1

    return answer

def dfs(graph, lose, win):
    for i, j in enumerate(graph[lose]):
        if j == lose:
            graph[win][i] = win
            graph[i][win] = win