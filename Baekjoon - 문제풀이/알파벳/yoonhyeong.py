R, C = map(int, input().split())

maps = []

for _ in range(R):
    maps.append(list(input()))

result = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

tmp = set()


def dfs(x, y, count):
    global result
    result = max(result, count)

    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]

        if 0 <= new_x < C and 0 <= new_y < R and not maps[new_y][new_x] in tmp:
            tmp.add(maps[new_y][new_x])
            dfs(new_x, new_y, count + 1)
            tmp.remove(maps[new_y][new_x])


tmp.add(maps[0][0])
dfs(0, 0, 1)
print(result)
