import collections
answer = []
graph = collections.defaultdict(list)
visited = collections.defaultdict(list)

def main():
    print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))

def dfs(s, cnt, list, l):
    if cnt == l:
        answer.append(list)
        return

    for a in range(len(graph[s])):
        if visited[s][a] == 0:
            visited[s][a] = 1
            dfs(graph[s][a], cnt+1, list+[graph[s][a]], l)
            visited[s][a] = 0

def solution(tickets):
    
    for a,b in tickets:
        graph[a].append(b)
        visited[a].append(0)
    for a, b in graph.items():
        graph[a].sort() ## sort

    dfs("ICN",0, ["ICN"], len(tickets))

    return answer[:][0]

if __name__ == "__main__":
    main()