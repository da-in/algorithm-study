

def main():
    print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]	))

def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    for start in range(n):
        if visited[start] == False:
            dfs(n,computers,start,visited)
            answer += 1
    return answer

def dfs(n,computers,start,visited):
    visited[start] = True
    for i in range(n):
        print(computers[start])
        print(start,i,computers[start][i])
        if(visited[i] == False and computers[start][i] == 1):
            visited = dfs(n,computers,i,visited)
    return visited

    
if __name__ == "__main__":
    main()