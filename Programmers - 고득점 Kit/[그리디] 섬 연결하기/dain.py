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
        ap = getParent(a)
        bp = getParent(b)
        if ap != bp:
            answer.append(cost)
            parent[ap] = parent[bp] = min(ap, bp)
        if len(answer) == n - 1:
            break

    return sum(answer)
