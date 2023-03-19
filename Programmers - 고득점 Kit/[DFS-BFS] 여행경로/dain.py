from collections import defaultdict

def solution(tickets):
    route = defaultdict(list)
    for i in range(len(tickets)):
        a, b = tickets[i]
        route[a].append(b)
    for t in route:
        route[t].sort(reverse=True)

    answer = []
    stack = ["ICN"]
    while stack:
        if not route[stack[-1]]:
            answer.append(stack.pop())
        else:
            stack.append(route[stack[-1]].pop())
    answer.reverse()

    return answer
