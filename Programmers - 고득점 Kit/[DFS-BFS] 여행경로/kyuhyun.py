from collections import defaultdict
def solution(tickets):
    answer = []
    graph = defaultdict(list)
    res = []

    for start, end in tickets:
        graph[start].append(end)

    for start in graph.keys():
        graph[start].sort(reverse=True)

    res.append("ICN")

    while res:
        start = res.pop()

        if not graph[start]:
            answer.append(start)
        else:    
            res.append(start)
            res.append(graph[start].pop())
    answer.reverse()
    return answer
