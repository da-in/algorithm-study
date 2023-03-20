import copy


def solution(game_board, table):
    answer = 0
    able_areas = []
    puzzles = []
    l = len(game_board)
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    sx = sy = 0
    dfs_target_number = 0

    def move(puzzle):
        temp = []
        [first_x, first_y] = [float("inf"), float("-inf")]
        for x, y in puzzle:
            if y > first_y:
                first_y = y
                first_x = x
            elif y == first_y and x < first_x:
                first_x = x
        for x, y in puzzle:
            temp.append((x - first_x, y - first_y))
        temp.sort()
        return temp

    def rotate(puzzle):
        result = [puzzle]
        for _ in range(3):
            temp = []
            for x, y in result[-1]:
                temp.append((y, -x))
            temp = move(temp)
            result.append(temp)
        return result

    def dfs(matrix, x, y):
        result = []
        matrix[x][y] = (dfs_target_number + 1) % 2
        result.append((x - sx, y - sy))
        for dx, dy in d:
            if 0 <= x + dx < l and 0 <= y + dy < l:
                if matrix[x + dx][y + dy] == dfs_target_number:
                    result += dfs(matrix, x + dx, y + dy)
        return result

    for i in range(l):
        for j in range(l):
            if game_board[i][j] == 0:
                sx = i
                sy = j
                able_areas.append(rotate(dfs(game_board, i, j)))

    dfs_target_number = 1
    for i in range(l):
        for j in range(l):
            if table[i][j] == 1:
                sx = i
                sy = j
                puzzles.append(move(dfs(table, i, j)))

    for puzzle in puzzles:
        for able_area in able_areas:
            if puzzle in able_area:
                able_areas.remove(able_area)
                answer += len(puzzle)

    return answer
