from collections import deque

def solution(routes):
    answer = 0
    routes.sort(key=lambda x: (x[1], x[0]))
    routes = deque(routes)
    while routes:
        answer += 1
        s, e = routes.popleft()
        while routes and routes[0][0] <= e:
            routes.popleft()
    return answer
