def solution(n, costs):
    answer = 0
    parents = [i for i in range(n)]
    costs.sort(key=lambda x: x[2])
    

    for cost in costs:
        if find(parents, cost[0]) != find(parents, cost[1]):
            union(parents, cost[0], cost[1])
            answer += cost[2]

    return answer


def find(parents, i):
    while i != parents[i]:
        i = parents[i]
    return i

def union(parents, i, j):
    i_root = find(parents, i)
    j_root = find(parents, j)
    parents[j_root] = i_root