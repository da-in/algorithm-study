import math
def main():
    print(solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))

def DFS(v, graph, visited, check):
    cnt = 1
    visited[v] = True
    
    for i in graph[v]:
        if visited[i] == False and check[v][i]:
            cnt += DFS(i, graph, visited, check)
    
    return cnt

def solution(n, wires):
    answer = math.inf
    
    # 없앤 간선인지 아닌지 체크 값이 들어있는 리스트
    check = [[True]*(n+1) for i in range(n+1)]
    
    graph = [[] for i in range(n+1)]
    
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    for a, b in wires:
        visited = [False]*(n+1)
        
        check[a][b] = False # a-b 간선 끊기
        cnt_a = DFS(a, graph, visited, check)
        cnt_b = DFS(b, graph, visited, check)
        check[a][b] = True # a-b 간선 다시 연결
        
        answer = min(answer, abs(cnt_a - cnt_b))
    
    return answer


    
if __name__ == "__main__":
    main()