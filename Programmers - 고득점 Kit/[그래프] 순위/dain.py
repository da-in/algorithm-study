def solution(n, results):
    answer = 0
    dict = {}

    for i in range(n):
        dict[i + 1] = {"up": set(), "down": set()}

    for r in results:
        a, b = r
        dict[a]["down"].add(b)
        dict[b]["up"].add(a)
        for d in dict[a]["down"]:
            dict[d]["up"] = dict[d]["up"] | dict[a]["up"]
        for u in dict[a]["up"]:
            dict[u]["down"] = dict[u]["down"] | dict[a]["down"]
        for d in dict[b]["down"]:
            dict[d]["up"] = dict[d]["up"] | dict[b]["up"]
        for u in dict[b]["up"]:
            dict[u]["down"] = dict[u]["down"] | dict[b]["down"]

    for k in dict.keys():
        if len(dict[k]["up"]) + len(dict[k]["down"]) == n - 1:
            answer += 1
    return answer
