def solution(n, costs):
    answer = []
    costs.sort(key=lambda x: x[2])
    parent = [i for i in range(n)]

    def getParent(i):
        if parent[i] == i:
            return i
        return getParent(parent[i])

    for c in costs:
        a, b, cost = c
        if getParent(a) != getParent(b):
            answer.append(cost)
            ap = getParent(a)
            bp = getParent(b)
            parent[ap] = parent[bp] = min(ap, bp)
        if len(answer) == n - 1:
            break

    return sum(answer)
