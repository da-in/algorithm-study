def solution(arrows):
    answer = 0
    graph = {(0, 0): set()}
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]
    x = y = nx = ny = 0

    def isCross(a, x, y):
        if a == 1 and (x, y + 1) in graph.keys() and (x + 1, y) in graph[(x, y + 1)]:
            return True
        elif a == 3 and (x, y - 1) in graph.keys() and (x + 1, y) in graph[(x, y - 1)]:
            return True
        elif a == 5 and (x, y - 1) in graph.keys() and (x - 1, y) in graph[(x, y - 1)]:
            return True
        elif a == 7 and (x, y + 1) in graph.keys() and (x - 1, y) in graph[(x, y + 1)]:
            return True
        return False

    for a in arrows:
        nx = x + dx[a]
        ny = y + dy[a]
        graph[(x, y)].add((nx, ny))
        if (nx, ny) in graph.keys():
            if (x, y) not in graph[(nx, ny)]:
                graph[(nx, ny)].add((x, y))
                answer += 1
                if isCross(a, x, y):
                    answer += 1
        else:
            graph[(nx, ny)] = {(x, y)}
            if isCross(a, x, y):
                answer += 1
        x, y = nx, ny
    return answer


# 오일러 정리를 이용한 코드
# v-e+f = 1
# v: 꼭짓점, e:모서리, f:면

def solution(arrows):
    # f = 1 + e - v
    e = set()
    v = {(0, 0)}
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]
    x = y = nx = ny = 0
    for a in arrows:
        for _ in range(2):
            nx = x + dx[a]
            ny = y + dy[a]
            v.add((nx, ny))
            e.add(frozenset({(nx, ny), (x, y)}))
            x, y = nx, ny
    return 1 + len(e) - len(v)
