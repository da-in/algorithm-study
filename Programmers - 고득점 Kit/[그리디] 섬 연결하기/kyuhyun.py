def solution(n, costs):
    answer = 0
    island = set({0})
    
    while len(island) != n:
        min = 10000
        for i in range(len(costs)):
            x, y, cost = costs[i]
            if x in island and y in island:
                continue
            if x in island:
                if min > cost:
                    min = cost
                    new_island = y
            if y in island:
                if min > cost:
                    min = cost
                    new_island = x
        answer += min
        island.add(new_island)
    return answer
