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
