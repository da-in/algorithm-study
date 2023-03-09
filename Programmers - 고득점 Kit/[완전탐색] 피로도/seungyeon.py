def main():
    print(solution(80,[[80,20],[50,40],[30,10]]))

answer = 0

def solution(k, dungeons):
    visited = [False for i in range(len(dungeons))]
    dfs(k,dungeons,visited,0)
    return answer


def dfs(k,dungeons,visited,cnt):

    global answer

    if cnt > answer:
        answer = cnt
    
    for i in range(len(dungeons)):
        if k >= dungeons[i][0] and not visited[i]:
            visited[i] = True
            dfs(k-dungeons[i][1],dungeons,visited,cnt+1)
            visited[i] = False








# def dfs(k,cnt,answer,dungeons,visited ):
#     if cnt > answer:
#         answer = cnt
#     for i in range(len(dungeons)):
#         if k >= dungeons[i][0] and not visited[i]:
#             visited[i] = True
#             dfs(k-dungeons[i][1],cnt+1,answer,dungeons,visited)
#             visited[i] = False
    
#     return answer

    
if __name__ == "__main__":
    main()